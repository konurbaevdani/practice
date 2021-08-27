# """
# 1)	В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.
# """

# with open('task.txt', 'r') as f:
    # file = f.readlines()
    # print(f'количество строк {len(file)}')
    # for i in file:
    #     c = i.replace("\n", "")
    #     print(f"количество символов {len(c)} количество слов {len(i.split())}")


# """
# 2)	Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл
# """



# def hello_makers():
#     print('Hello, Makers!')

# Хранить функции в переменных

# makers = hello_makers
# print(id(makers))
# print(id(hello_makers))

# Определить функци внутри другой функции

# def outeer_func():
#     def inner_func():
#         print('Hello, Makers')
#     inner_func()
# outeer_func()


# Передавать функции в качестве оргумента и возвращать их из других функций

# def main_func(func):
#     print(f'Я получил функцию {func} в качестве оргумента')
#     func()
#     return func

# def hello_makers():
#     print('Hello, Makers!')

# print(main_func(hello_makers))


# Декораторы

# def func1():
#     print("I'm called indide other function")

# def func2(func):
#     print("I'll do something before func calling")
#     func()

# def func3():
#     print('Hello, Makers!!!!!!')

# func2(func3)


# def decorator(func):
#     print("Я - функция - декоратор")
#     def wrapper():
#         print("Я - функция - обертка")
#         print("Вызываем обертнутую функцию")
#         func()
#         print("Выхожу из обертки")
#         return func
#     return wrapper

# @decorator
# def hello_bootcamp():
#     print('This is bootcamp')

# hello_bootcamp()


# @decorator
# def hello_makers():
#     print('Hello, Makers!')

# print(hello_makers())


# def chek_password(func):
#     def wrapper(parameter):   
#         return func(parameter).strip()
#     return wrapper

# @chek_password
# def get_info(param: str) -> str:
#     return param

# @chek_password
# def get_password(password):
#     return password


# param = input('Enter your info: ')
# print(get_info(param))

# @chek_password
# def get_emeil():
#     emeil = input("enter emeil: ")
#     return emeil

# print(get_emeil())


# def bread(func):
#     def wrapper(*args):
#         print('</-----\>')
#         func(*args)
#         print('</_____>\>')
#     return wrapper

# def ingredients(func):
#     def wrapper(*args):
#         print('#tomato')
#         func(*args)
#         print("--salad--")
#     return wrapper

# @bread
# @ingredients
# def get_sandwich(*fillers):
#     for filler in fillers:
#         print(filler)

# get_sandwich('--ham--','**sausages**', '&ketchup&')



# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'See what I got: {args}')
#         print(f'See what I got: {kwargs}')
#         func(*args, **kwargs)
#     return wrapper

# @decorator
# def func_without_params():
#     print("I'm poor func without params")

# func_without_params()

# @decorator
# def func_with_params(name, last_name):
#     print("I'm a happy func with params")
#     print(f"Hello, {name} {last_name}")

# func_with_params('Sam', last_name='Wrile')


# def benchmark(iters: int) -> int:
#     def actual_decorator(func):
#         import time
#         def wrapper(*args, **kwargs):
#             total = 0
#             for i in range(iters):
#                 start = time.time()
#                 func_call = func(*args, **kwargs)
#                 end = time.time()
#                 total = total + (end - start)

#                 print(f'Avarage complete time: {total / iters}')
#             return func_call
#         return wrapper
#     return actual_decorator

# @benchmark(iters=1)
# def get_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage


# print(get_webpage(url='http://yandex.ru'))



# def title(func):
#     def wrapper(*name):
#         name = func(name)
#         return name.title()
#     return wrapper

# def check_symbols(func):
#     def wrapper(name):
#         name_list = list(func(name))
#         print(list(name_list))
#         symbols_list = list('1234567890!@#$%^&*()_-+=/<>|')
#         name_list = [letter for letter in name_list if not letter in symbols_list]
#         print(name_list)
#         name = ''.join(name_list)
#         return name
#     return wrapper

# @title
# @check_symbols
# def get_name(name):
#     return name

# print(get_name('jo$hn98'))



# # def func(x):
# #     return x * 2

# # func(10)
# # func('2')
# # func([1, 2])

# # def func():
# #     pass


# # class A:
# #     pass

# # print(type(func))
# # print(type(A))

# # 1. Функцию можно присвоить переменной

# # def my_func():
# #     print('Hello world')

# # func1 = my_func
# # func1()

# # 2. Функция может принимать другую в качестве аргумента.
# # Функция может возвращать функцию в качестве результата
# # Функция может определять внутри себя другие функции

# def func():
#     def func2():
#         a = 10
#     pass

# def func1(x):
#     pass

# def func2():
#     pass

# class A:
#     pass

# func1(10)
# func1('2')
# func1({})
# func1(func2)
# # func1(A)

# # Декораторы - функции, для расширения возможностей других функций, без изменения кода.

# # Декоратор должен принимать функцию, добавлять в неё функционал, и возвращать изменённую функцию

# def decorator(function):
#     def wrapper(*args, **kwargs):
#         print('Код до вызова')
#         print('Вызываем функцию')
#         res = function(*args, **kwargs)
#         print('Код после вызова')
#         return res
#     return wrapper

# @decorator
# def my_func1():
#     print('Hello World')

# @decorator
# def my_func2(x, y):
#     return x * y

# print(my_func2(20, 10))

# # my_func1()
# # decorator(my_func1)
# #записывает в файл, какая функция была вызвана, время, с какими аргументами
# def decorator(func):
#     import datetime
#     def wrapper(*args, **kwargs):
#         current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
#         func(*args, **kwargs)
#         with open('log.txt', 'a') as file:
#             file.write(f'{func.__name__}\n')
#             file.write(f'вызвана {current_time}\n')
#             file.write(f'Args: {args}\n')
#             file.write(f'Kwargs: {kwargs}\n')
#             file.write('-----------------\n')
#     return wrapper

# @decorator
# def func1():
#     print('Hello world')

# @decorator
# def func2(x, y):
#     return x + y

# @decorator
# def func3(url):
#     import urllib.request
#     urllib.request.urlopen(url)


# func1()

# func2(20, 25)

# func3('https://google.com/')

# func2(x=10, y=20)

# Декоратор, замеряющий время выполнения функции (за n повторений)
# def timer(func):
#     import time
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         working_time = end - start
#         print(f'Время выполнения функции {func.__name__}: {working_time} секунд')
#     return wrapper


# def timer(count=1):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             import time
#             total_time = 0
#             for i in range(count):
#                 start = time.time()
#                 func(*args, **kwargs)
#                 end = time.time()
#                 working_time = end - start
#                 total_time += working_time
#             avg_time = total_time / count
#             print(f'Среднее время выполнения функции {func.__name__}: {avg_time} секунд')
#         return wrapper
#     return decorator

# @timer(count=20)
# def func1():
#     print('Hello world')

# @timer()
# def func2(x, y):
#     return x + y

# @timer(count=100)
# def func3(url):
#     import urllib.request
#     urllib.request.urlopen(url)


# func3('https://aknet.kg')












"""
Таски по декораторам
"""
"""
1) Напишите декоратор, который печатает перед вызовом полученной функции строку: "Вызываю функцию <имя_функции>". Затем следует вызов функции. После вызова функции должна печататься строка: "Вызов функции <имя_функции> прошёл успешно"
"""
# def decor(func):
#     def wrapper():
#         print(f"Вызываю функцию {func}")
#         func()
#         print(f'Вызов функции {func} прошел успешно')
#         return func
#     return wrapper

# @decor
# def main():
#     print("Hello")


# main()


"""
2) Создайте декоратор, который будет распечатывать дату и время вызова принимаемой функции, а затем вызывает саму функцию, например:
# @decorator
# def func():
#     print('Hello world')

# func() -> 
# Функция запущена 26.02.2021 21:51
# Hello World
Для этого воспользуйтесь модулем datetime.
"""





"""
3) Создайте 3 декоратора, каждый из которых применяет к тексту определённый стиль:
выделение жирным <b>...</b>\
курсив <i>...</i>
подчеркивание <u>...</u>.
Далее создайте функцию которая будет возвращать текст “Hello world”, примените к этой функции цепочку декораторов
"""
# def decor1(func1):
#     def main():
#         print('<b>')
#         func1()
#         print('</b>')
#         return func1
#     return main

# def decor2(func):
#     def wrapper():
#         print('<i>')
#         func()
#         print('</i>')
#         return func
#     return wrapper

# def decor3(func2):
#     def git():
#         print('<u>')
#         func2()
#         print('</u>')
#         return func2
#     return git

# @decor1
# @decor2
# @decor3
# def main():
#     print('Hello')

# main()





"""
4) Создайте декоратор, замеряющий время выполнения функции в секундах. Затем объявите функцию, которая выполняет GET-запрос на главную страницу Google, оберните в декоратор и вызовите её
"""


# from datetime import datetime

# def not_during_the_night(func):
#     import time
#     def wrapper():
#         if 8 <= time.time().hour < 22:
#             func()
#         else:
            # pass  # Тише, соседи спят!
    # return wrapper

# def say_whee():
#     print("Ура!")

# say_whee = not_during_the_night(say_whee)
# print(say_whee)



# def benchmark(iters: int) -> int:
#     def actual_decorator(func):
#         import time
#         def wrapper(*args, **kwargs):
#             total = 0
#             for i in range(iters):
#                 start = time.time()
#                 func_call = func(*args, **kwargs)
#                 end = time.time()
#                 total = total + (end - start)

#                 print(f'Avarage complete time: {total / iters}')
#             return func_call
#         return wrapper
#     return actual_decorator

# @benchmark(iters=1)
# def get_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage


# print(get_webpage(url='http://google.com'))










# users = {
#   'John': 4145,
#   'Alise': 3255,
#   'Ann': 6795,  
# }

# def decorator(func):
#     def wrapper(username, password):
#       if username not in users.keys():
#         raise KeyError
#       elif password != users.get(username):
#         raise Exception
#       else:
#         func(username,password)
#     return wrapper

# @decorator
# def login(username, password):
#     print(f'Welcome, {username}')

# login('John', 4145)

"""
5) Создайте словарь users и сохраните в нем несколько пользователей (ключом будет имя пользователя, а значением пароль пользователя).
Напишите следующую функцию:
# def login(username, password):
#     print(f'Welcome, {username}')
Допишите к этой функции декоратор, который будет проверять есть ли в словаре пользователь с таким username и совпадает ли пароль.
Если нет, то функция вызывает определенный тип исключения:
"""




# class SomeClass:
#     pass

# class A:
#     pass

# a = A()
# print(isinstance(a, A))

# class int:
    


# a = 4
# print(type(a))



# int, str, list, tuple, dict, bool, set, frozenset

# a = 5 
# print(type(a))

# b = 'Makers'
# print(type(b))

# c = [1, 2, 3, 4]
# print(type(c))




# class Dog:
#     owder = 'Jonn'
   
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'Name: {self.name}, age: {self.age}'

#     def bark(self):
#         print('Gav-gav')

#     def dog_info(self):
#         return f'This is {self.name}, he is {self.age} years old'

#     def birthday(self, cake):
#         self.age += 1
#         self.cake = cake
#         return f'{self.name} is {self.age} now'

#     def friends(self, friend):
#         self.friend = friend
#         friend.friend = self

# dog1 = Dog(name='Rex', age=3)
# dog2 = Dog(name='Bobik', age=2)
# dog3 = Dog(name='Orea', age=1)

# dog1.friends(dog2)
# print(dog1.friend.name)
# print(dog2.friend.age)
# print(dog1.birthday('chocolate'))
# print(dog2.birthday('vanilla'))
# print(dog3.birthday('srawberry'))
# print(dog3.cake)
# print(dog2.cake)
# print(dog1.cake)
# print(dog1.age)
# dog1.bark()
# dog2.bark()
# dog3.bark()
# print(dog1.dog_info())
# dog3.owder = 'Alice'
# print(dog1.name)
# dog1.name = 'Tuzik'
# dog1.food = 'meat'
# print(dog1.name)
# print(dog1.food)
# print(dog2.name)
# print(dog1.owder)
# print(dog2.owder)
# print(dog3.owder)
# print(dog2.age)



# class Rectangle:

#     default_color = 'red'

#     def __init__(self, width, length):
#         self.width = width
#         self.length = length

#     def area(self):
#         return self.width * self.length

# rec1 = Rectangle(4, 6)
# rec2 = Rectangle(2, 7)
# rec2.default_color = 'yellow'
# print(rec1.default_color)
# # print(rec1.width)
# print(rec2.default_color)



# class Car:

#     car_count = 0

#     def __init__(self):
#         Car.car_count += 1

# car1 = Car()
# print(Car.car_count)
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.car_count)






# import random

# class Sniper:

#     def __init__(self, name):
#         self.name = name
#         self.health = 100

#     def shoot(self, sniper):
#         sniper.health -= 20

# sniper1 = Sniper(name='Ben')
# sniper2 = Sniper(name='Sam')

# choices = (sniper1, sniper2)

# while True:
#     shooter = random.choice(choices)
#     if shooter == sniper1:
#         shot = sniper2
#     else:
#         shot = sniper1

#     shooter.shoot(shot)
#     print(f'Shooter {shooter.name} is shooting, {shot.name} has {shot.health} health points')

#     if sniper1.health == 0:
#         print(f'{sniper1.name} is dead. {sniper2.name} won!!!')
#         break

#     elif sniper2.health == 0:
#         print(f'{sniper2.name} is dead. {sniper1.name} won!!!')
#         break

#     else:
#         continue





"""
1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
"""
# class Circle:
#     color = 'синий'
#     pi = 3.14

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f'{self.name}'

#     def func(self, radiuse):
#         self.raudiuse = radiuse * 3.14 ** 2
#         return f'{self.raudiuse}'


# a = Circle(3.14)
# a.color = 'красный'
# print(a.func(3.14))
# print(a.color)


"""
2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
"""

# class Song:

#     def __init__(self, name, author, year):
#         self.author = author
#         self.name = name
#         self.year = year


#     def __str__(self):
#         return f'{self.name} {self.author} {self.year}'


#     def show_author(self, author):
#         self.author = author
#         print(f'Автор песни - {self.author}')

#     def show_title(self, name):
#         self.name = name
#         print(f'Название этой песни - {self.name}')

#     def show_year(self, year):
#         self.year = year
#         print(f'Эта песня вышла в {self.year} году')

# song1 = Song(name='Dancin', author='Smith', year=2013)
# song1.show_author('Smith')
# song1.show_title('Dancin')
# song1.show_year(2013)






"""
3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
"""

# class Taxi:

#     def __str__(self):
#         return f'{self.p_lan} {self.p_kl} {self.name}'

#     def func(self, lan, kl, name):
#         self.p_lan = lan
#         self.name = name
#         self.p_kl = kl
#         self.p_kl *= self.p_lan
#         print(f'Компания {self.name}, стоимость посадки {self.p_lan}, стоимость за каждый пройденный километр {self.p_kl}')

    
# company1 = Taxi()
# company1.func(lan=35, kl=4, name='Namba')
# company2 = Taxi()
# company2.func(lan=50, kl=4, name='Yandex')
# company3 = Taxi()
# company3.func(lan=42, kl=4, name='Jorgo')




"""
4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""

# class Contacts:

#     def __init__(self, name, number, surname):
#         self.name = name
#         self.number = number
#         self.surname = surname

#     def __str__(self):
#         return f'{self.name} {self.number} {self.surname}'

#     def info(self):
#         return f"Контакт: {self.name} {self.surname}, телефон: +996{self.number}"

# man = Contacts(name = 'Daniel', surname = 'Konurbaev', number = 709819382)
# print(man.info())



"""
5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
"""
# Например:
# 23% от 89 вычисляем так:
# 89 * 23 : 100 = 20,47.

# 115% от 39 вычисляем так:
# По правилу 39 * 115 : 100 = 44,85.

# class Salary:

#     def __init__(self,das, fyt, ter):
#         self.das = das
#         self.fyt = fyt
#         self.ter = ter

#     def __str__(self):
#         return f'{self.das} {self.fyt} {self.ter}'

#     def func(self):
#         b = self.das * self.fyt * self.ter / 100
#         print(f'{b}')

# man = Salary(das=8, fyt=250, ter=8)
# man.func()




# class Parent():
#     pass

# class Child(Parent):
#     pass

# int, list, tuple



# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# isinstance(object, class)
# a = A()
# b = B()
# c = C()
# print(isinstance(c, A))
# print(isinstance(c, B))
# print(isinstance(b, A))
# print(isinstance(a, A))



# class Polygon:

#     sides = 'many'

#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs

#     def get_perimetr(self):
#         if self.args:
#             return sum(self.args)
#         elif self.kwargs:
#             return sum(self.kwargs.values())

# class Rectangle(Polygon):
    
#     sides = 4                                                # (a + b) * 2

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def get_perimetr(self):
#         return (self.a + self.b) * 2

# class Square(Rectangle):
    
#     def __init__(self, a):
#         self.a = a

#     def get_perimetr(self):
#         return self.a * 4

# square = Square(a=5)
# print(square.sides)
# print(square.get_perimetr())

# class Triangle(Polygon):
#     sides = 3

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b 
#         self.c = c

#     def get_perimetr(self):
#         return self.a + self.b + self.c

# triangle1 = Triangle(a=2, b=3, c=4)
# print(triangle1.sides)
# print(triangle1.get_perimetr())

# rectangle = Rectangle(a=7, b=6)
# rectangle2 = Rectangle(a=9, b =2)
# print(rectangle.sides)
# print(rectangle.get_perimetr())
# print(rectangle2.get_perimetr())

# polygon = Polygon(b=8, a=9, c=10)
        
# print(polygon.get_perimetr())
# print(polygon.sides)


# class MyDict(dict):
#     def get(self, key, default='Makers'):
#         print('This method has been changed')
#         return dict.get(self, key, default)

# dict1 = dict(a=3,b=5,c=8)
# print(dict1.get('d'))

# dict2 = MyDict(a=3,b=5,c=8)
# print(dict2.get('d'))


# class Human:
#     def __init__(self, name, last_name, id_number):
#         self.name = name
#         self.lastname = last_name
#         self.id = id_number

#     def get_info(self):
#         print(f'{self.name} {self.lastname}, id: {self.id}')

# class Employee(Human):
#     def __init__(self, name, last_name, id_number, position, salary):
#         super().__init__(name, last_name, id_number)
#         self.position = position
#         self.salary = salary

#     def get_info(self):
#         super().get_info()
#         print(f'He works as {self.position} and his salary is {self.salary}')

# person =Human(name='Jonn', last_name='Snow', id_number=678)
# person.get_info()

# employee = Employee(name='Jonn',last_name='Snow', id_number=678, position='IT=specialist', salary=10000)

# employee.get_info()


# class Art:
#     student_count = 100

# class Music(Art):
#     student_count = 50

#     def __init__(self):
#         Music.student_count += 1
#         Art.student_count += 1

# class Acting(Art):
#     student_count = 50

#     def __init__(self):
#         Acting.student_count += 1
#         Art.student_count += 1

# student1 = Music()
# student2 = Acting()
# student3 = Acting()
# print(Music.student_count)
# print(Acting.student_count)
# print(Art.student_count)







# class Animal:
#     def sound(self):
#         raise NotImplementedError

# class Cat(Animal):
#     def sound(self):
#         print('Meow')

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# class Frog(Animal):
#     def sound(self):
#         print('Quak')

# animal = Animal()
# animal.sound()

# cat = Cat()
# cat.sound()

# dog = Dog()
# dog.sound()

# frog = Frog()
# frog.sound()



"""
1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.
"""

# class Class1:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def func1(self):
#         return self.a + self.b

#     def func2(self):
#         return self.a * self.b

# class Class2(Class1):
#     def func3(self):
#         return self.a // self.b

#     def func4(self):
#         return self.a - self.b

# summing = Class2(6, 3)
# print(summing.func1())
# print(summing.func2())
# print(summing.func3())
# print(summing.func4())



"""
2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.
"""
# class A:
#     def __init__(sefl):
#         pass

#     def func1(self):
#         print(f'Основной функционал')

# class B(A):
#     def __init__(self):
#         pass

#     def func2(self):
#         super().func1()
#         print("Дополнительный функционал")

# b = B()
# b.func2()



"""
3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:
append, который будет принимать строку и добавлять её в конец исходной
pop, который удаляет из строки последний элемент и возвращает его.
Пример:
# example = MyString('String')
# example.append('hello')
# print(example) -> 'Stringhello'
# print(example.pop()) -> 'o'
# print(example) -> 'Stringhell'
"""

# class MyString(str):

#     def __init__(self, string):
#         self.string = string

#     def append_(self, hello):
#         self.hello = hello
#         if self.string != '':
#             self.string += self.hello
#         print(self.string)
#         # self.string += self.hello
#         # print(self.string)

#     def pop_(self):
#         b = self.string [0:-1]
#         self.string = [0:-1]
#         return b


# a = MyString('String')
# a.append_('hello')
# print(a.pop_())
# print(a)



"""
4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.
"""

# class MyDict(dict):
#     def get(self, key, default='Are you kidding?'):
#         return dict.get(self, key, default)

# dict1 = MyDict(a=3,b=5,c=8)
# print(dict1.get('b'))


"""
5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.
Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.
Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.
"""
# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f'Имя: {self.name},\n Возраст:{self.age}')

# class Student(Person):

#     def __init__(self, name, age, direction):
#         super().__init__(name, age)
#         self.dir = direction

#     def display_student(self):
#         super().display()
#         print(f'Направление:{self.dir}')

# student = Student(name='Макс', age=20, direction='Инженер')
# student.display()
# student.display_student()



"""
6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.
"""
# class ContactList(list):
#     def __getitem__(self, index):
#         if index < 0:
#             super().__getitem__(index)
#         elif index == 0 or index > len(self):
#             raise IndexError
#         else:
#             return super().__getitem__(index -1)

# my_list1 = ContactList(['Jonn', 'Ann', 'Alice'])
# print(my_list1['Jonn'])







# https://replit.com/@konurbaev/week-5-hw-tasks-5#main.py




# class A:
#     a = 10

# class B:
#     a = 15


# class C(A,B):
#     def get_a(self):
#         print(self.a)

# c1 = C()
# c1.get_a()







# https://replit.com/@konurbaev/week-5-hw-tasks-5#main.py







# a = 6
# b = 9
# print(a + b)
# c = '6'
# d = '9'
# print(c + d)
# f = [1,2,3,4,5]
# e = [6,7,8,9]
# print(f + e)



# dir()

# a = 'makers'
# b = 3
# c = [True, 'bootcamp', 677]
# d = {'makers': 'bootcamp'}
# e = (6, 7, 8, 9)
# f = {False, 'makers', 6, 3, 8}
# print(f'This is string methods: {dir(a)}')
# print(f'This is integer methods: {dir(b)}')
# print(f'This is list methods: {dir(c)}')
# print(f'This is dict methods: {dir(d)}')
# print(f'This is tuple methods: {dir(e)}')
# print(f'This is set methods: {dir(f)}')


# pop() -> list, dict, set

# list_ = [3, 4, 5, 6]
# dict_ = dict(a=1, b=2, c=3)
# set_ = {True, 'makers', 78, 0}

# list_.pop(1)
# dict_.pop('b')
# set_.pop()

# print(list_)
# print(dict_)
# print(set_)


"""
2) Напишите декоратор, который печатает перед вызовом полученной функции строку: "Вызываю функцию <имя_функции>". Затем следует вызов функции.
После вызова функции должна печататься строка: "Вызов функции <имя_функции> прошёл успешно"
"""
# def info(name):
#     def wrapper():
#         print(f"Вызываю функцию {name()}")
#         name()
#         print(f"Вызов функции {name()} прошёл успешно")
#         return name
#     return wrapper

# @info
# def main():
#     print('Jonn')

# main()


# def info():
#   def wrapper():
#     print(f'Вызываю функцию имени {main}')
#     main()
#     print(f'Вызов функции {main} прошёл успешно')
#   return wrapper


# @info
# def main(name):
#   print(f'Функиция от имени {name}')

# main('hello')











"""
3) Создайте 3 декоратора, каждый из которых применяет к тексту определённый стиль:
выделение жирным <b>...</b>\
курсив <i>...</i>
подчеркивание <u>...</u>.
Далее создайте функцию которая будет возвращать текст “Hello world”, примените к этой функции цепочку декораторов
"""
# def a(func):
#     def wrapper():
#         return f'<b> {func()} </b>'
#     return wrapper

# def b(func):
#     def wrapper():
#         return f'<i> {func()} </i>'
#     return wrapper

# def c(func):
#     def wrapper():
#         return f'<u> {func()} </u>'
#     return wrapper

# @a
# @b
# @c
# def main():
#     return 'Hello world'

# print(main())




"""
4) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). 
Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. 
Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
"""
# from math import pi
# class Circle:
#     color = 'red'
#     Pi = pi
#     def __init__(self, radiuse):
#         self.rad = radiuse

#     def func(self):
#         print(self.Pi * self.rad ** 2)

    

# a = Circle(radiuse=4)
# a.color = 'Blue'
# a.func()
# print(a.color)




"""
5) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения 
о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
"""


# class Song:
#     def __init__(self, show_author, show_title, show_year):
#         self.author = show_author
#         self.title = show_title
#         self.year = show_year

#     def author_(self):
#         return f"Автор этой песни {self.author}"

#     def title_(self):
#         return f'Название этой песни {self.title}'

#     def year_(self):
#         return f"Эта песня вышла в {self.year}году"

# a = Song(show_author='Smith', show_year=2013, show_title='Dancin')
# print(a.author_())
# print(a.title_())
# print(a.year_())




"""
7) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, 
который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и 
вызовите метод method1.
"""

# class A:
#     def method1(self):
#         return "Основной функционал"

# class B(A):
#     def method1(self):
#         b = super().method1()
#         print(b)
#         return "Дополнительный функционал"

# a = B()
# print(a.method1())
    













# update()-> dict, set

# dict_ = dict(a=1, b=2, c=3)
# set_ = {True, 'makers', 78, 0}

# dict_.update(d=4, e=5)
# set_.update({8, 0, -1})
# print(dict_)
# print(set_)



# class Car:
#     def __init__(self, name):
#         self.name = name

#     def go(self, destination):
#         print(f'{self.name} is going by car to {destination}')

# class Ship:
#     def __init__(self, name):
#         self.name = name

#     def go(self, destination):
#         print(f'{self.name} is going by ship to {destination}')


# class Airplane:
#     def __init__(self, name):
#         self.name = name

#     def go(self, destination):
#         print(f'{self.name} is flying by airplane in {destination}')

# class Train:
#     def __init__(self, name):
#         self.name = name

#     def go(self, detination):
#         print(f'{self.name} is going by trains to {detination}')


# class InfoMixin:
#     def info(self):
#         my_class = self.__class__.__name__
#         print(f"I'm a {my_class}, naned {self.name}, age {self.age}")






# class Cat(InfoMixin):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print('Neow')

# class Dog(InfoMixin):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print('Woof')

# class Duck(InfoMixin):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print('Quack')

# animal = Duck('Tom', 7)
# animal.info()


# class T1:
#     def __init__(self, iterable):
#         self.list = iterable

#     def total(self):
#         return sum(self.list)

# class T2:
#     def __init__(self, iterable):
#         self.list = iterable

#     def total(self):
#         return len(self.list)

# t1 = T1([1,2,3,4,5,6,7])
# t2 = T2([1,2,3,4,5,6,7])
# print(t1.total())
# print(t2.total())




# 3) Мебель
# 1. class House: тип дома, общая площадь, оставшаяся площадь и список мебели.
# 2. Мебель имеет название и площадь, например, кровать: 4 м2, шкаф-купе: 2 м2,
# стол: 1,5 квадратных метров.
# 3. Добавьте вышеуказанную мебель в дом.
# 4. При печати информации о доме требуется вывод: тип дома, общая площадь,
# оставшаяся площадь, список мебели.

# class House:
#     def __init__(self, type, total_area, furniture):
#         self.type = type
#         self.total_area = total_area
#         self.furniture = furniture

# furniture = {'кровать': 4, 'шкаф-купе':2}








# list_ = [3, 4, 5, 6]
# dict_ = dict(a=1, b=2, c=3)
# set_ = {True, 'makers', 78, 0}




"""
1) Объявите 3 переменных, запишите в них строку, список и словарь. Затем запишите их в список, пройдитесь по нему циклом и распечатайте длину каждого из объектов.
""" 

# a = 'makers'
# b = ['name', 234]
# c = {'a':1, 'b':2, 'c':3}
# def func(d):
#     e = []
#     if d == str:
#         print(len(d))
#         f = len(d)
#     elif d == list:
#         for i in d:
#             print(len(i))
#             e = len(i)
#     return f'{e}, {f}'
    
    # return e
    # print(e)
    # else:


# func(a)
# func(b)
# func(c)



















#     d = 0
#     for i in c:
#         d += len(i)
#         print(d)

# print(len(a))
# func(a)
# func(b)
# print(len(b))







"""
2) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
"""
# class Dog:
#     def voice(self):
#         print('Гав')

# class Cat:
#     def voice(self):
#         print('Мяу')    


# def to_pet(name):
#     name.voice()

# Rex = Dog()
# Tom = Cat()
# to_pet(Tom)
# to_pet(Rex)

# class InfoMixin:
#     def info(self):
#         my_class = self.__class__.__name__
#         print(f"I'm a {my_class}, naned {self.name}, age {self.age}")







"""
3) Создайте 3 класса: Person, Employee и Student, при этом Employee и Student должны наследоваться от Person. Определите во всех трёх классах метод get_info():
-для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.
-для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
-для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.
"""
# class Person:
#     def get_info(self):
#         print('Привет, меня зовут Иван Петров')

# class Employee(Person):
#     def get_info(self):
#         print('Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности "директор"')

# class Student(Person):
#     def get_info(self):
#         print('Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе')


# def get_human_info(name):
#     name.get_info()

# Ivan1 = Person()
# Ivan2 = Employee()
# Ivan3 = Student()

# get_human_info(Ivan1)
# get_human_info(Ivan2)
# get_human_info(Ivan3)






"""
4) Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.

Затем наследуйте от Shape три класса: Triangle, Square и Circle.
-треугольник создаётся с заданными основанием и высотой
-квадрат создаётся с заданной длиной стороны
-круг создаётся с заданным радиусом
Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

Подсказка: для создания абстрактных классов воспользуйтесь модулем abc
"""
# class Shape:

#     def get_area(self, a, b):
#         self.a = a
#         self.b = b
#         return self.a * self.b * 2

# class Triangle(Shape):

#     def get_area(self, c, a, b):
#         self.c = c
#         self.a = a
#         self.b = b 
#         return self.a * self.b * self.c

# class Square(Shape):
#     def get_area(self, a):
#         self.a = a
#         return self.a ** 2

# class Circle(Shape):
#     def get_area(self, a, b):
#         self.a = a
#         self.b = b
#         return self.a * self.b ** 2

# e1 = Triangle()
# e2 = Square()
# e3 = Circle()
# print(e1.get_area(a=5, b=9, c=6))
# print(e2.get_area(a=4))
# print(e3.get_area(a=5, b=9))


# модификаторы доступа:
"""
1. public - password, get_info()
2. protected - _password, _get_info()
3. private - __password, __get_info()
"""

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password

#     def get_password(self, username):
#         if self.username == username:
#             return self.__password
#         else:
#             return "I kill you!"


#     def set_passeord(self, old_password, new_password):
#         if self.__password == old_password:
#             self.__password = new_password
#         else:
#             return "I kill you!"

#     def __get_info(self):
#         print(f'Username - {self.username}, password: {self.__password}')

# user1 = User(username='makers123', password='bootcamp567')
# print(user1.username)
# print(user1.password(username='makers123'))
# user1.set_passeord(old_password='bootcamp567',
#                     new_password='helloworld777')
# print(user1.get_password(username='qwerty'))
# print(user1.get_password(username='makers123'))








# class Divider:
#     def __init__(self):
#         self.__divide_num = 2

#     @property                       # <- getter
#     def divider(self):
#         return self.__divide_num

#     @divider.setter                 # <- setter
#     def divider(self, value):
#         if not value == 0:
#             self.__divide_num = value
#             return "I see you!"
#         else:
#             return "I kill you!"

#     def divide(self, value):
#         return value / self.__divide_num

# obj = Divider()
# print(obj.divider)
# obj.__divide_num = 0
# print(obj.divide(7))
# obj.divider = 999
# print(obj.divider)
# print(obj.get_divider())
# print(obj.__divide_num)
# print(obj._Divider__divide_num)





# class Person:

#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name

#     @property
#     def full_name(self):
#         return f"{self.name}, {self.last_name}"

# person = Person(name='Jonn', last_name="Snow")
# print(person.full_name)








# person = Person()
# person.name = 'Makers'
# person.age = 2
# print(person.name)
# print(person.age)







# class Car:

#     def _inject_fuel(self):
#         print('Fuel injected')

#     def _init_bang(self):
#         print('Bang!!!')

#     def _send_signal_to_ignition_system(self):
#         print('Ignition started')
#         self._inject_fuel()
#         self._init_bang()

#     def _send_signal_to_pc(self):
#         print('Start')
#         self._send_signal_to_ignition_system()

#     def start_engine(self):
#         self._send_signal_to_pc()


# car = Car()
# car.start_engine()


"""
1. underscore
2. protected - мы еще можем получить скрытые данные
3. protected данные наследуются в дочерных классах
"""

# class A:
#     def _say_hello(self):
#         print('Hello, makers')

# class B(A):
#     pass

# b = B()
# b._say_hello()




"""
1)Создайте класс и объявите в нём 3 метода: публичный, защищённый и приватный. Затем создайте экземпляр данного класса и вызовите по очереди каждый из методов.
"""

# class A:
#     def a1(self):
#         print('Hello')

#     def _a2(self):
#         print('Hello')

#     def __a3(self):
#         print('Hello')

# a = A()
# a.a1()
# a._a2()
# a.__a3()




"""
2)Определите класс A, в нём объявите метод method1, который печатает строку "Hello World". Затем создайте класс B, который будет наследоваться от класса A. Создайте экземпляр от класса B, и через него вызовите метод method1.
"""

# class A:
#     def method1(self):
#         print('Hello World')

# class B(A):
#     pass

# b = B()
# b.method1()




"""
3)Объявите класс Car, в котором будет приватный атрибут экземпляра speed. Затем определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, с помощью которого Вы будете получать значение скорости.
"""

# class Car:

#     speed = 0

#     def _set_speed(self):
#         print(f'speed: {self.speed}')

#     def show_speed(self):
#         self._set_speed()

# car =  Car()
# car.speed = 68
# car.show_speed()



"""
4)Перепишите класс Car из предыдущего задания.
Перепишите метод set_speed() с использованием декоратора @speed.setter, а метод show_speed() с использованием декоратора @property, для того чтобы можно было работать с данным классом следующим образом:

car = Car()
car.speed = 120
print(car.speed)
"""



# class Car:

#     __speed = 0

#     @property
#     def set_speed(self):
#       return self.__speed

#     @set_speed.setter
#     def show_speed(self, new_speed):
#         self.__speed = new_speed

# car = Car()
# car.speed = 120
# print(car.speed)

# class Car:

#     speed = 0

#     @property
#     def set_speed(self):
#         print(f'speed: {self.speed}')

#     @set_speed.setter
#     def show_speed(self):
#         self._set_speed()




# car = Car()
# car.speed = 120
# print(car.speed)


"""
2. Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня
заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 %
заряда при каждом обращении.
Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
разряжен).
Также предусмотрите возможность заряжания батареи.
"""



# from functools import reduce
# class ToDoList:
#     def __init__(self):
#         self.list_ = []
#     def put(self, to_do):
#         self.list_.append(to_do)
#     def get(self):
#         get = [[i.task, i.prio] for i in self.list_]
#         if get:
#             max_value = [reduce(lambda x, y: x if x > y else y, get)]
#             return max_value
#         else:
#             return None
# class Task(ToDoList):
#     def __init__(self, task, prio=3):
#         self.task = task
#         self.prio = prio
        
#     def __str__(self):
#         return f'{self.task}{self.prio}'


# test = ToDoList()
# a = Task('buy_milk', 5)
# b = Task('Buy_wather', 3)
# test.put(a)
# test.put(b)
# print(test.get())



"""
 Задание:

  Класс Tomato:
1. Создайте класс Tomato
2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
3. Создайте метод init(), внутри которого будут определены два динамических protected свойства: 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
"""

# class Tomato:
#     states = []

#     def __init__(self, _index, _state):
#         self._index = _index
#         self._state = _state

#     def grow(self):


"""
Класс TomatoBush
1. Создайте класс TomatoBush
2. Определите метод init(), который будет принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
"""

"""
Класс Gardener
1. Создайте класс Gardener
2. Создайте метод init(), внутри которого будут определены два динамических свойства: 1) name - передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является protected
3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
5. Создайте  метод knowledge_base(), который выведет в консоль справку по садоводству.
"""

"""
Реализуйте:
1. Вызовите справку по садоводству
2. Создайте объекты классов TomatoBush и Gardener
3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
4. Попробуйте собрать урожай
5. Если томаты еще не дозрели, продолжайте ухаживать за ними
6. Соберите урожай
"""





# class Perent:
#     def who_am_i(self):
#         print("I'm a parent")

# class Son(Perent):
#     def who_am_i(self):
#         super().who_am_i()
#         print("I'm a son")

# son = Son()
# son.who_am_i()



# class Grandpa:
#     def talant(self):
#         print("I'm good at dancing")

# class Grandma:
#     def talant(self):
#         print("I'm good at singing")

# class Father:
#     def talant(self):
#         print("I'm good at dancing")

# class Grandma:
#     def talant(self):
#         print("I'm good at singing")

# class Father:
#     last_name = 'White'

#     def talant(self):
#         print("I can build houses")

# class Mother(Grandpa, Grandma):
#     last_name = 'Brown'

# class Son(Father, Mother):
#     pass

# son = Son()
# print(son.last_name)
# son.talant()
# print(Son.mro())



# class A:
#     def __init__(self, param1):
#         print(f'Hey, I"s A class, I got {param1}, parametr')

#     def get_a(self):
#         print('Aaaa')

# class B:
#     def __init__(self, param):
#         print(f'Hey, I"s B class, I got {param} parametr')

#     def get_b(self):
#         print('Bbbb')

# class C(B, A):
#     def get_c(self):
#         print('Cccc')

# c = C('Makers')
# # print(C.mro())
# c.get_a()
# c.get_b()
# c.get_c()


# class A:
#     def method(self):
#         print('hello, i am A')

# class B(A):
#     def method(self):
#         super().method()
#         print('hello, i am B')

# class C(A):
#     def method(self):
#         # super().method()
#         print('hello, i am C')

# class D(B, C):
    # def method(self):
    #     print('hey, D')
#     pass

# d = D()
# d.method()
# print(D.mro())

# SOLID

# class Insects:
#     def __init__(self):
#         print("I am an Insect")

# class Bird:
#     def __init__(self):
#         print("I'm a bird")

# class FlyMixin:
#     def fly(self):
#         print("I can fly")

# class Butterfly(Insects, FlyMixin):
#     pass

# class Hawk(Bird, FlyMixin):
#     pass

# class Eagle(Bird, FlyMixin):
#     pass

# class Pinguin(Bird):
#     pass

# hawk = Hawk()
# hawk.fly()

# eagle = Eagle()
# eagle.fly()

# pin = Pinguin()

# butterfly = Butterfly()
# butterfly.fly()




# class Gadgets:
#     pass

# class Vehicle:
#     pass

# class Shower:
#     pass

# class RadioMixin:
#     def play_songs(self, station):
#         print(f'Playing some song on station {station}')

# class Car(Vehicle, RadioMixin):
#     pass

# class Phone(Gadgets, RadioMixin):
#     pass

# class ShowerCabin(Shower, RadioMixin):
#     pass

# car = Car()
# car.play_songs('Europa +')

# phone = Phone()
# phone.play_songs('Makers Bootcamp')

# showercabin = ShowerCabin()
# showercabin.play_songs('RetroFM')




'''
1. Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water. Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
'''

# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('floating on water')

# class Amphibian(Auto, Boat):
#     pass

# a = Amphibian()
# a.ride()
# a.swim()





'''
2. Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина
'''


# class RadioMixin:
#     def play_music(self, music):
#         self.music = music

# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass

# class Amphibian(RadioMixin):
#     pass



'''
3. Будильник. Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника. Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к нему метод для установки будильника, при вызове которого должен включатся будильник.
'''

# class Clock:
#     def 



'''
4. Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы.
'''
# class Coder:
#     experience
#     count_code__time = 0
#     def get_info(self):
#         pass

#     def coding(self):
#         pass







# class All:
#     def say_hi(self):
#         print('hi people')


# class A(All):
#     def method_B(self):
#         print('This is nethod A')


# class B(All):
#     def method_B(self):
#         print('This is method A')


# class C(A, B):
#     def method_C(self):
#         print('This is method C')


# c = C()
# c.say_hi()






# class WheelsMixin:
#     def __init__(self, wheels):
#         self.wheels = wheels


# class Radio:
#     def play_music(self, music):
#         print(f'You listen this {music}')


# class Engine:
#     def __init__(self, engine, volume):
#         self.engine = engine
#         self.volume = volume


# class Oil:
#     def __init__(self, oil):
#         self.oil = oil
#         print(f'вы ездите на {self.oil} топливе')


# class Car(Oil, Engine, Radio, WheelsMixin):
#     def __init__(self, oil, engine, volume, type, wheels):
#         # super().__init__(oil, engine, volume, wheels)
#         self.type = type


# class Boat(Oil, Engine, Radio):
#     def __init__(self, oil, engine, volume, type):
#         # super().__init__(oil, engine, volume)
#         self.type = type


# class Bike(Oil, Engine, Radio, WheelsMixin):
#     def __init__(self, oil, engine, volume, type, wheels):
#         # super().__init__(oil, engine, volume, wheels)
#         self.type = type



# buggati = Car('бензин', "V8", '220hp', 'Машина', 4)


# class X:
#     pass

# obj = X()
# print(dir(obj))
# print(dir(6))
# print(dir('makers'))
# def func():
#     pass

# print(dir(func))

# 1.__init__() 

# class User:
#     def __init__(self, **kwargs):
#         print('Object is initializing...')
#         self.name = kwargs['name']
#         self.familia = kwargs['last_name']
#         print('Object is initialized')

# user = User(name='Linus', last_name='Torvalds')
# print(user.name)
# print(user.familia)



# 2.__new__()

# class Human(object):
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         instance = object.__new__(cls)
#         instance.heart = '4xкамерное'
#         print('Object created')
#         return instance

#     def __init__(self, name, last_name):
#         print('Object is initializing...')
#         self.name = name
#         self.familia = last_name

# human1 = Human(name='Linus', last_name='Torvalds')
# print(human1.heart)


# Singleton - от одного класса можно создать только один объект
# class Sun:
#     instance = None

#     def __new__(cls):
#         if cls.instance is None:
#             cls.instance = object.__new__(cls)
#         return cls.instance

# sun1 = Sun()
# sun2 = Sun()
# sun3 = Sun()
# print(sun1 is sun2)
# print(id(sun1))
# print(id(sun2))
# print(id(sun3))



# 3.__str__

# class Human:
#     def __init__(self, name, last_name):
#         self.last_name = last_name
#         self.name = name

#     def get_fullname(self):
#         return f'{self.name}, {self.last_name}'

#     def __str__(self):
#         return self.get_fullname()

# human1 = Human('Linus', 'Torvalds')
# print(human1)


# 4__repr__()


# class Human:
#     def __init__(self, name, last_name):
#         self.last_name = last_name
#         self.name = name

#     def __str__(self):
#         return f'{self.name}, {self.last_name} - сработал метод str'

#     def __repr__(self):
#         return f'{self.name}, {self.last_name} - сработал метод repr'

# human = Human('Jonn', 'Snow')
# print(human)


"""
__add__(self, other) -> +
__sub__(self, other) -> -
__mul__(self, other) -> *
__truediv__(self, other) -> /
__mod__(self, other) -> %
"""

# class MyInt(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         # self.value + oth
#         return self.value + other/3

#     def __sub__(self, other):
#         # self.value - other
#         print('This is substraction')
#         return self.value - other + 100

#     def __mul__(self, other):
#         # self.value * other
#         print('This is my multiplication')
#         return self.value + other - 1

#     def __truediv__(self, other):
#         # self.value / other
#         print('This is my division')
#         return self.value / other + 1

#     def __mod__(self, other):
#         # self.value % other
#         return f'Остаток от деления: {self.value % other}'

#     """ Отраженные фрифматические операторы"""
#     # self.value + other, self.value - other
#     # other + self.value, other - self.value

#     def __radd__(self, other):
#         # other + self.value
#         print('This is my r-addition')
#         return other + self.value + 20

#     def __rsub__(self, other):
#         print('This is my r-subraction')
#         return other - self.value

#     def __rmul__(self, other):
#         print('This is my r-multiplication')
#         return other * self.value + 5

#     def __rtruediv__(self, other):
#         print('This is my r-division')
#         return other / self.value - 7

#     """Составное присваивание"""

#     # a = 7
#     # a += 7   == a = a + 7

#     def __iadd__(self, other):
#         print('This is my i-addition')
#         return self.value + other

#     def __isub__(self, other):
#         print('This is my i-substraction')
#         return self.value - other - 1

#     def __imul__(self, other):
#         print('This is my i-multiplication')
#         return self.value ** other 

#     def __itruediv__(self, other):
#         print('This is my i-division')
#         return self.value % other

# a = MyInt(10)
# a /= 6
# print(a)
# print(10000 / a)
# print(5 * a)
# print(20 - a)
# print(5 + a)
# print(a + 5)
# print(a - 5)
# print(a * 3)
# print(a / 5)
# print(a % 3)


"""
__eq__ -> ==
__ne__ -> !=
__gt__ -> >
__lt__ -> <
__le__ -> <=
__ge__ -> >=
"""

# class Human:
#     def __init__(self, name, familia, age):
#         self.name = name
#         self.familia = familia
#         self.age = age

#     def __eq__(self, other):
#         # print('Ages are ....')
#         return self.age == other.age

#     def __ne__(self, other):
#         return self.age != other.age

#     def __gt__(self, other):
#         return len(self.name) > len(other.name)

#     def __lt__(self, other):
#         return len(self.name) < len(other.name)

#     def __ge__(self, other):
#         return len(self.familia) >= len(other.familia)

#     def __le__(self, other):
#         return len(self.familia) <= len(other.familia)

# human1 = Human(name='Tom', familia='Levi', age='14')
# human2 = Human(name='Jonn', familia='Snow', age=34)
# print(human1 < human2)
# print(human1 == human2)
# print(human1 != human2)
# print(human1 >= human2)
# print(human1 <= human2)


# __getatter__, __setatter__, __delattr__
# __getattribute__

# class MyClass:
#     def __init__(self):
#         self.name = 'Makers'
#         self.last_name = 'Bootcamp'
#         # print(self.__dict__)
    
#     def __getattr__(self, item):
#         print(self.__dict__)
#         return self.__dict__.get(item, 'Hello world')

#     def __getattribute__(self, item):
#         print('This is custom getattribute magic method')
#         return super().__getattribute__(item)

#     def __setattr__(self, item, value):        # self.item = value
#         print('I want to set attribute {item} with value {value}')
#         self.__dict__[item] = value

#     def __delattr__(self, item):        # del self.item
#         print(f'I want to delete attribute named {item}')
#         self.__dict__.pop(item, 0)


# obj = MyClass()
# # print(obj.name)
# obj.age = 2
# del obj.age
# print(obj.age)


"""
__len__(self) -> len()
__getitem__(self, key) -> self.key
__setitem__(self, key, value) -> self[key] = value
__delitem__(self, key) -> del self[key]
__contains__(self, item) -> item in self or item not in self --> True or False
"""


# class MyClass(dict):
#     def __getitem__(self, key):
#         print(f'I am giving you a value of {key}')
#         result = super().__getitem__(key) + 1
#         return result

#     def __setattr__(self, key, value):
#         value += 1
#         super().__setattr__(key, value)

# dict_ = MyClass(a=6, b=7, c=8)
# print(dict_)
# print(dict_['c'])
# dict_['d'] = 9
# print(dict_)


# class MyList(list):
#     def __init__(self, iterable):
#         self.list = iterable

#     def __contains__(self, item):
#         if item in self.list:
#             return False
#         else:
#             return True

# a = MyList([1, 2, 3, 4, 5])
# print(6 in a)




'''
1. Создайте класс Account и переопределите в нем методы __init__, __repr__, __str__ и __del__.
Объекты класса должны содержать атрибуты имени, баланса и города, где открыт счет.
Метод __init__ должен возвращать сообщение о создании счета, __repr__ только имя держателя счета
и баланс, а __str__ сообщение с приветствием и также информацией о держателе счета, 
балансе и филиале банка в котором зарегистрирован клиент, __del__ в свою очередь сообщение об удаление 
и слово "Пока!"
'''

# class Accont:

#     def __init__(self, name, city, balance):
#         self.name = name
#         self.city = city
#         self.balance = balance
#         print('Счет баланса создан')

#     def __repr__(self):
#         return f'Держатель: {self.name}'

#     def __str__(self):
#         return f'Welcome {self.name}!!\nYour name: {self.name} \nYour town: {self.city} \nYour balance:{self.balance}'

#     def __delattr__(self, item):
#         print("Deleted! \nПока!")
#         self.__dict__.pop(item, 0)

# Hrome = Accont(name='Martin', city='Tokyo', balance=4000)
# print(Hrome)
# del Hrome.balance


#     def __delattr__(self, item):        # del self.item
#         print(f'I want to delete attribute named {item}')
#         self.__dict__.pop(item, 0)







'''
2. Определите класс MyNumber который наследуется от класса int. 
У экземпляра класса должен быть обязательный атрибут value. 
Переопределите методы сложения, вычитания, умножения и деления для класса таким  образом чтобы при при использовании операторов + - * / - результат возвращался с сообщением об использованном методе, 
например:print(num + 5)  -------> "Это сложение и Ваш результат равен 10Это сложение и Ваш результат равен 10"
'''

# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return f'Это сложение и Ваш результат равен {self.value + other}'
    
#     def __sub__(self, other):
#         return f'Это сложение и Ваш результат равен {self.value - other}'

#     def __mul__(self, other):
#         return f'Это сложение и Ваш результат равен {self.value * other}'

#     def __truediv__(self, other):
#         return f'Это сложение и Ваш результат равен {self.value / other}'

# f = MyNumber(8)
# print(f + 6)
# print(f - 2)
# print(f * 4)
# print(f / 3)

# class MyInt(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         # self.value + oth
#         return self.value + other/3

#     def __sub__(self, other):
#         # self.value - other
#         print('This is substraction')
#         return self.value - other + 100

#     def __mul__(self, other):
#         # self.value * other
#         print('This is my multiplication')
#         return self.value + other - 1

#     def __truediv__(self, other):
#         # self.value / other
#         print('This is my division')
#         return self.value / other + 1

#     def __mod__(self, other):
#         # self.value % other
#         return f'Остаток от деления: {self.value % other}'







'''
3. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1
'''

# class MyList(list):

#     def __init__(self, list_):
#         self.list_ = list_

# x = MyList([1, 2, 3, 4, 5])






# class MyList(list):
#     def __init__(self, iterable):
#         self.list = iterable

#     def __contains__(self, item):
#         if item in self.list:
#             return False
#         else:
#             return True

# a = MyList([1, 2, 3, 4, 5])
# print(6 in a)








# a = (0,1,2,3,4,5,6)
# print(a[1])






'''
4. Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
'''




# class Student:
#     def __init__(self, name, familia, class_, **grade):
#         self.name = name
#         self.familia = familia
#         self.class_ = class_
#         self.grade = grade

#     def __ge__(self, other):
#         f = sum(self.grade.values())/ 3
#         j = sum(other.grade.values()) / 3
#         return f >= j

# f = Student(name='Lusi', familia='Jonnson', class_=11, math= 94, history= 97, literature= 98)
# c = Student(name='Max', familia='Martin', class_=11, math=85, history=90, literature=92)
# print(f >= c)





# print(sum(a.grade.values())/ 3)
        
    

# human1 = Human(name='Tom', familia='Levi', age='14')
# human2 = Human(name='Jonn', familia='Snow', age=34)
# print(human1 < human2)
# print(human1 == human2)
# print(human1 != human2)
# print(human1 >= human2)
# print(human1 <= human2)


#     def __ge__(self, other):
#         return len(self.familia) >= len(other.familia)





'''
5. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
Также в методе __new__ напишите условие для удаления
пробелов и пустых строк в созданных словах.
'''



# class Word:

#     def __new__(cls, *args, **kwargs):
#         c = 'h e   l   l    o'
#         d = c.replace(' ', '')
#         print(d)

#     def __init__(self, string):
#         self.string = string

#     def __gt__(self, other):
#         return len(self.string) > len(other.string)

#     def __lt__(self, other):
#         return len(self.string) < len(other.string)

#     def __ge__(self, other):
#         return len(self.string) >= len(other.string)

#     def __le__(self, other):
#         return len(self.string) <= len(other.string)

# a = Word(string='Hello')
# b = Word(string='Hi')
# print(a > b)
# c = 'h e   l   l    o'
# d = c.replace(' ', '')
# print(d)


# 2.__new__()

# class Human(object):
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         instance = object.__new__(cls)
#         instance.heart = '4xкамерное'
#         print('Object created')
#         return instance


#     def __gt__(self, other):
#         return len(self.name) > len(other.name)

#     def __lt__(self, other):
#         return len(self.name) < len(other.name)

#     def __ge__(self, other):
#         return len(self.familia) >= len(other.familia)

#     def __le__(self, other):
#         return len(self.familia) <= len(other.familia)








"""
instance method -> self
class method - @classmathod -> cls
static method - @staticmethod
"""

# class Makers:
#     language_choices = 'Python', 'JavaScript'

#     def __init__(self, name):
#         self.name = name

#     def instance_method(self):
#         return f'Hello, {self.name}'

#     @classmethod
#     def class_method(cls):
#         return f'Welcome to Makers! What type of language do you choose?: {cls.language_choices}'

#     @staticmethod
#     def static_method(choice):
#         return f'Great! You chose {choice} course'

# student1 = Makers(name='Jonn')
# print(student1.instance_method())
# print(student1.class_method())
# print(student1.static_method(choice='Python'))
# print()
# student2 = Makers(name='Alice')
# print(student2.instance_method())
# print(student2.class_method())
# print(student2.static_method(choice='JavaScript'))





# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def get_info(self):
#         return f'{self.name}, {self.email}'

#     @classmethod
#     def add_data(cls, user_info:list):
#         name, email = user_info
#         return cls(name, email)

# list_of_users = [
#     ['Danny', 'emai@yahoo.cim'],
#     ['Bonny', 'bon2gmail.com'],
#     ['Karen', 'karen@gmail.com']
# ]

# for info in list_of_users:
#     user = User.add_data(info)
#     print(user.get_info())

# user1 = User(name='Danny', email='emai@yahoo.cim')
# print(user1.get_info())



# class Lottery:
#     def __init__(self, name):
#         self.name = name

#     @staticmethod
#     def _generate_number():
#         import random
#         number = random.sample(list('123456789'), k=5)
#         number = ''.join(number)
#         return number

#     def get_number(self):
#         number = self._generate_number()
#         self.number = number
#         return f'Dear {self.name}! Your lucky number is {self.number}'



# participant1 = Lottery(name='Lucas')
# print(participant1.get_number())




# class Pizza:

#     def __init__(self, ingredients:list):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f'Pizza with {self.ingredients}'

# pizza1 = Pizza(['tomatoes', 'mozarella', 'basil'])
# pizza2 = Pizza(['meat', 'chilli pepper', 'cheese'])
# print(pizza1)
# print(pizza2)














# class Pizza:

#     def __init__(self, ingredients:list):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f'Pizza with {self.ingredients}'

#     @staticmethod
#     def circle_area(radius):
#         import math
#         area = round(math.pi * radius ** 2, 2)
#         return f'Pizza"s area is {area} sn2'

#     def area(self, radius):
#         self.radius = radius
#         return self.circle_area(self.radius)

#     @classmethod
#     def margarita(cls):
#         return cls(['mozarella', 'tomatoes', 'basil'])

#     @classmethod
#     def pepperoni(cls):
#         return cls(['pepperoni', 'cheese'])


# print('-----------------------------------')
# print('-----------------------------------')
# print('-----------------------------------')
# pizza1 = Pizza.margarita()
# print(pizza1)
# print(pizza1.area(4))
# print('-----------------------------------')
# print('-----------------------------------')
# print('-----------------------------------')
# pizza2 = Pizza.pepperoni()
# print(pizza2)
# print(pizza2.area(8))
# print('-----------------------------------')
# print('-----------------------------------')
# print('-----------------------------------')






# print(Pizza.pepperoni())






'''
1. Dollar.
Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
долларизованный формат:
dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000
Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
- init - инициализирует значение атрибута amount
- update - задаёт объекту новое значение amount
- repr - возвращает значение float
- str - метод, который реализует логику функции dollarize()

//Вывод должен выглядеть следующим образом:
cash = MoneyFmt(12345678.021)
print(cash) -- выводит "$12,345,678.02"
cash.update(100000.4567)
print(cash) -- выводит "$100,000.46"
cash.update(-0.3)
print(cash) -- выводит "-$0.30"
repr(cash) -- выводит -0.3 
'''

# class MoneyFmt:
#     def __init__(self, amount):
#         self.amount = amount

#     def update(self):
#         pass

#     def __repr__(self):
#         pass

#     def __str__(self):
#         a = round(self.amount, 2)
#         return a

# a = MoneyFmt(amount=12345678.021)
# print(a)





#     @staticmethod
#     def circle_area(radius):
#         import math
#         area = round(math.pi * radius ** 2, 2)
#         return f'Pizza"s area is {area} sn2'
















'''
2. Велосипед.
Создайте класс Bike в котором будут инициализированы следующие атрибуты: self.cost
(стоимость)
'''

# class Bike:
#     def __init__(self, cost, make, model, year, condition, _sale_price=None, sold=False):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self._sale_price = _sale_price
#         self.sold = sold

    

'''
self.make (производитель)
self.model (модель)
self.year (год выпуска)
self.condition (состояние)
self._sale_price = None (цена для продажи, по умолчанию None)
self.sold = False (продан или нет, по умолчания False)

Также укажите мин. прибыль, которая должна прийти с продажи велосипеда. Создайте метод
для указания цены для продажи, который принимает цену и если она меньше стоимости, то
ставит дефолтную цену для продажи (стоимость + мин. прибыль).

Для ремонта велосипеда будет использоваться метод service, которая принимает стоимость
ремонта и новое состояние велосипеда, соответственно продажная цена велосипеда
возрастает на столько, сколько обошелся ремонт и возвращает нынешнюю цену для продажи.
При продаже велосипеда будет использоваться метод sell, который меняет значение self.sold на True
и возвращает прибыль с продажи.

Допишите метод get_default_bike, который будет создавать дефолтный велосипед. Создайте
объект bike = Bike.get_default_bike() и используете его методы и получите значения всех его
атрибутов.
'''











# 

# Instance методы - Имеют доступ к экземпляру класса, также и к классу (имеют доступ ко всем методам и атрибутам, которые определены в классе)

# class A:
#     attr1 = 10

#     def __init__(self, value):
#         self.attr2 = value

#     def method1(self):
#         print(self.attr1)
#         print(self.attr2)

# Class методы - имеют доступ только к атрибутам и методам класса

# class MyClass:
#     attr1 = 10

#     def __init__(self, value):
#         self.attr2 = value

#     def method1(self):
#         print(self.attr1)
#         print(self.attr2)

#     @classmethod
#     def method2(cls):
#         print(cls.attr1)
        # print(cls.attr2) #Error

# obj1 = MyClass(20)
# obj1.method2()

# MyClass.method1()
# MyClass.attr2


# Static методы методы - отдельная функция, которая не имеет доступа ни к классу, ни к его объектам

# Используются в случае, если нужно добавить определенную функцию

# class A:
    # # def method1(self):
    # #     print('Hello world')

    # @staticmethod
    # def method1():
    #     print('Hello world')

# class User:

#     # def __new__(cls, *args, **kwargs):
#     #     email = args[0]
#     #     user = object.__new__(*args, **kwargs)
#     #     cls.send_mail(email)
#     #     return user

#     def __init__(self, email, password):
#         self.email = email
#         self.password = password
#         self.send_mail(self.email)

#     @staticmethod
#     def send_mail(email):
        # ...



# class A:
#     attr1 = 10

#     def method1(self, new_value):
#         self.attr1 = new_value

#     @classmethod
#     def method2(cls, new_value):
#         cls.attr1 = new_value

#     def method3(self, new_value):
#         self.__class__.attr1 = new_value

# a1 = A()
# a2 = A()
# a3 = A()

# # a1.method1(20)
# # a2.method2(30)
# a3.method3(25)

# print(a1.attr1)
# print(a2.attr1)
# print(a3.attr1)

# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y                                                                                             

# class Arithmetics:
#     @staticmethod
#     def add(x, y):
#         return x + y

#     @staticmethod
#     def sub(x, y):
#         return x - y

# Arithmetics.add(20, 15)



# dict.fromkeys(['a', 'b', 'c'], 0)

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = self.encrypt_password(password)

#     @staticmethod
#     def encrypt_password(rav_password):
#         from hashlib import md5
#         res = md5(rav_password.encode()).hexdigest()
#         return res

#     def login(self, username, password):
#         enc_pass = self.encrypt_password(password)
#         self.password == enc_pass

# user1 = User('superuser', 'qwerty')
# print(user1.password)

# username1 = 'user1'
# username2 = 'user2'

# pass1 = 'qwerty'
# pass2 = 'qwerty'

# from hashlib import sha512, pbkdf2_hmac

# # hash2 = sha512((pass2 + username2).encode()).hexdigest()

# hash1 = pbkdf2_hmac('sha256', pass1.encode(), username1.encode(), 10000)
# hash2 = pbkdf2_hmac('sha256', pass2.encode(), username2.encode(), 10000)

# print(hash1)
# print(hash2)

# # import hmac
# # hmac.compare_digest(hash1, pbkdf2_hmac('sha256', pass1.encode(), username1.encode(), 10000))




"""
dump(), dumps()
"""

# import json
# info = {
#     "name": 'Alice', 
#     'age': 79, 
#     'book': 'Chamber of Secrets'
# }

# print(type(info))

# with open('info.json', 'w') as my_file:
#     json.dump(info, my_file)

# json_obj = json.dumps(info)
# print(json_obj)
# print(type(json_obj))



# import json

"""
load(), loads()
"""

# with open('info.json') as my_file:
#     python_object = json.load(my_file)
#     print(type(python_object))

# python_object['name'] = 'Jonn'
# print(python_object)

# with open('info.json', 'w') as my_file:
#     json.dump(python_object, my_file)

# import json

# json_str = '{"name": "Alice", "age": 79, "book": "Chember of Secrets"}'
# python_object = json.loads(json_str)
# print(json_str)
# print(python_object)
# python_object.update({'color': 'yellow'})
# print(python_object)



'''
1. Напишите программу Python для создания нового файла JSON из существующего файла JSON. 
'''








'''
2. Напишите программу Python для преобразования данных в кодировке JSON в объекты Python.
'''

# import json


# info = {
#     "name": 'Alex', 
#     'age': 26, 
# }

# with open('info.json', 'w') as my_file:
#     json.dump(info, my_file)


# with open('info.json') as my_file:
#     python_object = json.load(my_file)
#     print(python_object)




'''
3. Напишите программу Python для преобразования объектов Python в строки JSON. Распечатайте все значения.
'''

# import json

# info = {
#     "name": 'Alex', 
#     'age': 26, 
# }


# json_obj = json.dumps(info)
# print(json_obj)



'''
4. Напишите программу Python для преобразования данных JSON в объект Python.
'''

# import json

# json_str = '{"name": "Alex", "age": 26}'
# python_object = json.loads(json_str)
# print(json_str)
# print(python_object)





'''
5. Напишите программу Python для доступа только к уникальному значению ключа объекта Python.
'''

# info = {
#     "name": 'Alex', 
#     'age': 26, 
# }

# print(info['name'])










'''
4. Разработчики
Напишите абстрактный класс Coder с атрибутом count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать обязательный параметр languages_backend, а Frontend — languages_frontend соответственно.

Переопределите в обоих классах методы get_info(Должен возвращать язык программирования и количество часов кодинга) и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time).

Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов.

Создайте экземпляры от классов Backend, Frontend, FullStack (obj_back, obj_front, obj_full_stack) и вызовите все их методы.
'''

# from abc import ABC, abstractmethod

# class Coder(ABC):
#     count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#         pass

#     @abstractmethod
#     def coding(self):
#         pass


# class Backend(Coder):
#     def __init__(self,languages_backend):
#         self.languages_backend = languages_backend

#     def coding(self, time):
#         self.count_code_time  += time
#         return self.count_code_time

#     def get_info(self):
#         return self.languages_backend, self.count_code_time


# class Frontend(Coder):
#     def __init__(self, languages_frontend):
#         self.languages_frontend = languages_frontend

#     def coding(self, time):
#         self.count_code_time  += time
#         return self.count_code_time

#     def get_info(self):
#         return self.languages_frontend, self.count_code_time



# class FullStack(Frontend, Backend):
#     pass

# obj_back = Backend('Python')
# obj_front = Frontend('JS')
# obj_full_stack = FullStack('C++')
# obj_back.coding(5)
# obj_front.coding(7)
# obj_full_stack.coding(3)
# print(obj_back.get_info())
# print(obj_front.get_info())
# print(obj_full_stack.get_info())



# --------------------------------------------------------------------------------------------------------------------------------














# Given an integer n, return a string array answer (1-indexed) where:
#     • answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#     • answer[i] == "Fizz" if i is divisible by 3.
#     • answer[i] == "Buzz" if i is divisible by 5.
#     • answer[i] == i if non of the above conditions are true.
#  
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuz


# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:


# class Solution:
#     def fizzBuzz(self, n:int):
#         list_ = []
#         for i in range(1, n+1):
#             if i % 3 == 0 and i % 5 == 0:
#                 list_.append('FizzBuzz')
#             elif i % 3 == 0:
#                 list_.append('Fizz')
#             elif i % 5 == 0:
#                 list_.append('Buzz')
#             list_.append(i)
#         return list_
            

# a = Solution()
# print(a.fizzBuzz(25))











# JSON (JavaScript Object Notation) - формат обмена данными

# notebook = {
#     'brand': 'Acer',
#     'Model': 'Aspire',
#     'ram': 8,
#     'hdd': 500,
#     'has_type_c': True,
#     'cd_drive': None
# }

# Используются двойные ковычки
# Ключом может быть только строка

# class Notebook:
#     def __init__(self, brand, model, ram, hdd, accessories):
#         self.brand = brand
#         self.model = model
#         self.ram = ram
#         self.hdd = hdd
#         self.accessories = accessories

# note1 = Notebook('Apple', 'Macbook Pro', 16, 256, ['headphones', 'case', 'bag'])
# note2 = Notebook('Asus', 'ROG', 24, 100, [])
# notebooks = [note1, note2]
# import json

# class NotebookEncoder(json.JSONEncoder):
#     def default(self, o):
#         return o.__dict__

# res = json.dumps(notebooks, indent=2, cls=NotebookEncoder)
# print(res)






# notes = '[{"brand": "Acer", "model": "Aspire", "ram": 8, "hdd": 500, "has_type_c": true, "cd_drive": null}, {"brand": "Asus", "model": "Zenbook", "ram": 8, "hdd": 400, "has_type_c": false, "cd_drive": null'

# class Notebook:
#     def __init__(self, brand, model, ram, hdd, has_type_c, cd_drive):
#         self.brand = brand
#         self.model = model
#         self.ram = ram
#         self.hdd = hdd
#         self.has_type_c = has_type_c
#         self.cd_drive = cd_drive

# import json

# from collections import namedtuple

# def decoder(notebook_dict):
#     return namedtuple('Notebook', notebook_dict.keys())(*notebook_dict.values())

# notebooks = json.loads(notes, object_hook=decoder)
# print(notebooks)
# print(type(notebooks))


# sudo apt_get install git
# установка

git --version
# проверка, что git установлен

git config --global user.email "адрес почты"
git config --global user.email "юзернейм от github"

git config --list #проверка настроек

ssh-keygen #создание ssh ключа

cat ~/.ssh/id_rsa.pub #получение созданного публичного ключа

git init - превращает текущую директорию в git репозиторий

git remote #работа с удаленными репозиториями

git remote add название ссылка_на_репо #привюзка удаленного репозиторию

git remote -v #просмотр списка удаленных репозиториев

git remote remove название #отвязывание удаленного репозитория

git remote rename старое_название новое_название #переименование удаленного репозитория

git remote set-url название новая_ссылка #изменение ссылки на репозиторий

git add #добавдяет файды в версию(commit)

git add . #добавление всех файлов

git add file1 file2 #добавление конкретных файлов

git reset #убирает файлы из версии

# git reset - убирает все файды
git reset file1 file2 #убирает конкретные файлы

git commit #создание версии (коммита)

git commit -m"Описание"

git push #отправка коммитов на удаленный репозиторий

git push название_репо название_ветки









































































































































































































































































































































































































