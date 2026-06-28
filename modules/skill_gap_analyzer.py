import pandas as pd
import os

def analyze_skill_gaps(missing_skills):

    skills_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "skills_db.csv"
    )

    df = pd.read_csv(skills_path)

    print("\n========== SKILL GAP ANALYSIS ==========\n")

    for skill in missing_skills:

        row = df[df["skill"] == skill]

        if not row.empty:

            difficulty = row.iloc[0]["difficulty"]
            weeks = row.iloc[0]["learning_weeks"]

            print(f"{skill}")
            print(f"Difficulty: {difficulty}")
            print(f"Estimated Time: {weeks} weeks")
            print()