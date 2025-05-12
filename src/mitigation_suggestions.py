def generate_mitigation_suggestions(risk_summary):
    """
    Generate recommendations based on the risk_summary.
      - For each user with anomalies, suggest additional security measures.
    """
    suggestions = {}
    for user, count in risk_summary.items():
        if count > 2:
            suggestions[user] = [
                "Enforce multi-factor authentication (MFA)",
                "Review and restrict access privileges",
                "Schedule periodic security training and audits"
            ]
        else:
            suggestions[user] = ["Monitor activity closely"]
    return suggestions

if __name__ == '__main__':
    sample_summary = {'alice': 3, 'bob': 1}
    sugg = generate_mitigation_suggestions(sample_summary)
    print(sugg)
