class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            raise ValueError("Оценка должна быть в диапазоне от 0 до 10")

    def get_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print("Имя: {self.name}")
        print("ID студента: {self.student_id}")
        print("Оценки: {', '.join(map(str, self.grades))}")
        print("Средний балл: {self.get_average()}")

    def __str__(self):
        return f"Студент({self.name}, {self.student_id}, {self.grades})"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    def __len__(self):
        return len(self.grades)
