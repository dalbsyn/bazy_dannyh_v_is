import psycopg2 as p


class DataAccessor:
    def __init__(self):
        super().__init__()

        self.user = 'postgres'
        self.password = '123'
        self.dbname = 'studocurs'
        self.host = 'localhost'
        self.connection = p.connect(user = self.user, password = self.password, dbname = self.dbname, host = self.host)
        self.cursor = self.connection.cursor()

    def get_table(self):
        self.query = '''select courses.id, courses.name, courses.teacher,
        students_courses.id, students_courses.student_id, students_courses.courses_id
        from courses
        join students_courses on students_courses.courses_id = courses.id;'''
        self.cursor.execute(self.query)
        return self.cursor.fetchall()

    def add_student(self, student, course):
        self.query = '''insert into students_courses (student_id, course_id) values
        ({0}, {1});'''.format(student, course)
        self.cursor.execute(self.query)
        self.connection.commit()

    def del_student(self, student):
        self.query = '''delete from students where student_id = {0}'''.format(student);


temp = DataAccessor()
print(temp.get_table())
