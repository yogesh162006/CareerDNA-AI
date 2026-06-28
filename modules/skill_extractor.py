import pandas as pd
import os
import re

def extract_skills(text):

    skills_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "skills_db.csv"
    )

    skills_df = pd.read_csv(skills_path)

    text = str(text).lower()

    found_skills = []

    for _, row in skills_df.iterrows():

        skill = str(row["skill"]).strip()

        aliases = []
        if "aliases" in skills_df.columns:
            aliases = str(row["aliases"]).split(";")

        matched = False

        # Check skill name
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            matched = True

        # Check aliases
        if not matched:

            for alias in aliases:

                alias = alias.strip().lower()

                if alias == "":
                    continue

                pattern = r"\b" + re.escape(alias) + r"\b"

                if re.search(pattern, text):
                    matched = True
                    break

        if matched:

            skill_data = {
                "skill": skill,
                "category": row["category"] if "category" in skills_df.columns else "General",
                "learning_weeks": int(row["learning_weeks"]) if "learning_weeks" in skills_df.columns else 1
            }

            found_skills.append(skill_data)

    # Remove duplicates

    unique_skills = {}

    for item in found_skills:
        unique_skills[item["skill"]] = item

    return list(unique_skills.values())