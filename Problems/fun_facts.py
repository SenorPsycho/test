import random

fun_facts = [
    "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs.",
    "Bananas are berries, but strawberries are not.",
    "A group of flamingos is called a 'flamboyance'.",
    "Octopuses have three hearts.",
    "The Eiffel Tower can be 15 cm taller during hot days.",
    "Wombat poop is cube-shaped.",
    "There are more stars in the universe than grains of sand on Earth.",
    "Some turtles can breathe through their butts.",
    "A day on Venus is longer than a year on Venus.",
    "The inventor of the Frisbee was turned into a Frisbee after he died."
]

def get_fun_fact():
    return random.choice(fun_facts)

if __name__ == "__main__":
    print("Fun Fact:", get_fun_fact())