
""" class MyClass:
    count = 0

    def __init__(self, num):
        self.count = num

    @classmethod
    def clsMethod(cls):
        cls.count += 1 
        print(f"cls count = {cls.count}")

    def instMethod(self):
        self.count += 1 
        print(f"instance = {self.count}")

MyClass.clsMethod()

obj = MyClass(10)

obj.instMethod()
print(obj.count)

print(MyClass.count)
print(MyClass.count) """


# 클래스 정의 예시
""" class Champion:
    lv = 1
    movSpd = 0
    basicMovSpd = 325
    atkSpd = 0.658
    
    def __init__(self, ChamNam, speed):
        self.hp = 100
        self.ChamNam = ChamNam
        self.level = 1
        self.setSpeed(speed)
        self.setAtkSpd()
        self.setMovSpd()
        
    def setAtkSpd(self):
        self.atkSpd = 0.658*((1.0334)**(Champion.lv - 1))
        
    def beAtk(self, dem):
        print("be attak", dem, 1-100.0/(100.0+100))
        self.dem = dem*(100.0/(100.0+100))
        print(self.dem)
        self.hp = self.hp - self.dem
        
    def setSpeed(self, sp):
        if (sp == 1):
            self.speed = 50
        else:
            self.speed = 0
            
    def setMovSpd(self):
        print("set Mov spd")
        self.movSpd = (20 + self.speed)*(1.00)*(100)
        
    def printStatus(self):
        print("ChamNme: %s, hp:%f, lv:%d, mvSpg:%f, atkSpd%f" % (self.ChamNam, self.hp, self.lv, self.movSpd, self.atkSpd))
        
ashe = Champion("ashe", 474.0)
mipo = Champion("mipo", 520.0)
    
ashe.printStatus()
mipo.printStatus()

mipo.beAtk(63.0)
mipo.printStatus() """
    
            


""" class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1

class Yasuo(Champion) :
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)
        
class Garen(Champion) :
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)
        
user1 = Yasuo("pyrhon")
user2 = Garen("hello")

user1.getName()
user1.getLevel()

user2.getName()
user2.getLevel() """
        


# 상속
""" class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1

class Yasuo(Champion) :
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)
        
class Garen(Champion) :
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)
        
class Yasuo(Champion):()
class Garen(Champion):() """


# 오버라이딩(overrriding) - 재정의 오버로딩은 지원 안됨
""" class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1
    
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)


class Yasuo(Champion) :
    def attck(self, key):
        print(f"attack - {key} steel tempest")
        return


class Garen(Champion) :
    def attck(self, key):
        print(f"attack - {key} demacian justice")
        return

user1 = Yasuo("pyrhon")
user2 = Garen("hello")

user1.getLevel()
user2.getLevel()

user1.attck("q")
user2.attck("r")

user1.levelup()
user2.levelup()

user1.getLevel()
user2.getLevel() """


# 추상화
""" 사물의 개체나 시스템을 모델링하기 위해 필요한 특징을 추출하고 강조하는 프로세스를 의미
객체의 복잡성을 관리하고 중요한 부분을 강조하며, 핵심 특성을 구성하는데 사용됩니다. """

""" from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circ = Circle(5)
rect = Rectangle(4, 6)

print(circ.area())
print(rect.area())

sett = [circ, rect]
for st in sett:
    print(st.area()) """

# 객체가 달라짐으로 인해서 값이 달라집니당


# 정보은닉
""" class Person:
    def __init__(self, name, age, num):
        self._name = name
        self._age = age
        self._number = num

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def number(self):
        return self._number

    @name.setter
    def name(self, new):
        self._number = new

    @age.setter
    def age(self, nAge):
        self._age = nAge
        
user1 = Person("Alice", 30, "01011112222")

print(user1.age)
print(user1._age)
print(user1.name)
print(user1._name)
print(user1.number)
print(user1._number)

user1._age = 21
user1.age = 23
print(user1.age) """


# 다형성
""" 동일한 인터페이스를 통해 다양한 객체 타입을 구성할 수 있는 매카니즘.
코드의 유연성과 재사용성을 향상시키는 역할. """
class Person :
    def __init__(self, name, age, num) :
        self.name = name
        self.age = age
        self.number = num
    
    def getName(self) :
        return self.name
    
    def getAge(self) :
        return self.age
    
    def getNumber(self) :
        return self.number

class Student(Person) : ()

class Teacher(Person) : ()

def getPersonName(person) :
    return person.getName()

user1 = Student("alice", 23, "01011112222")
user2 = Teacher("bob", 25, "01033334444")

print(getPersonName(user1))
print(getPersonName(user2))


# 캡슐화
""" 객체와 관련된 데이터와 메서드를 하나의 단위로 묶는 것을 의미
묶인 객체는 외부에서 직접 접근하지 못하도록 보호되고
데이터에 접근하려면 메서드를 이용해 접근 및 조작 """

class Person : 
    def __init__(self, name, age, num) :
        self.name = name
        self.age = age
        self.number = num 
    
    def getName(self) :
        return self.name
    
    def setName(self, newName) :
     self.name = newName
     return

    def getNumber(self) :
     return self.number

    def setNumber(self, newNum) :
     self.number = newNum
     
p1 = Person("puthon", 23, "01012345678")
p2 = Person("hello", 21, "01087654321")

p1.getNumber()
p2.getNumber()

p1.setNumber("11111111111")
p1.setNumber("22222222222")
