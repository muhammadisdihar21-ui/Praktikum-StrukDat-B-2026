"""#classes/objects
#membuat class
class MyClass:
  x = 5

#membuat object
p1 = MyClass()
print(p1.x)

#menghapus object
del p1

#membuat beberapa object
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#the pass statement
class Person:
  pass

#__init__ Method
#membuat class dengan metode __init__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("isdihar", 19)

print(p1.name)
print(p1.age)

#membuat class tanpa metode __init__()
class Person:
  pass

p1 = Person()
p1.name = "Isdihar"
p1.age = 19

print(p1.name)
print(p1.age)

#menetapkan nilai default pada parameter metode __init__()
class Person:
  def __init__(self, name, age=19):
    self.name = name
    self.age = age

p1 = Person("Isdihar")
p2 = Person("Abi", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

#membuat parameter sebanyak apapun yang dibutuhkan pada __init__()
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Isdihar", 19, "Pekanbaru", "Indonesia")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

#Self Parameter
#menggunakan self untuk mengakses properti class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("isdihar", 19)
p1.greet()

#menggunakan kata-kata myobject dan abc sebagai pengganti self
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Isdihar", 19)
p1.greet()

#bisa juga mengakses beberapa properti menggunakan self
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2026)
car1.display_info()

#memanggil satu metode dari metode lain menggunakan self
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Isdihar")
p1.welcome()

#Class Properties
#Mengubah properti class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Isdihar", 19)
print(p1.age)

p1.age = 20
print(p1.age)

#menghapus properti class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Isdihar", 19)

del p1.age

print(p1.name) #ini bisa dijalankan
#print(p1.age) #jika ini dijalankan maka akan error

#memodifikasi properti class
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Isdihar")
p2 = Person("Budi")

Person.lastname = "Albert"

print(p1.lastname)
print(p2.lastname)

#menambahkan properti baru
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Isdihar")

p1.age = 19
p1.city = "Pekanbaru"

print(p1.name)
print(p1.age)
print(p1.city)
"""
#Class Methods
#membuat metode dengan parameter
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

#membuat metode yang dapat memodifikasi properti suatu object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Isdihar", 18)
p1.celebrate_birthday()

#metode __str__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Isdihar", 19)
print(p1)

#membuat beberapa metode dalam sebuah class
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

#menghapus sebuah metode dari sebuah class
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Isdihar")

del Person.greet

p1.greet() #ini jika dijalankan akan error