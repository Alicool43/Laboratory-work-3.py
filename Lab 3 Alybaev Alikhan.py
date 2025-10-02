                                                                     # Alybaev Alikhan Lab 3
# Python Classes
# Task 1:
class StringClass:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

obj = StringClass()
obj.getString()
obj.printString()

# Task 2:
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


sq = Square(5)
print( "Square area:", sq.area())

# Task 3:
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(4, 7)
print("Area of a rectangle:", rect.area())

# Task 4:
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

p1 = Point(2, 3)
p2 = Point(5, 7)

p1.show()
p2.show()

print("Distance between points:", p1.dist(p2))

p1.move(-1, 2)
p1.show()

# Task 5:
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawal: {amount}. Balance: {self.balance}")

acc = Account("Ali", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)  

# Task 6:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 11, 15, 17, 20]

primes = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", primes)

# Python Function
# Task 1:
def grams_to_ounces(grams):
    return 28.3495231 * grams

print(grams_to_ounces(10)) 

# Task 2:
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

print(fahrenheit_to_celsius(100)) 

# Task 3:
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None, None

print(solve(35, 94))

# Task 4:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

print(filter_prime([1, 2, 3, 4, 5, 15, 17])) 

# Task 5:
import itertools

def all_permutations(s):
    perms = itertools.permutations(s)
    for p in perms:
        print(''.join(p))

all_permutations("abc")

# Task 6:
def reverse_sentence(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

print(reverse_sentence("We are ready"))

# Task 7:
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))       
print(has_33([1, 3, 1, 3]))    
print(has_33([3, 1, 3]))

# Task 8:
def spy_game(nums):
    code = [0, 0, 7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if not code:  
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))   
print(spy_game([1,0,2,4,0,5,7]))   
print(spy_game([1,7,2,0,4,5,0]))   

# Task 9:
import math

def sphere_volume(r):
    return (4/3) * math.pi * (r**3)

print(sphere_volume(3))

# Task 10:
def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

print(unique_list([1,2,2,3,4,4,5])) 

# Task 11:
def is_palindrome(word):
    word = word.replace(" ", "").lower()  
    return word == word[::-1]

print(is_palindrome("madam"))        
print(is_palindrome("hello"))    

# Task 12:
def histogram(lst):
    for n in lst:
        print('*' * n)

histogram([4, 9, 7])

# Task 13:
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)

    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()

# Python Function
# Task:
# Dictionary of movies
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_above_55(movie):
    return movie["imdb"] > 5.5

def movies_above_55(movies):
    return [m for m in movies if m["imdb"] > 5.5]

def movies_by_category(movies, category):
    return [m for m in movies if m["category"].lower() == category.lower()]

def average_imdb(movies):
    if not movies:
        return 0
    return sum(m["imdb"] for m in movies) / len(movies)

def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies)

print("1. Is 'Hitman' above 5.5?", is_above_55(movies[1]))
print("\n2. Movies above 5.5:")
for m in movies_above_55(movies):
    print("-", m["name"])

print("\n3. Movies in Romance category:")
for m in movies_by_category(movies, "Romance"):
    print("-", m["name"])

print("\n4. Average IMDB of all movies:", average_imdb(movies))

print("\n5. Average IMDB of Romance movies:", average_imdb_by_category(movies, "Romance"))