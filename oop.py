class dog():
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says Woof!")
my_dog = dog("Buddy")
my_dog.bark()  # Output: Buddy says Woof!