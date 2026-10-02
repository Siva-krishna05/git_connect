'''i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")'''
    
'''for i in range(1):
    print("#")
else:
    print("#")'''
    
'''var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")'''
    
'''var = 1
while var < 10:
    print("#")
    var = var << 1
'''
'''a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)'''

'''my_list = [3, 1, -2]
print(my_list[my_list[-1]])'''

'''nums = [1, 2, 3]
vals = nums[-1:-2]
print(vals)'''

'''my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
    print(my_list_2)'''
'''my_list = [1, 2, 3]
for v in range(3):
    my_list.insert(1, my_list[v])
    print(my_list)
'''
'''my_list = [i for i in range(-1, 2)]
print(my_list)'''

'''t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
    print(s)'''
    

'''my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])
'''

'''def message(number):
    print("Enter a number:", number)

number=123
message(90)
print("number:",number)'''

'''def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")'''

'''def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")'''

'''def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(surname="Skywalker", first_name="Luke")'''
'''def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(1, 2, 3)'''

'''def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)
introduction("James", "Doe")'''

'''def hi(name):
 print("hii",name)
hi("shiva")'''

'''def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
        
        
    print("Happy New Year!")
'''

'''def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)'''

'''def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")'''

'''print(None + 2)'''
'''value = None
if value is None:
    print("Sorry, you don't carry any value")

'''

'''def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(23))
print(strange_function(100))'''

'''def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s
print(list_sum([2,4,6]))'''

'''def multiply(a, b):
    return a * b

print(multiply(3, 4))    # outputs: 12


def multiply(a, b):
    return

print(multiply(3, 4))    # outputs: None
'''
'''def wishes():
    return "Happy Birthday!"

w = wishes()

print(w)    # outputs: Happy Birthday!'''

'''def wishes():
    print("My Wishes")
    return "Happy Birthday"
print(wishes())'''

'''def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)

hi_everybody(["Adam", "John", "Lucy"])'''
'''
list=["siva","raghu","ram"]
for i in list:
    print("hiii",i)'''
    
'''def create_list(n):
    my_list = []
    for i in range(n):
        my_list.insert(0,i) #[4,3,2,1,0]
        my_list.append(i)   #[0,1,2,3,4]
    return my_list

print(create_list(5))'''

'''def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))'''

'''def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))'''

'''def lb_to_kg(lb):
    return lb * 0.45359237


print(lb_to_kg(2))'''

'''def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(1, 1))'''

'''def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.4535923


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))'''

'''def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))'''

'''def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))'''

'''def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))'''

'''def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')'''
    
'''def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))'''

# Recursive implementation of the factorial function.

'''def factorial(n):
    if n == 1:    # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) # 4 * 3 * 2 * 1 = 24'''

'''def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))'''

'''dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)'''

'''dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary['swan'] = 'cygne'

for key in dictionary.keys():
    print(key, "->", dictionary[key])'''
    
'''dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)'''
    
'''dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in sorted(dictionary.values()):
    print(french)'''

'''colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)'''

'''try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')'''
    
'''while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")
        
while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except ValueError:
        print("Wrong value.")
    except ZeroDivisionError:
        print("Sorry. I cannot divide by zero.")
    except:
        print("I don't know what to do...")'''

'''try:
    value = int(input("Enter a value: "))
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except:
    print("Booo!")'''
    
'''def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)


print(f(3))
'''
'''def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x)'''

dictionary = {}
my_list = ['a', 'b', 'c', 'd']

'''for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0])# Insert your code here'''
    
'''def func(a, b):
    return a ** a


print(func(2))'''
'''ef func_1(a):
    return a ** a


def func_2(a):
    return func_1(a) * func_1(a)


print(func_2(2))
'''
'''def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return


print(fun(fun(2)) + 1)'''
'''def fun(x):
    global y
    y = x * x
    return y


fun(2)
print(y)'''
'''def any():
    print(var + 1, end='')


var = 1
any()
print(var)'''
my_list =  ['Mary', 'had', 'a', 'little', 'lamb']


''''def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'


print(my_list(my_list))'''
'''def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))'''
'''dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]

print(v)'''
'''tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)'''
my_list = [1, 2]

'''for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)'''

'''for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)
'''
my_list =  [x * x for x in range(5)]


'''def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(my_list))'''
'''x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z


print(x, y, z)'''

'''a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
'''
'''def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(2))'''
'''nums = [1, 2, 3]
vals = nums
del vals[:]
print(vals)'''
'''print("a", "b", "c", sep="sep")'''
'''x = 1 // 5 + 1/ 5
print(x)'''

'''x = float(input())
y = float(input())
print(y ** (1 / x))'''
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

'''for k in range(len(dct)):
    v = dct[v]

print(v)'''
'''lst = [i for i in range(-1, -2)]
print(lst)'''

'''def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


print(fun(0, 3))
'''
'''i = 0
while i < i + i :
    i += 1
    print("*")
else:
    print("*")'''
    
dd = {"1": "0", "0": "1"}
'''for x in dd.vals():
    print(x, end="")'''
'''dd = {"1": "0", "0": "1"}
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")
    print(dct)'''
'''lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")'''
'''try:
    value = input("Enter a value: ")
    print(int(value)/len(value))
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")'''
'''
import json
data={"name":"siva","active":"True"}
with open("user.json") as f:
    data = json.load(f)
print(type(data))'''
'''
import requests
url = "https://www.programiz.com/html/online-compiler"

response = requests.get(url)

print(response.status_code)
print(response.text)
from bs4 import BeautifulSoup

html = response.text

soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)'''
word =input()
length=len(word)
empty_space=""
for i in range (length):
    number=int(input())
    empty_space=empty_space+word[number]
print(empty_space)







































































































        






 





























