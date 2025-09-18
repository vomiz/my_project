from db.database import cursor, conn
import psycopg2

from core.security import verify_data,hash_data
def autorize_client(user_name:str,password:str)->tuple:
    """
    Авторизация
    :param user_name: имя пользователя
    :param password: пароль
    :return: Информация о найденном пользователе, None - в случае отсутствия
    """
    cursor.execute("SELECT * FROM client where username=%s",(user_name))
    result=cursor.fetchone()
    if result:
        client=verify_data(password, hash_data(password))
        return client
    else:
        return None

def addition_course(course_id, course_name, language_id, duration_hours, price)-> bool:
    """
    Добавление курса
    :param course: id клиента
    :param name: название
    :param language: язык
    :param hours: часы
    :param price: цена
    :return: True, если добавление успешно, иначе False
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO courses (course_id, course_name, language_id, duration_hours, price) VALUES (%s, %s, %s, %s, %s)", (course_id, course_name, language_id, duration_hours, price))
        conn.commit()
        return True
    except psycopg2.Error as e:
        print(f"Error adding employee: {e}")
        return False
    
def get_all_courses():
    """
    Получение всех курсов
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses")
        return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Error getting courses: {e}")
        return []
    
def change_price(course_id, price):
    cursor.execute("UPDATE courses SET price = %s WHERE course_id = %s", (price, course_id))
    conn.commit()
    return True


def delete_course(course_id):
    cursor.execute("DELETE FROM courses WHERE course_id = %s", (course_id))
    conn.commit()
    return True