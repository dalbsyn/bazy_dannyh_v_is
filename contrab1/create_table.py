import psycopg2

user = 'postgres'
password = '123'
dbname = 'studocurs'
host = 'localhost'

connection = psycopg2.connect(user=user, password=password, dbname = dbname, host=host)
cursor = connection.cursor()

def create():
	cursor.execute('''create table courses
		       (id serial primary key,
		       name varchar(128),
		       teacher varchar(128));''')
	cursor.execute('''create table students_courses
		       (id serial primary key,
		       student_id int,
		       courses_id int references courses (id)
		       );''')
	connection.commit()
    connection.close()

def fill():
    cursor.execute('''insert into courses (name, teacher) values
    ('чет', 'никита'),
    ('хрень', 'владислав'),
    ('гречка', 'борис');''')
    cursor.execute('''insert into students_courses (student_id, courses_id) values
    (1, 1),
    (23, 3),
    (34, 2);''')
    connection.commit()
    connection.close()

fill()
