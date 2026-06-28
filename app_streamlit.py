import streamlit as st
import os

from modules.resume_parser import extract_resume_text
from modules.skill_extractor import extract_skills
from modules.semantic_matcher import compare_skills
from modules.excel_generator import create_excel_study_plan

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="CareerDNA AI",
    page_icon="🚀",
    layout="wide"
)

# =====================================
# HEADER
# =====================================

st.title("🚀 CareerDNA AI")
st.subheader("AI-Powered Career Intelligence Platform")

# =====================================
# INPUTS
# =====================================

resume_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

jd_text = st.text_area(
    "Paste Job Description",
    height=250
)

# =====================================
# ANALYZE
# =====================================

if st.button("Analyze Resume"):

    if resume_file is None:
        st.error("Please upload a resume PDF.")

    elif jd_text.strip() == "":
        st.error("Please paste a Job Description.")

    else:

        # Save Resume

        os.makedirs("uploads", exist_ok=True)

        resume_path = os.path.join(
            "uploads",
            resume_file.name
        )

        with open(resume_path, "wb") as f:
            f.write(resume_file.getbuffer())

        # Extract Resume Text

        resume_text = extract_resume_text(
            resume_path
        )

        # Extract Skills

        resume_skills = extract_skills(
            resume_text
        )

        jd_skills = extract_skills(
            jd_text
        )

        # Match Skills

        matched, missing, score = compare_skills(
            resume_skills,
            jd_skills
        )

        # =====================================
        # SCORE
        # =====================================

        st.success("Analysis Completed!")

        st.metric(
            "CareerDNA Match Score",
            f"{score}%"
        )

        # =====================================
        # ELIGIBILITY
        # =====================================

        st.subheader("Eligibility Status")

        if score >= 70:
            st.success("Highly Eligible ✅")

        elif score >= 40:
            st.warning("Partially Eligible ⚠️")

        else:
            st.error("Not Yet Eligible ❌")

        # =====================================
        # RESUME SKILLS
        # =====================================

        st.subheader("📄 Resume Skills")

        if resume_skills:

            for skill in resume_skills:

                st.success(
                    f"✅ {skill['skill']}"
                )

                st.caption(
                    f"Category: {skill['category']} | "
                    f"Learning Time: {skill['learning_weeks']} weeks"
                )

        else:

            st.warning(
                "No skills detected in resume."
            )

        # =====================================
        # JD SKILLS
        # =====================================

        st.subheader("📌 Job Description Skills")

        if jd_skills:

            for skill in jd_skills:

                st.info(
                    f"📌 {skill['skill']}"
                )

                st.caption(
                    f"Category: {skill['category']} | "
                    f"Learning Time: {skill['learning_weeks']} weeks"
                )

        else:

            st.warning(
                "No skills detected from Job Description."
            )

        # =====================================
        # MATCHED
        # =====================================

        st.subheader("✅ Matched Skills")

        if matched:

            for skill in matched:

                st.success(
                    f"✅ {skill['skill']}"
                )

        else:

            st.warning(
                "No matching skills found."
            )

        # =====================================
        # MISSING
        # =====================================

        st.subheader("❌ Missing Skills")

        if missing:

            for skill in missing:

                st.error(
                    f"❌ {skill['skill']} "
                    f"({skill['learning_weeks']} weeks)"
                )

        else:

            st.success(
                "No missing skills."
            )

        # =====================================
        # EXCEL STUDY PLAN
        # =====================================

        if missing:

            excel_path = create_excel_study_plan(
                [skill["skill"] for skill in missing]
            )

            with open(
                excel_path,
                "rb"
            ) as file:

                st.download_button(
                    label="📥 Download Study Plan",
                    data=file,
                    file_name="study_plan.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )