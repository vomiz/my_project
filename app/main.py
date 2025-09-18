from registration import reg
from db.database import init_db
from views.courses_view import *
from controllers.course_controller import *


if reg() == True:
    def main():
        init_db()
        while True:
            print("\nМеню:")
            print("1. Добавить курс")
            print("2. Вывод всех курсов")
            print("3. Изменение курса")
            print("4. Удаление курса")
            print("5. Выход")
            choice = input("Выберите действие: ")
            if choice == "1":
                course_id,course_name,language_id, duration_hours, price=add_courses()
                success=addition_course(course_id,course_name, language_id, duration_hours, price)
                add_course_result(success)
            elif choice == "2":
                courses = get_all_courses()
                display_all_courses(courses)
            elif choice == "3":
                course_id, price=update_price()
                change_price(course_id, price)
            elif choice == "4":
                course_id=delete_course_by_id()
                delete_course(course_id)
            elif choice == "5":
                print("Выход")
                break
            else:
                print("Неверный выбор")
    if __name__=="__main__":
        main()