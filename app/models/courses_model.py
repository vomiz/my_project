class Courses():
    def __init__(self, course_id, course_name, language_id, duration_hours, price):
        self.course_id=course_id
        self.course_name=course_name
        self.language_id=language_id
        self.duration_hours=duration_hours
        self.price=price

    def __repr__(self):
        return (Courses({self.course_id},{self.course_name},{self.language_id},{self.duration_hours},{self.price}))
