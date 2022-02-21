import random


class Student:
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        return sum(grades) / len(grades)
    
    def show_progession(self):
        max_value = len(self.data_sheet.courses) * 150
        sum_ects = sum(self.data_sheet.get_ects())
        return sum_ects  / max_value * 100
    


class Course:
    def __init__(self, name, class_room, teacher, ects, grade=None):
        self.name = name
        self.class_room = class_room
        self.teacher = teacher
        self.ects = ects
        self.grade = grade

    def set_grade(self):
        grades = [0, 2, 4, 7, 10, 12]
        self.grade = random.choice(grades)


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
        return [course.grade for course in self.courses if course.grade != None]

    def get_ects(self):
        return [course.ects for course in self.courses]


def generate_students(amount, name_list, courses, img_url_list):
    genders = ["Male", "Female"]
    index = 0
    students = []
    while index <= amount:
        randCourseArray = []
        randCourse = random.choice(courses)
        randCourse.set_grade()
        randCourseArray.append(randCourse)
        currentStud = Student(
            random.choice(name_list),
            random.choice(genders),
            DataSheet(randCourseArray),
            random.choice(img_url_list),
        )
        students.append(currentStud)
        index += 1
    return students


course_list = []

course_list.append(Course("Python", "105", "Thomas", 150, 4))
course_list.append(Course("Game Development", "105", "Jesper", 150, 12))
course_list.append(Course("OOA/OOD", "105", "Kim", 150, 10))

d1 = DataSheet(course_list)

s1 = Student("Janus", "Male", d1, "www.image.com")
s2 = Student("Rasmus", "Male", d1, "www.image.com")
s3 = Student("Frederik", "Male", d1, "www.image.com")


names = [
    "Bob",
    "Lise",
    "Karen",
    "Rasmus",
    "Jon",
    "Jørgen",
    "Viggo",
    "Merete",
    "Inge-Lise",
    "Ingvar",
    "Johnny",
]

url_list = []
url_list.append("www.erdetfredag.dk")
url_list.append("www.arla.dk")
url_list.append("www.dr.dk")
url_list.append("www.youtube.com")
url_list.append("www.digitalocean.com")


# print(generate_students(5, names, course_list, url_list))
#print(d1.get_grades_as_list())
# print(s2.get_avg_grade())
#print(d1.get_ects())
#print(s1.show_progession())
