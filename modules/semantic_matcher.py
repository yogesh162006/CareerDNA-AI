def compare_skills(resume_skills, jd_skills):

    resume_names = {
        skill["skill"]
        for skill in resume_skills
    }

    jd_names = {
        skill["skill"]
        for skill in jd_skills
    }

    matched_names = resume_names & jd_names
    missing_names = jd_names - resume_names

    matched = [
        skill
        for skill in jd_skills
        if skill["skill"] in matched_names
    ]

    missing = [
        skill
        for skill in jd_skills
        if skill["skill"] in missing_names
    ]

    score = 0

    if len(jd_skills) > 0:
        score = round(
            (len(matched) / len(jd_skills)) * 100,
            2
        )

    return matched, missing, score