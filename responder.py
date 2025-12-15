# src/responder.py
def suggest_reply(category, priority):
    if category == "Work":
        return "Thank you for the update. I will review this and get back to you shortly."

    if priority == "High":
        return "Thanks for bringing this up. I will address this immediately."

    if category == "Newsletter":
        return "Thank you for the information."

    if category == "Personal":
        return "Thanks for your message! I’ll respond soon."

    return "Thank you for your email."
