# Research Designs in Psychology

## Experimental Designs

### True Experiments

**Characteristics**:
- Random assignment to conditions
- Manipulation of independent variable(s)
- Control of extraneous variables
- Allows causal inference

### Between-Subjects Design

```
Participants randomly assigned to ONE condition

Group A (Experimental) → Treatment → Measure
Group B (Control) → No Treatment → Measure

Example: Testing a new therapy
- Experimental: Receives CBT intervention
- Control: Waitlist or treatment as usual
```

**Advantages**:
- No carryover effects
- Shorter participant commitment
- Simpler analysis

**Disadvantages**:
- Individual differences increase error variance
- Larger sample size needed
- Less statistical power

**Power Considerations**:
```python
# Sample size for between-subjects t-test
# d = 0.5 (medium), α = .05, power = .80
# Required: n ≈ 64 per group
```

### Within-Subjects Design (Repeated Measures)

```
ALL participants experience ALL conditions

Participants → Condition A → Condition B → Condition C
                  (counterbalanced)

Example: Memory study with different encoding strategies
- Each participant uses visual, verbal, and combined strategies
- Order counterbalanced across participants
```

**Advantages**:
- Controls individual differences
- Smaller sample size needed
- Higher statistical power

**Disadvantages**:
- Order effects (practice, fatigue)
- Carryover effects
- Longer sessions

**Counterbalancing Methods**:

| Method | Description | Use When |
|--------|-------------|----------|
| Complete | All possible orders | Few conditions |
| Latin Square | Each condition in each position | Moderate conditions |
| Balanced Latin Square | Controls first-order carryover | Carryover concern |
| Random | Each participant random order | Many conditions |

### Factorial Designs

**2×2 Factorial**:
```
                    Factor B
                  Level 1    Level 2
Factor A  Level 1   AB₁₁      AB₁₂
          Level 2   AB₂₁      AB₂₂

Effects:
- Main effect of A: Compare rows
- Main effect of B: Compare columns
- A×B interaction: Pattern differs across levels
```

**Example**: Therapy type (CBT vs. medication) × Severity (mild vs. severe)

**Higher-Order Factorials**:
```
2×2×2 = 8 cells
2×3×2 = 12 cells
3×3×3 = 27 cells

Consider:
- Sample size requirements
- Interpretability of higher-order interactions
- Practical constraints
```

### Mixed Designs

```
Between-subjects factor × Within-subjects factor

Example: Treatment group (between) × Time point (within)

         Baseline    Post-Treatment    Follow-up
CBT         ✓              ✓               ✓
Control     ✓              ✓               ✓

Advantages:
- Reduces sample size vs. pure between
- Examines change over time
- Tests group × time interactions
```

---

## Quasi-Experimental Designs

**When true experiments are not possible or ethical**

### Non-Equivalent Control Group

```
Existing Group A (Treatment) → Treatment → Posttest
Existing Group B (Control) → No Treatment → Posttest

Example: Compare training program effects across departments
- Treatment: Department that volunteered
- Control: Department that didn't

Threats:
- Selection bias (groups differ at baseline)
- Selection × maturation interaction
```

**Mitigation strategies**:
- Pretest measurement
- Matching
- Statistical control (ANCOVA)
- Propensity score methods

### Interrupted Time Series

```
O₁ O₂ O₃ O₄ O₅ X O₆ O₇ O₈ O₉ O₁₀

Multiple observations before (O₁-O₅)
Intervention (X)
Multiple observations after (O₆-O₁₀)

Example: Policy change effect on behavior
- Weekly measurements for 10 weeks before
- Policy implemented
- Weekly measurements for 10 weeks after

Analysis:
- Change in level (immediate effect)
- Change in slope (gradual effect)
- Stability of change
```

### Regression Discontinuity

```
Assignment based on cutoff score

         Treatment
         |
Score    |     ●●●●
         |   ●●
---------+------------ Cutoff
         | ●●
         |●●●     Control

Causal inference:
- Compare outcomes just above/below cutoff
- Assumes continuous relationship
- Strong internal validity near cutoff
```

---

## Correlational Designs

### Cross-Sectional Studies

**Characteristics**:
- Single time point
- Examines relationships between variables
- Cannot establish causation
- Cannot determine temporal order

**Uses**:
- Prevalence estimation
- Relationship exploration
- Hypothesis generation
- Psychometric validation

**Limitations**:
- No causal inference
- Third variable problem
- Direction of causality unclear

### Longitudinal Designs

**Panel Studies**:
```
Same participants measured multiple times

Time 1 → Time 2 → Time 3 → Time 4
  ↓        ↓        ↓        ↓
  P₁       P₁       P₁       P₁
  P₂       P₂       P₂       P₂
  ...      ...      ...      ...

Advantages:
- Examine within-person change
- Establish temporal precedence
- Identify developmental trajectories

Challenges:
- Attrition
- Practice effects
- Historical effects
```

**Cohort Studies**:
```
Follow group defined by shared characteristic

Birth cohort → Follow over years
              Measure outcomes at intervals

Example: Track 1990 birth cohort for depression onset
```

**Cross-Sequential (Accelerated Longitudinal)**:
```
Combine cross-sectional and longitudinal

Age at Time 1:   10    12    14
                  ↓     ↓     ↓
                  ↓     ↓    [14]
                  ↓    [12→14]
                 [10→12→14]

Allows:
- Faster coverage of age range
- Separate age, period, cohort effects
- Reduced attrition per participant
```

### Experience Sampling Method (ESM)

```
Multiple measurements per day in naturalistic settings

Day 1:  📱  📱  📱  📱  📱  📱
Day 2:  📱  📱  📱  📱  📱  📱
...
Day 14: 📱  📱  📱  📱  📱  📱

Measures:
- Momentary affect
- Current activity
- Social context
- Symptoms
- Behaviors

Analysis:
- Within-person variability
- Contextual effects
- Lagged relationships
```

---

## Qualitative Research Designs

### Phenomenology

**Purpose**: Understand lived experience of a phenomenon

**Sample**: 5-25 participants with direct experience

**Data Collection**: In-depth interviews (60-120 min)

**Analysis**:
1. Read and re-read transcripts
2. Identify significant statements
3. Create meaning units
4. Develop themes
5. Describe essence of experience

**Quality Criteria**:
- Rich description
- Bracketing of researcher assumptions
- Member checking

### Grounded Theory

**Purpose**: Develop theory from data

**Sample**: Theoretical sampling until saturation (20-60)

**Process**:
```
Data Collection ←→ Data Analysis (iterative)
      ↓
Open Coding (identify concepts)
      ↓
Axial Coding (relate categories)
      ↓
Selective Coding (core category)
      ↓
Theory Development
```

**Key Concepts**:
- Theoretical saturation
- Constant comparison
- Memo writing
- Theoretical sensitivity

### Thematic Analysis

**Purpose**: Identify patterns across qualitative data

**Flexibility**: Works with various theoretical frameworks

**Phases (Braun & Clarke)**:
1. Familiarization with data
2. Generating initial codes
3. Searching for themes
4. Reviewing themes
5. Defining and naming themes
6. Producing report

### Interpretative Phenomenological Analysis (IPA)

**Purpose**: Understand how individuals make sense of experience

**Sample**: Small, homogeneous (3-10 participants)

**Double Hermeneutic**: Researcher interprets participant's interpretation

**Analysis Steps**:
1. Read and re-read
2. Initial noting
3. Develop emergent themes
4. Search for connections
5. Move to next case
6. Look for patterns across cases

### Case Study

**Purpose**: In-depth examination of bounded system

**Types**:
- Single case (unique, critical, typical)
- Multiple case (replication logic)

**Data Sources**:
- Interviews
- Documents
- Observations
- Artifacts

---

## Mixed Methods Designs

### Convergent Parallel

```
Quantitative Data Collection    Qualitative Data Collection
           ↓                               ↓
Quantitative Analysis          Qualitative Analysis
           ↓                               ↓
           └──────── Compare ─────────────┘
                        ↓
                 Interpretation

Purpose: Validate findings through triangulation
Timing: Concurrent data collection
```

### Explanatory Sequential

```
Quantitative          Qualitative          Integration
   Phase                 Phase
    ↓                     ↓                    ↓
QUAN → Results → qual design → QUAL → Explain QUAN findings

Purpose: Explain quantitative results in depth
Example: Survey identifies groups → Interviews explore differences
```

### Exploratory Sequential

```
Qualitative            Quantitative          Integration
   Phase                  Phase
    ↓                      ↓                    ↓
QUAL → Findings → QUAN instrument → QUAN → Test QUAL findings

Purpose: Develop and test instrument
Example: Interviews identify themes → Survey items → Validation study
```

### Embedded Design

```
Primary Design (QUAN or QUAL)
┌────────────────────────────────┐
│                                │
│  ┌─────────────┐              │
│  │ Secondary   │              │
│  │ data strand │              │
│  └─────────────┘              │
│                                │
└────────────────────────────────┘

Purpose: Supplement primary method
Example: Experimental study with qualitative process data
```

---

## Validity Threats and Controls

### Internal Validity Threats

| Threat | Description | Control |
|--------|-------------|---------|
| History | External events | Control group |
| Maturation | Natural change | Control group |
| Testing | Practice effects | Control group, alternate forms |
| Instrumentation | Measure changes | Standardization |
| Regression | Extreme scores regress | Random assignment |
| Selection | Group differences | Random assignment |
| Attrition | Differential dropout | Intent-to-treat |
| Diffusion | Treatment spreads | Separate locations |
| Compensation | Control receives extras | Monitor |
| Demoralization | Control gives up | Monitor, partial disclosure |

### External Validity Considerations

**Population Validity**:
- Who can results generalize to?
- Sampling method
- Response rate
- Demographic coverage

**Ecological Validity**:
- Lab vs. real-world settings
- Artificial tasks
- Demand characteristics
- Hawthorne effect

**Temporal Validity**:
- Would results replicate at different times?
- Historical context
- Cohort effects
