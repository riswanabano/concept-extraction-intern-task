import argparse
from csv_reader import read_subject_csv
import csv
import os

# Simulated rule-based concept extraction
def extract_concepts(question_text):
    keyword_to_concept = {
        "harappa": "Harappan Civilization",
        "mohenjo": "Harappan Civilization",
        "ashoka": "Ashokan Edicts",
        "vedic": "Vedic Period",
        "gupta": "Gupta Empire",
        "arthashastra": "Kautilya's Arthashastra",
        "tax": "Revenue Systems",
        "temple": "Temple Architecture",
        "surgery": "Ancient Indian Medicine",
        "sin": "Ancient Indian Mathematics",
        "quadrilateral": "Geometry in India"
        # Add more mappings as needed
    }

    found_concepts = set()
    lowered = question_text.lower()
    for keyword, concept in keyword_to_concept.items():
        if keyword in lowered:
            found_concepts.add(concept)

    return "; ".join(found_concepts) if found_concepts else "General Concept"

def main():
    parser = argparse.ArgumentParser(description="Intern Test Task: Question to Concept Mapping")
    parser.add_argument('--subject', required=True, choices=['ancient_history', 'math', 'physics', 'economics'], help='Subject to process')
    args = parser.parse_args()

    data = read_subject_csv(args.subject)
    print(f"Loaded {len(data)} questions for subject: {args.subject}")

    output_rows = []

    for row in data:
        question_num = row["Question Number"]
        question = row["Question"]
        concepts = extract_concepts(question)
        output_rows.append({
            "Question Number": question_num,
            "Question": question,
            "Concepts": concepts
        })
        print(f"Question {question_num}: {concepts}")

    # Write to output CSV
    output_file = "output_concepts.csv"
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Question Number", "Question", "Concepts"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"\n✅ Output written to {output_file}")

if __name__ == "__main__":
    main()