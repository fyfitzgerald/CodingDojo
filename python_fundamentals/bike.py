class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print("Price:", self.price)
        print("Speed:", self.max_speed)
        print("Miles:", self.miles)
        return self

    def ride(self):
        self.miles += 10
        print("Riding")
        return self

    def reverse(self):
        self.miles -= 10
        if self.miles < 0:
            self.miles = 0
        print("Reversing")
        return self


# bike1 = Bike(200, "25mph")
# bike1.ride().ride().ride().reverse().displayInfo()

# bike2 = Bike(350, "32mph")
# bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(180, "20mph")
bike3.reverse().reverse().reverse().displayInfo()


The ride and reverse methods can return self to allow for chaining.
You prevent negative miles by inserting an "if" function (see above).