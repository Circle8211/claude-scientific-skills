# Effect Sizes in Psychology Research

## Overview

Effect sizes quantify the magnitude of a phenomenon or the strength of a relationship, independent of sample size. They are essential for:
- Interpreting practical significance
- Comparing across studies
- Meta-analysis
- Power analysis

---

## Standardized Mean Difference Family

### Cohen's d

**Use**: Comparing two group means

**Formula**:
```
d = (M₁ - M₂) / SD_pooled

Where:
SD_pooled = √[((n₁-1)s₁² + (n₂-1)s₂²) / (n₁+n₂-2)]
```

**Interpretation** (Cohen, 1988):
| d | Interpretation |
|---|----------------|
| 0.20 | Small |
| 0.50 | Medium |
| 0.80 | Large |

**Python Implementation**:
```python
import numpy as np

def cohens_d(group1, group2):
    """Calculate Cohen's d with pooled standard deviation."""
    n1, n2 = len(group1), len(group2)
    var1 = np.var(group1, ddof=1)
    var2 = np.var(group2, ddof=1)

    pooled_sd = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    d = (np.mean(group1) - np.mean(group2)) / pooled_sd

    return d
```

### Hedges' g

**Use**: Corrects Cohen's d for small sample bias

**Formula**:
```
g = d × J

Where J ≈ 1 - 3/(4(n₁+n₂) - 9)
```

**When to use**: Preferred when n < 20 per group or for meta-analysis

```python
def hedges_g(group1, group2):
    """Hedges' g with small sample correction."""
    d = cohens_d(group1, group2)
    n = len(group1) + len(group2)
    j = 1 - (3 / (4*(n - 2) - 1))
    return d * j
```

### Glass's Δ (Delta)

**Use**: When control group SD is theoretically more appropriate

**Formula**:
```
Δ = (M_treatment - M_control) / SD_control
```

**When to use**: When treatment may affect variability

### Cohen's d for Paired Data

**Formula**:
```
d_z = (M_diff) / SD_diff

Or (using correlation):
d_av = (M₁ - M₂) / √[(s₁² + s₂²)/2]

d_rm = (M₁ - M₂) / √[s₁² + s₂² - 2rs₁s₂] × √[2(1-r)]
```

```python
def cohens_d_paired(before, after):
    """Cohen's d for paired samples (dz)."""
    diff = np.array(after) - np.array(before)
    return np.mean(diff) / np.std(diff, ddof=1)
```

---

## Correlation Family

### Pearson's r

**Use**: Linear relationship between continuous variables

**Interpretation**:
| |r| | Interpretation |
|---|----------------|
| 0.10 | Small |
| 0.30 | Medium |
| 0.50 | Large |

**Coefficient of Determination**: r² = proportion of shared variance

```python
from scipy import stats

def correlation_effect(x, y):
    """Calculate r and r-squared."""
    r, p = stats.pearsonr(x, y)
    return {
        'r': r,
        'r_squared': r**2,
        'p_value': p,
        'interpretation': 'small' if abs(r) < 0.3 else 'medium' if abs(r) < 0.5 else 'large'
    }
```

### Point-Biserial Correlation (rpb)

**Use**: Correlation between continuous and binary variable

**Interpretation**: Same as Pearson's r

### Spearman's ρ (rho)

**Use**: Monotonic relationship (ordinal data or non-linear)

**Interpretation**: Same as Pearson's r

---

## Variance-Explained Family

### Eta-Squared (η²)

**Use**: Proportion of variance explained in ANOVA

**Formula**:
```
η² = SS_effect / SS_total
```

**Interpretation**:
| η² | Interpretation |
|---|----------------|
| 0.01 | Small |
| 0.06 | Medium |
| 0.14 | Large |

**Limitation**: Overestimates population effect (especially with small N)

### Partial Eta-Squared (η²p)

**Use**: Variance explained controlling for other factors

**Formula**:
```
η²p = SS_effect / (SS_effect + SS_error)
```

**Note**: Most commonly reported in factorial ANOVA
**Interpretation**: Same as η²

```python
def partial_eta_squared(ss_effect, ss_error):
    """Calculate partial eta-squared."""
    return ss_effect / (ss_effect + ss_error)

def eta_squared_from_F(F, df_effect, df_error):
    """Calculate eta-squared from F statistic."""
    ss_effect = F * df_effect
    ss_error = df_error
    return ss_effect / (ss_effect + ss_error)
```

### Omega-Squared (ω²)

**Use**: Less biased estimate of population effect

**Formula**:
```
ω² = (SS_effect - df_effect × MS_error) / (SS_total + MS_error)
```

**Advantage**: Adjusts for sample size bias

```python
def omega_squared(ss_effect, ss_total, df_effect, ms_error):
    """Calculate omega-squared (less biased than eta-squared)."""
    return (ss_effect - df_effect * ms_error) / (ss_total + ms_error)
```

### R-Squared (R²)

**Use**: Proportion of variance explained in regression

**Adjusted R²**:
```
R²_adj = 1 - [(1-R²)(n-1)/(n-k-1)]

Where k = number of predictors
```

### Cohen's f

**Use**: ANOVA effect size for power analysis

**Formula**:
```
f = √(η² / (1 - η²))
```

**Interpretation**:
| f | Interpretation |
|---|----------------|
| 0.10 | Small |
| 0.25 | Medium |
| 0.40 | Large |

```python
def cohens_f_from_eta(eta_sq):
    """Convert eta-squared to Cohen's f."""
    return np.sqrt(eta_sq / (1 - eta_sq))

def cohens_f_squared(r_sq):
    """Cohen's f² for regression."""
    return r_sq / (1 - r_sq)
```

---

## Odds Ratio and Risk

### Odds Ratio (OR)

**Use**: Binary outcomes, logistic regression

**Formula**:
```
       | Outcome + | Outcome - |
Exposed|    a      |     b     |
Control|    c      |     d     |

OR = (a/b) / (c/d) = ad/bc
```

**Interpretation**:
| OR | Interpretation |
|---|----------------|
| 1.5 | Small |
| 2.5 | Medium |
| 4.3 | Large |

**Note**: OR ≈ 1 = no effect

```python
def odds_ratio(a, b, c, d):
    """
    Calculate odds ratio from 2x2 table.

    a: exposed with outcome
    b: exposed without outcome
    c: unexposed with outcome
    d: unexposed without outcome
    """
    or_val = (a * d) / (b * c)
    se = np.sqrt(1/a + 1/b + 1/c + 1/d)
    ci_lower = np.exp(np.log(or_val) - 1.96 * se)
    ci_upper = np.exp(np.log(or_val) + 1.96 * se)

    return {'OR': or_val, 'CI': (ci_lower, ci_upper)}
```

### Relative Risk (RR)

**Use**: Prospective studies, true incidence rates

**Formula**:
```
RR = [a/(a+b)] / [c/(c+d)]
```

**Interpretation**: Similar to OR for rare outcomes

### Number Needed to Treat (NNT)

**Use**: Clinical significance of treatment effects

**Formula**:
```
NNT = 1 / |ARR|

Where ARR = Absolute Risk Reduction = Risk_control - Risk_treatment
```

**Interpretation**: Number of patients needed to treat to prevent one adverse outcome

---

## Categorical Data

### Phi Coefficient (φ)

**Use**: 2×2 contingency tables

**Formula**:
```
φ = (ad - bc) / √[(a+b)(c+d)(a+c)(b+d)]
```

**Interpretation**: Same as r

### Cramér's V

**Use**: Larger contingency tables

**Formula**:
```
V = √(χ²/n(k-1))

Where k = min(rows, columns)
```

**Interpretation**:
| V | Interpretation (df*=1) | Interpretation (df*≥2) |
|---|----------------------|------------------------|
| 0.10 | Small | Small |
| 0.30 | Medium | 0.21 Medium |
| 0.50 | Large | 0.35 Large |

### Cohen's w

**Use**: Chi-square tests

**Formula**:
```
w = √(Σ(P₀ᵢ - P₁ᵢ)² / P₀ᵢ)
```

**Interpretation**:
| w | Interpretation |
|---|----------------|
| 0.10 | Small |
| 0.30 | Medium |
| 0.50 | Large |

---

## Effect Size Conversions

```python
import numpy as np

def d_to_r(d):
    """Convert Cohen's d to correlation r."""
    return d / np.sqrt(d**2 + 4)

def r_to_d(r):
    """Convert correlation r to Cohen's d."""
    return (2 * r) / np.sqrt(1 - r**2)

def d_to_or(d):
    """Convert Cohen's d to odds ratio."""
    return np.exp(d * np.pi / np.sqrt(3))

def or_to_d(odds_ratio):
    """Convert odds ratio to Cohen's d."""
    return np.log(odds_ratio) * np.sqrt(3) / np.pi

def eta_to_d(eta_sq, n1, n2):
    """Convert eta-squared to Cohen's d."""
    return 2 * np.sqrt(eta_sq / (1 - eta_sq))

def d_to_eta(d):
    """Convert Cohen's d to eta-squared."""
    return d**2 / (d**2 + 4)

def f_to_eta(f):
    """Convert Cohen's f to eta-squared."""
    return f**2 / (1 + f**2)

def eta_to_f(eta_sq):
    """Convert eta-squared to Cohen's f."""
    return np.sqrt(eta_sq / (1 - eta_sq))
```

---

## Confidence Intervals for Effect Sizes

### CI for Cohen's d

```python
from scipy import stats

def d_confidence_interval(d, n1, n2, confidence=0.95):
    """
    Calculate confidence interval for Cohen's d.

    Uses noncentral t distribution.
    """
    # Approximate SE for d
    se = np.sqrt((n1 + n2) / (n1 * n2) + d**2 / (2 * (n1 + n2)))

    # t critical value
    df = n1 + n2 - 2
    t_crit = stats.t.ppf((1 + confidence) / 2, df)

    ci_lower = d - t_crit * se
    ci_upper = d + t_crit * se

    return (ci_lower, ci_upper)
```

### CI for Correlation

```python
def r_confidence_interval(r, n, confidence=0.95):
    """
    Calculate confidence interval for r using Fisher's z transformation.
    """
    # Fisher's z
    z = np.arctanh(r)
    se = 1 / np.sqrt(n - 3)

    z_crit = stats.norm.ppf((1 + confidence) / 2)

    z_lower = z - z_crit * se
    z_upper = z + z_crit * se

    # Transform back
    r_lower = np.tanh(z_lower)
    r_upper = np.tanh(z_upper)

    return (r_lower, r_upper)
```

---

## Effect Size Selection Guide

| Analysis | Recommended Effect Size |
|----------|------------------------|
| t-test (independent) | Cohen's d or Hedges' g |
| t-test (paired) | Cohen's d (dz or drm) |
| One-way ANOVA | η², ω², or Cohen's f |
| Factorial ANOVA | Partial η² |
| Correlation | r and r² |
| Regression | R², ΔR², f² |
| Chi-square (2×2) | φ or OR |
| Chi-square (larger) | Cramér's V |
| Logistic regression | OR |
| Mixed ANOVA | Partial η² per effect |

---

## Reporting Standards (APA 7th)

**Required**: Effect sizes with confidence intervals

**Examples**:
```
"There was a significant difference between groups,
t(58) = 2.45, p = .017, d = 0.64, 95% CI [0.12, 1.15]."

"The model explained significant variance, R² = .34,
F(3, 96) = 16.52, p < .001, f² = 0.52."

"The correlation was significant, r(98) = .42,
p < .001, 95% CI [.24, .57]."

"There was a significant main effect of condition,
F(2, 87) = 5.23, p = .007, η²p = .11, 90% CI [.02, .21]."
```
