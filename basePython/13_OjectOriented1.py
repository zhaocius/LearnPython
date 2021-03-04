#继承和多态
from abc import ABCMeta,abstractmethod
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def watch_tv(self):
        if self.age>18:
            print("watch big tv")
        else:
            print("watch small tv")
    def play(self):
        print("play majiang")

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade

    def study(self):
        print("study %s grade " %(self.grade))

    def play(self):
        print("play puke")

def main():
    stu=Student('zhao',18,'9')
    print(stu.study())
    print(stu.watch_tv())
    print(stu.play())


if __name__ == '__main__':
    main()

