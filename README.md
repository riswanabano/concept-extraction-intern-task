# Concept Extraction from Competitive Exam Questions

This project extracts **underlying concepts** from competitive exam questions (like UPSC – Ancient History). It helps in understanding which areas (e.g., "Harappan Civilization", "Temple Architecture", etc.) are being tested.

## Objective

Given a subject-wise CSV of MCQs, the tool identifies what **concepts** each question is testing and saves the result to a CSV.


## Folder Structure
.
├── main.py                 # Entry point (run this file)
├── llm_api.py              # Placeholder for LLM integration (not used now)
├── csv_reader.py           # Reads subject CSVs
├── resources/              # Folder with CSVs like ancient_history.csv
├── .env                    # API key file (not used, just placeholder)
├── requirements.txt        # Python dependencies
├── Makefile                # Easy command line usage
└── README.md               # This file
---

## How to Run

### Step 1: Install Dependencies
```bash
make install
Step 2: Run for any subject
python main.py --subject=ancient_history
Other choices: math, physics, economics
Simulated Output
Question 6: Harappan Civilization
Question 13: Ashokan Edicts
Question 19: Gupta Empire; Ancient Indian Mathematics
...
Also saved to output_concepts.csv in this format:
Question Number,Question,Concepts
6,Which of the following was a feature of the Harappan civilization?,Harappan Civilization
13,Which edicts talk about Dhamma?,Ashokan Edicts
...
LLM Prompt Format (used manually for testing)
Given the question: "<question here>", identify the historical concept(s) this question is based on.
Example:
Q: Which of the following was a feature of the Harappan civilization?

→ Concepts: Harappan Civilization, Urban Planning
Optional Enhancements (Future Scope)
	•	Use real LLMs like OpenAI/Anthropic via llm_api.py
	•	Build a concept keyword dictionary (e.g., “Ashoka” → Ashokan Edicts)
	•	Use NLP for better extraction
	•	Improve accuracy with Named Entity Recognition (NER)

	•	Name: Riswana Bano
	•	Roll No: 22b1038

# concept-extraction-intern-task

