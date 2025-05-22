from array import array

# Điều kiện logic
x = 5
y = 3
result = (x > 2) and (y < 4)
print("Result 1:", result)

x = 5
y = 3
result = (x > 2) or (y > 4)
print("Result 2:", result)

x = 5
result = not (x == 5)
print("Result 3:", result)

x = 5
result = (x == 5)
print("Result 4:", result)

x = 5
result = (x != 3)
print("Result 5:", result)

x = 5
result1 = (x > 3)
result2 = (x < 3)
print("Result 6 (result1, result2):", result1, result2)

x = 5
result1 = (x >= 3)
result2 = (x <= 3)
print("Result 7 (result1, result2):", result1, result2)

# Nhập/xuất
name = input("Nhap ten cua ban: ")
print("Xin chao, ", name)

age = 20
print("Tuoi cua ban: ", age)

print("python", "la", "ngon", "ngu", "lap", "trinh", sep="-")
print("xin chao", end=" ")
print("cac ban!")

# Câu lệnh điều kiện
x = 10
if x > 5:
    print("x lon hon 5")
elif x == 5:
    print("x bang 5")
else:
    print("x nho hon 5")

# Vòng lặp
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 1

for i in range(1, 101):
    if i % 5 == 0:
        print("So chia het cho 5 dau tien la: ", i)
        break

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

# Chuỗi
string_single_quotes = "day la mot chuoi su dung dau ngoac don."
string_double_quotes = "day la mot chuoi su dung dau ngoac kep."
string_triple_quotes = '''day la mot chuoi su dung dau ngoac ba, 
                        co the trai dai qua nhieu dong.'''
print("String single quotes:", string_single_quotes)
print("String double quotes:", string_double_quotes)
print("String triple quotes:", string_triple_quotes)

my_string = "hello, world!"
print(my_string[0])
print(my_string[7])

string1 = "hello"
string2 = "world"
concatenated_string = string1 + " " + string2
print("Concatenated string:", concatenated_string)

my_string = "hello world!"
length = len(my_string)
print("Length of string:", length)

my_string = "hello world!"
print(my_string.strip())

my_string = "hello world!"
print(my_string.split())

# Hàm


def my_function(parameter1, parameter2):
    result = parameter1 + parameter2
    return result


result = my_function(10, 20)
print("Result of my_function:", result)


def calculate_sum(a, b):
    result = a + b
    return result


sum_result = calculate_sum(10, 20)
print("Tong hai so la: ", sum_result)


def greet(name):
    print("xin chao", name)


greet("tommy")

# Danh sách
my_list = [1, 2, 3, 4, 5]
names = ["alice", "bob", "charlie"]
mixed_list = [10, "hello", 3.14, True]
print(my_list[0])
print(names[2])
my_list[1] = 20
print(my_list)
names.append("david")
print(names)
del my_list[2]
print(my_list)
for element in names:
    print(element)

# Tuple
my_tuple = (1, 2, 3, 4, 5)
names = ("alice", "bob", "charlie")
mix_tuple = (10, "hello", 3.14)
print(my_tuple[0])
print(names[2])
my_tuple = (1, 2, 3, 1, 4, 1)
print(my_tuple.count(1))

my_tuple = ('a', 'b', 'c', 'd', 'b')
print(my_tuple.index('b'))

# Từ điển
person = {"name": "alice", "age": 25, "city": "ny"}
print(person["name"])
print(person["age"])
person["email"] = "alice@example.com"
person["age"] = 25
del person["city"]
age = person.pop("age")
print(person.keys())
print(person.values())
print(person.items())

# Lớp


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"{self.brand} {self.model}"


car = Car("Toyota", "Camry")
print(car.get_info())


class ClassName:
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2


class_attribute = "Class Attribute"
