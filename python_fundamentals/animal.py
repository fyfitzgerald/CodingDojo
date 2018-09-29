class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self
    
    def displayHealth(self):
        print("Health:", self.health)
        return self

# animal1 = Animal("giraffe", 90)
# animal1.walk().walk().walk().run().run().displayHealth()


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dog1 = Animal("labrador", 150)
dog1.walk().walk().walk().run().run().pet().displayHealth()


class Dragon(Animal):
    def __init__(self):
        super().__init__()
        self.health = 170
    def fly(self):
        self.health -= 10        