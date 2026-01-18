---
name: medical-education-research
description: Design medical curricula, create assessments, conduct educational research studies, and analyze learning outcomes in healthcare education
allowed-tools: [Read, Write, Edit, Bash]
license: MIT License
metadata:
    skill-author: K-Dense Inc.
---

# Medical Education Research Skill

## Overview

This skill provides comprehensive support for medical education research, curriculum development, and assessment design. It encompasses the full spectrum of medical education scholarship from instructional design through outcomes research and program evaluation.

## When to Use This Skill

Use this skill when you need to:

- Design or revise medical school curricula
- Develop competency-based assessments
- Conduct educational research studies in healthcare settings
- Analyze learning outcomes and student performance data
- Create validated assessment instruments
- Evaluate educational interventions
- Write medical education research manuscripts
- Design faculty development programs
- Implement simulation-based education
- Apply educational theories to clinical training

## Visual Enhancement with Scientific Schematics

This skill integrates with `scientific-schematics` to generate:
- Curriculum maps and competency frameworks
- Assessment blueprints and matrices
- Learning progression diagrams
- Research study flowcharts
- Statistical result visualizations

## Core Capabilities

### 1. Curriculum Design and Development

#### Competency-Based Medical Education (CBME)

Support for major competency frameworks:

**ACGME Core Competencies:**
- Patient Care and Procedural Skills
- Medical Knowledge
- Practice-Based Learning and Improvement
- Interpersonal and Communication Skills
- Professionalism
- Systems-Based Practice

**CanMEDS Roles:**
- Medical Expert
- Communicator
- Collaborator
- Leader
- Health Advocate
- Scholar
- Professional

**Entrustable Professional Activities (EPAs):**
- Core EPA identification and mapping
- Milestones alignment
- Assessment of entrustment decisions
- Supervision level documentation

#### Instructional Design Models

**ADDIE Framework:**
```
Analysis → Design → Development → Implementation → Evaluation
```

**Kern's Six-Step Approach:**
1. Problem Identification and General Needs Assessment
2. Targeted Needs Assessment
3. Goals and Objectives
4. Educational Strategies
5. Implementation
6. Evaluation and Feedback

**Backward Design (Understanding by Design):**
1. Identify desired results
2. Determine acceptable evidence
3. Plan learning experiences

### 2. Learning Objectives and Outcomes

#### Bloom's Taxonomy for Medical Education

**Cognitive Domain:**
| Level | Verbs | Medical Education Example |
|-------|-------|---------------------------|
| Remember | Define, list, recall | List the cranial nerves |
| Understand | Explain, describe, summarize | Explain the pathophysiology of heart failure |
| Apply | Demonstrate, solve, use | Apply ACLS protocols in simulation |
| Analyze | Compare, differentiate, examine | Analyze ECG findings to differentiate MI types |
| Evaluate | Assess, critique, judge | Evaluate treatment options for diabetic patient |
| Create | Design, develop, formulate | Develop a treatment plan for complex patient |

**Psychomotor Domain (Simpson's Taxonomy):**
- Perception → Set → Guided Response → Mechanism → Complex Overt Response → Adaptation → Origination

**Affective Domain (Krathwohl's Taxonomy):**
- Receiving → Responding → Valuing → Organization → Characterization

#### Writing Effective Learning Objectives

**SMART Objectives Format:**
- **S**pecific: Clear, unambiguous statement
- **M**easurable: Observable and assessable
- **A**chievable: Realistic for learner level
- **R**elevant: Aligned with program goals
- **T**ime-bound: Specify when mastery expected

**Example Objective Construction:**
```
By the end of [timeframe], learners will be able to [action verb] [content]
[condition] [criterion/standard].

Example: By the end of the clerkship, students will be able to perform
a focused cardiac examination on standardized patients with 90% accuracy
on the skills checklist.
```

### 3. Assessment Methods

#### Formative Assessment

**Workplace-Based Assessments:**
- Mini-Clinical Evaluation Exercise (Mini-CEX)
- Direct Observation of Procedural Skills (DOPS)
- Case-Based Discussion (CBD)
- Multi-Source Feedback (360-degree)

**Progressive Assessment:**
- Progress testing
- Spaced retrieval practice
- Low-stakes quizzing

#### Summative Assessment

**Knowledge Assessment:**
- Multiple Choice Questions (MCQs)
  - Single best answer
  - Extended matching questions
  - Script concordance testing
- Short answer questions
- Essay examinations

**Clinical Skills Assessment:**
- Objective Structured Clinical Examinations (OSCEs)
- Standardized Patient Encounters
- Simulation-Based Assessment
- Workplace-Based Assessment

**MCQ Item Writing Guidelines:**
```
Stem:
- Present a clear clinical scenario
- Include all necessary information
- Avoid negative phrasing
- Lead logically to the question

Options:
- One clearly correct answer
- Plausible distractors
- Similar length and grammatical structure
- Avoid "all of the above" or "none of the above"
- Alphabetize when appropriate
```

#### Psychometric Analysis

**Classical Test Theory Metrics:**
- Item difficulty (p-value): Target 0.3-0.7
- Item discrimination: Target >0.2
- Point-biserial correlation
- Cronbach's alpha for reliability

**Item Response Theory (IRT):**
- Difficulty parameter (b)
- Discrimination parameter (a)
- Pseudo-guessing parameter (c)
- Item information functions

**Standard Setting Methods:**
- Angoff method
- Ebel method
- Borderline regression
- Contrasting groups
- Hofstee method

### 4. Educational Research Methods

#### Study Designs in Medical Education

**Quantitative Designs:**

| Design | Use Case | Strengths | Limitations |
|--------|----------|-----------|-------------|
| Randomized Controlled Trial | Intervention comparison | Causal inference | Feasibility, ethics |
| Quasi-experimental | Natural experiments | Practical | Selection bias |
| Cross-sectional | Snapshot assessment | Quick, inexpensive | No causation |
| Cohort study | Longitudinal outcomes | Temporal sequence | Time, attrition |
| Pre-post study | Single intervention | Simple | Maturation threats |

**Qualitative Designs:**

| Approach | Focus | Data Collection |
|----------|-------|-----------------|
| Phenomenology | Lived experience | In-depth interviews |
| Grounded theory | Theory generation | Iterative sampling |
| Ethnography | Cultural context | Observation, immersion |
| Case study | Bounded systems | Multiple sources |
| Narrative inquiry | Stories, meaning | Narratives, artifacts |

**Mixed Methods:**
- Convergent parallel design
- Explanatory sequential design
- Exploratory sequential design
- Embedded design

#### Kirkpatrick's Four Levels of Evaluation

| Level | Focus | Measurement Examples |
|-------|-------|---------------------|
| 1 - Reaction | Satisfaction | Course evaluations, feedback |
| 2 - Learning | Knowledge/skills | Pre-post tests, OSCEs |
| 3 - Behavior | Transfer to practice | Workplace observation |
| 4 - Results | Patient/system outcomes | Quality metrics |

**Extended to Kirkpatrick-Barr Framework:**
- Level 4a: Change in organizational practice
- Level 4b: Benefits to patients/clients

#### Validity Evidence (Messick's Framework)

**Five Sources of Validity Evidence:**
1. **Content**: Domain coverage, expert review
2. **Response Process**: Think-aloud, eye tracking
3. **Internal Structure**: Factor analysis, reliability
4. **Relations to Other Variables**: Convergent, discriminant
5. **Consequences**: Impact, unintended effects

### 5. Statistical Analysis for Education Research

#### Common Statistical Tests

**Comparing Groups:**
```python
# Independent samples
- t-test (2 groups, continuous outcome)
- ANOVA (>2 groups, continuous outcome)
- Mann-Whitney U (2 groups, non-parametric)
- Kruskal-Wallis (>2 groups, non-parametric)
- Chi-square (categorical outcomes)

# Paired/Repeated measures
- Paired t-test
- Repeated measures ANOVA
- Wilcoxon signed-rank
- Friedman test
```

**Correlation and Regression:**
```python
# Correlation
- Pearson r (continuous, linear)
- Spearman rho (ordinal, non-linear)
- Point-biserial (continuous vs binary)

# Regression
- Linear regression (continuous outcome)
- Logistic regression (binary outcome)
- Ordinal regression (ordered categories)
- Multilevel modeling (nested data)
```

**Reliability Analysis:**
```python
# Internal consistency
- Cronbach's alpha
- McDonald's omega
- Split-half reliability

# Inter-rater reliability
- Cohen's kappa (2 raters)
- Fleiss' kappa (>2 raters)
- Intraclass correlation coefficient (ICC)

# Generalizability theory
- G-study design
- D-study optimization
```

#### Effect Size Reporting

| Measure | Use | Small | Medium | Large |
|---------|-----|-------|--------|-------|
| Cohen's d | Mean difference | 0.2 | 0.5 | 0.8 |
| Hedges' g | Adjusted d | 0.2 | 0.5 | 0.8 |
| Eta-squared | ANOVA | 0.01 | 0.06 | 0.14 |
| Partial eta-squared | Factorial ANOVA | 0.01 | 0.06 | 0.14 |
| Cohen's f | ANOVA | 0.10 | 0.25 | 0.40 |
| Odds ratio | Logistic regression | 1.5 | 2.5 | 4.0 |
| r | Correlation | 0.10 | 0.30 | 0.50 |

### 6. Simulation-Based Education

#### Simulation Modalities

**Types of Simulation:**
- Task trainers (procedural skills)
- Mannequin-based simulation (high/low fidelity)
- Standardized patients
- Virtual reality / augmented reality
- Screen-based simulation
- Hybrid simulation

#### Debriefing Frameworks

**PEARLS (Promoting Excellence and Reflective Learning in Simulation):**
1. Reactions phase
2. Description phase
3. Analysis phase (directive feedback or learner self-assessment)
4. Summary phase

**Plus-Delta:**
- What went well (+)
- What would you change (Δ)

**Advocacy-Inquiry:**
- State observation (advocacy)
- Share perspective
- Inquire about learner's reasoning

**Debriefing with Good Judgment:**
- Genuine curiosity about frames
- Advocacy-inquiry technique
- Closing performance gaps

### 7. Faculty Development

#### Teaching Skills Development

**Microteaching Components:**
- Brief teaching episodes
- Specific skill focus
- Immediate feedback
- Re-teaching opportunity

**Direct Observation and Feedback:**
- Stanford Faculty Development Model
- One-Minute Preceptor
- SNAPPS (learner-centered)

**One-Minute Preceptor Steps:**
1. Get a commitment
2. Probe for supporting evidence
3. Teach general rules
4. Reinforce what was done well
5. Correct mistakes

**SNAPPS for Learner Presentations:**
- **S**ummarize the case
- **N**arrow the differential
- **A**nalyze the differential
- **P**robe the preceptor
- **P**lan management
- **S**elect a learning issue

### 8. Program Evaluation

#### Logic Model Components

```
Inputs → Activities → Outputs → Short-term Outcomes → Long-term Impact

Inputs: Resources, staff, funding, facilities
Activities: Educational interventions, curriculum delivery
Outputs: Number trained, sessions delivered, materials produced
Outcomes: Knowledge gained, skills improved, behaviors changed
Impact: Patient outcomes, system improvements, workforce changes
```

#### Accreditation Standards

**LCME Standards (Medical Schools):**
- Mission, Planning, Organization, and Integrity
- Leadership and Administration
- Academic and Learning Environments
- Faculty Preparation, Productivity, Participation, and Policies
- Educational Resources and Infrastructure
- Competencies, Curricular Objectives, and Curricular Design
- Curricular Content
- Curricular Management, Evaluation, and Enhancement
- Teaching, Supervision, Assessment, and Student Safety
- Medical Student Selection, Assignment, and Progress
- Medical Student Academic Support, Career Advising, and Records
- Medical Student Health Services, Personal Counseling, and Financial Aid

**ACGME Requirements (Residency Programs):**
- Institutional requirements
- Common program requirements
- Specialty-specific requirements
- Milestones and Clinical Competency Committees

## Use Cases

### Medical School Curriculum Development

```markdown
## Curriculum Revision Project

### Phase 1: Needs Assessment
- Review accreditation feedback
- Analyze student performance data
- Survey stakeholders (faculty, students, graduates, employers)
- Benchmark against peer institutions

### Phase 2: Design
- Define program-level competencies
- Map competencies to EPAs
- Develop course-level objectives
- Create assessment blueprint
- Design integrated curriculum threads

### Phase 3: Implementation
- Faculty development workshops
- Pilot courses with feedback
- Iterative refinement
- Full rollout with monitoring

### Phase 4: Evaluation
- Formative feedback collection
- Summative outcome analysis
- Continuous quality improvement cycle
```

### Educational Research Study

```markdown
## Study Protocol: Effect of Spaced Retrieval on Anatomy Retention

### Research Question
Does spaced retrieval practice improve long-term retention of anatomical
knowledge compared to massed practice in first-year medical students?

### Design
Randomized controlled trial with parallel groups

### Participants
- N = 120 first-year medical students
- Inclusion: Enrolled in anatomy course
- Exclusion: Prior anatomy coursework, learning disabilities

### Intervention
- Control: Traditional study (massed practice)
- Intervention: Spaced retrieval schedule (expanding intervals)

### Outcomes
- Primary: Anatomy exam score at 3 months
- Secondary: Retention at 6 months, study time, satisfaction

### Analysis
- ANCOVA controlling for baseline knowledge
- Effect size calculation (Cohen's d)
- Per-protocol and intention-to-treat analyses
```

### OSCE Development

```markdown
## OSCE Blueprint

### Station 1: Chest Pain Assessment
- Competencies: History taking, clinical reasoning
- Time: 10 minutes (8 encounter + 2 feedback)
- Standardized patient case
- Checklist + global rating scale

### Station 2: Breaking Bad News
- Competencies: Communication, professionalism
- Time: 10 minutes
- Standardized patient (cancer diagnosis)
- Communication skills checklist

### Station 3: ECG Interpretation
- Competencies: Medical knowledge, data interpretation
- Time: 5 minutes
- Written station with 3 ECG strips
- Structured answer key

### Quality Assurance
- Case author training
- SP training and calibration
- Pilot testing
- Post-hoc psychometric analysis
```

## Practical Examples

### Creating Learning Objectives

```python
# Learning Objective Generator Pattern

def create_learning_objective(
    timeframe: str,
    action_verb: str,
    content: str,
    condition: str = None,
    criterion: str = None
) -> str:
    """
    Generate SMART learning objectives for medical education.

    Args:
        timeframe: When mastery expected (e.g., "end of clerkship")
        action_verb: Observable action from Bloom's taxonomy
        content: Knowledge/skill to be learned
        condition: Context for demonstration (optional)
        criterion: Standard for acceptable performance (optional)

    Returns:
        Formatted learning objective string
    """
    objective = f"By the {timeframe}, learners will be able to {action_verb} {content}"

    if condition:
        objective += f" {condition}"

    if criterion:
        objective += f" {criterion}"

    return objective + "."

# Example usage
objective = create_learning_objective(
    timeframe="end of the internal medicine clerkship",
    action_verb="formulate",
    content="a differential diagnosis for chest pain",
    condition="given a clinical vignette",
    criterion="including at least 5 conditions ranked by probability"
)
```

### Item Analysis

```python
import numpy as np
from scipy import stats

def analyze_mcq_item(responses: np.ndarray, correct_answer: int,
                     total_scores: np.ndarray) -> dict:
    """
    Perform classical item analysis for MCQ.

    Args:
        responses: Array of student responses (1-indexed options)
        correct_answer: The correct option number
        total_scores: Array of total test scores for each student

    Returns:
        Dictionary with item statistics
    """
    n = len(responses)
    correct = responses == correct_answer

    # Difficulty (p-value)
    difficulty = np.mean(correct)

    # Point-biserial correlation
    point_biserial, p_value = stats.pointbiserialr(correct, total_scores)

    # Option analysis
    options = {}
    unique_opts = np.unique(responses)
    for opt in unique_opts:
        opt_mask = responses == opt
        options[f"option_{opt}"] = {
            "proportion": np.mean(opt_mask),
            "mean_score": np.mean(total_scores[opt_mask]) if np.any(opt_mask) else 0
        }

    return {
        "difficulty": round(difficulty, 3),
        "discrimination": round(point_biserial, 3),
        "p_value": round(p_value, 4),
        "n_responses": n,
        "option_analysis": options,
        "quality_flag": "good" if 0.3 <= difficulty <= 0.7 and point_biserial > 0.2 else "review"
    }
```

### Reliability Calculation

```python
import numpy as np

def cronbachs_alpha(item_scores: np.ndarray) -> float:
    """
    Calculate Cronbach's alpha for internal consistency.

    Args:
        item_scores: 2D array (students x items)

    Returns:
        Cronbach's alpha coefficient
    """
    n_items = item_scores.shape[1]
    item_variances = np.var(item_scores, axis=0, ddof=1)
    total_variance = np.var(np.sum(item_scores, axis=1), ddof=1)

    alpha = (n_items / (n_items - 1)) * (1 - np.sum(item_variances) / total_variance)

    return round(alpha, 3)

def inter_rater_reliability(ratings: np.ndarray, method: str = "icc") -> dict:
    """
    Calculate inter-rater reliability.

    Args:
        ratings: 2D array (subjects x raters)
        method: "icc" for ICC or "kappa" for Fleiss' kappa

    Returns:
        Reliability statistics
    """
    n_subjects, n_raters = ratings.shape

    if method == "icc":
        # ICC(2,1) - two-way random, single measures
        grand_mean = np.mean(ratings)

        # Between-subjects variance
        subject_means = np.mean(ratings, axis=1)
        ms_between = n_raters * np.var(subject_means, ddof=1)

        # Within-subjects variance
        ms_within = np.mean(np.var(ratings, axis=1, ddof=1))

        # ICC calculation
        icc = (ms_between - ms_within) / (ms_between + (n_raters - 1) * ms_within)

        return {
            "icc": round(icc, 3),
            "interpretation": interpret_icc(icc)
        }

    return {"error": "Method not implemented"}

def interpret_icc(icc: float) -> str:
    if icc < 0.5:
        return "poor"
    elif icc < 0.75:
        return "moderate"
    elif icc < 0.9:
        return "good"
    else:
        return "excellent"
```

## Integration with Other Skills

This skill works well with:

- **scientific-writing**: For manuscript preparation and publication
- **hypothesis-generation**: For developing research questions
- **statistical-analysis**: For advanced statistical methods
- **scientific-schematics**: For curriculum maps and diagrams
- **literature-review**: For evidence synthesis in education research
- **research-grants**: For educational research funding proposals
- **clinical-decision-support**: For integration with clinical training

## Dependencies

**Python Packages:**
- numpy
- scipy
- pandas
- statsmodels
- scikit-learn (for advanced psychometrics)

**Recommended Tools:**
- R with psych package (advanced psychometrics)
- Mplus or lavaan (structural equation modeling)
- SPSS or Stata (traditional education statistics)

## References

Key resources for medical education research:

1. Kern DE, et al. Curriculum Development for Medical Education: A Six-Step Approach
2. Downing SM, Yudkowsky R. Assessment in Health Professions Education
3. Cook DA, et al. Best practices in medical education research
4. Sullivan GM. Getting off the "gold standard": Randomized controlled trials and education research
5. AMEE Guides in Medical Education series
6. Medical Education journal and Academic Medicine for current research

## Journals and Resources

- Academic Medicine
- Medical Education
- Medical Teacher
- Teaching and Learning in Medicine
- Advances in Health Sciences Education
- BMC Medical Education
- Journal of Graduate Medical Education
- MedEdPORTAL
