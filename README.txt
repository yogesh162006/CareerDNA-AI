# CareerDNA AI

## Overview

CareerDNA AI is an AI-powered Career Intelligence Platform that helps job seekers understand their eligibility for a specific role by analyzing their resume against a job description.

The system identifies matching skills, detects missing skills, calculates an eligibility score, and generates a personalized study plan to help users improve their career readiness.

---

## Features

### Resume Analysis

* Upload Resume PDF
* Extract resume text automatically
* Identify technical and soft skills

### Job Description Analysis

* Analyze job descriptions
* Extract required skills
* Support for IT and software-related roles

### Skill Gap Detection

* Compare resume skills with job requirements
* Identify matched skills
* Identify missing skills

### Eligibility Scoring

* Calculate CareerDNA Match Score
* Determine eligibility status:

  * Highly Eligible
  * Partially Eligible
  * Not Yet Eligible

### Personalized Study Plan

* Generate week-wise learning roadmap
* Export study plan as Excel file
* Track learning progress

---

## Technology Stack

* Python
* Streamlit
* Pandas
* OpenPyXL
* PDF Text Extraction
* CSV Skill Database

---

## Project Structure

CareerDNA-AI/

├── App.py

├── app_streamlit.py

├── data/

│   └── skills_db.csv

├── modules/

│   ├── resume_parser.py

│   ├── skill_extractor.py

│   ├── semantic_matcher.py

│   ├── excel_generator.py

│   ├── jd_parser.py

│   ├── report_generator.py

│   └── study_plan_generator.py

├── uploads/

├── reports/

└── README.md

---

## How It Works

1. Upload a resume PDF.
2. Paste a job description.
3. CareerDNA AI extracts skills from both sources.
4. The platform compares resume skills against job requirements.
5. A match score is calculated.
6. Missing skills are identified.
7. A personalized Excel study plan is generated.

---

## Example Output

### Match Score

82%

### Eligibility Status

Highly Eligible ✅

### Matched Skills

* Python
* SQL
* Git
* Machine Learning

### Missing Skills

* Docker
* AWS
* Kubernetes

### Study Plan

Generated as downloadable Excel file.

---

## Future Enhancements

* AI-powered skill extraction using NLP
* Book recommendations
* Course recommendations
* Career readiness scoring
* Recruiter dashboard
* Multi-role analysis
* Resume improvement suggestions
* Interview preparation roadmap

---

## Author

A. Yogeshwaran - B.TECH AI&ML

Project: CareerDNA AI

Version: 1.0

---

## License

This project is intended for educational, research, and portfolio purposes.
