import os

import pandas as pd
import plotly.express as px
import streamlit as st

from ai_engine import (
    analyze_performance,
    generate_badge,
    generate_study_plan
)

from database import (
    create_database,
    get_student_scores,
    save_score
)

from quiz_data import quiz_questions

from report_generator import create_report


# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="EduMentor AI",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# DATABASE
# ============================================================

create_database()


# ============================================================
# SESSION STATE
# ============================================================

if "latest_score" not in st.session_state:
    st.session_state.latest_score = None

if "latest_subject" not in st.session_state:
    st.session_state.latest_subject = None

if "latest_level" not in st.session_state:
    st.session_state.latest_level = None

if "latest_status" not in st.session_state:
    st.session_state.latest_status = None

if "latest_recommendation" not in st.session_state:
    st.session_state.latest_recommendation = None

if "latest_badge" not in st.session_state:
    st.session_state.latest_badge = None


# ============================================================
# FUNCTIONS
# ============================================================

def get_student_data(name):

    columns = [
        "ID",
        "Name",
        "Subject",
        "Level",
        "Score"
    ]

    if not name.strip():
        return pd.DataFrame(columns=columns)

    records = get_student_scores(name.strip())

    if not records:
        return pd.DataFrame(columns=columns)

    return pd.DataFrame(
        records,
        columns=columns
    )


def create_progress_chart(student_df):

    chart_df = student_df.copy()

    chart_df["Attempt"] = range(
        1,
        len(chart_df) + 1
    )

    fig = px.line(
        chart_df,
        x="Attempt",
        y="Score",
        markers=True
    )

    fig.update_layout(
        title="Your Quiz Performance",
        yaxis=dict(
            range=[0, 100],
            title="Score (%)"
        ),
        xaxis=dict(
            title="Quiz Attempt"
        ),
        height=350
    )

    return fig


def create_demo_chart():

    data = pd.DataFrame(
        {
            "Attempt": [1, 2, 3, 4, 5],
            "Score": [40, 52, 65, 75, 85]
        }
    )

    fig = px.line(
        data,
        x="Attempt",
        y="Score",
        markers=True
    )

    fig.update_layout(
        title="Example Learning Progress",
        yaxis=dict(
            range=[0, 100],
            title="Score (%)"
        ),
        xaxis=dict(
            title="Quiz Attempt"
        ),
        height=350
    )

    return fig


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🎓 EduMentor AI")

st.sidebar.write(
    "Personalized Learning Platform"
)

st.sidebar.divider()

st.sidebar.subheader(
    "Learning Setup"
)

student_name = st.sidebar.text_input(
    "Student Name",
    placeholder="Enter your name"
)

subject = st.sidebar.selectbox(
    "Subject",
    [
        "Python",
        "Cybersecurity",
        "AI"
    ]
)

level = st.sidebar.selectbox(
    "Learning Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Study Plan",
        "Take Quiz",
        "Progress Analytics",
        "Achievements",
        "Student Report"
    ]
)


# ============================================================
# STUDENT DATA
# ============================================================

student_df = get_student_data(
    student_name
)

total_quizzes = len(
    student_df
)

if total_quizzes > 0:

    average_score = round(
        student_df["Score"].mean(),
        1
    )

    best_score = int(
        student_df["Score"].max()
    )

    latest_score = int(
        student_df.iloc[-1]["Score"]
    )

else:

    average_score = 0
    best_score = 0
    latest_score = 0


# ============================================================
# LEARNING PLAN
# ============================================================

topics = generate_study_plan(
    subject,
    level
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.title(
        "🎓 EduMentor AI"
    )

    if student_name.strip():

        st.header(
            f"Welcome back, {student_name.strip()}! 👋"
        )

        st.write(
            f"Continue your {subject} learning journey."
        )

    else:

        st.header(
            "Welcome to EduMentor AI! 👋"
        )

        st.write(
            "Your personalized space for learning, "
            "practice, and progress tracking."
        )

    st.divider()

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Quizzes",
            total_quizzes
        )

    with col2:

        st.metric(
            "Average Score",
            f"{average_score}%"
        )

    with col3:

        st.metric(
            "Best Score",
            f"{best_score}%"
        )

    with col4:

        st.metric(
            "Latest Score",
            f"{latest_score}%"
        )

    st.divider()

    # --------------------------------------------------------
    # CURRENT GOAL
    # --------------------------------------------------------

    st.header(
        "🎯 Current Learning Goal"
    )

    if topics:

        if total_quizzes < len(topics):

            current_topic = topics[
                total_quizzes
            ]

        else:

            current_topic = topics[-1]

        st.info(
            f"**Next Topic: {current_topic}**\n\n"
            f"This is the next stage in your "
            f"{subject} learning path."
        )

        progress = min(
            total_quizzes / len(topics),
            1.0
        )

        st.progress(progress)

        st.write(
            f"{min(total_quizzes, len(topics))} "
            f"of {len(topics)} learning stages completed"
        )

    else:

        st.warning(
            "No learning plan is available."
        )

    st.divider()

    # --------------------------------------------------------
    # AI INSIGHT
    # --------------------------------------------------------

    st.header(
        "🧠 AI Learning Insight"
    )

    if total_quizzes == 0:

        st.info(
            "You have not completed a quiz yet. "
            "Take your first quiz to allow EduMentor AI "
            "to analyze your performance."
        )

    elif average_score >= 90:

        st.success(
            "Excellent performance. "
            "You can start exploring more advanced topics."
        )

    elif average_score >= 70:

        st.info(
            "You have a solid foundation. "
            "Continue practicing and review weaker areas."
        )

    elif average_score >= 50:

        st.warning(
            "You are making progress. "
            "Review your core concepts and keep practicing."
        )

    else:

        st.warning(
            "Focus on the fundamentals and practice regularly."
        )

    st.divider()

    # --------------------------------------------------------
    # PERFORMANCE
    # --------------------------------------------------------

    st.header(
        "📈 Learning Performance"
    )

    if student_df.empty:

        st.plotly_chart(
            create_demo_chart(),
            width="stretch"
        )

        st.caption(
            "This is an example chart. "
            "Your actual performance will appear after "
            "you complete a quiz."
        )

    else:

        st.plotly_chart(
            create_progress_chart(student_df),
            width="stretch"
        )

    st.divider()

    # --------------------------------------------------------
    # ROADMAP
    # --------------------------------------------------------

    st.header(
        "📚 Learning Roadmap"
    )

    if topics:

        for index, topic in enumerate(
            topics,
            start=1
        ):

            if index <= total_quizzes:

                st.success(
                    f"✅ {index}. {topic} — Completed"
                )

            elif index == total_quizzes + 1:

                st.info(
                    f"🔵 {index}. {topic} — Current"
                )

            else:

                st.write(
                    f"⚪ {index}. {topic} — Upcoming"
                )

    else:

        st.write(
            "No roadmap available."
        )

    st.divider()

    # --------------------------------------------------------
    # QUICK ACTIONS
    # --------------------------------------------------------

    st.header(
        "🚀 Continue Learning"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader(
            "📚 Study Plan"
        )

        st.write(
            "Follow your personalized learning roadmap."
        )

        st.info(
            "Choose **Study Plan** from the sidebar."
        )

    with col2:

        st.subheader(
            "📝 Knowledge Check"
        )

        st.write(
            "Test your knowledge with an interactive quiz."
        )

        st.info(
            "Choose **Take Quiz** from the sidebar."
        )

    with col3:

        st.subheader(
            "🏆 Achievements"
        )

        st.write(
            "Track your learning milestones."
        )

        st.info(
            "Choose **Achievements** from the sidebar."
        )


# ============================================================
# STUDY PLAN
# ============================================================

elif page == "Study Plan":

    st.title(
        "📚 Study Plan"
    )

    st.write(
        f"Subject: **{subject}**"
    )

    st.write(
        f"Level: **{level}**"
    )

    st.divider()

    if not topics:

        st.warning(
            "No study plan is available."
        )

    else:

        progress = min(
            total_quizzes / len(topics),
            1.0
        )

        st.progress(progress)

        st.write(
            f"{min(total_quizzes, len(topics))} "
            f"of {len(topics)} stages completed"
        )

        st.divider()

        for index, topic in enumerate(
            topics,
            start=1
        ):

            if index <= total_quizzes:

                st.success(
                    f"✅ {index}. {topic} — Completed"
                )

            elif index == total_quizzes + 1:

                st.info(
                    f"🔵 {index}. {topic} — Current"
                )

            else:

                st.write(
                    f"⚪ {index}. {topic} — Upcoming"
                )


# ============================================================
# QUIZ
# ============================================================

elif page == "Take Quiz":

    st.title(
        "📝 Knowledge Check"
    )

    st.write(
        f"Test your understanding of **{subject}**."
    )

    st.divider()

    if not student_name.strip():

        st.warning(
            "Please enter your name in the sidebar first."
        )

    else:

        questions = quiz_questions.get(
            subject,
            []
        )

        if not questions:

            st.error(
                "No questions are available for this subject."
            )

        else:

            st.subheader(
                f"{len(questions)} Questions"
            )

            answers = []

            for index, question in enumerate(
                questions
            ):

                st.write(
                    f"### Question {index + 1}"
                )

                st.write(
                    question["question"]
                )

                answer = st.radio(
                    "Select your answer",
                    question["options"],
                    key=f"question_{subject}_{index}"
                )

                answers.append(
                    answer
                )

                st.divider()

            if st.button(
                "Submit Quiz",
                type="primary",
                width="stretch"
            ):

                correct_answers = 0

                for index, question in enumerate(
                    questions
                ):

                    if answers[index] == question["answer"]:

                        correct_answers += 1

                score = round(
                    (
                        correct_answers /
                        len(questions)
                    ) * 100
                )

                status, recommendation = analyze_performance(
                    score
                )

                badge = generate_badge(
                    score
                )

                save_score(
                    student_name.strip(),
                    subject,
                    level,
                    score
                )

                st.session_state.latest_score = score
                st.session_state.latest_subject = subject
                st.session_state.latest_level = level
                st.session_state.latest_status = status
                st.session_state.latest_recommendation = recommendation
                st.session_state.latest_badge = badge

                st.success(
                    "Quiz submitted successfully! 🎉"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Score",
                        f"{score}%"
                    )

                with col2:

                    st.metric(
                        "Correct",
                        f"{correct_answers}/{len(questions)}"
                    )

                with col3:

                    st.metric(
                        "Performance",
                        status
                    )

                st.divider()

                st.subheader(
                    "🧠 AI Learning Feedback"
                )

                st.info(
                    recommendation
                )

                st.subheader(
                    "🏆 Achievement"
                )

                st.success(
                    badge
                )


# ============================================================
# PROGRESS ANALYTICS
# ============================================================

elif page == "Progress Analytics":

    st.title(
        "📈 Progress Analytics"
    )

    st.write(
        "Track how your performance changes over time."
    )

    st.divider()

    if not student_name.strip():

        st.info(
            "Enter your name in the sidebar."
        )

    elif student_df.empty:

        st.info(
            "Complete a quiz to generate your analytics."
        )

    else:

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Attempts",
                total_quizzes
            )

        with col2:

            st.metric(
                "Average Score",
                f"{average_score}%"
            )

        with col3:

            st.metric(
                "Best Score",
                f"{best_score}%"
            )

        st.divider()

        st.plotly_chart(
            create_progress_chart(student_df),
            width="stretch"
        )

        st.subheader(
            "Quiz History"
        )

        history = student_df[
            [
                "Subject",
                "Level",
                "Score"
            ]
        ]

        st.dataframe(
            history,
            width="stretch",
            hide_index=True
        )


# ============================================================
# ACHIEVEMENTS
# ============================================================

elif page == "Achievements":

    st.title(
        "🏆 Achievements"
    )

    st.write(
        "Track your learning milestones."
    )

    st.divider()

    if not student_name.strip():

        st.info(
            "Enter your name to begin."
        )

    elif student_df.empty:

        st.info(
            "Complete your first quiz to unlock achievements."
        )

    else:

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Quizzes",
                total_quizzes
            )

        with col2:

            st.metric(
                "Best Score",
                f"{best_score}%"
            )

        with col3:

            st.metric(
                "Average",
                f"{average_score}%"
            )

        st.divider()

        st.subheader(
            "Current Achievement"
        )

        st.success(
            generate_badge(best_score)
        )

        st.divider()

        st.subheader(
            "Milestones"
        )

        if total_quizzes >= 1:

            st.success(
                "✅ First Quiz"
            )

        else:

            st.info(
                "○ First Quiz"
            )

        if total_quizzes >= 3:

            st.success(
                "✅ Consistent Learner"
            )

        else:

            st.info(
                "○ Consistent Learner"
            )

        if best_score >= 90:

            st.success(
                "✅ High Performer"
            )

        else:

            st.info(
                "○ High Performer"
            )

        if average_score >= 80:

            st.success(
                "✅ Advanced Progress"
            )

        else:

            st.info(
                "○ Advanced Progress"
            )


# ============================================================
# STUDENT REPORT
# ============================================================

elif page == "Student Report":

    st.title(
        "📄 Student Report"
    )

    st.write(
        "Generate a professional PDF report from your latest quiz."
    )

    st.divider()

    if not student_name.strip():

        st.info(
            "Enter your name in the sidebar first."
        )

    elif st.session_state.latest_score is None:

        st.info(
            "Complete a quiz during this session first."
        )

    else:

        score = st.session_state.latest_score
        latest_subject = st.session_state.latest_subject
        latest_level = st.session_state.latest_level
        status = st.session_state.latest_status
        recommendation = st.session_state.latest_recommendation

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Score",
                f"{score}%"
            )

        with col2:

            st.metric(
                "Subject",
                latest_subject
            )

        with col3:

            st.metric(
                "Level",
                latest_level
            )

        st.divider()

        st.subheader(
            "Performance Feedback"
        )

        st.info(
            f"**Status:** {status}\n\n"
            f"{recommendation}"
        )

        os.makedirs(
            "reports",
            exist_ok=True
        )

        safe_name = (
            student_name
            .strip()
            .replace(" ", "_")
        )

        safe_subject = (
            latest_subject
            .replace(" ", "_")
        )

        filename = (
            f"reports/"
            f"{safe_name}_"
            f"{safe_subject}_"
            f"report.pdf"
        )

        try:

            create_report(
                filename,
                student_name.strip(),
                latest_subject,
                score,
                status,
                recommendation
            )

            with open(
                filename,
                "rb"
            ) as pdf_file:

                pdf_data = pdf_file.read()

            st.success(
                "Your personalized report is ready."
            )

            st.download_button(
                "Download PDF Report",
                data=pdf_data,
                file_name=os.path.basename(filename),
                mime="application/pdf",
                type="primary",
                width="stretch"
            )

        except Exception as error:

            st.error(
                f"Report generation failed: {error}"
            )