# Python Classes, Variables, and Methods

## 📌 Overview

This project demonstrates fundamental concepts of Python Object-Oriented Programming (OOP) through practical examples.
It explores how classes and objects work, how class variables and instance variables differ, how instance methods access object data, and how class methods modify class-level attributes.
The examples use real-world scenarios such as banking, online shopping, student information, and school subjects.

## 🎯 Concepts Covered

* Classes and Objects
* Class Variables
* Instance Variables
* Instance Methods
* Class Methods (`@classmethod`)
* The `self` Parameter
* The `cls` Parameter
* Modifying Class Attributes
* Calling Methods Within a Class
* Object-Specific Data

## 📂 Examples Included

### 1. Bank — Class Variables and Object Modification

The `Bank` class contains two class variables:

* `Holder`: Stores the account holder's name.
* `bal`: Stores the account balance.

The `Data()` method displays the account information.

This example demonstrates two ways of modifying attributes:

**Modification through an object:**

```python
b.Holder = "PQR"
b.bal = 9000
```

These assignments create instance attributes on `b`. They do not change the original class variables.

**Modification through the class name:**

```python
Bank.Holder = "Joy"
Bank.bal = 5000
```

These assignments modify the class variables.

**Key learning:** Class variables are shared at the class level, while instance attributes belong to individual objects. An instance attribute can override the value accessed through an object without changing the class variable.

### 2. Flipkart — Accessing Class Variables

The `Flipkart` class contains:

* `total_item`: Stores the total item count.
* `add`: Stores the customer's address.

The methods `Data()` and `Information()` display these values.

An object is created using:

```python
f = Flipkart()
f.Data()
f.Information()
```

Because the object does not have its own attributes with these names, Python retrieves the values from the class.

### 3. Flipkart — Calling One Method from Another

This example demonstrates how one instance method can call another instance method.
Inside `Data()`, the code calls:

```python
self.Information()
```

When `Data()` executes, it displays the item count and then calls `Information()` to display the customer's address.

**Key learning:** Using `self` allows one instance method to call another method on the same object.

### 4. Student — Instance Variables

The `Student` class defines an `Information()` method that creates three instance variables:

* `name`: Student's name.
* `age`: Student's age.
* `sub`: Student's subject.

The method displays the student's information.

**Key learning:** Instance variables store data associated with an object. In this example, the variables are created when `Information()` executes.

### 5. Mock — Passing Data to an Instance Method

The `Mock` class defines a `study()` method that accepts three parameters:

* `name`
* `subject`
* `rating`

These values are stored in instance variables and displayed.

The method is called multiple times:

```python
m = Mock()

m.study("A", "Python", "*")
m.study("B", "SQL", "#")
m.study("C", "Web_tech", "5")
```

Each call assigns new values to the same object's instance variables.

**Key learning:** An instance method can accept arguments and use them to update an object's attributes.

### 6. Evening — Understanding Class Methods

The `Evening` example introduces the `@classmethod` decorator.

However, the original code has an issue:

```python
@classmethod
def demo(cls):
    def demo(pranay):
        print("Demo Method")
```

The inner `demo()` function is defined but never called. It also does not replace the outer method.

Therefore, calling `e.demo()` will not print `"Demo Method"`.

A corrected example is:

```python
class Evening:
    @classmethod
    def demo(cls):
        print("Demo Method")

e = Evening()
e.demo()
```

**Output:**

```text
Demo Method
```

**Key learning:** A class method receives the class as its first argument, conventionally named `cls`.

### 7. School — Modifying a Class Variable Using a Class Method

The `School` class contains a class variable:

```python
sub = "SQL"
```

It defines two class methods.

**`display()`**

Displays the current subject name.

**`show(new_sub)`**

Updates the class variable and displays the new subject.

Example:

```python
School.display()
School.show("Python")
```

**Output:**

```text
Subject Name is SQL
Modificaation name is Python
```

**Key learning:** Class methods can access and modify class variables using `cls`.

### 8. School — Modifying a Class Variable Directly

This example demonstrates modifying a class variable without using a class method.

```python
School.sub = "Python"
School.display()
```

The assignment changes the class-level subject from `"SQL"` to `"Python"`.

**Output:**

```text
Subject Name is Python
```

This approach is useful when you want to update a class attribute directly.

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

## ▶️ How to Run

1. Install Python 3 on your computer.
2. Copy the example you want to run into a Python file.
3. Save the file as `python_oop_basics.py`.
4. Open a terminal in the folder containing the file.
5. Run the following command:

```bash
python python_oop_basics.py
```

**Important:** Most examples in the original code are enclosed in triple quotes (`''' ... '''`). Python treats these as string literals, so the enclosed code will not execute as ordinary statements. Remove the surrounding triple quotes from the example you want to run.

## 📚 Learning Outcomes

After completing this project, you should understand:

* How classes and objects work in Python.
* The difference between class variables and instance variables.
* How instance methods use `self`.
* How class methods use `cls`.
* How to modify class attributes through a class method or the class name.
* How to call one instance method from another.
* How to pass arguments to methods and update object attributes.

## 👨‍💻 Author

**Pranay Jadhao**

Learning Python, Object-Oriented Programming, and software development.

