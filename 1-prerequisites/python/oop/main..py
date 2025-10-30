#--- Class ---
class Microwave:
    #initialiser
    def __init__(self, brand:str, powerRating: str):
        self.brand = brand
        self.powerRating = powerRating
        self.turnedOn: bool = False

    #methods
    def turnOn(self) -> None:
        if self.turnedOn:
            print(f"Microwave {self.brand} is aready turned on!")
        else:
            self.turnedOn = True
            print(f"Microwave {self.brand} is now turned on!")

    def turnOff(self) -> None:
        if self.turnedOn:
            self.turnedOn = False
            print(f"Microwave {self.brand} is now turned off!")
            
        else:
            print(f"Microwave {self.brand} is aready turned off!")
            
    def run(self, seconds:int) -> None:
        if self.turnedOn:
            print(f"Running {self.brand} for {seconds} seconds")
        else:
            print("Bruh turn on the microwave first!")

    # dunder method / magic methods
    def __add__(self, other):
        return f'{self.brand} + {other.brand}'
    
    def __mul__(self, other):
        return f'{self.brand} * {other.brand}'
    
    def __str__(self) -> str:
        return f'{self.brand} (Rating: {self.powerRating})'
    
    def __repr__(self):
        return f'Microwave (brand = "{self.brand}", power_rating = "{self.powerRating}")'
        
walton = Microwave('Walton', 'A')

walton.turnOn()
walton.run(30)
walton.turnOff()
walton.run(10)

nova = Microwave("Nova", 'B')

nova.turnOn()
nova.turnOff()
nova.run(20)



print(walton + nova)
print(walton * nova)

print(walton)
print(repr(nova))
