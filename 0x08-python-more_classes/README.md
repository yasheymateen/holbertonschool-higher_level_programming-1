# 0x08. Python - More Classes and Objects

---
## Description
This project in the High Level Programming series is about:
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python


## Files
---
File|Task
---|---
0-rectangle.py | Write an empty class `Rectangle` that defines a rectangle.
1-rectangle.py | Add private instance attribute `width` and `height` and __init__ method
2-rectangle.py | Add public instance methods `area` and `perimeter`
3-rectangle.py | Add str representation __str__ to print the rectangle with the character `#`
4-rectangle.py | Add __repr___ method which should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
5-rectangle.py | Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
6-rectangle.py | Create a Public class attribute `number_of_instances` that is Initialized to 0, Incremented during each new instance instantiation and Decremented during each instance deletion
7-rectangle.py | Add Public class attribute `print_symbol`: 	       Initialized to `#`, used as symbol for string representation, and can be any type
8-rectangle.py | Add Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
9-rectangle.py | Add Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`


## Author
Jinji Zhang
