def generate_study_plan(subject, level):

    plans = {

        "Python": [
            "Variables",
            "Data Types",
            "Conditions",
            "Loops",
            "Functions",
            "Object-Oriented Programming",
            "Mini Project"
        ],

        "Cybersecurity": [
            "Networking Basics",
            "CIA Triad",
            "Authentication",
            "Phishing",
            "Firewalls",
            "Incident Response",
            "Security Project"
        ],

        "AI": [
            "Python Fundamentals",
            "Data Processing",
            "Machine Learning Basics",
            "Model Training",
            "Evaluation",
            "Deployment",
            "AI Project"
        ]
    }

    topics = plans.get(subject, [])

    return topics


def analyze_performance(score_percentage):

    if score_percentage >= 90:
        return (
            "Excellent",
            "Outstanding performance. Continue with advanced topics."
        )

    elif score_percentage >= 70:
        return (
            "Good",
            "Strong understanding. Focus on refining weaker concepts."
        )

    elif score_percentage >= 50:
        return (
            "Needs Improvement",
            "Review core concepts and increase practice."
        )

    else:
        return (
            "At Risk",
            "Additional study and guided practice are recommended."
        )


def generate_badge(score_percentage):

    if score_percentage >= 90:
        return "🥇 High Performer"

    elif score_percentage >= 70:
        return "🥈 Consistent Learner"

    elif score_percentage >= 50:
        return "🏅 Active Learner"

    else:
        return "🚀 Future Champion"