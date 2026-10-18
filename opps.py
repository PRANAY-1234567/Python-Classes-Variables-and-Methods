'''#way --2

class Bank:
    Holder ="ABC"
    bal=100
    def Data(self):
        print(f'Holder Name is {Bank.Holder}\n'
              f'Total Balance is {Bank.bal}')
b=Bank()
b.Data()
#Modification through object
b.Holder="PQR"
b.bal=9000
#Modification through ClassName
Bank.Holder='Joy'
Bank.bal=5000
b.Data()'''

'''class Flipkart:
    total_item=12
    add="Pune"
    def Data(self):
        print(f'Total item count is {self.total_item}')

    def Information(self):
        print(f'Customer current address is {self.add}')

f=Flipkart()
f.Data()
f.Information()'''

'''class Flipkart:
    total_item=12
    add="Pune"
    def Data(self):
        print(f'Total item count is {self.total_item}')
        self.Information()  #f.Information()

    def Information(self):
        print(f'Customer current address is {self.add}')

f=Flipkart()
f.Data()
f.Information()'''

'''
class Flipkart:
    total_item=12
    add="Pune"
    def Data(self):
        print(f'Total item count is {self.total_item}')

    def Information(self):
        print(f'Customer current address is {self.add}')

f=Flipkart()
f.Data()
f.Information()'''

'''class Student:
    def Information(self):
        self.name="Ravi"
        self.age=23
        self.sub="python"

        print(f'Student Name is {self.name}\n'
              f'student age is {self.age}\n'
              f'student subject is {self.sub}')'''


'''class Mock:
    def study(self, name,subject, rating):
        self.name = name           #self.n=name
        self.subject = subject     #self.s=subject
        self.rating = rating       #self.r=rating

        print(f'Student name is {self.name} \n'
              f'student subject is {self.subject} \n'
              f'student rating {self.rating}')

m=Mock()
m.study("a","Python","*")
print()
m.study("B", "SQL", "#")
print()
m.study("C", "Web_tech", "5")
print()'''


'''class Evening:
    @classmethod
    def demo(cls):
        def demo(pranay):
            print("Demo Method")
e= Evening()
print(e)
e.demo()'''

'''class School:
    sub = "SQL"
    @classmethod
    def display(cls):
        print(f'Subject Name is {cls.sub}')

    @classmethod
    def show (cls, new_sub):
        cls.sub=new_sub
        print(f'Modificaation name is {cls.sub}')

School.display()
School.show("Python")'''

'''
class School:
    sub = "SQL"
    @classmethod
    def display(cls):
        print(f'Subject Name is {cls.sub}')

    @classmethod
    def show (cls, new_sub):
        cls.sub=new_sub
        print(f'Modificaation name is {cls.sub}')

School.sub=("Python")
School.display()'''

'''
class School:
    sub = "SQL"
    @classmethod
    def display(cls):
        print(f'Subject Name is {cls.sub}')

    @classmethod
    def show (cls, new_sub):
        cls.sub=new_sub
        print(f'Modificaation name is {cls.sub}')

School.display()
School.show("Python")'''
