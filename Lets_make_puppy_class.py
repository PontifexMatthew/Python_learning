class Puppy:

  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

  def __str__(self):
    return f"{self.breed} puppy named {self.name}, age: {self.age}"

  def woof_woof(self):
    print("Woof woof!")

  def introduce(self):
    self.woof_woof()
    print(f"My name is {self.name} and I am a baby {self.breed} puppy!")
    self.woof_woof()

dubu = Puppy(name = "dubu", age = 2, breed = "Shiba")
hodu = Puppy(name = "hodu", age = 3, breed = "Chihuahua")

dubu.introduce()