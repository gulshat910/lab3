class Person:
    def __init__(self, name, age): #Инициализация нового экземпляра класса Person
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject): #Инициализация нового экземпляра класса Teacher
        super().__init__(name, age) #Вызов конструктора базового класса Person
        self.subject = subject #Преподаваемый предмет
        self.students = [] #Список студентов

    def add_student(self, student): #Добавляет студента в список студентов преподавателя
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student): #Удаляет студента из списка студентов преподавателя
        if student in self.students:
            self.students.remove(student)

    def list_students(self): #Возвращает список студентов преподавателя
        return self.students

