def detect_event(text):

    text = text.lower()

    if "deploy" in text or "military" in text:
        return "Military Activity"

    if "sanction" in text:
        return "Economic Sanction"

    if "earthquake" in text:
        return "Climate Disaster"

    if "election" in text:
        return "Political Event"

    return "General Event"
