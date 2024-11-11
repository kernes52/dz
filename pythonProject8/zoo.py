class Zookeeper:
    def __init__(self, name):
        self.name = name

    def clean_enclosure(self, enclosure):
        enclosure.is_clean = True
        print(f"{self.name} почистив вольєр '{enclosure.name}'.")

    def feed_animal(self, animal):
        if animal.is_hungry:
            animal.eat()
            print(f"{self.name} нагодував '{animal.name}'.")
        else:
            print(f"{animal.name} вже не голодний.")

class Enclosure:
    def __init__(self, name):
        self.name = name
        self.is_clean = False
        self.is_open = False
        self.animals = []

    def open(self):
        sel.is_open = True
        print(f"Вольєр '{self.name}' відкрито.")

    def close(self):
        self.is_open = False
        print(f"Вольєр '{self.name}' закрито.")

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} додано до вольєру '{self.name}'.")

    def check_animals(self):
        for animal in self.animals:
            animal.update_mood(self)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_hungry = True
        self.is_happy = False

    def eat(self):
        self.is_hungry = False

    def update_mood(self, enclosure):
        if not self.is_hungry and enclosure.is_clean:
            self.is_happy = True
        else:
            self.ishappy = False
        mood = "радий" if self.is_happy else "не радий"
        print(f"{self.name} ({self.species}) на даний момент {mood}.")

keeper = Zookeeper("Bob")
tiger_enclosure = Enclosure("Tiger enclosure")
elephant_enclosure = Enclosure("Elephant enclosure")
lion_enclosure = Enclosure("Lion enclosure")

tiger = Animal("Jim", "tiger")
elephant = Animal("Bimbo", "elephant")
lion = Animal("Bobbie", "lion")

tiger_enclosure.add_animal(tiger)
elephant_enclosure.add_animal(elephant)
lion_enclosure.add_animal(lion)

print("\nРанок у зоопарку")
keeper.clean_enclosure(tiger_enclosure)
keeper.clean_enclosure(elephant_enclosure)
keeper.clean_enclosure((lion_enclosure))

keeper.feed_animal(tiger)
keeper.feed_animal(elephant)
keeper.feed_animal((lion))

tiger_enclosure.check_animals()
elephant_enclosure.check_animals()
lion_enclosure.check_animals()