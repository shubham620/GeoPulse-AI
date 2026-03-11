def risk_score(event_type):

    scores = {
        "Military Activity": 0.9,
        "Economic Sanction": 0.7,
        "Climate Disaster": 0.8,
        "Political Event": 0.6,
        "General Event": 0.4
    }

    return scores.get(event_type, 0.4)
