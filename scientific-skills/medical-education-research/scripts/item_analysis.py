#!/usr/bin/env python3
"""
Item Analysis for Medical Education Assessments

Performs classical test theory analysis on MCQ and other assessment data.
Calculates difficulty, discrimination, and reliability metrics.

Usage:
    python item_analysis.py --data exam_responses.csv --key answer_key.csv
    python item_analysis.py --data responses.csv --correct-col correct --score-col total
"""

import argparse
import numpy as np
import pandas as pd
from scipy import stats
from typing import Dict, List, Tuple, Optional


def calculate_item_difficulty(responses: np.ndarray) -> float:
    """
    Calculate item difficulty (p-value).

    Args:
        responses: Binary array of correct (1) and incorrect (0) responses

    Returns:
        Proportion of correct responses (0-1)
    """
    return np.mean(responses)


def calculate_discrimination_index(
    item_responses: np.ndarray,
    total_scores: np.ndarray,
    method: str = "point_biserial"
) -> Dict[str, float]:
    """
    Calculate item discrimination using multiple methods.

    Args:
        item_responses: Binary array for single item
        total_scores: Array of total test scores
        method: "point_biserial" or "upper_lower"

    Returns:
        Dictionary with discrimination statistics
    """
    # Corrected point-biserial (remove item from total)
    corrected_total = total_scores - item_responses
    rpb, p_value = stats.pointbiserialr(item_responses, corrected_total)

    result = {
        "point_biserial": round(rpb, 3),
        "p_value": round(p_value, 4)
    }

    # Upper-lower 27% method
    n = len(total_scores)
    cutoff = int(n * 0.27)

    sorted_indices = np.argsort(total_scores)
    upper_group = sorted_indices[-cutoff:]
    lower_group = sorted_indices[:cutoff]

    p_upper = item_responses[upper_group].mean()
    p_lower = item_responses[lower_group].mean()
    d_index = p_upper - p_lower

    result["upper_lower_D"] = round(d_index, 3)

    return result


def distractor_analysis(
    responses: np.ndarray,
    correct_answer: str,
    total_scores: np.ndarray
) -> pd.DataFrame:
    """
    Analyze effectiveness of each response option.

    Args:
        responses: Array of response options selected
        correct_answer: The correct option
        total_scores: Array of total test scores

    Returns:
        DataFrame with distractor statistics
    """
    results = []
    n_total = len(responses)

    for option in np.unique(responses):
        selected = responses == option
        n_selected = selected.sum()

        if n_selected > 0:
            mean_score = total_scores[selected].mean()
            # Point-biserial for this option
            rpb, _ = stats.pointbiserialr(selected.astype(int), total_scores)

            results.append({
                "option": option,
                "n": n_selected,
                "percentage": round(n_selected / n_total * 100, 1),
                "mean_total_score": round(mean_score, 2),
                "point_biserial": round(rpb, 3),
                "is_correct": option == correct_answer,
                "quality": "Good" if (option == correct_answer and rpb > 0) or
                                    (option != correct_answer and rpb < 0) else "Review"
            })

    return pd.DataFrame(results)


def cronbachs_alpha(item_scores: np.ndarray) -> Dict[str, float]:
    """
    Calculate Cronbach's alpha for internal consistency.

    Args:
        item_scores: 2D array (examinees × items)

    Returns:
        Dictionary with alpha and interpretation
    """
    n_items = item_scores.shape[1]
    item_variances = np.var(item_scores, axis=0, ddof=1)
    total_variance = np.var(np.sum(item_scores, axis=1), ddof=1)

    alpha = (n_items / (n_items - 1)) * (1 - np.sum(item_variances) / total_variance)

    # Interpretation
    if alpha >= 0.90:
        interpretation = "Excellent (suitable for high-stakes decisions)"
    elif alpha >= 0.80:
        interpretation = "Good (suitable for group comparisons)"
    elif alpha >= 0.70:
        interpretation = "Acceptable (suitable for research)"
    elif alpha >= 0.60:
        interpretation = "Questionable"
    else:
        interpretation = "Poor"

    return {
        "alpha": round(alpha, 3),
        "interpretation": interpretation,
        "n_items": n_items
    }


def standard_error_of_measurement(reliability: float, sd_scores: float) -> float:
    """
    Calculate Standard Error of Measurement.

    Args:
        reliability: Reliability coefficient (e.g., Cronbach's alpha)
        sd_scores: Standard deviation of total scores

    Returns:
        SEM value
    """
    return sd_scores * np.sqrt(1 - reliability)


def item_quality_flags(
    difficulty: float,
    discrimination: float
) -> List[str]:
    """
    Generate quality flags for an item.

    Args:
        difficulty: Item difficulty (p-value)
        discrimination: Item discrimination index

    Returns:
        List of quality flags/recommendations
    """
    flags = []

    # Difficulty flags
    if difficulty < 0.20:
        flags.append("Very difficult - consider revising or removing")
    elif difficulty < 0.30:
        flags.append("Difficult - review for clarity")
    elif difficulty > 0.90:
        flags.append("Very easy - may not discriminate well")
    elif difficulty > 0.80:
        flags.append("Easy - consider if appropriate for level")

    # Discrimination flags
    if discrimination < 0:
        flags.append("NEGATIVE DISCRIMINATION - check answer key")
    elif discrimination < 0.10:
        flags.append("Poor discrimination - consider removing")
    elif discrimination < 0.20:
        flags.append("Marginal discrimination - review item")

    if not flags:
        flags.append("Item meets quality standards")

    return flags


def full_item_analysis(
    responses: pd.DataFrame,
    answer_key: Optional[pd.Series] = None,
    correct_col: Optional[str] = None
) -> Tuple[pd.DataFrame, Dict]:
    """
    Perform comprehensive item analysis.

    Args:
        responses: DataFrame with item responses (one column per item)
        answer_key: Series with correct answers for each item
        correct_col: Column prefix for pre-scored correct columns

    Returns:
        Tuple of (item statistics DataFrame, test statistics dict)
    """
    if answer_key is not None:
        # Convert to binary scored
        item_scores = responses.apply(lambda col: (col == answer_key[col.name]).astype(int))
    elif correct_col:
        item_scores = responses.filter(like=correct_col)
    else:
        # Assume already binary scored
        item_scores = responses

    total_scores = item_scores.sum(axis=1)

    item_stats = []
    for col in item_scores.columns:
        item_data = item_scores[col].values

        difficulty = calculate_item_difficulty(item_data)
        discrimination = calculate_discrimination_index(item_data, total_scores.values)

        item_stats.append({
            "item": col,
            "difficulty": round(difficulty, 3),
            "discrimination_rpb": discrimination["point_biserial"],
            "discrimination_D": discrimination["upper_lower_D"],
            "p_value": discrimination["p_value"],
            "quality": item_quality_flags(difficulty, discrimination["point_biserial"])
        })

    item_df = pd.DataFrame(item_stats)

    # Test-level statistics
    alpha_stats = cronbachs_alpha(item_scores.values)
    sem = standard_error_of_measurement(alpha_stats["alpha"], total_scores.std())

    test_stats = {
        "n_examinees": len(responses),
        "n_items": len(item_scores.columns),
        "mean_score": round(total_scores.mean(), 2),
        "sd_score": round(total_scores.std(), 2),
        "min_score": int(total_scores.min()),
        "max_score": int(total_scores.max()),
        "mean_difficulty": round(item_df["difficulty"].mean(), 3),
        "cronbachs_alpha": alpha_stats["alpha"],
        "alpha_interpretation": alpha_stats["interpretation"],
        "sem": round(sem, 2)
    }

    return item_df, test_stats


def main():
    parser = argparse.ArgumentParser(
        description="Perform item analysis on assessment data"
    )
    parser.add_argument(
        "--data", "-d",
        required=True,
        help="Path to CSV file with response data"
    )
    parser.add_argument(
        "--key", "-k",
        help="Path to CSV file with answer key"
    )
    parser.add_argument(
        "--correct-col",
        help="Column prefix for pre-scored correct columns"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output path for results CSV"
    )
    parser.add_argument(
        "--format",
        choices=["csv", "json", "text"],
        default="text",
        help="Output format"
    )

    args = parser.parse_args()

    # Load data
    responses = pd.read_csv(args.data)

    answer_key = None
    if args.key:
        key_df = pd.read_csv(args.key)
        answer_key = key_df.iloc[0]  # Assume first row is answers

    # Run analysis
    item_stats, test_stats = full_item_analysis(
        responses,
        answer_key=answer_key,
        correct_col=args.correct_col
    )

    # Output results
    if args.format == "text":
        print("\n" + "="*60)
        print("ITEM ANALYSIS REPORT")
        print("="*60)

        print("\nTEST-LEVEL STATISTICS")
        print("-"*40)
        for key, value in test_stats.items():
            print(f"  {key}: {value}")

        print("\nITEM-LEVEL STATISTICS")
        print("-"*40)
        print(item_stats.to_string(index=False))

        print("\nITEM QUALITY SUMMARY")
        print("-"*40)
        problematic = item_stats[
            (item_stats["difficulty"] < 0.20) |
            (item_stats["difficulty"] > 0.90) |
            (item_stats["discrimination_rpb"] < 0.15)
        ]
        if len(problematic) > 0:
            print(f"  {len(problematic)} items flagged for review")
            for _, row in problematic.iterrows():
                print(f"    - {row['item']}: {row['quality']}")
        else:
            print("  All items meet quality standards")

    elif args.format == "csv":
        if args.output:
            item_stats.to_csv(args.output, index=False)
            print(f"Results saved to {args.output}")
        else:
            print(item_stats.to_csv(index=False))

    elif args.format == "json":
        import json
        output = {
            "test_statistics": test_stats,
            "item_statistics": item_stats.to_dict(orient="records")
        }
        print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
