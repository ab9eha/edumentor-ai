# 🎓 EduMentor AI

### AI-Powered Personalized Learning & Student Performance Platform

EduMentor AI is an educational platform designed to provide students with a more personalized learning experience.

The system allows students to choose a subject and learning level, complete interactive quizzes, receive performance-based feedback, follow a structured study plan, track their progress, and generate a personalized PDF learning report.

The project combines **Python, AI-based performance analysis, data visualization, SQLite, and Streamlit** into one educational application.

---

## 🚀 Live Demo

**Streamlit App:**
[🚀 Launch EduMentor AI](https://edumentor-ai1.streamlit.app/)

---

## 📌 Project Overview

Many educational platforms provide the same learning material to every student. EduMentor AI explores a different approach by using quiz performance to provide personalized learning feedback.

The platform analyzes a student's quiz score and categorizes their performance into different levels:

* 🥇 Excellent
* 🥈 Good
* 🏅 Needs Improvement
* 🚀 At Risk

Based on the result, the system provides a learning recommendation and tracks the student's progress over time.

---

## ✨ Features

### 🎯 Personalized Learning

Students can select:

* Subject
* Learning level
* Learning roadmap

The platform then provides a structured study plan based on the selected subject.

### 📝 Interactive Quizzes

Students can test their knowledge through subject-specific quizzes.

Currently supported subjects include:

* Python
* Cybersecurity
* Artificial Intelligence

The system automatically calculates the student's score after submitting the quiz.

### 🧠 AI-Based Performance Analysis

EduMentor AI analyzes quiz performance and generates feedback based on the student's score.

For example:

```text
Score: 85%

Status: Good

Recommendation:
Strong understanding. Focus on refining weaker concepts.
```

This creates a simple personalized feedback system rather than providing the same message to every student.

### 📈 Progress Analytics

The platform stores quiz results in a SQLite database and uses the saved information to display:

* Total quiz attempts
* Average score
* Best score
* Latest score
* Performance history
* Progress charts

Interactive charts are generated using Plotly.

### 🏆 Achievement System

Students can unlock learning milestones based on their activity and performance.

Examples include:

* First Quiz
* Consistent Learner
* High Performer
* Advanced Progress

### 📄 Personalized PDF Reports

EduMentor AI can generate a professional PDF report containing:

* Student name
* Subject
* Learning level
* Quiz score
* Performance status
* AI learning recommendation

Reports are generated using **ReportLab**.

---

## 🏗️ System Architecture

```text
Student
   │
   ▼
Streamlit Interface
   │
   ├── Subject Selection
   ├── Learning Level
   └── Quiz
   │
   ▼
Performance Analysis
   │
   ├── Score Calculation
   ├── Performance Classification
   └── Learning Recommendation
   │
   ▼
SQLite Database
   │
   ├── Quiz History
   ├── Student Progress
   └── Performance Records
   │
   ▼
Analytics & Visualization
   │
   ├── Progress Charts
   └── Achievement Tracking
   │
   ▼
Personalized PDF Report
```

---

## 🛠️ Technology Stack

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| Python       | Core programming language      |
| Streamlit    | Web application interface      |
| Pandas       | Data processing                |
| NumPy        | Numerical operations           |
| Plotly       | Interactive data visualization |
| Scikit-learn | Machine learning ecosystem     |
| SQLite       | Student progress database      |
| ReportLab    | PDF report generation          |

---

## 📂 Project Structure

```text
edumentor-ai/
│
├── app.py
├── ai_engine.py
├── database.py
├── quiz_data.py
├── report_generator.py
├── requirements.txt
├── README.md
│
├── assets/
│
└── reports/
```

### File Descriptions

**`app.py`**

Main Streamlit application containing the user interface and application workflow.

**`ai_engine.py`**

Contains the performance analysis, study-plan generation, and achievement logic.

**`database.py`**

Handles SQLite database creation and student progress storage.

**`quiz_data.py`**

Contains the subject-specific quiz questions and answers.

**`report_generator.py`**

Creates personalized PDF learning reports using ReportLab.

**`requirements.txt`**

Contains the Python packages required to run the project.

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ab9eha/edumentor-ai.git
```

### 2. Enter the project folder

```bash
cd edumentor-ai
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 📊 Example Workflow

A typical student workflow looks like this:

```text
Enter Student Name
        ↓
Choose Subject
        ↓
Choose Learning Level
        ↓
Follow Study Plan
        ↓
Take Quiz
        ↓
Calculate Score
        ↓
Analyze Performance
        ↓
Generate Recommendation
        ↓
Store Progress
        ↓
View Analytics
        ↓
Generate PDF Report
```

---

## 🔬 Educational & Technical Purpose

EduMentor AI was developed as a portfolio project exploring how artificial intelligence concepts and data-driven programming can be applied to education.

The project demonstrates practical experience with:

* Python application development
* Streamlit web applications
* Data processing
* Performance analytics
* Database management
* Interactive visualization
* AI-assisted personalization
* Automated PDF generation

Rather than attempting to replace teachers or provide fully automated educational decisions, the project is designed as an educational prototype demonstrating how student performance data can support personalized learning feedback.

---

## 🔮 Future Improvements

Potential future versions could include:

* 🤖 More advanced machine-learning models
* 📚 Larger question banks
* 🎯 Topic-level weakness detection
* 🧠 Adaptive quiz difficulty
* 💬 AI-powered tutoring chatbot
* 👩‍🏫 Teacher dashboard
* 👥 Multi-student accounts
* ☁️ Cloud database integration
* 🔐 User authentication
* 📱 Mobile-friendly interface
* 🌍 Additional subjects and languages

---

## ⚠️ Project Limitations

This is an educational prototype.

The current personalization system primarily uses quiz scores and predefined learning rules. It is not intended to provide professional educational assessment or replace qualified teachers.

The current quiz dataset is also relatively small. Future versions could use larger and more diverse datasets to support more advanced analysis.

---

## 👩‍💻 Author

**Abeeha Zeeshan**

Student Developer | AI & Computer Science

Interested in:

* Artificial Intelligence
* Cybersecurity
* Machine Learning
* Software Development
* Educational Technology

---

## ⭐ Project Goal

The goal of EduMentor AI is to explore how technology can make learning more **personalized, measurable, and interactive** while providing students with useful feedback about their progress.

If you find the project interesting, feel free to explore the code and experiment with the platform.
