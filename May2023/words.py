words = [
    "polo",
    "england",
    "skyscraper",
    "drees",
    "tuxedo",
    "agent",
    "compound",
    "deck",
    "shoe",
    "shorts",
    "boot",
    "plane",
    "school",
    "cap",
    "texas",
    "bomb",
    "dash",
    "telescope",
    "tin",
    "glove",
    "kiss",
    "governor",
    "sherlock",
    "suit",
    "sun",
    "space",
    "mill",
    "circle",
    "duck",
    "powder",
    "fever",
    "scorpion",
    "octopus",
    "silk",
    "war",
    "hotel",
    "foam",
    "cuckoo",
    "sheet",
    "penguin",
    "rabbit",
    "mud",
    "glasses",
    "shark",
    "dog",
    "turtle",
    "cloak",
    "reindeer",
    "ice",
    "eagle",
    "bank",
    "soup",
    "cheese",
    "well",
    "potato",
    "magazine",
    "pie",
    "salad",
    "carrot",
    "pizza",
    "army",
    "paddle",
    "hamburger",
    "himalayas",
    "country",
    "cycle",
    "bride",
    "biscuit",
    "pacific",
    "lab",
    "ash",
    "kid",
    "queen",
    "novel",
    "jet",
]

points = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10,
}

for word in words:
    val = sum(points[c] for c in word)
    if val & 1:
        print(word)

"""
england
skyscraper
compound
deck
shoe
shorts
plane
school
cap
telescope
tin
glove
sherlock
sun
space
duck
fever
octopus
foam
dog
cloak
reindeer
ice
cheese
well
pie
pizza
army
hamburger
himalayas
biscuit
lab
"""