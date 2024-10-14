import random
import time

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 50

    def feed(self):
        """Feed the pet to decrease hunger and slightly decrease happiness."""
        if self.hunger > 0:
            self.hunger -= 20
            self.happiness -= 5
            print(f"{self.name} has been fed!")
        else:
            print(f"{self.name} is not hungry!")

    def play(self):
        """Play with the pet to increase happiness and slightly increase hunger."""
        if self.happiness < 100:
            self.happiness += 15
            self.hunger += 5
            print(f"{self.name} enjoyed playing!")
        else:
            print(f"{self.name} is too happy to play!")

    def check_status(self):
        """Display the current happiness and hunger levels of the pet."""
        print(f"{self.name}'s Happiness: {self.happiness}, Hunger: {self.hunger}")

    def update_status(self):
        """Automatically update pet's status over time."""
        self.hunger += 1
        self.happiness -= 1

        # Check for sad or hungry pet conditions
        if self.hunger > 100:
            print(f"Oh no! {self.name} has become too hungry and has run away!")
            return True  # Game over
        if self.happiness <= 0:
            print(f"Oh no! {self.name} is too sad and has lost the will to play!")
            return True  # Game over
        return False  # Game continues

def main():
    print("Welcome to the Virtual Pet Simulator!")
    
    # User names the pet
    pet_name = input("What would you like to name your pet? ")
    pet = VirtualPet(pet_name)

    while True:
        print("\nMenu:")
        print("1. Feed the pet")
        print("2. Play with the pet")
        print("3. Check pet's status")
        print("4. Quit")
        
        choice = input("Choose an action (1-4): ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.check_status()
        elif choice == '4':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Update pet's status automatically
        if pet.update_status():
            break

        # Simulate time passing
        time.sleep(1)

if __name__ == "__main__":
    main()
