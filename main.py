class animal: 
  def __init__(self, name, kingdom, colour, sound, Breed,):
    self.name = name
    self.kingdom = kingdom
    self.colour = colour
    self.sound = sound
    self.Breed = Breed

  def Animal_Info(self):
    print(f"{self.name}, the {self.Breed} {self.colour} {self.kingdom} make a {self.sound} sound.")

obj = animal("Miru", "cat", "blue", "meow", "British Shorthair")
obj.Animal_Info()

obj2 = animal("Kimi", "dog", "red", "woof", "German Sheperd")
obj2.Animal_Info()