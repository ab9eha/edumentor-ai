import sqlite3


DB_NAME = "student_progress.db"


def get_connection():
    """Create and return a connection to the SQLite database."""
    return sqlite3.connect(DB_NAME)


def create_database():
    """Create the progress table if it does not exist."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT NOT NULL,
            level TEXT,
            score INTEGER NOT NULL
        )
    """)

    # Check whether the level column exists.
    cursor.execute("PRAGMA table_info(progress)")

    columns = cursor.fetchall()

    column_names = [
        column[1]
        for column in columns
    ]

    # Upgrade an older database automatically.
    if "level" not in column_names:

        cursor.execute("""
            ALTER TABLE progress
            ADD COLUMN level TEXT
        """)

    conn.commit()
    conn.close()


def save_score(name, subject, level, score):
    """Save a student's quiz result."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO progress
        (name, subject, level, score)
        VALUES (?, ?, ?, ?)
    """, (
        name,
        subject,
        level,
        score
    ))

    conn.commit()
    conn.close()


def get_all_scores():
    """Return all quiz results."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            subject,
            level,
            score
        FROM progress
        ORDER BY id ASC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_student_scores(name):
    """Return all quiz results for a specific student."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            subject,
            level,
            score
        FROM progress
        WHERE name = ?
        ORDER BY id ASC
    """, (name,))

    data = cursor.fetchall()

    conn.close()

    return data


def delete_all_scores():
    """Delete all saved quiz results."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM progress
    """)

    conn.commit()
    conn.close()


def reset_database():
    """Delete and recreate the progress table."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS progress
    """)

    cursor.execute("""
        CREATE TABLE progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT NOT NULL,
            level TEXT,
            score INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()