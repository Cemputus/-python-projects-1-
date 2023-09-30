import sqlite3

def create_database():
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        amount REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def add_expense(date, category, description, amount):
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses (date, category, description, amount)
    VALUES (?, ?, ?, ?)
    """, (date, category, description, amount))

    conn.commit()
    conn.close()

def get_expenses_by_category(category):
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM expenses WHERE category = ?
    """, (category,))

    expenses = cursor.fetchall()
    conn.close()

    return expenses

def get_total_expenses():
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_expenses = cursor.fetchone()[0] or 0

    conn.close()

    return total_expenses
