from flask import Flask, render_template, request

app = Flask(__name__)

def generate_response(user_message):
    message = user_message.lower()

    # 🚨 Crisis Support
    if any(word in message for word in ["suicide", "kill myself", "end my life", "self harm"]):
        return (
            "I'm really sorry you're feeling this way.\n\n"
            "You matter more than you know.\n"
            "Please consider reaching out to someone you trust right now.\n"
            "If you're in immediate danger, contact emergency services.\n\n"
            "You are not alone."
        )

    # 😔 Depression
    elif any(word in message for word in ["depress", "sad", "hopeless", "empty"]):
        return (
            "I’m really sorry you're feeling low.\n\n"
            "Try one small gentle thing for yourself today — "
            "a short walk, a glass of water, or a few deep breaths.\n\n"
            "You don’t have to carry this alone."
        )

    # 😰 Anxiety / Panic
    elif any(word in message for word in ["anxiety", "panic", "nervous", "overthinking"]):
        return (
            "It sounds like anxiety might be rising.\n\n"
            "Try this breathing exercise:\n"
            "Inhale for 4 seconds\n"
            "Hold for 4 seconds\n"
            "Exhale for 6 seconds\n\n"
            "Repeat slowly 5 times."
        )

    # 📚 Stress / Exams
    elif any(word in message for word in ["exam", "stress", "pressure", "deadline"]):
        return (
            "That sounds stressful.\n\n"
            "Break your work into 25-minute focus sessions.\n"
            "After each session, take a 5-minute break.\n\n"
            "Small steps reduce overwhelm."
        )

    # 💪 Motivation
    elif any(word in message for word in ["tired", "unmotivated", "lazy", "no energy"]):
        return (
            "It’s okay to feel low energy sometimes.\n\n"
            "Start with one tiny task that takes 2 minutes.\n"
            "Momentum builds from small beginnings.\n\n"
            "You’re capable of more than you think."
        )

    # 🌿 Default Support
    else:
        return (
            "ehh...sorry.\n\n"
            " My developer pushes to production and says ‘let’s see what happens'."
            " So, please try the limited datasets."
        )


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_message = request.form.get("message")

        if user_message:
            bot_reply = generate_response(user_message)
            return render_template("index.html", response=bot_reply)

    return render_template("index.html")


if __name__ == "__main__":

    app.run(debug=True)

