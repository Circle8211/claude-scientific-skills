---
name: psychology-research
description: Design psychology studies, analyze behavioral data, use validated instruments, and conduct statistical analyses for psychological research
allowed-tools: [Read, Write, Edit, Bash]
license: MIT License
metadata:
    skill-author: K-Dense Inc.
---

# Psychology Research Skill

## Overview

This skill provides comprehensive support for psychological research methodology, from study design through data analysis and reporting. It covers experimental, correlational, and qualitative research approaches across various psychology subdisciplines including clinical, cognitive, developmental, social, and organizational psychology.

## When to Use This Skill

Use this skill when you need to:

- Design psychological experiments or studies
- Select and implement validated psychological instruments
- Conduct power analyses for study planning
- Analyze behavioral and psychological data
- Calculate and interpret effect sizes
- Perform psychometric validation of instruments
- Apply appropriate statistical methods for psychology research
- Write psychology research manuscripts (APA format)
- Conduct systematic reviews and meta-analyses
- Navigate IRB and ethical considerations

## Visual Enhancement with Scientific Schematics

This skill integrates with `scientific-schematics` to generate:
- Experimental design diagrams
- Study flow charts (CONSORT, PRISMA)
- Statistical result visualizations
- Path diagrams for structural models
- Mediation and moderation models

## Core Capabilities

### 1. Research Design

#### Experimental Designs

**Between-Subjects (Independent Groups):**
```
Randomization → Group A (Treatment) → Measure
             → Group B (Control) → Measure

Advantages: No carryover effects, shorter sessions
Disadvantages: Individual differences, larger N needed
```

**Within-Subjects (Repeated Measures):**
```
All Participants → Condition A → Condition B → Condition C
                   (counterbalanced)

Advantages: Controls individual differences, smaller N
Disadvantages: Order effects, fatigue, practice effects
```

**Mixed Designs:**
```
Between-subjects factor (e.g., treatment group)
× Within-subjects factor (e.g., time points)

Example: Treatment vs Control (between) × Pre/Post/Follow-up (within)
```

**Factorial Designs:**
```
2×2 Factorial:
                Factor B
              Low    High
Factor A  Low   A1B1   A1B2
         High   A2B1   A2B2

Allows examination of main effects and interactions
```

#### Quasi-Experimental Designs

| Design | Description | Threats to Validity |
|--------|-------------|---------------------|
| Non-equivalent control group | Pre-existing groups | Selection bias |
| Interrupted time series | Multiple observations before/after | History, maturation |
| Regression discontinuity | Assignment by cutoff | Functional form |
| Propensity score matching | Statistical matching | Unmeasured confounds |

#### Correlational and Observational Designs

**Cross-Sectional:**
- Single time point measurement
- Examines relationships at one moment
- Cannot establish temporal precedence

**Longitudinal:**
- Panel study: Same participants over time
- Cohort study: Group defined by shared characteristic
- Time-lag study: Different cohorts at same age

**Experience Sampling Method (ESM):**
- Multiple measurements per day
- Ecological momentary assessment (EMA)
- Real-time capture of experiences

#### Qualitative Research Designs

| Approach | Focus | Sample Size | Data Collection |
|----------|-------|-------------|-----------------|
| Phenomenology | Lived experience | 5-25 | In-depth interviews |
| Grounded theory | Theory development | 20-60 | Interviews, observations |
| Thematic analysis | Pattern identification | Variable | Multiple sources |
| Narrative analysis | Life stories | 1-10 | Narratives, life histories |
| IPA | Individual meaning | 3-10 | Semi-structured interviews |
| Discourse analysis | Language use | Variable | Text, talk |

### 2. Sampling and Power Analysis

#### Sample Size Determination

**A Priori Power Analysis:**
```python
# Using G*Power conventions
# Required inputs:
# - Effect size (d, f, r, OR, etc.)
# - Alpha level (typically .05)
# - Desired power (typically .80 or .90)
# - Statistical test

# Example for independent t-test:
# d = 0.5 (medium effect)
# α = .05 (two-tailed)
# Power = .80
# Required N per group ≈ 64

# Example for correlation:
# r = .30 (medium effect)
# α = .05 (two-tailed)
# Power = .80
# Required N ≈ 84
```

**Effect Size Conventions (Cohen, 1988):**

| Measure | Small | Medium | Large |
|---------|-------|--------|-------|
| d | 0.20 | 0.50 | 0.80 |
| r | 0.10 | 0.30 | 0.50 |
| f | 0.10 | 0.25 | 0.40 |
| f² | 0.02 | 0.15 | 0.35 |
| η² | 0.01 | 0.06 | 0.14 |
| ω² | 0.01 | 0.06 | 0.14 |
| OR | 1.5 | 2.5 | 4.3 |

#### Sampling Methods

**Probability Sampling:**
- Simple random sampling
- Stratified random sampling
- Cluster sampling
- Systematic sampling
- Multistage sampling

**Non-Probability Sampling:**
- Convenience sampling
- Purposive sampling
- Snowball sampling
- Quota sampling

### 3. Validated Psychological Instruments

#### Depression and Anxiety

| Instrument | Items | Time | Reliability | Use |
|------------|-------|------|-------------|-----|
| PHQ-9 | 9 | 5 min | α = .89 | Depression screening |
| GAD-7 | 7 | 3 min | α = .92 | Anxiety screening |
| BDI-II | 21 | 10 min | α = .93 | Depression severity |
| BAI | 21 | 10 min | α = .92 | Anxiety severity |
| DASS-21 | 21 | 10 min | α = .88-.94 | Depression, anxiety, stress |
| HAM-D | 17-21 | 20 min | ICC = .92 | Clinician-rated depression |
| CES-D | 20 | 5 min | α = .85-.90 | Depression epidemiology |

#### Personality

| Instrument | Items | Constructs | Reliability |
|------------|-------|------------|-------------|
| Big Five Inventory (BFI-2) | 60 | OCEAN traits | α = .80-.90 |
| NEO-PI-R | 240 | Five factors + facets | α = .86-.92 |
| HEXACO-PI-R | 100/200 | Six factors | α = .80-.90 |
| Ten Item Personality Inventory | 10 | Big Five (brief) | α = .68-.72 |
| MMPI-3 | 335 | Clinical scales | Various |

#### Cognitive Function

| Instrument | Domain | Time | Psychometrics |
|------------|--------|------|---------------|
| MoCA | Cognitive screening | 10 min | Sensitivity .90 |
| MMSE | Cognitive screening | 10 min | Specificity .82 |
| Stroop Test | Inhibition | 5 min | Test-retest .80 |
| Trail Making A/B | Processing/flexibility | 5 min | Test-retest .79 |
| Digit Span | Working memory | 5 min | α = .80 |
| WAIS-IV | Intelligence | 90 min | α = .97 |
| Wisconsin Card Sort | Executive function | 20 min | Test-retest .83 |

#### Well-Being and Quality of Life

| Instrument | Items | Constructs | Reliability |
|------------|-------|------------|-------------|
| SWLS | 5 | Life satisfaction | α = .87 |
| PANAS | 20 | Positive/negative affect | α = .86-.90 |
| WEMWBS | 14 | Mental well-being | α = .89 |
| SF-36 | 36 | Health-related QoL | α = .78-.93 |
| WHOQOL-BREF | 26 | QoL domains | α = .66-.84 |
| PWB | 42-84 | Psychological well-being | α = .86-.93 |

#### Social and Interpersonal

| Instrument | Items | Constructs |
|------------|-------|------------|
| UCLA Loneliness Scale | 20 | Loneliness |
| Experiences in Close Relationships (ECR) | 36 | Attachment |
| Social Support Questionnaire (SSQ) | 27 | Social support |
| Interpersonal Reactivity Index (IRI) | 28 | Empathy |
| Rosenberg Self-Esteem Scale | 10 | Self-esteem |

#### Stress and Coping

| Instrument | Items | Focus |
|------------|-------|-------|
| Perceived Stress Scale (PSS) | 10/14 | Perceived stress |
| Brief COPE | 28 | Coping strategies |
| Life Events Checklist (LEC) | 17 | Trauma exposure |
| Maslach Burnout Inventory | 22 | Burnout |
| Connor-Davidson Resilience Scale | 25 | Resilience |

### 4. Statistical Methods

#### Descriptive Statistics

```python
import pandas as pd
import numpy as np
from scipy import stats

def descriptive_summary(data: pd.Series) -> dict:
    """Calculate comprehensive descriptive statistics."""
    return {
        'n': len(data.dropna()),
        'mean': data.mean(),
        'sd': data.std(),
        'se': data.sem(),
        'median': data.median(),
        'iqr': data.quantile(0.75) - data.quantile(0.25),
        'skewness': data.skew(),
        'kurtosis': data.kurtosis(),
        'min': data.min(),
        'max': data.max(),
        '95_ci': stats.t.interval(0.95, len(data)-1,
                                   loc=data.mean(),
                                   scale=data.sem())
    }
```

#### Group Comparisons

**Two Groups:**
```python
from scipy import stats

# Independent samples t-test
t_stat, p_value = stats.ttest_ind(group1, group2)

# Welch's t-test (unequal variances)
t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)

# Mann-Whitney U (non-parametric)
u_stat, p_value = stats.mannwhitneyu(group1, group2, alternative='two-sided')

# Paired samples t-test
t_stat, p_value = stats.ttest_rel(before, after)

# Wilcoxon signed-rank (non-parametric paired)
w_stat, p_value = stats.wilcoxon(before, after)
```

**Multiple Groups:**
```python
from scipy import stats
import pingouin as pg

# One-way ANOVA
f_stat, p_value = stats.f_oneway(group1, group2, group3)

# Welch's ANOVA (unequal variances)
result = pg.welch_anova(data=df, dv='score', between='group')

# Kruskal-Wallis (non-parametric)
h_stat, p_value = stats.kruskal(group1, group2, group3)

# Post-hoc tests
posthoc = pg.pairwise_tukey(data=df, dv='score', between='group')
# or
posthoc = pg.pairwise_gameshowell(data=df, dv='score', between='group')
```

**Repeated Measures:**
```python
import pingouin as pg

# Repeated measures ANOVA
result = pg.rm_anova(data=df, dv='score', within='time', subject='participant')

# Mixed ANOVA
result = pg.mixed_anova(data=df, dv='score', within='time',
                        between='group', subject='participant')

# Mauchly's sphericity test
sphericity = pg.sphericity(data=df, dv='score', within='time',
                           subject='participant')

# Greenhouse-Geisser correction applied automatically when violated
```

#### Correlation Analysis

```python
from scipy import stats
import pingouin as pg

# Pearson correlation
r, p = stats.pearsonr(x, y)

# Spearman correlation
rho, p = stats.spearmanr(x, y)

# Partial correlation
partial = pg.partial_corr(data=df, x='x', y='y', covar='z')

# Correlation matrix with p-values
corr_matrix = pg.pairwise_corr(df, columns=['var1', 'var2', 'var3'])
```

#### Regression Analysis

```python
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Simple linear regression
model = smf.ols('y ~ x', data=df).fit()
print(model.summary())

# Multiple regression
model = smf.ols('y ~ x1 + x2 + x3', data=df).fit()

# Hierarchical regression
model1 = smf.ols('y ~ x1', data=df).fit()
model2 = smf.ols('y ~ x1 + x2', data=df).fit()
model3 = smf.ols('y ~ x1 + x2 + x3', data=df).fit()

# Compare models
from scipy import stats
f_change = ((model2.rsquared - model1.rsquared) / 1) / \
           ((1 - model2.rsquared) / (model2.df_resid))

# Logistic regression
model = smf.logit('outcome ~ x1 + x2', data=df).fit()

# Moderation analysis (interaction)
model = smf.ols('y ~ x * m', data=df).fit()  # includes x, m, and x:m
```

#### Mediation Analysis

```python
import pingouin as pg

# Simple mediation (Baron & Kenny + Sobel)
mediation = pg.mediation_analysis(data=df, x='x', m='mediator', y='y')

# For more complex models, use process macro or lavaan in R
# Or semopy in Python for SEM-based mediation

from semopy import Model

model_spec = """
mediator ~ x
y ~ mediator + x
"""
model = Model(model_spec)
model.fit(df)
```

### 5. Effect Size Calculations

```python
import numpy as np
from scipy import stats

def cohens_d(group1, group2, pooled=True):
    """
    Calculate Cohen's d effect size.

    Args:
        group1, group2: Arrays of scores
        pooled: Use pooled SD (True) or control group SD (False)
    """
    n1, n2 = len(group1), len(group2)
    mean_diff = np.mean(group1) - np.mean(group2)

    if pooled:
        # Pooled standard deviation
        var1 = np.var(group1, ddof=1)
        var2 = np.var(group2, ddof=1)
        pooled_sd = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
        d = mean_diff / pooled_sd
    else:
        # Control group SD (Glass's delta)
        d = mean_diff / np.std(group2, ddof=1)

    return d

def hedges_g(group1, group2):
    """Hedges' g with small sample correction."""
    d = cohens_d(group1, group2)
    n = len(group1) + len(group2)
    # Correction factor
    j = 1 - (3 / (4 * (n - 2) - 1))
    return d * j

def eta_squared(f_stat, df_between, df_within):
    """Calculate eta-squared from F statistic."""
    ss_between = f_stat * df_between
    ss_total = ss_between + df_within
    return ss_between / ss_total

def partial_eta_squared(f_stat, df_effect, df_error):
    """Calculate partial eta-squared."""
    return (f_stat * df_effect) / (f_stat * df_effect + df_error)

def omega_squared(f_stat, df_between, df_within, ms_error):
    """Calculate omega-squared (less biased than eta-squared)."""
    ss_between = f_stat * df_between * ms_error
    ss_total = ss_between + (df_within + 1) * ms_error
    return (ss_between - df_between * ms_error) / (ss_total + ms_error)

def r_to_d(r):
    """Convert correlation to Cohen's d."""
    return (2 * r) / np.sqrt(1 - r**2)

def d_to_r(d):
    """Convert Cohen's d to correlation."""
    return d / np.sqrt(d**2 + 4)

def odds_ratio_to_d(or_val):
    """Convert odds ratio to Cohen's d."""
    return np.log(or_val) * np.sqrt(3) / np.pi
```

### 6. Psychometric Validation

#### Reliability Analysis

```python
import numpy as np
import pingouin as pg

def cronbachs_alpha(items_df):
    """Calculate Cronbach's alpha for scale reliability."""
    return pg.cronbach_alpha(items_df)

def mcdonalds_omega(items_df):
    """Calculate McDonald's omega (requires factor analysis)."""
    # Simplified - for full omega use factor analysis
    from factor_analyzer import FactorAnalyzer

    fa = FactorAnalyzer(n_factors=1, rotation=None)
    fa.fit(items_df)
    loadings = fa.loadings_

    # Omega = (sum of loadings)^2 / ((sum of loadings)^2 + sum of unique variances)
    sum_loadings = np.sum(loadings)
    unique_var = 1 - loadings**2
    omega = sum_loadings**2 / (sum_loadings**2 + np.sum(unique_var))

    return omega

def split_half_reliability(items_df, method='odd_even'):
    """Calculate split-half reliability with Spearman-Brown correction."""
    if method == 'odd_even':
        odd_items = items_df.iloc[:, ::2].sum(axis=1)
        even_items = items_df.iloc[:, 1::2].sum(axis=1)
    else:  # first_half
        mid = items_df.shape[1] // 2
        odd_items = items_df.iloc[:, :mid].sum(axis=1)
        even_items = items_df.iloc[:, mid:].sum(axis=1)

    r = np.corrcoef(odd_items, even_items)[0, 1]

    # Spearman-Brown prophecy formula
    reliability = (2 * r) / (1 + r)

    return reliability
```

#### Validity Analysis

```python
from scipy import stats
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_kmo
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity

def assess_factorability(df):
    """Check if data is suitable for factor analysis."""
    # Kaiser-Meyer-Olkin measure
    kmo_all, kmo_model = calculate_kmo(df)

    # Bartlett's test of sphericity
    chi_square, p_value = calculate_bartlett_sphericity(df)

    return {
        'kmo': kmo_model,
        'kmo_interpretation': 'adequate' if kmo_model > 0.6 else 'inadequate',
        'bartlett_chi2': chi_square,
        'bartlett_p': p_value,
        'bartlett_significant': p_value < 0.05
    }

def exploratory_factor_analysis(df, n_factors, rotation='varimax'):
    """Perform EFA with specified rotation."""
    fa = FactorAnalyzer(n_factors=n_factors, rotation=rotation)
    fa.fit(df)

    return {
        'loadings': pd.DataFrame(fa.loadings_,
                                  index=df.columns,
                                  columns=[f'Factor{i+1}' for i in range(n_factors)]),
        'eigenvalues': fa.get_eigenvalues(),
        'variance_explained': fa.get_factor_variance(),
        'communalities': fa.get_communalities()
    }

def convergent_validity(scale1, scale2):
    """Assess convergent validity via correlation."""
    r, p = stats.pearsonr(scale1, scale2)
    return {
        'correlation': r,
        'p_value': p,
        'interpretation': 'good' if r > 0.5 else 'moderate' if r > 0.3 else 'weak'
    }

def discriminant_validity(scale1, scale2, threshold=0.85):
    """Assess discriminant validity - correlations should be < threshold."""
    r, p = stats.pearsonr(scale1, scale2)
    return {
        'correlation': r,
        'discriminant_valid': abs(r) < threshold
    }
```

### 7. Meta-Analysis

```python
import numpy as np
from scipy import stats

def fixed_effects_meta(effect_sizes, standard_errors):
    """
    Fixed-effects meta-analysis.

    Args:
        effect_sizes: Array of effect sizes (d, r, etc.)
        standard_errors: Array of standard errors
    """
    weights = 1 / (standard_errors ** 2)
    pooled_es = np.sum(weights * effect_sizes) / np.sum(weights)
    pooled_se = np.sqrt(1 / np.sum(weights))

    z = pooled_es / pooled_se
    p = 2 * (1 - stats.norm.cdf(abs(z)))

    ci_lower = pooled_es - 1.96 * pooled_se
    ci_upper = pooled_es + 1.96 * pooled_se

    return {
        'pooled_effect': pooled_es,
        'se': pooled_se,
        'z': z,
        'p': p,
        'ci_95': (ci_lower, ci_upper)
    }

def random_effects_meta(effect_sizes, standard_errors):
    """
    Random-effects meta-analysis using DerSimonian-Laird method.
    """
    k = len(effect_sizes)
    weights = 1 / (standard_errors ** 2)

    # Q statistic
    pooled_fixed = np.sum(weights * effect_sizes) / np.sum(weights)
    q = np.sum(weights * (effect_sizes - pooled_fixed) ** 2)

    # Tau-squared (between-study variance)
    c = np.sum(weights) - np.sum(weights ** 2) / np.sum(weights)
    tau2 = max(0, (q - (k - 1)) / c)

    # Random effects weights
    re_weights = 1 / (standard_errors ** 2 + tau2)

    # Pooled effect
    pooled_es = np.sum(re_weights * effect_sizes) / np.sum(re_weights)
    pooled_se = np.sqrt(1 / np.sum(re_weights))

    z = pooled_es / pooled_se
    p = 2 * (1 - stats.norm.cdf(abs(z)))

    ci_lower = pooled_es - 1.96 * pooled_se
    ci_upper = pooled_es + 1.96 * pooled_se

    # I-squared
    i_squared = max(0, (q - (k - 1)) / q * 100) if q > 0 else 0

    return {
        'pooled_effect': pooled_es,
        'se': pooled_se,
        'z': z,
        'p': p,
        'ci_95': (ci_lower, ci_upper),
        'tau2': tau2,
        'q': q,
        'i_squared': i_squared,
        'heterogeneity': 'low' if i_squared < 25 else 'moderate' if i_squared < 75 else 'high'
    }
```

### 8. Ethical Considerations

#### IRB Requirements

**Elements of Informed Consent:**
1. Purpose of research
2. Procedures involved
3. Duration of participation
4. Risks and discomforts
5. Benefits to participant/others
6. Alternatives to participation
7. Confidentiality protections
8. Compensation (if any)
9. Contact information
10. Voluntary participation statement
11. Right to withdraw without penalty

**Vulnerable Populations:**
- Children (parental consent + assent)
- Prisoners
- Pregnant women
- Cognitively impaired individuals
- Economically/educationally disadvantaged

**Special Considerations:**
- Deception: Justified only when necessary, requires debriefing
- Sensitive topics: Additional safeguards, referral resources
- Online research: IP addresses, data security, platform terms

#### Data Management

```markdown
## Data Security Checklist

- [ ] De-identification procedures documented
- [ ] Secure storage (encrypted, access-controlled)
- [ ] Data sharing agreement if applicable
- [ ] Retention period specified
- [ ] Destruction procedures defined
- [ ] Backup procedures in place
- [ ] Transfer protocols (if applicable)
```

### 9. APA Reporting Standards

#### Statistical Results Format

```markdown
## APA 7th Edition Formatting

### t-test
"An independent samples t-test revealed a significant difference between
groups, t(58) = 2.45, p = .017, d = 0.64, 95% CI [0.12, 1.15]."

### ANOVA
"A one-way ANOVA showed a significant main effect of condition,
F(2, 87) = 5.23, p = .007, η²p = .11."

### Correlation
"Depression scores were negatively correlated with life satisfaction,
r(98) = -.42, p < .001, 95% CI [-.57, -.24]."

### Regression
"The model explained 34% of the variance in well-being, R² = .34,
F(3, 96) = 16.52, p < .001. Significant predictors included social
support (β = .35, p < .001) and optimism (β = .28, p = .003)."

### Chi-square
"There was a significant association between treatment condition and
recovery status, χ²(2) = 8.45, p = .015, Cramér's V = .29."
```

#### Table Formatting

```markdown
Table 1
Descriptive Statistics and Correlations Among Study Variables

Variable         M      SD      1       2       3       4
1. Depression   12.34   5.67    —
2. Anxiety      8.92    4.21    .54***  —
3. Support      3.45    0.89   -.38**  -.29**   —
4. Well-being   5.12    1.23   -.61*** -.48***  .52***  —

Note. N = 245.
*p < .05. **p < .01. ***p < .001.
```

## Use Cases

### Experimental Study Protocol

```markdown
## Study: Effect of Mindfulness on Stress Reactivity

### Design
2 (Condition: Mindfulness vs. Control) × 2 (Time: Pre/Post) mixed design

### Participants
- N = 80 (40 per condition)
- Power analysis: d = 0.6, α = .05, power = .80
- Inclusion: Ages 18-65, no current meditation practice
- Exclusion: Current psychiatric treatment, meditation experience

### Procedure
1. Baseline assessments (PSS, cortisol)
2. Randomization to condition
3. 8-week intervention or waitlist
4. Post-intervention assessments
5. Stress induction task (TSST)
6. Stress reactivity measures

### Measures
- Perceived Stress Scale (PSS-10)
- Salivary cortisol
- State anxiety (STAI-S)
- Heart rate variability

### Analysis Plan
- Mixed ANOVA for primary outcomes
- Mediation analysis for mechanisms
- Intention-to-treat and per-protocol analyses
```

### Survey Study Design

```markdown
## Study: Social Media Use and Well-Being

### Design
Cross-sectional survey with moderation analysis

### Sample
- N = 500 (online panel)
- Stratified by age and gender
- Attention checks included

### Measures
- Social Media Use: Screen time (objective), SMU questionnaire
- Well-Being: WEMWBS, SWLS
- Moderators: Social comparison (INCOM), FOMO scale
- Controls: Age, gender, SES, personality (BFI-10)

### Analysis Plan
1. Descriptive statistics and correlations
2. Hierarchical regression (controls → SMU → moderators → interactions)
3. Simple slopes analysis for significant interactions
4. Sensitivity analyses (outliers, missing data)
```

### Qualitative Study Protocol

```markdown
## Study: Lived Experience of Recovery from Depression

### Approach
Interpretative Phenomenological Analysis (IPA)

### Participants
- N = 10 (purposive sampling)
- Inclusion: History of MDD, self-identified as "recovered"
- Recruitment: Mental health organizations, social media

### Data Collection
- Semi-structured interviews (60-90 min)
- Audio recorded and transcribed verbatim
- Interview guide with open-ended questions

### Analysis
1. Reading and re-reading transcripts
2. Initial noting (descriptive, linguistic, conceptual)
3. Developing emergent themes
4. Searching for connections across themes
5. Moving to next case
6. Looking for patterns across cases

### Trustworthiness
- Reflexivity journal
- Member checking
- Peer debriefing
- Audit trail
```

## Integration with Other Skills

This skill works well with:

- **hypothesis-generation**: For developing research questions
- **scientific-writing**: For APA-formatted manuscripts
- **statistical-analysis**: For advanced statistical methods
- **scientific-schematics**: For study diagrams and visualizations
- **literature-review**: For systematic reviews
- **research-grants**: For funding applications
- **medical-education-research**: For educational psychology studies

## Dependencies

**Python Packages:**
- numpy
- scipy
- pandas
- statsmodels
- pingouin
- factor_analyzer
- semopy (for SEM)
- scikit-learn

**R Packages (for advanced analyses):**
- psych
- lavaan
- lme4/lmerTest
- metafor
- ggplot2

## References

Key resources for psychology research:

1. American Psychological Association. (2020). Publication Manual (7th ed.)
2. Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences
3. Field, A. (2018). Discovering Statistics Using IBM SPSS Statistics
4. Hayes, A. F. (2022). Introduction to Mediation, Moderation, and Conditional Process Analysis
5. Kazdin, A. E. (2017). Research Design in Clinical Psychology
6. Tabachnick, B. G., & Fidell, L. S. (2019). Using Multivariate Statistics

## Journals

- Psychological Bulletin
- Psychological Methods
- Journal of Consulting and Clinical Psychology
- Journal of Personality and Social Psychology
- Psychological Science
- Journal of Experimental Psychology (various)
- Behavior Research Methods
- Multivariate Behavioral Research
