from openpyxl import Workbook
from openpyxl.styles import Font
import os

def create_excel_study_plan(missing_skills):

    wb = Workbook()
    ws = wb.active

    ws.title = "CareerDNA Study Plan"

    # Headers

    headers = [
        "Week",
        "Skill",
        "Status",
        "Completed"
    ]

    ws.append(headers)

    for cell in ws[1]:
        cell.font = Font(bold=True)

    # Data

    for week, skill in enumerate(
        missing_skills,
        start=1
    ):

        ws.append([
            f"Week {week}",
            skill,
            "Pending",
            "☐"
        ])

    # Column Widths

    ws.column_dimensions["A"].width = 15
    ws.column_dimensions["B"].width = 30
    ws.column_dimensions["C"].width = 15
    ws.column_dimensions["D"].width = 15

    # Save

    reports_folder = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        "reports"
    )

    os.makedirs(
        reports_folder,
        exist_ok=True
    )

    excel_path = os.path.join(
        reports_folder,
        "study_plan.xlsx"
    )

    wb.save(excel_path)

    return excel_path