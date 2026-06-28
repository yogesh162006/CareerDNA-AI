from modules.resume_parser import extract_resume_text
from modules.jd_parser import extract_jd_text
from modules.skill_extractor import extract_skills
from modules.semantic_matcher import compare_skills
from modules.excel_generator import create_excel_study_plan


resume_text = extract_resume_text(
    "sample_resume.pdf"
)

jd_text = extract_jd_text(
    "sample_jd.txt"
)

resume_skills = extract_skills(
    resume_text
)

jd_skills = extract_skills(
    jd_text
)

matched, missing, score = compare_skills(
    resume_skills,
    jd_skills
)

print("\n========== CareerDNA AI ==========\n")

print(
    f"Match Score: {score}%"
)

print("\nMatched Skills:")

for skill in matched:

    print(
        f"✓ {skill['skill']}"
    )

print("\nMissing Skills:")

for skill in missing:

    print(
        f"✗ {skill['skill']}"
    )

excel_path = create_excel_study_plan(
    missing
)

print(
    f"\nStudy Plan Created:\n{excel_path}"
)