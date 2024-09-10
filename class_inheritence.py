class Dog:

  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  def sleep(self):
    print("zzzzzz....")

class GuardDog(Dog):

  def __init__(self, name, breed):
    super().__init__(
      name,
      breed,
      5
    )
    self.aggresive = True

  def rrrrr(self):
    print("stay away!")

class Puppy(Dog):

  def __init__(self, name, breed):
    super().__init__(
      name,
      breed,
      0.1
    )
    self.spoiled = True

  def __str__(self):
    return f"{self.breed} puppy named {self.name}"

  def woof_woof(self):
    print("Woof woof!")

  def break_furniture(self, spoiled):
    if spoiled:
      print("I'd like to break house!")
    else:
      print("I'm kind puppy that I will clean my house")

dubu = Puppy(
  name = "dubu",
  breed = "Shiba"
)

hodu = GuardDog(
  name = "hodu",
  breed = "Chihuahua"
)

dubu.sleep()
hodu.sleep()
dubu.break_furniture(spoiled=False)