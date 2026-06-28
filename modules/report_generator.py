def generate_report(matched, missing, score):

    print("\n========== ELIGIBILITY REPORT ==========\n")

    if score >= 70:
        status = "Highly Eligible"
    elif score >= 40:
        status = "Partially Eligible"
    else:
        status = "Not Yet Eligible"

    print(f"Status: {status}")
    print(f"\nMatch Score: {score}%")

    print("\nStrengths:")
    for skill in matched:
        print(f"✓ {skill}")

    print("\nNeed Improvement:")
    for skill in missing:
        print(f"✗ {skill}")