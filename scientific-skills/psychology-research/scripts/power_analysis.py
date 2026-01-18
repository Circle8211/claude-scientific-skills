#!/usr/bin/env python3
"""
Power Analysis for Psychology Research

Calculate sample sizes and statistical power for common psychology research designs.

Usage:
    python power_analysis.py --test ttest --effect-size 0.5 --power 0.80
    python power_analysis.py --test anova --groups 3 --effect-size 0.25
    python power_analysis.py --test correlation --effect-size 0.30
"""

import argparse
import math
from typing import Dict, Optional, Tuple
from scipy import stats
import numpy as np


def ttest_sample_size(
    effect_size: float,
    alpha: float = 0.05,
    power: float = 0.80,
    two_tailed: bool = True,
    paired: bool = False
) -> Dict:
    """
    Calculate required sample size for t-test.

    Args:
        effect_size: Cohen's d
        alpha: Significance level
        power: Desired statistical power
        two_tailed: Two-tailed test (default True)
        paired: Paired samples test

    Returns:
        Dictionary with sample size and parameters
    """
    # Z-values
    if two_tailed:
        z_alpha = stats.norm.ppf(1 - alpha / 2)
    else:
        z_alpha = stats.norm.ppf(1 - alpha)

    z_beta = stats.norm.ppf(power)

    if paired:
        # For paired t-test
        n = ((z_alpha + z_beta) / effect_size) ** 2
        n = math.ceil(n)
        return {
            "test": "Paired samples t-test",
            "n_total": n,
            "effect_size_d": effect_size,
            "alpha": alpha,
            "power": power,
            "two_tailed": two_tailed
        }
    else:
        # For independent samples t-test
        n_per_group = 2 * ((z_alpha + z_beta) / effect_size) ** 2
        n_per_group = math.ceil(n_per_group)
        return {
            "test": "Independent samples t-test",
            "n_per_group": n_per_group,
            "n_total": n_per_group * 2,
            "effect_size_d": effect_size,
            "alpha": alpha,
            "power": power,
            "two_tailed": two_tailed
        }


def ttest_power(
    n: int,
    effect_size: float,
    alpha: float = 0.05,
    two_tailed: bool = True,
    paired: bool = False
) -> Dict:
    """
    Calculate power for given sample size in t-test.

    Args:
        n: Sample size (per group for independent, total for paired)
        effect_size: Cohen's d
        alpha: Significance level
        two_tailed: Two-tailed test
        paired: Paired samples test

    Returns:
        Dictionary with power and parameters
    """
    if two_tailed:
        z_alpha = stats.norm.ppf(1 - alpha / 2)
    else:
        z_alpha = stats.norm.ppf(1 - alpha)

    if paired:
        z_beta = effect_size * math.sqrt(n) - z_alpha
    else:
        z_beta = effect_size * math.sqrt(n / 2) - z_alpha

    power = stats.norm.cdf(z_beta)

    return {
        "test": "Paired t-test" if paired else "Independent t-test",
        "n": n,
        "effect_size_d": effect_size,
        "alpha": alpha,
        "power": round(power, 3),
        "two_tailed": two_tailed
    }


def anova_sample_size(
    effect_size: float,
    n_groups: int,
    alpha: float = 0.05,
    power: float = 0.80
) -> Dict:
    """
    Calculate required sample size for one-way ANOVA.

    Args:
        effect_size: Cohen's f
        n_groups: Number of groups
        alpha: Significance level
        power: Desired power

    Returns:
        Dictionary with sample size and parameters
    """
    from scipy.stats import f as f_dist

    # Iterative solution
    df1 = n_groups - 1

    for n_per_group in range(5, 1000):
        df2 = n_groups * (n_per_group - 1)
        # Non-centrality parameter
        lambda_nc = n_per_group * n_groups * effect_size ** 2

        # Critical F value
        f_crit = f_dist.ppf(1 - alpha, df1, df2)

        # Power calculation
        current_power = 1 - f_dist.cdf(f_crit, df1, df2, loc=lambda_nc)

        if current_power >= power:
            return {
                "test": "One-way ANOVA",
                "n_per_group": n_per_group,
                "n_total": n_per_group * n_groups,
                "n_groups": n_groups,
                "effect_size_f": effect_size,
                "alpha": alpha,
                "power": round(current_power, 3)
            }

    return {"error": "Could not find solution within range"}


def correlation_sample_size(
    effect_size: float,
    alpha: float = 0.05,
    power: float = 0.80,
    two_tailed: bool = True
) -> Dict:
    """
    Calculate required sample size for correlation.

    Args:
        effect_size: Expected correlation (r)
        alpha: Significance level
        power: Desired power
        two_tailed: Two-tailed test

    Returns:
        Dictionary with sample size and parameters
    """
    if two_tailed:
        z_alpha = stats.norm.ppf(1 - alpha / 2)
    else:
        z_alpha = stats.norm.ppf(1 - alpha)

    z_beta = stats.norm.ppf(power)

    # Fisher's z transformation
    z_r = 0.5 * math.log((1 + effect_size) / (1 - effect_size))

    # Sample size formula
    n = ((z_alpha + z_beta) / z_r) ** 2 + 3

    return {
        "test": "Correlation (Pearson's r)",
        "n": math.ceil(n),
        "effect_size_r": effect_size,
        "alpha": alpha,
        "power": power,
        "two_tailed": two_tailed
    }


def regression_sample_size(
    effect_size: float,
    n_predictors: int,
    alpha: float = 0.05,
    power: float = 0.80
) -> Dict:
    """
    Calculate required sample size for multiple regression.

    Args:
        effect_size: Cohen's f² (R²/(1-R²))
        n_predictors: Number of predictors
        alpha: Significance level
        power: Desired power

    Returns:
        Dictionary with sample size and parameters
    """
    from scipy.stats import f as f_dist

    # Rule of thumb minimum
    min_n = n_predictors * 10 + 50

    for n in range(min_n, 2000):
        df1 = n_predictors
        df2 = n - n_predictors - 1

        if df2 < 1:
            continue

        # Non-centrality parameter
        lambda_nc = effect_size * n

        # Critical F
        f_crit = f_dist.ppf(1 - alpha, df1, df2)

        # Power
        current_power = 1 - f_dist.cdf(f_crit, df1, df2, loc=lambda_nc)

        if current_power >= power:
            return {
                "test": "Multiple Regression",
                "n": n,
                "n_predictors": n_predictors,
                "effect_size_f2": effect_size,
                "alpha": alpha,
                "power": round(current_power, 3)
            }

    return {"error": "Could not find solution within range"}


def chi_square_sample_size(
    effect_size: float,
    df: int,
    alpha: float = 0.05,
    power: float = 0.80
) -> Dict:
    """
    Calculate required sample size for chi-square test.

    Args:
        effect_size: Cohen's w
        df: Degrees of freedom
        alpha: Significance level
        power: Desired power

    Returns:
        Dictionary with sample size and parameters
    """
    from scipy.stats import ncx2

    for n in range(20, 2000):
        # Non-centrality parameter
        lambda_nc = n * effect_size ** 2

        # Critical chi-square
        chi_crit = stats.chi2.ppf(1 - alpha, df)

        # Power from non-central chi-square
        current_power = 1 - ncx2.cdf(chi_crit, df, lambda_nc)

        if current_power >= power:
            return {
                "test": "Chi-square test",
                "n": n,
                "df": df,
                "effect_size_w": effect_size,
                "alpha": alpha,
                "power": round(current_power, 3)
            }

    return {"error": "Could not find solution within range"}


def effect_size_interpretation(
    effect_type: str,
    value: float
) -> str:
    """
    Interpret effect size magnitude.

    Args:
        effect_type: Type of effect size (d, r, f, f2, w, eta2)
        value: Effect size value

    Returns:
        Interpretation string
    """
    benchmarks = {
        "d": [(0.20, "small"), (0.50, "medium"), (0.80, "large")],
        "r": [(0.10, "small"), (0.30, "medium"), (0.50, "large")],
        "f": [(0.10, "small"), (0.25, "medium"), (0.40, "large")],
        "f2": [(0.02, "small"), (0.15, "medium"), (0.35, "large")],
        "w": [(0.10, "small"), (0.30, "medium"), (0.50, "large")],
        "eta2": [(0.01, "small"), (0.06, "medium"), (0.14, "large")]
    }

    if effect_type not in benchmarks:
        return "Unknown effect size type"

    thresholds = benchmarks[effect_type]
    value = abs(value)

    for threshold, label in thresholds:
        if value < threshold:
            return f"Below {label} ({effect_type} < {threshold})"

    return f"Large ({effect_type} >= {thresholds[-1][0]})"


def print_power_table(
    test: str,
    effect_sizes: list,
    sample_sizes: list,
    alpha: float = 0.05
) -> None:
    """
    Print a power table for various effect sizes and sample sizes.
    """
    print(f"\nPower Table for {test}")
    print(f"Alpha = {alpha}")
    print("-" * 60)

    # Header
    header = "N\t" + "\t".join([f"ES={es}" for es in effect_sizes])
    print(header)
    print("-" * 60)

    for n in sample_sizes:
        row = f"{n}\t"
        for es in effect_sizes:
            if test == "ttest":
                result = ttest_power(n, es, alpha)
                power = result["power"]
            else:
                power = "N/A"
            row += f"{power}\t"
        print(row)


def main():
    parser = argparse.ArgumentParser(
        description="Power analysis for psychology research"
    )
    parser.add_argument(
        "--test", "-t",
        choices=["ttest", "paired_ttest", "anova", "correlation", "regression", "chi_square"],
        required=True,
        help="Statistical test"
    )
    parser.add_argument(
        "--effect-size", "-e",
        type=float,
        required=True,
        help="Expected effect size"
    )
    parser.add_argument(
        "--power", "-p",
        type=float,
        default=0.80,
        help="Desired power (default: 0.80)"
    )
    parser.add_argument(
        "--alpha", "-a",
        type=float,
        default=0.05,
        help="Significance level (default: 0.05)"
    )
    parser.add_argument(
        "--groups", "-g",
        type=int,
        default=2,
        help="Number of groups (for ANOVA)"
    )
    parser.add_argument(
        "--predictors",
        type=int,
        help="Number of predictors (for regression)"
    )
    parser.add_argument(
        "--df",
        type=int,
        help="Degrees of freedom (for chi-square)"
    )
    parser.add_argument(
        "--n",
        type=int,
        help="Sample size (for power calculation)"
    )
    parser.add_argument(
        "--table",
        action="store_true",
        help="Print power table"
    )

    args = parser.parse_args()

    print("\n" + "="*60)
    print("POWER ANALYSIS RESULTS")
    print("="*60)

    if args.test == "ttest":
        if args.n:
            result = ttest_power(args.n, args.effect_size, args.alpha)
        else:
            result = ttest_sample_size(args.effect_size, args.alpha, args.power)

    elif args.test == "paired_ttest":
        if args.n:
            result = ttest_power(args.n, args.effect_size, args.alpha, paired=True)
        else:
            result = ttest_sample_size(args.effect_size, args.alpha, args.power, paired=True)

    elif args.test == "anova":
        result = anova_sample_size(args.effect_size, args.groups, args.alpha, args.power)

    elif args.test == "correlation":
        result = correlation_sample_size(args.effect_size, args.alpha, args.power)

    elif args.test == "regression":
        n_pred = args.predictors or 3
        result = regression_sample_size(args.effect_size, n_pred, args.alpha, args.power)

    elif args.test == "chi_square":
        df = args.df or 1
        result = chi_square_sample_size(args.effect_size, df, args.alpha, args.power)

    # Print results
    print(f"\nTest: {result.get('test', args.test)}")
    print("-" * 40)

    for key, value in result.items():
        if key != "test":
            print(f"  {key}: {value}")

    # Effect size interpretation
    es_type_map = {
        "ttest": "d",
        "paired_ttest": "d",
        "anova": "f",
        "correlation": "r",
        "regression": "f2",
        "chi_square": "w"
    }

    es_type = es_type_map.get(args.test, "d")
    interpretation = effect_size_interpretation(es_type, args.effect_size)
    print(f"\nEffect size interpretation: {interpretation}")

    if args.table and args.test in ["ttest", "paired_ttest"]:
        effect_sizes = [0.2, 0.5, 0.8]
        sample_sizes = [20, 30, 50, 75, 100, 150, 200]
        print_power_table("ttest", effect_sizes, sample_sizes, args.alpha)


if __name__ == "__main__":
    main()
