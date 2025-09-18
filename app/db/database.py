import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
def init_db():
    """

    :return:
    """
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", "language_school"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASS", "postgres"),
            host=os.getenv("DB_HOST","localhost"),
            port=os.getenv("DB_PORT", "5432")
        )
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS courses (
            course_id SERIAL PRIMARY KEY,
            course_name VARCHAR(100) NOT NULL,
            language_id INTEGER NOT NULL,
            duration_hours INTEGER NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (language_id) REFERENCES languages(language_id)
        );

        CREATE TABLE IF NOT EXISTS employees (
            employee_id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(100),
            salary DECIMAL(10, 2)
        );

        CREATE TABLE IF NOT EXISTS groups (
            group_id SERIAL PRIMARY KEY,
            group_name VARCHAR(100) NOT NULL UNIQUE,
            course_id INTEGER NOT NULL,
            teacher_id INTEGER NOT NULL,
            FOREIGN KEY (course_id) REFERENCES courses(course_id),
            FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
        );

        CREATE TABLE IF NOT EXISTS languages (
            language_id SERIAL PRIMARY KEY,
            language_name VARCHAR(100) NOT NULL UNIQUE
        );
                       
        CREATE TABLE IF NOT EXISTS lessons (
            lesson_id SERIAL PRIMARY KEY,
            group_id INTEGER NOT NULL,
            lesson_date DATE NOT NULL,
            topic VARCHAR(100),
            FOREIGN KEY (group_id) REFERENCES groups(group_id)
        );
                       
        CREATE TABLE IF NOT EXISTS student_groups (
            student_group_id SERIAL PRIMARY KEY,
            student_id INTEGER NOT NULL,
            group_id INTEGER NOT NULL,
            final_grade DECIMAL(4, 2),
            UNIQUE(student_id, group_id),
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (group_id) REFERENCES groups(group_id)
        );
                       
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(100),
            date_of_birth DATE
        );
                       
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id INTEGER PRIMARY KEY,
            specialization VARCHAR(100) NOT NULL,
            experience_years INTEGER,
            hourly_rate DECIMAL(8, 2) NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES employees(employee_id)
        );
                       
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username character varying(50) UNIQUE NOT NULL,
            password_hash character varying(200) NOT NULL
            );
        ''')

        conn.commit()
        print("База данных инициализирована успешно!")
        return conn, cursor

    except psycopg2.IntegrityError as e:
        print(f"Ошибка инициализации базы данных: {e}")
        return None, None
    
    # Создание подключения и курсора
conn, cursor = init_db()
if conn and cursor:
    print("Можно продолжать работу")
else:
    print("Не удалось подключиться к базе данных")