import sqlite3

DB_NAME = "summaries.db"


def create_table_if_not_exists() -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chapter_number INTEGER,
            summary TEXT
        )
    """
    )
    conn.commit()
    conn.close()


def store_summary_in_database(chapter_number: int, summary: str) -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO summaries (chapter_number, summary) VALUES (?, ?)", (chapter_number, summary))
    conn.commit()
    conn.close()


def get_chapter_summary(chapter_number: int) -> str:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT summary FROM summaries WHERE chapter_number = ?", (chapter_number,))
    summary = cursor.fetchone()[0]
    conn.close()
    return str(summary)
