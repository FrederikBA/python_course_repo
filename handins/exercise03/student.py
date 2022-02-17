class Student:
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        return sum(grades) / len(grades)


class Course:
    def __init__(self, name, class_room, teacher, ects, grade=None):
        self.name = name
        self.class_room = class_room
        self.teacher = teacher
        self.ects = ects
        self.grade = grade


class DataSheet:
    def __init__(self, courses):
        self.courses = []
        for course in courses:
            new_course = Course(
                course.name,
                course.class_room,
                course.teacher,
                course.ects,
                course.grade,
            )
            self.courses.append(new_course)

    def get_grades_as_list(self):
        return [course.grade for course in self.courses if course.grade is not None]


course_list = []

course_list.append(Course("Python", "105", "Thomas", 130, 4))
course_list.append(Course("Game Development", "105", "Jesper", 130, 12))
course_list.append(Course("OOA/OOD", "105", "Kim", 130, 10))

d1 = DataSheet(course_list)

s1 = Student("Janus", "Male", d1, "www.image.com")
s2 = Student("Rasmus", "Male", d1, "www.image.com")
s3 = Student("Frederik", "Male", d1, "www.image.com")

print(d1.get_grades_as_list())
print(s2.get_avg_grade())
