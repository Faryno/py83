#print(len([elem for elem in some_string.split() if  elem[-1] == 'k']))

#lst2 = []
#if len[lst] == 1:
#    print(lst)
#for i in range(len(lst)):
#    if i == 0:
 #       lst2.append(lst[-1 ] + lst[1])
  #  elif i == len(lst) -1:
   #     lst2.append(lst[-2] + lst[0])
    #else:
   #     lst2.append(lst[ i - 1] + lst[i + 1])
#tpl = 6,7,8,9
#temp = 0
#for elem in tpl:
 #   for i in range(2, elem // 2 +1):
  #      if elem % i == 0:
    #        temp += i
         #   if temp == elem:
               # print(temp)
               # если чт-то пустое -- это Foulse
#phone = {}
#while True:
 #   friend = input()
  #  if friend == '.':
 #       break
 #   friend = friend.split()
 #   print(friend)
#    if len(friend) >= 2:
  #      phone[" ".join(friend[:-1])] = friend[-1]
   # if len(friend) == 1:
    #    if friend[0] in phone:
    #        print(phone[friend[0]])
  #  else:
  #     print(f"{friend[0]} not found")
#def pancakes():
 #   print("взять ингредиенты")
  #  print('смешать их')
   # print('мешаем')
   # for i in range(5):
   #     fried()
    #    print(f"gjhwbz {i+1} готова")
#def fried():
 #   print('жарим')
  #  print('ждем и переворачиваем')
 #   print('выложить на тарелку')
   # print('добавить варенья')
#pancakes()
#fun = lambda x,y: x+y

##    return x+y
#print(fun(2,1))
#print(fun(5,2))
#def chet(number):
 #   return not number %2
#kr = lambda x: "Yes" if x % 3 == 0 else "No"
#print(kr(8))
#lst = ["Jonz",'mar','Sherak']
#lst.sort(key = len)
#print(lst)
#lst = [64,23,25432,54]
#balance ={'john':6372,'Mark': 732,"Anna":729}
#for name in  map(lambda name, money: balance[name] +200 if balance[name] < 200 else balance[name], balance):
#    print(name,balance[name])
#lst =[1,2,3,4,5,]
#lst2 = list(filter(lambda x: not x % 2, lst))
#print(lst2)
##words2 = list(filter(lambda elem: len([sym for sym in elem if sym in "AEYUOIaeyuio"])== 2, words))
#print(words2)
#Global
#x = 2
#def fun():
#    global  x
#    x += 3
#    print(x)
#fun()
#def fun():
#    def wraper():
 #       print('hello')
 #   wraper()
#fun()
#def fun(numb):
 #   def wraper():
  #      nonlocal numb
 #       numb +=1
   #     print(numb)
  #  wraper()
#fun(42)
#def person(name):
  #  def wraper():
   #     print(name.capitalize())
    #return wraper
#p = person('oleg')
#p()
#Эффект Кложа
#def counter(x):
#    def wraper(a):
 #       nonlocal x
   #     x += a
 #       print(x)
 #   return wraper
#c = counter(0)
#c(1)
#c(1)
#def counter2(x):
  #  return x + 1
#print(counter2(1))
#print(counter2(1))
#print(counter2(1))
#дикоратор -- ункция принимающая функцию модернизирует ее и возвращает
#def grirings(name: str):
#    return "hello " + name
#def decorator(fun):# fun = gritings
#    def wraper(name):
#       if name.capitalize() == name:
#            return fun(name)
 #       else:
 #           return 'hello ' + name.capitalize()
  #  return wraper
#decorsau = decorator(grirings)
#grirings = decorator(grirings)
#print(grirings('peter'))
#print(decorsau('peter'))
#@decorator
#def grirings(name: str):
#    return "hello " + name
#print(grirings('peter'))
#users = {"Max":657,'Jac':748,"Anna":900}
#def balance(**kwargs):
    #for name,price in kwargs.items():
   #     if price < 500:
  #          kwargs[name] += 100
 #   return kwargs
#users = balance(**users)
#print(users)
#lst = [1,3,4,55,4,1,6,8,9]
# varss = set(lst)
# count = 0
# for i in range(len(lst)):
#     if lst[i] in varss:
#         count +=1
#     if count >=2:
# school = {"DNS": "-компьютерная система для получения, хранения и обработки информации о доменных именах",
# "Интрасеть": "-это замкнутая внутренняя сеть какой-либо организации, работающая по Интернет-протоколу TCP/IP",
# "Фича": "-недокументированная дополнительная возможность, фишка"}
# print(school)
# while 1:
#     a = input()
#     if a == '.':
#         break
#     if a in school:
#         print(school[a])
#     else:
#         print('Не найдено')
#     a = ""

# phone ={}
# while 1:
#     a = input()
#     if a == ".":
#         break
#     a = a.split()
#     if len(a) == 2:
#         phone[a[0]] = a[1]
#     if len(a) == 1:
#         if a[0] in phone:
#             print(phone[a[0]])
#         else:
#             print("Абанент не найден")




# factareal()
# n = int(input())
# def fibanachy():
#     fib1 = 1
#     fib2 = 1
#     fibsum = 0
#     for i in range(2, n):
#         fibsum = fib2 +fib1
#         fib1 = fib2
#         fib2 = fibsum
#     print(fibsum)
# fibanachy()
# def factorial(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f
# print(factorial(n))
# def closet_mod_5(x):
#     if x % 5 == 0:
#         return x
#     else:
#         while x % 5 != 0:
#             x += 1
#             if x % 5 == 0:
#                 return x
# print(closet_mod_5(21))

# def check_variable(v):
#     if v[0].isdigit():
#         return 'error'
#     else:
#         for elem in v:
#             if elem in '!@#$%^&*(){}[]:;"<>?/., ':
#                 return 'error'
#     return 'true'
# print(check_variable('1233helloworld'))

# def bank(a,year):
#     i = 1
#     while i < year +1:
#         a += a * 0.01
#         i +=1
#     return a
# print(bank(1000, 5))

# from datetime import datetime
#  import time
#
#
# def elapsed(func):
#     def wrapper(a, b, delay=0):
#         start = datetime.now()
#         func(a, b, delay)
#         end = datetime.now()
#         elapsed = (end - start).total_seconds()
#         print(f'>> функция {func.__name__} время выполнения (ms): {elapsed}')
#
#     return wrapper
#
#
# @elapsed
# def add_with_delay(a,b, delay = 0):
#     time.sleep(delay)
#     for i in range(a, b):
#         print(i)
#
#
# print('старт программы')
# add_with_delay(1,101,1)
# print('конец программы')

# from datetime import datetime
# import time
#
#
# def elapsed(func):
#     def wrapper(delay=0):
#         start = datetime.now()
#         func(delay)
#         end = datetime.now()
#         elapsed = (end - start).total_seconds()
#         print(f'>> функция {func.__name__} время выполнения (ms): {elapsed}')
#
#     return wrapper
#
#
# @elapsed
# def registr(delay=0):
#     print('Введите пароль')
#     password = int(input())
#     print('Введите логин')
#     login = input()
#     time.sleep(delay)
#
#
# print('старт программы')
# registr()

# print('конец программы')

# file = open("7.txt", 'a')
# file.write('btbatbt' + '!' + '\n')
# file.close()

# file = open('input.txt', 'w')
# num = 1
# for i in range(1,11):
#     num *= i
#     file.write(str(i) + '\n')
# file = open('output.txt', 'w')
#
# file.write(str(num))
# file.close()

good1 = {'cars':2, 2022.12,1000001}
print(good1)
with open('test1.txt','r') as file:
    some_str = file.read()
    for line in some_str[2]:
        if line > 1000000 and line < 2023.1:
            print(line.rstrip())



















































