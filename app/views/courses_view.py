from db.database import cursor, conn
def add_courses():
    """
    Добавление курса
    """
    course_id = input("Enter course id: ")
    course_name = input("Enter course name: ")
    language_id = input("Enter language id: ")
    duration_hours = input("Enter duration hours: ")
    price = input("Enter price: ")
    return course_id, course_name, language_id, duration_hours, price
def add_course_result(success: bool):
    if success:
        print("Course added successfully")
    else:
        print("Course addition failed")



def display_all_courses(courses):
    """
    Отображение всех курсов
    """
    if not courses:
        print("Курсы не найдены")
        return
    
    print(f"{'ID курса'} {'Название курса'} {'ID языка'} {'Продолжительность курса в часах'} {'Цена'}")
    
    for course in courses:
        course_id = course[0] or ''
        course_name = course[1] or ''
        language_id = course[2] or ''
        duration_hours = course[3] or ''
        price = course[4] or ''
        
        print(f"{course_id} {course_name} {language_id} {duration_hours} {price}")
    
    print(f"\nВсего курсов: {len(courses)}")


def update_price():
    course_id = input("ID предмета для изменения цены: ")
    price = input("Новая цена: ")
    cursor.execute("UPDATE courses SET price = %s WHERE course_id = %s", (price, course_id))
    conn.commit()
    print("Цена обновлена.")
    return course_id, price



def delete_course_by_id():
    course_id = input("ID курса для удаления: ")
    cursor.execute("DELETE FROM courses WHERE course_id = %s", (course_id))
    conn.commit()
    print("Курс удален.")
    return course_id