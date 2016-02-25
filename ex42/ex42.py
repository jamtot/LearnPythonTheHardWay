## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self):
        print "An animal has been created."

## class Dog is-a Animal
class Dog(Animal):
    
    def __init__(self, name = "Dog"):
        super(Dog, self).__init__()
        ## class Dog has-a name
        self.name = name
        ## class Dog has-many tricks
        self.tricks = []
        print "A dog named %s has been created." % self.name

    def addTrick(self, trick):
        self.tricks.append(trick)
        print "Trick: '%s' added." % trick

    def listTricks(self):
        print "Listing all %s's tricks." % self.name
        for trick in self.tricks:
            print "\to %s" % trick

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name = "Cat"):
        super(Cat, self).__init__()
        ## class Cat has a name
        self.name = name
        print "A cat named %s has been made." % self.name

## class Person is-a object
class Person(object):

    def __init__(self, name):
        ## class Person has a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def introduction(self):
        print "Hi, my name is %s." % self.name
        if self.pet != None:
            print "I have a pet. My pets' name is %s." % self.pet.name

## class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

    def introduction(self):
        super(Employee, self).introduction()
        print "I am an employee. I make %d annually." % self.salary

## class Fish is-a object
class Fish(object):
    
    def __init__(self):
        print "A fish has been created."

## class Salmon is-a Fish
class Salmon(Fish):
    def __init__(self, name):
        self.name = name
        super(Salmon, self).__init__()
        print "It is a salmon.",
        if self.name:        
            print "A salmon named %s" % name
        else: print "\n"

## class Halibut is-a Fish
class Halibut(Fish):
    def __init__(self, name = None):
        self.name = name
        super(Halibut, self).__init__()
        print "It is a halibut.",
        if self.name:      
            print "A halibut named %s" % name
        else: print "\n"

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

cat = Cat()

## mary is-a Person
mary = Person("Mary")

## mary has-a pet, satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet, rover
frank.pet = rover

## flipper is-a Fish 
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon("Crouse")

## harry is-a Halibut
harry = Halibut()

mary.introduction()
frank.introduction()

rover.addTrick("Roll over")
rover.addTrick("Play dead")
rover.addTrick("Fetch")
rover.listTricks()
