import os

def extract_jd_text(file_name):

    jd_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        file_name
    )

    with open(jd_path, "r", encoding="utf-8") as file:
        return file.read()