# 访问可见性
# 如果属性或者方法私有，加上两个下划线
# 建议将属性设为私有，使用@property包装器，包装getter和setter。
# Python是动态语言，允许在运行过程中给对象绑定属性。可以使用 __slots__=('_name','_age')等限定属性
# 静态方法和类方法 @staticmethod  @classmethod


class Student:
    __slots__ = ('name','age')
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def study(self,cource_name):
        print('%s正在学习%s' %(self.name,cource_name))

    def fillForm(self):
        print('%s填写年龄%d' %(self.name,self.age))

    @staticmethod
    def is_valid(age):
        return age<18

    @classmethod
    def is_real_valid(cls,age):
        return age<18



def main():
    print(Student.is_valid(19))
    print(Student.is_real_valid(19))
    stu1=Student('zhao',18)
    stu2=Student('liu',19)
    stu1.study('zhongwen')
    stu2.fillForm()

class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age=age

    @name.setter
    def name(self,name):
        self._name=name
    def play(self):
        print('play')

def main1():
    person=Person('zhao',18)
    person.name='liu'
    person.age=19
    person.play()

if __name__ == '__main__':
    main()
    main1()




