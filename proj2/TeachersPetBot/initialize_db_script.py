import sqlite3

conn = sqlite3.connect("db.sqlite")

c = conn.cursor()

SQL_STATEMENT = """CREATE TABLE IF NOT EXISTS ta_office_hours (
                        guild_id    INT,
                        ta          VARCHAR(50),
                        day         VARCHAR(4),
                        begin_time  DATETIME,
                        end_time    DATETIME
                    )"""

c.execute(SQL_STATEMENT)

SQL_STATEMENT = """CREATE TABLE IF NOT EXISTS exams (
                        guild_id    INT,
                        title       VARCHAR(50),
                        desc        VARCHAR(300),
                        duration    VARCHAR(15),
                        begin_date  DATETIME,
                        end_date    DATETIME
                    );"""

c.execute(SQL_STATEMENT)


SQL_STATEMENT = """CREATE TABLE IF NOT EXISTS assignments (
                        guild_id    INT,
                        title       VARCHAR(50),
                        link        VARCHAR(300),
                        desc        VARCHAR(300),
                        date        DATETIME
                    );"""

c.execute(SQL_STATEMENT)

SQL_STATEMENT = """CREATE TABLE IF NOT EXISTS qna (
                        guild_id    INT,
                        author       VARCHAR(50),
                        answer        VARCHAR(300),
                        qnumber      INT
                    );"""

c.execute(SQL_STATEMENT)

SQL_STATEMENT = """INSERT INTO assignments VALUES(
                        1,
                        "Assignment #1",
                        "https://drive.google.com/assign1.html",
                        "Covers lecture material up to to the due date.",
                        "2021-09-25 18:30:00"
                    );"""

c.execute(SQL_STATEMENT)

SQL_STATEMENT = """INSERT INTO assignments VALUES(
                        1,
                        "Assignment #1.2",
                        "https://drive.google.com/assign1.html",
                        "Covers lecture material up to to the due date.",
                        "2021-09-26 18:30:00"
                    );"""

c.execute(SQL_STATEMENT)

SQL_STATEMENT = """CREATE TABLE IF NOT EXISTS email_address (
                        author_id    INT,
                        email_id       VARCHAR(50),
                        is_active   BOOLEAN NOT NULL CHECK (is_active IN (0, 1))
                    );"""

c.execute(SQL_STATEMENT)

SQL_STATEMENT = """INSERT INTO assignments VALUES(
                        1,
                        "Assignment #2",
                        "https://drive.google.com/assign2.html",
                        "Covers lecture material up to to the due date.",
                        "2021-09-28 18:30:00"
                    );"""

c.execute(SQL_STATEMENT)

SQL_STATEMENT = """INSERT INTO exams VALUES(
                        1,
                        "Exam 1",
                        "All materials up to the date of the exam.",
                        "180 minutes",
                        "2021-09-29 10:30:00",
                        "2021-10-05 10:30:00"
                    );"""

c.execute(SQL_STATEMENT)

SQL_STATEMENT = """INSERT INTO exams VALUES(
                        1,
                        "Exam 2",
                        "All materials after previous exam.",
                        "180 minutes",
                        "2021-10-06 16:30:00",
                        "2021-10-20 18:30:00"
                    );"""

c.execute(SQL_STATEMENT)

SQL_STATEMENT = """INSERT INTO exams VALUES(
                        1,
                        "Final Exam",
                        "Final exam - covers everything taught!",
                        "180 minutes",
                        "2021-12-02 14:30:00",
                        "2021-12-02 18:30:00"
                    );"""

c.execute(SQL_STATEMENT)

SQL_STATEMENT = """INSERT INTO qna VALUES(
                        1,
                        "kailash98 s",
                        "Hello World",
                        1
                    );"""

c.execute(SQL_STATEMENT)

SQL_STATEMENT = """INSERT INTO qna VALUES(
                        1,
                        "kailash98 s",
                        "Hello",
                        2
                    );"""

SQL_STATEMENT = """INSERT INTO ta_office_hours VALUES(
                        1,
                        "kailash98 s",
                        "Mon",
                        "1900-01-01 14:30:00",
                        "1900-01-01 18:30:00"
                    );"""

c.execute(SQL_STATEMENT)

conn.commit()

conn.close()
