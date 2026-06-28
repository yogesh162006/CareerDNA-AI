def generate_study_plan(missing_skills):

    print("\n========== STUDY PLAN ==========\n")

    for week, skill in enumerate(missing_skills, start=1):
        print(f"Week {week}: Learn {skill}")