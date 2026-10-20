import sqlite3
from datetime import datetime

DATABASE = "users.db"


def create_history_table():
    """Create the detection history table and safely update older databases."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS detection_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            message TEXT NOT NULL,
            result TEXT NOT NULL,
            risk_score REAL NOT NULL,
            detected_at TEXT NOT NULL,
            detection_type TEXT NOT NULL DEFAULT 'Message'
        )
    """)

    # Existing users.db files may have been created before detection_type existed.
    cursor.execute("PRAGMA table_info(detection_history)")
    columns = {row[1] for row in cursor.fetchall()}
    if "detection_type" not in columns:
        cursor.execute(
            "ALTER TABLE detection_history "
            "ADD COLUMN detection_type TEXT NOT NULL DEFAULT 'Message'"
        )

    conn.commit()
    conn.close()


def save_detection(username, message, result, risk_score, detection_type="Message"):
    """Save a message or link detection for the current user."""
    conn = sqlite3.connect(DATABASE)
    try:
        detected_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO detection_history
                (username, message, result, risk_score, detected_at, detection_type)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            username,
            message,
            result,
            float(risk_score),
            detected_at,
            detection_type
        ))
        conn.commit()
    finally:
        conn.close()


def get_history(username):
    """Return this user's detections, newest first, including their type."""
    conn = sqlite3.connect(DATABASE)
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT message, result, risk_score, detected_at, detection_type
            FROM detection_history
            WHERE username = ?
            ORDER BY id DESC
        """, (username,))
        return cursor.fetchall()
    finally:
        conn.close()


create_history_table()
