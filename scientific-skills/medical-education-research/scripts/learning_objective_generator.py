#!/usr/bin/env python3
"""
Learning Objective Generator for Medical Education

Creates SMART learning objectives aligned with Bloom's Taxonomy
and maps them to assessment methods.

Usage:
    python learning_objective_generator.py --domain cognitive --level apply
    python learning_objective_generator.py --interactive
"""

import argparse
import random
from typing import Dict, List, Optional

# Bloom's Taxonomy Cognitive Domain
BLOOMS_COGNITIVE = {
    "remember": {
        "description": "Retrieve relevant knowledge from long-term memory",
        "verbs": [
            "define", "list", "recall", "identify", "recognize", "name",
            "state", "describe", "match", "label", "select"
        ],
        "assessment_methods": [
            "Multiple choice (recognition)",
            "Fill-in-the-blank",
            "Matching exercises",
            "Labeling diagrams"
        ],
        "medical_examples": [
            "List the cranial nerves in order",
            "Identify the bones of the hand on an X-ray",
            "Define the criteria for metabolic syndrome",
            "Recall the steps of the coagulation cascade"
        ]
    },
    "understand": {
        "description": "Construct meaning from instructional messages",
        "verbs": [
            "explain", "describe", "summarize", "interpret", "classify",
            "compare", "contrast", "exemplify", "infer", "paraphrase"
        ],
        "assessment_methods": [
            "Short answer questions",
            "Case summaries",
            "Concept mapping",
            "Oral explanations"
        ],
        "medical_examples": [
            "Explain the pathophysiology of heart failure",
            "Compare Type 1 and Type 2 diabetes",
            "Summarize the mechanism of action of beta-blockers",
            "Interpret the findings on this chest X-ray"
        ]
    },
    "apply": {
        "description": "Carry out or use a procedure in a given situation",
        "verbs": [
            "demonstrate", "apply", "solve", "use", "implement",
            "execute", "perform", "calculate", "practice"
        ],
        "assessment_methods": [
            "OSCE stations",
            "Simulation scenarios",
            "Case-based problems",
            "Skill demonstrations"
        ],
        "medical_examples": [
            "Perform a focused cardiac examination",
            "Apply ACLS protocols in a simulated cardiac arrest",
            "Calculate the anion gap from laboratory values",
            "Use the Ottawa Ankle Rules to determine need for imaging"
        ]
    },
    "analyze": {
        "description": "Break material into parts and determine relationships",
        "verbs": [
            "analyze", "differentiate", "organize", "attribute",
            "compare", "contrast", "distinguish", "examine", "question"
        ],
        "assessment_methods": [
            "Case analysis",
            "Diagnostic reasoning exercises",
            "Literature critique",
            "Root cause analysis"
        ],
        "medical_examples": [
            "Analyze ECG findings to differentiate types of MI",
            "Compare treatment options for a patient with multiple comorbidities",
            "Examine the evidence supporting screening recommendations",
            "Differentiate between viral and bacterial meningitis"
        ]
    },
    "evaluate": {
        "description": "Make judgments based on criteria and standards",
        "verbs": [
            "evaluate", "assess", "critique", "judge", "justify",
            "appraise", "defend", "prioritize", "recommend"
        ],
        "assessment_methods": [
            "Case management plans",
            "Ethics consultations",
            "Peer review exercises",
            "Treatment justification"
        ],
        "medical_examples": [
            "Evaluate treatment options and recommend therapy",
            "Assess a patient's capacity to make medical decisions",
            "Critique the methodology of a clinical trial",
            "Prioritize problems in a patient with multiple active issues"
        ]
    },
    "create": {
        "description": "Put elements together to form a coherent whole",
        "verbs": [
            "create", "design", "develop", "formulate", "construct",
            "produce", "generate", "plan", "compose", "synthesize"
        ],
        "assessment_methods": [
            "Treatment plan development",
            "Quality improvement projects",
            "Research proposals",
            "Patient education materials"
        ],
        "medical_examples": [
            "Develop a comprehensive treatment plan for a diabetic patient",
            "Design a quality improvement intervention",
            "Formulate a research question and study design",
            "Create patient education materials for heart failure self-management"
        ]
    }
}

# Bloom's Psychomotor Domain (Simpson's Taxonomy)
BLOOMS_PSYCHOMOTOR = {
    "perception": {
        "description": "Use sensory cues to guide motor activity",
        "verbs": ["detect", "recognize", "observe", "relate"],
        "level": 1
    },
    "set": {
        "description": "Readiness to act (mental, physical, emotional)",
        "verbs": ["prepare", "position", "begin", "show"],
        "level": 2
    },
    "guided_response": {
        "description": "Early stages of learning a complex skill",
        "verbs": ["attempt", "copy", "follow", "replicate", "try"],
        "level": 3
    },
    "mechanism": {
        "description": "Intermediate stage - learned responses become habitual",
        "verbs": ["assemble", "complete", "demonstrate", "perform"],
        "level": 4
    },
    "complex_overt_response": {
        "description": "Skillful performance of motor acts",
        "verbs": ["coordinate", "execute", "integrate", "manage"],
        "level": 5
    },
    "adaptation": {
        "description": "Modify movement patterns to fit special requirements",
        "verbs": ["adapt", "alter", "modify", "revise", "vary"],
        "level": 6
    },
    "origination": {
        "description": "Create new movement patterns for specific situations",
        "verbs": ["create", "design", "develop", "originate"],
        "level": 7
    }
}

# Bloom's Affective Domain (Krathwohl's Taxonomy)
BLOOMS_AFFECTIVE = {
    "receiving": {
        "description": "Willingness to receive or attend",
        "verbs": ["ask", "attend", "listen", "observe", "follow"],
        "level": 1
    },
    "responding": {
        "description": "Active participation",
        "verbs": ["answer", "assist", "comply", "participate", "volunteer"],
        "level": 2
    },
    "valuing": {
        "description": "Worth or value attached to object, phenomenon, or behavior",
        "verbs": ["appreciate", "demonstrate", "prefer", "propose", "share"],
        "level": 3
    },
    "organization": {
        "description": "Organize values into priorities",
        "verbs": ["compare", "integrate", "organize", "synthesize"],
        "level": 4
    },
    "characterization": {
        "description": "Value system controls behavior",
        "verbs": ["act", "display", "influence", "practice", "verify"],
        "level": 5
    }
}


def generate_objective(
    content: str,
    level: str,
    timeframe: str = "end of the rotation",
    domain: str = "cognitive",
    condition: Optional[str] = None,
    criterion: Optional[str] = None
) -> Dict:
    """
    Generate a SMART learning objective.

    Args:
        content: The knowledge or skill to be learned
        level: Bloom's taxonomy level
        timeframe: When mastery is expected
        domain: cognitive, psychomotor, or affective
        condition: Context for demonstration (optional)
        criterion: Standard for acceptable performance (optional)

    Returns:
        Dictionary with objective and metadata
    """
    if domain == "cognitive":
        taxonomy = BLOOMS_COGNITIVE
    elif domain == "psychomotor":
        taxonomy = BLOOMS_PSYCHOMOTOR
    elif domain == "affective":
        taxonomy = BLOOMS_AFFECTIVE
    else:
        raise ValueError(f"Unknown domain: {domain}")

    if level not in taxonomy:
        raise ValueError(f"Unknown level: {level}. Valid levels: {list(taxonomy.keys())}")

    level_info = taxonomy[level]
    verb = random.choice(level_info["verbs"])

    # Build objective
    objective = f"By the {timeframe}, learners will be able to {verb} {content}"

    if condition:
        objective += f" {condition}"

    if criterion:
        objective += f" {criterion}"

    objective += "."

    return {
        "objective": objective,
        "domain": domain,
        "level": level,
        "verb": verb,
        "description": level_info.get("description", ""),
        "alternative_verbs": level_info["verbs"],
        "suggested_assessments": level_info.get("assessment_methods", [])
    }


def suggest_assessment_alignment(level: str) -> List[Dict]:
    """
    Suggest assessment methods aligned with cognitive level.

    Args:
        level: Bloom's taxonomy cognitive level

    Returns:
        List of suggested assessment methods with descriptions
    """
    if level not in BLOOMS_COGNITIVE:
        return []

    level_info = BLOOMS_COGNITIVE[level]

    suggestions = []
    for method in level_info.get("assessment_methods", []):
        suggestions.append({
            "method": method,
            "cognitive_level": level,
            "alignment": "Strong"
        })

    # Add complementary lower-level assessments
    levels = list(BLOOMS_COGNITIVE.keys())
    current_idx = levels.index(level)

    for i in range(max(0, current_idx - 1), current_idx):
        lower_level = levels[i]
        for method in BLOOMS_COGNITIVE[lower_level].get("assessment_methods", []):
            suggestions.append({
                "method": method,
                "cognitive_level": lower_level,
                "alignment": "Prerequisite"
            })

    return suggestions


def validate_objective(objective: str) -> Dict:
    """
    Validate a learning objective against SMART criteria.

    Args:
        objective: The learning objective text

    Returns:
        Dictionary with validation results
    """
    results = {
        "specific": False,
        "measurable": False,
        "achievable": True,  # Cannot determine automatically
        "relevant": True,    # Cannot determine automatically
        "timebound": False,
        "issues": [],
        "suggestions": []
    }

    objective_lower = objective.lower()

    # Check for timeframe
    time_indicators = ["by the", "end of", "within", "after", "during"]
    results["timebound"] = any(ind in objective_lower for ind in time_indicators)
    if not results["timebound"]:
        results["issues"].append("Missing timeframe")
        results["suggestions"].append("Add a timeframe (e.g., 'By the end of the clerkship...')")

    # Check for action verb
    all_verbs = []
    for level_info in BLOOMS_COGNITIVE.values():
        all_verbs.extend(level_info["verbs"])

    has_verb = any(verb in objective_lower for verb in all_verbs)
    results["measurable"] = has_verb
    if not has_verb:
        results["issues"].append("Missing observable action verb")
        results["suggestions"].append("Use a specific action verb from Bloom's taxonomy")

    # Check for vague terms
    vague_terms = ["understand", "know", "learn", "appreciate", "be aware of", "be familiar with"]
    has_vague = any(term in objective_lower for term in vague_terms)
    if has_vague:
        results["issues"].append("Contains vague/unmeasurable terms")
        results["suggestions"].append("Replace vague terms with specific action verbs")

    # Check specificity (presence of content)
    results["specific"] = len(objective.split()) >= 10 and not has_vague

    results["is_valid"] = (
        results["specific"] and
        results["measurable"] and
        results["timebound"]
    )

    return results


def create_objective_set(
    topic: str,
    levels: Optional[List[str]] = None
) -> List[Dict]:
    """
    Create a set of objectives spanning multiple cognitive levels.

    Args:
        topic: The topic for objectives
        levels: List of cognitive levels to include

    Returns:
        List of objectives at different levels
    """
    if levels is None:
        levels = ["remember", "understand", "apply", "analyze"]

    objectives = []
    for level in levels:
        obj = generate_objective(
            content=topic,
            level=level,
            timeframe="end of the course"
        )
        objectives.append(obj)

    return objectives


def main():
    parser = argparse.ArgumentParser(
        description="Generate and validate learning objectives"
    )
    parser.add_argument(
        "--domain",
        choices=["cognitive", "psychomotor", "affective"],
        default="cognitive",
        help="Learning domain"
    )
    parser.add_argument(
        "--level",
        help="Taxonomy level"
    )
    parser.add_argument(
        "--content",
        help="Learning content"
    )
    parser.add_argument(
        "--timeframe",
        default="end of the rotation",
        help="When mastery expected"
    )
    parser.add_argument(
        "--validate",
        help="Validate an existing objective"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Interactive mode"
    )
    parser.add_argument(
        "--list-levels",
        action="store_true",
        help="List available levels"
    )

    args = parser.parse_args()

    if args.list_levels:
        print("\nCOGNITIVE DOMAIN (Bloom's Taxonomy)")
        print("-" * 50)
        for level, info in BLOOMS_COGNITIVE.items():
            print(f"\n{level.upper()}")
            print(f"  {info['description']}")
            print(f"  Verbs: {', '.join(info['verbs'][:5])}...")

        print("\nPSYCHOMOTOR DOMAIN (Simpson's Taxonomy)")
        print("-" * 50)
        for level, info in BLOOMS_PSYCHOMOTOR.items():
            print(f"  Level {info['level']}: {level}")

        print("\nAFFECTIVE DOMAIN (Krathwohl's Taxonomy)")
        print("-" * 50)
        for level, info in BLOOMS_AFFECTIVE.items():
            print(f"  Level {info['level']}: {level}")

        return

    if args.validate:
        print("\nVALIDATING OBJECTIVE")
        print("-" * 50)
        print(f"Objective: {args.validate}")
        results = validate_objective(args.validate)
        print(f"\nValid: {results['is_valid']}")
        print(f"Specific: {results['specific']}")
        print(f"Measurable: {results['measurable']}")
        print(f"Time-bound: {results['timebound']}")

        if results["issues"]:
            print("\nIssues found:")
            for issue in results["issues"]:
                print(f"  - {issue}")

        if results["suggestions"]:
            print("\nSuggestions:")
            for sugg in results["suggestions"]:
                print(f"  - {sugg}")

        return

    if args.interactive:
        print("\n" + "="*60)
        print("LEARNING OBJECTIVE GENERATOR")
        print("="*60)

        domain = input("\nDomain (cognitive/psychomotor/affective) [cognitive]: ").strip() or "cognitive"

        if domain == "cognitive":
            print("\nCognitive levels: remember, understand, apply, analyze, evaluate, create")
        level = input("Level: ").strip()

        content = input("Content (what should learners be able to do): ").strip()
        timeframe = input("Timeframe [end of the rotation]: ").strip() or "end of the rotation"
        condition = input("Condition (optional): ").strip() or None
        criterion = input("Criterion (optional): ").strip() or None

        result = generate_objective(
            content=content,
            level=level,
            timeframe=timeframe,
            domain=domain,
            condition=condition,
            criterion=criterion
        )

        print("\n" + "-"*60)
        print("GENERATED OBJECTIVE")
        print("-"*60)
        print(f"\n{result['objective']}")
        print(f"\nDomain: {result['domain'].capitalize()}")
        print(f"Level: {result['level'].capitalize()}")
        print(f"Action verb: {result['verb']}")

        if result.get("suggested_assessments"):
            print("\nSuggested Assessment Methods:")
            for method in result["suggested_assessments"]:
                print(f"  - {method}")

        return

    if args.content and args.level:
        result = generate_objective(
            content=args.content,
            level=args.level,
            timeframe=args.timeframe,
            domain=args.domain
        )

        print(f"\nObjective: {result['objective']}")
        print(f"Domain: {result['domain']}")
        print(f"Level: {result['level']}")

        if result.get("suggested_assessments"):
            print("\nSuggested assessments:")
            for method in result["suggested_assessments"]:
                print(f"  - {method}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
