#!/usr/bin/env python3
"""
Effect Size Calculator for Psychology Research

Calculate and convert between different effect size measures.

Usage:
    python effect_size_calculator.py --type cohens_d --m1 10.5 --m2 8.2 --sd1 2.1 --sd2 2.3
    python effect_size_calculator.py --type from_t --t 2.45 --n1 30 --n2 30
    python effect_size_calculator.py --convert --from d --to r --value 0.5
"""

import argparse
import math
import numpy as np
from scipy import stats
from typing import Dict, Tuple, Optional


def cohens_d(
    m1: float, m2: float,
    sd1: float, sd2: float,
    n1: int, n2: int,
    pooled: bool = True
) -> Dict:
    """
    Calculate Cohen's d effect size.

    Args:
        m1, m2: Group means
        sd1, sd2: Group standard deviations
        n1, n2: Group sample sizes
        pooled: Use pooled SD (True) or control group SD (False)

    Returns:
        Dictionary with d and confidence interval
    """
    mean_diff = m1 - m2

    if pooled:
        # Pooled standard deviation
        pooled_var = ((n1 - 1) * sd1**2 + (n2 - 1) * sd2**2) / (n1 + n2 - 2)
        pooled_sd = math.sqrt(pooled_var)
        d = mean_diff / pooled_sd
        es_type = "Cohen's d (pooled SD)"
    else:
        # Glass's delta (control group SD)
        d = mean_diff / sd2
        pooled_sd = sd2
        es_type = "Glass's delta"

    # Standard error of d
    se = math.sqrt((n1 + n2) / (n1 * n2) + d**2 / (2 * (n1 + n2)))

    # 95% CI
    ci_lower = d - 1.96 * se
    ci_upper = d + 1.96 * se

    return {
        "type": es_type,
        "d": round(d, 4),
        "se": round(se, 4),
        "ci_95": (round(ci_lower, 4), round(ci_upper, 4)),
        "interpretation": interpret_d(d)
    }


def hedges_g(d: float, n1: int, n2: int) -> Dict:
    """
    Calculate Hedges' g (bias-corrected d).

    Args:
        d: Cohen's d value
        n1, n2: Group sample sizes

    Returns:
        Dictionary with g value
    """
    # Correction factor J
    df = n1 + n2 - 2
    j = 1 - (3 / (4 * df - 1))
    g = d * j

    # Standard error
    se = math.sqrt((n1 + n2) / (n1 * n2) + g**2 / (2 * (n1 + n2)))
    ci_lower = g - 1.96 * se
    ci_upper = g + 1.96 * se

    return {
        "type": "Hedges' g",
        "g": round(g, 4),
        "correction_factor": round(j, 4),
        "ci_95": (round(ci_lower, 4), round(ci_upper, 4)),
        "interpretation": interpret_d(g)
    }


def cohens_d_paired(
    mean_diff: float,
    sd_diff: float,
    n: int,
    correlation: Optional[float] = None
) -> Dict:
    """
    Calculate Cohen's d for paired/repeated measures.

    Args:
        mean_diff: Mean of differences
        sd_diff: Standard deviation of differences
        n: Number of pairs
        correlation: Pre-post correlation (for alternative formula)

    Returns:
        Dictionary with d values
    """
    # dz (standardized by SD of differences)
    dz = mean_diff / sd_diff

    # Standard error
    se_dz = math.sqrt(1/n + dz**2 / (2*n))
    ci_lower = dz - 1.96 * se_dz
    ci_upper = dz + 1.96 * se_dz

    result = {
        "dz": round(dz, 4),
        "se_dz": round(se_dz, 4),
        "ci_95_dz": (round(ci_lower, 4), round(ci_upper, 4)),
        "interpretation": interpret_d(dz)
    }

    # If correlation provided, calculate dav and drm
    if correlation is not None:
        # dav (average variance standardizer)
        dav = dz * math.sqrt(2 * (1 - correlation))
        result["dav"] = round(dav, 4)

        # drm (repeated measures d with correction)
        drm = dz * math.sqrt(2 * (1 - correlation))
        result["drm"] = round(drm, 4)

    return result


def d_from_t(t: float, n1: int, n2: int) -> Dict:
    """
    Calculate Cohen's d from t-statistic.

    Args:
        t: t-statistic value
        n1, n2: Group sample sizes

    Returns:
        Dictionary with d value
    """
    d = t * math.sqrt((n1 + n2) / (n1 * n2))

    se = math.sqrt((n1 + n2) / (n1 * n2) + d**2 / (2 * (n1 + n2)))
    ci_lower = d - 1.96 * se
    ci_upper = d + 1.96 * se

    return {
        "type": "Cohen's d (from t)",
        "d": round(d, 4),
        "t": t,
        "ci_95": (round(ci_lower, 4), round(ci_upper, 4)),
        "interpretation": interpret_d(d)
    }


def eta_squared(ss_effect: float, ss_total: float) -> Dict:
    """
    Calculate eta-squared from sum of squares.
    """
    eta2 = ss_effect / ss_total

    return {
        "type": "Eta-squared",
        "eta2": round(eta2, 4),
        "percentage": f"{round(eta2 * 100, 2)}%",
        "interpretation": interpret_eta2(eta2)
    }


def partial_eta_squared(ss_effect: float, ss_error: float) -> Dict:
    """
    Calculate partial eta-squared.
    """
    eta2p = ss_effect / (ss_effect + ss_error)

    return {
        "type": "Partial eta-squared",
        "eta2p": round(eta2p, 4),
        "percentage": f"{round(eta2p * 100, 2)}%",
        "interpretation": interpret_eta2(eta2p)
    }


def omega_squared(
    ss_effect: float,
    ss_total: float,
    df_effect: int,
    ms_error: float
) -> Dict:
    """
    Calculate omega-squared (less biased than eta-squared).
    """
    omega2 = (ss_effect - df_effect * ms_error) / (ss_total + ms_error)
    omega2 = max(0, omega2)  # Cannot be negative

    return {
        "type": "Omega-squared",
        "omega2": round(omega2, 4),
        "percentage": f"{round(omega2 * 100, 2)}%",
        "interpretation": interpret_eta2(omega2)
    }


def cohens_f(eta2: float) -> Dict:
    """
    Calculate Cohen's f from eta-squared.
    """
    f = math.sqrt(eta2 / (1 - eta2))

    return {
        "type": "Cohen's f",
        "f": round(f, 4),
        "interpretation": interpret_f(f)
    }


def correlation_to_r2(r: float) -> Dict:
    """
    Convert correlation to R-squared.
    """
    r2 = r ** 2

    return {
        "type": "R-squared",
        "r": round(r, 4),
        "r2": round(r2, 4),
        "percentage": f"{round(r2 * 100, 2)}%",
        "interpretation": interpret_r(r)
    }


def r_confidence_interval(r: float, n: int, confidence: float = 0.95) -> Tuple[float, float]:
    """
    Calculate confidence interval for correlation using Fisher's z.
    """
    # Fisher's z transformation
    z = 0.5 * math.log((1 + r) / (1 - r))
    se = 1 / math.sqrt(n - 3)

    z_crit = stats.norm.ppf((1 + confidence) / 2)

    z_lower = z - z_crit * se
    z_upper = z + z_crit * se

    # Back-transform
    r_lower = (math.exp(2 * z_lower) - 1) / (math.exp(2 * z_lower) + 1)
    r_upper = (math.exp(2 * z_upper) - 1) / (math.exp(2 * z_upper) + 1)

    return (round(r_lower, 4), round(r_upper, 4))


def odds_ratio(a: int, b: int, c: int, d: int) -> Dict:
    """
    Calculate odds ratio from 2x2 contingency table.

    Table format:
              Outcome+  Outcome-
    Exposed      a         b
    Control      c         d
    """
    or_val = (a * d) / (b * c)

    # Log odds ratio SE
    se_log = math.sqrt(1/a + 1/b + 1/c + 1/d)

    # 95% CI on log scale, then transform
    log_or = math.log(or_val)
    ci_lower = math.exp(log_or - 1.96 * se_log)
    ci_upper = math.exp(log_or + 1.96 * se_log)

    return {
        "type": "Odds Ratio",
        "OR": round(or_val, 4),
        "log_OR": round(log_or, 4),
        "ci_95": (round(ci_lower, 4), round(ci_upper, 4)),
        "interpretation": interpret_or(or_val)
    }


# Conversion functions
def d_to_r(d: float) -> float:
    """Convert Cohen's d to correlation r."""
    return d / math.sqrt(d**2 + 4)


def r_to_d(r: float) -> float:
    """Convert correlation r to Cohen's d."""
    return (2 * r) / math.sqrt(1 - r**2)


def d_to_odds_ratio(d: float) -> float:
    """Convert Cohen's d to odds ratio."""
    return math.exp(d * math.pi / math.sqrt(3))


def odds_ratio_to_d(or_val: float) -> float:
    """Convert odds ratio to Cohen's d."""
    return math.log(or_val) * math.sqrt(3) / math.pi


def eta2_to_f(eta2: float) -> float:
    """Convert eta-squared to Cohen's f."""
    return math.sqrt(eta2 / (1 - eta2))


def f_to_eta2(f: float) -> float:
    """Convert Cohen's f to eta-squared."""
    return f**2 / (1 + f**2)


def d_to_eta2(d: float) -> float:
    """Convert Cohen's d to eta-squared (for two groups)."""
    return d**2 / (d**2 + 4)


# Interpretation functions
def interpret_d(d: float) -> str:
    """Interpret Cohen's d magnitude."""
    d = abs(d)
    if d < 0.2:
        return "negligible"
    elif d < 0.5:
        return "small"
    elif d < 0.8:
        return "medium"
    else:
        return "large"


def interpret_r(r: float) -> str:
    """Interpret correlation magnitude."""
    r = abs(r)
    if r < 0.1:
        return "negligible"
    elif r < 0.3:
        return "small"
    elif r < 0.5:
        return "medium"
    else:
        return "large"


def interpret_eta2(eta2: float) -> str:
    """Interpret eta-squared magnitude."""
    if eta2 < 0.01:
        return "negligible"
    elif eta2 < 0.06:
        return "small"
    elif eta2 < 0.14:
        return "medium"
    else:
        return "large"


def interpret_f(f: float) -> str:
    """Interpret Cohen's f magnitude."""
    if f < 0.1:
        return "negligible"
    elif f < 0.25:
        return "small"
    elif f < 0.4:
        return "medium"
    else:
        return "large"


def interpret_or(or_val: float) -> str:
    """Interpret odds ratio magnitude."""
    or_val = max(or_val, 1/or_val)  # Normalize direction
    if or_val < 1.5:
        return "negligible"
    elif or_val < 2.5:
        return "small"
    elif or_val < 4.3:
        return "medium"
    else:
        return "large"


def convert_effect_size(from_type: str, to_type: str, value: float) -> Dict:
    """
    Convert between effect size types.
    """
    converters = {
        ("d", "r"): d_to_r,
        ("r", "d"): r_to_d,
        ("d", "or"): d_to_odds_ratio,
        ("or", "d"): odds_ratio_to_d,
        ("d", "eta2"): d_to_eta2,
        ("eta2", "f"): eta2_to_f,
        ("f", "eta2"): f_to_eta2,
    }

    key = (from_type.lower(), to_type.lower())

    if key in converters:
        result = converters[key](value)
        return {
            "from": from_type,
            "from_value": value,
            "to": to_type,
            "to_value": round(result, 4)
        }
    else:
        return {"error": f"Conversion from {from_type} to {to_type} not supported"}


def main():
    parser = argparse.ArgumentParser(
        description="Calculate and convert effect sizes"
    )

    parser.add_argument(
        "--type", "-t",
        choices=["cohens_d", "hedges_g", "paired_d", "from_t", "eta2", "partial_eta2",
                 "omega2", "cohens_f", "r", "odds_ratio"],
        help="Effect size type to calculate"
    )

    # For Cohen's d
    parser.add_argument("--m1", type=float, help="Mean of group 1")
    parser.add_argument("--m2", type=float, help="Mean of group 2")
    parser.add_argument("--sd1", type=float, help="SD of group 1")
    parser.add_argument("--sd2", type=float, help="SD of group 2")
    parser.add_argument("--n1", type=int, help="N of group 1")
    parser.add_argument("--n2", type=int, help="N of group 2")

    # For paired d
    parser.add_argument("--mean-diff", type=float, help="Mean difference")
    parser.add_argument("--sd-diff", type=float, help="SD of differences")
    parser.add_argument("--n", type=int, help="Sample size")
    parser.add_argument("--correlation", type=float, help="Pre-post correlation")

    # For t-statistic conversion
    parser.add_argument("--t", type=float, help="t-statistic")

    # For ANOVA effect sizes
    parser.add_argument("--ss-effect", type=float, help="SS effect")
    parser.add_argument("--ss-error", type=float, help="SS error")
    parser.add_argument("--ss-total", type=float, help="SS total")
    parser.add_argument("--df-effect", type=int, help="df effect")
    parser.add_argument("--ms-error", type=float, help="MS error")

    # For correlation
    parser.add_argument("--r", type=float, help="Correlation coefficient")

    # For odds ratio
    parser.add_argument("--a", type=int, help="Cell a (exposed, outcome+)")
    parser.add_argument("--b", type=int, help="Cell b (exposed, outcome-)")
    parser.add_argument("--c", type=int, help="Cell c (control, outcome+)")
    parser.add_argument("--d", type=int, help="Cell d (control, outcome-)")

    # Conversion
    parser.add_argument("--convert", action="store_true", help="Convert between effect sizes")
    parser.add_argument("--from", dest="from_type", help="Source effect size type")
    parser.add_argument("--to", help="Target effect size type")
    parser.add_argument("--value", type=float, help="Value to convert")

    args = parser.parse_args()

    print("\n" + "="*60)
    print("EFFECT SIZE CALCULATOR")
    print("="*60)

    if args.convert:
        result = convert_effect_size(args.from_type, args.to, args.value)
        print(f"\nConversion: {args.from_type} → {args.to}")
        print("-" * 40)
        for key, value in result.items():
            print(f"  {key}: {value}")

    elif args.type == "cohens_d":
        result = cohens_d(args.m1, args.m2, args.sd1, args.sd2, args.n1, args.n2)
        print("\nCohen's d Calculation")
        print("-" * 40)
        for key, value in result.items():
            print(f"  {key}: {value}")

        # Also calculate Hedges' g
        g_result = hedges_g(result["d"], args.n1, args.n2)
        print(f"\n  Hedges' g: {g_result['g']} (correction factor: {g_result['correction_factor']})")

    elif args.type == "from_t":
        result = d_from_t(args.t, args.n1, args.n2)
        print("\nCohen's d from t-statistic")
        print("-" * 40)
        for key, value in result.items():
            print(f"  {key}: {value}")

    elif args.type == "paired_d":
        result = cohens_d_paired(args.mean_diff, args.sd_diff, args.n, args.correlation)
        print("\nPaired Samples Effect Size")
        print("-" * 40)
        for key, value in result.items():
            print(f"  {key}: {value}")

    elif args.type == "eta2":
        result = eta_squared(args.ss_effect, args.ss_total)
        print("\nEta-squared")
        print("-" * 40)
        for key, value in result.items():
            print(f"  {key}: {value}")

    elif args.type == "r":
        result = correlation_to_r2(args.r)
        ci = r_confidence_interval(args.r, args.n or 100)
        print("\nCorrelation Effect Size")
        print("-" * 40)
        for key, value in result.items():
            print(f"  {key}: {value}")
        print(f"  95% CI: {ci}")

    elif args.type == "odds_ratio":
        result = odds_ratio(args.a, args.b, args.c, args.d)
        print("\nOdds Ratio")
        print("-" * 40)
        for key, value in result.items():
            print(f"  {key}: {value}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
