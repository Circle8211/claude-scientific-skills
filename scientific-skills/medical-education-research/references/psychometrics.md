# Psychometrics in Medical Education

## Classical Test Theory (CTT)

### Fundamental Concepts

**True Score Model**:
```
Observed Score (X) = True Score (T) + Error (E)

Where:
- X = Score obtained on a test
- T = Hypothetical "true" ability
- E = Random measurement error
```

**Reliability**:
```
Reliability = True Score Variance / Observed Score Variance
           = σ²T / (σ²T + σ²E)
```

### Item Analysis

#### Item Difficulty (p-value)

```python
def item_difficulty(n_correct: int, n_total: int) -> float:
    """
    Calculate item difficulty (proportion correct).

    Interpretation:
    - p < 0.30: Difficult item
    - p = 0.30-0.70: Moderate difficulty (optimal)
    - p > 0.70: Easy item
    """
    return n_correct / n_total
```

**Optimal Difficulty**:
- For maximum discrimination: p = 0.50
- For 4-option MCQ: p = 0.62 (accounting for guessing)
- For 5-option MCQ: p = 0.60

#### Item Discrimination

```python
from scipy import stats

def item_discrimination_upper_lower(item_scores, total_scores, proportion=0.27):
    """
    Upper-Lower method for item discrimination.

    Compare performance on item between high and low scorers.
    """
    n = len(total_scores)
    cutoff = int(n * proportion)

    sorted_indices = np.argsort(total_scores)
    upper_group = sorted_indices[-cutoff:]
    lower_group = sorted_indices[:cutoff]

    p_upper = item_scores[upper_group].mean()
    p_lower = item_scores[lower_group].mean()

    discrimination = p_upper - p_lower
    return discrimination

# Interpretation:
# D > 0.40: Very good discrimination
# D = 0.30-0.39: Good discrimination
# D = 0.20-0.29: Marginal, needs review
# D < 0.20: Poor, revise or discard
```

#### Point-Biserial Correlation

```python
from scipy.stats import pointbiserialr

def point_biserial_discrimination(item_scores, total_scores):
    """
    Point-biserial correlation for item discrimination.

    Correlates dichotomous item score with continuous total score.
    """
    # Remove the item from total score (corrected point-biserial)
    corrected_total = total_scores - item_scores

    r_pbi, p_value = pointbiserialr(item_scores, corrected_total)
    return r_pbi, p_value

# Interpretation:
# r_pbi > 0.30: Excellent
# r_pbi = 0.20-0.30: Good
# r_pbi = 0.10-0.20: Marginal
# r_pbi < 0.10: Poor (item not discriminating)
# r_pbi < 0: Problematic (wrong keying or flawed item)
```

### Distractor Analysis

```python
def distractor_analysis(responses, correct_answer, total_scores):
    """
    Analyze effectiveness of each response option.

    Good distractors:
    - Selected by some students
    - Selected more by low scorers than high scorers
    - Negative point-biserial correlation
    """
    results = {}
    n_total = len(responses)

    for option in np.unique(responses):
        selected = responses == option
        n_selected = selected.sum()

        if n_selected > 0:
            mean_score = total_scores[selected].mean()
            r_pbi, _ = pointbiserialr(selected.astype(int), total_scores)

            results[option] = {
                'frequency': n_selected,
                'percentage': n_selected / n_total * 100,
                'mean_total_score': mean_score,
                'point_biserial': r_pbi,
                'is_correct': option == correct_answer
            }

    return results
```

### Reliability Estimation

#### Cronbach's Alpha

```python
def cronbachs_alpha(item_scores):
    """
    Calculate Cronbach's alpha for internal consistency.

    item_scores: 2D array (examinees × items)

    Interpretation:
    α ≥ 0.90: Excellent (high-stakes decisions)
    α = 0.80-0.89: Good (group comparisons)
    α = 0.70-0.79: Acceptable (research)
    α < 0.70: Questionable
    """
    n_items = item_scores.shape[1]
    item_variances = item_scores.var(axis=0, ddof=1)
    total_variance = item_scores.sum(axis=1).var(ddof=1)

    alpha = (n_items / (n_items - 1)) * (1 - item_variances.sum() / total_variance)
    return alpha
```

#### Kuder-Richardson 20 (KR-20)

```python
def kr20(item_scores):
    """
    KR-20 for dichotomous items (special case of alpha).
    """
    n_items = item_scores.shape[1]
    p_values = item_scores.mean(axis=0)  # Item difficulties
    pq_sum = (p_values * (1 - p_values)).sum()
    total_variance = item_scores.sum(axis=1).var(ddof=1)

    kr20 = (n_items / (n_items - 1)) * (1 - pq_sum / total_variance)
    return kr20
```

#### Standard Error of Measurement (SEM)

```python
def standard_error_of_measurement(reliability, sd_scores):
    """
    Calculate SEM from reliability and score SD.

    SEM represents expected variability in observed scores
    around the true score.
    """
    sem = sd_scores * np.sqrt(1 - reliability)
    return sem

def confidence_interval(observed_score, sem, confidence=0.95):
    """
    Calculate confidence interval around observed score.
    """
    from scipy.stats import norm
    z = norm.ppf((1 + confidence) / 2)

    lower = observed_score - z * sem
    upper = observed_score + z * sem

    return lower, upper
```

---

## Item Response Theory (IRT)

### One-Parameter Logistic Model (1PL/Rasch)

```
P(θ) = 1 / (1 + e^(-(θ - b)))

Where:
- P(θ) = Probability of correct response
- θ = Person ability
- b = Item difficulty
```

### Two-Parameter Logistic Model (2PL)

```
P(θ) = 1 / (1 + e^(-a(θ - b)))

Where:
- a = Item discrimination
- b = Item difficulty
- θ = Person ability
```

### Three-Parameter Logistic Model (3PL)

```
P(θ) = c + (1 - c) / (1 + e^(-a(θ - b)))

Where:
- c = Pseudo-guessing parameter (lower asymptote)
- a = Discrimination
- b = Difficulty
- θ = Ability
```

### Item Characteristic Curves (ICC)

```python
import numpy as np
import matplotlib.pyplot as plt

def icc_3pl(theta, a, b, c):
    """Three-parameter logistic ICC."""
    return c + (1 - c) / (1 + np.exp(-a * (theta - b)))

def plot_icc(a, b, c, item_name=""):
    """Plot item characteristic curve."""
    theta = np.linspace(-4, 4, 100)
    prob = icc_3pl(theta, a, b, c)

    plt.figure(figsize=(8, 6))
    plt.plot(theta, prob, 'b-', linewidth=2)
    plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
    plt.axvline(x=b, color='gray', linestyle='--', alpha=0.5)
    plt.xlabel('Ability (θ)')
    plt.ylabel('P(Correct)')
    plt.title(f'Item Characteristic Curve {item_name}')
    plt.ylim([0, 1])
    plt.grid(True, alpha=0.3)
    plt.show()
```

### Item Information Function

```python
def item_information(theta, a, b, c):
    """
    Calculate item information at each ability level.

    More information = more precision for ability estimation.
    """
    p = icc_3pl(theta, a, b, c)
    q = 1 - p

    # Information formula for 3PL
    info = (a**2 * q / p) * ((p - c) / (1 - c))**2
    return info

def test_information(theta, item_params):
    """
    Test information is sum of item informations.

    item_params: list of (a, b, c) tuples
    """
    total_info = np.zeros_like(theta)
    for a, b, c in item_params:
        total_info += item_information(theta, a, b, c)
    return total_info
```

### IRT Parameter Interpretation

| Parameter | Range | Interpretation |
|-----------|-------|----------------|
| b (difficulty) | -3 to +3 | Higher = more difficult |
| a (discrimination) | 0.5 to 2.5 | Higher = better discriminating |
| c (guessing) | 0 to 0.35 | Lower = less guessing |

---

## Generalizability Theory

### Variance Components

```
Total Variance = Person + Rater + Item + Occasion + Interactions + Error
```

### G-Study (Generalizability Study)

**Purpose**: Estimate variance components from data

```python
# Example: OSCE with multiple stations and raters
# Crossed design: All candidates × All stations × All raters

# Variance components:
# - σ²p: Person variance (true differences between candidates)
# - σ²s: Station variance (some stations easier/harder)
# - σ²r: Rater variance (some raters lenient/strict)
# - σ²ps: Person × Station interaction
# - σ²pr: Person × Rater interaction
# - σ²sr: Station × Rater interaction
# - σ²psr,e: Residual/error variance
```

### D-Study (Decision Study)

**Purpose**: Determine optimal measurement design

```python
def generalizability_coefficient(var_components, n_stations, n_raters):
    """
    Calculate G-coefficient (relative decisions).

    Analogous to reliability but for complex designs.
    """
    sigma_p = var_components['person']
    sigma_ps = var_components['person_x_station']
    sigma_pr = var_components['person_x_rater']
    sigma_psr = var_components['residual']

    universe_score_variance = sigma_p
    relative_error_variance = (sigma_ps / n_stations +
                                sigma_pr / n_raters +
                                sigma_psr / (n_stations * n_raters))

    g_coef = universe_score_variance / (universe_score_variance + relative_error_variance)
    return g_coef

def phi_coefficient(var_components, n_stations, n_raters):
    """
    Calculate Phi-coefficient (absolute decisions/standard setting).
    """
    sigma_p = var_components['person']
    sigma_s = var_components['station']
    sigma_r = var_components['rater']
    sigma_ps = var_components['person_x_station']
    sigma_pr = var_components['person_x_rater']
    sigma_sr = var_components['station_x_rater']
    sigma_psr = var_components['residual']

    universe_score_variance = sigma_p
    absolute_error_variance = (sigma_s / n_stations +
                                sigma_r / n_raters +
                                sigma_ps / n_stations +
                                sigma_pr / n_raters +
                                sigma_sr / (n_stations * n_raters) +
                                sigma_psr / (n_stations * n_raters))

    phi = universe_score_variance / (universe_score_variance + absolute_error_variance)
    return phi
```

### Optimization

```python
def optimize_design(var_components, target_g=0.80, max_cost=None):
    """
    Find combinations of stations/raters to achieve target reliability.

    Balance reliability against practical constraints (time, cost).
    """
    results = []

    for n_stations in range(4, 20):
        for n_raters in range(1, 4):
            g = generalizability_coefficient(var_components, n_stations, n_raters)

            if g >= target_g:
                results.append({
                    'stations': n_stations,
                    'raters': n_raters,
                    'g_coefficient': g,
                    'total_observations': n_stations * n_raters
                })

    return sorted(results, key=lambda x: x['total_observations'])
```

---

## Standard Setting

### Angoff Method

```python
def angoff_standard_setting(expert_ratings, item_max_scores):
    """
    Angoff method for setting cut scores.

    Experts estimate probability that minimally competent candidate
    would answer correctly.

    expert_ratings: 2D array (experts × items), values 0-1
    """
    # Average across experts for each item
    mean_ratings = expert_ratings.mean(axis=0)

    # Sum gives expected score for borderline candidate
    cut_score = mean_ratings.sum()

    # Standard error based on expert variability
    sem = expert_ratings.std(axis=0).mean() * np.sqrt(len(item_max_scores))

    return {
        'cut_score': cut_score,
        'cut_percentage': cut_score / item_max_scores.sum() * 100,
        'standard_error': sem
    }
```

### Borderline Regression Method

```python
from scipy import stats

def borderline_regression(checklist_scores, global_ratings):
    """
    Borderline regression for OSCE standard setting.

    Regress checklist scores on global ratings.
    Cut score = predicted checklist score for borderline global rating.

    global_ratings: Often 1-5 scale, borderline typically = 2 or 3
    """
    slope, intercept, r, p, se = stats.linregress(global_ratings, checklist_scores)

    borderline_global = 2.5  # Adjust based on your scale
    cut_score = slope * borderline_global + intercept

    return {
        'cut_score': cut_score,
        'r_squared': r**2,
        'slope': slope,
        'intercept': intercept
    }
```

### Contrasting Groups Method

```python
def contrasting_groups(scores, group_labels):
    """
    Contrasting groups standard setting.

    groups: 'pass' and 'fail' as determined by external criterion
    Cut score at intersection of distributions.
    """
    from scipy.stats import norm

    pass_scores = scores[group_labels == 'pass']
    fail_scores = scores[group_labels == 'fail']

    # Find intersection of normal distributions
    mu1, sd1 = pass_scores.mean(), pass_scores.std()
    mu2, sd2 = fail_scores.mean(), fail_scores.std()

    # Solve for intersection (quadratic formula if sd1 != sd2)
    a = 1/(2*sd1**2) - 1/(2*sd2**2)
    b = mu2/sd2**2 - mu1/sd1**2
    c = mu1**2/(2*sd1**2) - mu2**2/(2*sd2**2) - np.log(sd2/sd1)

    cut_scores = np.roots([a, b, c])

    # Select the one between the means
    cut_score = [x for x in cut_scores if mu2 < x < mu1 or mu1 < x < mu2][0]

    return cut_score
```

---

## Equating and Scaling

### Linear Equating

```python
def linear_equating(form_x_stats, form_y_stats):
    """
    Linear equating to put Form X scores on Form Y scale.

    form_x_stats: dict with 'mean' and 'sd'
    form_y_stats: dict with 'mean' and 'sd'
    """
    slope = form_y_stats['sd'] / form_x_stats['sd']
    intercept = form_y_stats['mean'] - slope * form_x_stats['mean']

    def convert(x_score):
        return slope * x_score + intercept

    return convert
```

### Equipercentile Equating

```python
def equipercentile_equating(form_x_scores, form_y_scores):
    """
    Equipercentile equating using percentile ranks.
    """
    from scipy import interpolate

    # Calculate percentile ranks for both forms
    x_percentiles = np.percentile(form_x_scores, np.arange(0, 101))
    y_percentiles = np.percentile(form_y_scores, np.arange(0, 101))

    # Create conversion function
    convert = interpolate.interp1d(x_percentiles, y_percentiles,
                                    bounds_error=False, fill_value='extrapolate')

    return convert
```
