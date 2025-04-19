class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} is eating.")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} is sleeping.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} is playing.")
        else:
            print(f"{self.name} is too tired to play.")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(self.happiness + 1, 10)
            print(f"{self.name} learned {trick}!")
        else:
            print(f"{self.name} already knows {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    def get_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")
        print("--------------------------\n")


class Cat(Pet):  # Subclass that overrides behavior (polymorphism)
    def play(self):
        if self.energy >= 1:
            self.energy -= 1
            self.happiness = min(self.happiness + 3, 10)
            self.hunger = min(self.hunger + 2, 10)
            print(f"{self.name} is chasing a laser pointer! 😹")
        else:
            print(f"{self.name} just wants to nap... 😴")

    def sleep(self):
        super().sleep()
        print(f"{self.name} curls up in a sunny spot. 🌞")


# Interactive loop
def pet_game():
    name = input("What is your cat's name? ")
    pet = Cat(name)

    print(f"\nWelcome, {pet.name} the Cat! 😺")
    print("Type a command: eat, sleep, play, train <trick>, show, status, exit")

    while True:
        command = input(">>> ").strip().lower()

        if command == "eat":
            pet.eat()
        elif command == "sleep":
            pet.sleep()
        elif command == "play":
            pet.play()
        elif command.startswith("train"):
            parts = command.split()
            if len(parts) > 1:
                trick = " ".join(parts[1:])
                pet.train(trick)
            else:
                print("Please specify a trick to train.")
        elif command == "show":
            pet.show_tricks()
        elif command == "status":
            pet.get_status()
        elif command == "exit":
            print(f"Goodbye from {pet.name}! 🐱")
            break
        else:
            print("Unknown command. Try again.")

# Start the game
pet_game()
