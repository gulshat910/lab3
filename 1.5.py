class Student:
    def __init__(self, name, student_id): #Инициализация нового экземпляра класса Student
        self.name = name
        self.student_id = student_id
        self.grades = [] #Список оценок студента

    def add_grade(self, grade): #Добавление оценки с проверкой валидности
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            raise ValueError("Оценка должна быть в диапазоне от 0 до 10") #Ошибка,если оценка выходит за пределы диапазона 0-10

    def get_average(self): #Возвращает средний балл студента
        if len(self.grades) == 0:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def display_info(self): # Выводит информацию о студенте в удобном формате
        print(f"Имя: {self.name}")
        print(f"ID студента: {self.student_id}")
        print(f"Оценки: {', '.join(map(str, self.grades))}")
        print(f"Средний балл: {self.get_average()}")

    def __str__(self): #Cтроковое представление объекта Student
        return f"Студент {self.name} (ID: {self.student_id})"

    def __eq__(self, other): #Сравнивает два объекта Student по их student_id
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    def __len__(self): #Возвращает количество оценок у студента
        return len(self.grades)
