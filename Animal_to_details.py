import random

def choose_pet (user_input):
    if user_input.lower() in AnimalsToDetails:
        return AnimalsToDetails[user_input.lower()]
    else:
        print("Invalid pet name")
        return None
    
def roll_for_pet():
    if


    # common_pets = [pet for pet, details in AnimalsToDetails.items() if details[0] == "common"]
    # rare_pets = [pet for pet, details in AnimalsToDetails.items() if details[0] == "rare"]
    # very_rare_pets = [pet for pet, details in AnimalsToDetails.items() if details[0] == "very rare"]
    
    all_non_legendary_pets = common_pets + rare_pets + very_rare_pets
    return random.choice(all_non_legendary_pets)

def rando_marry_gen():
    all_pets = list(AnimalsToDetails.keys())
    return random.choice(all_pets)

listOfAbilities = [
    # for now this is all i can think of but later i can just add more
    "part time jobs give 5% more points", 
    "increases chances of lucky draws by 5%",
    "increase number of pets allowed in your roster by 1", 
    "increase time it takes for pets to abandon you by 6 hours"
]

length = len(listOfAbilities)

# ability is taken randomly for a list of abilities and uses the index to use the ability
AnimalsToDetails = {
    "cat": ["common", random.randint(0, length), "pet starts meowing"], 
    "dog": ["common", random.randint(0, length), "pet starts barking"],
    "dragon": ["legendary", random.randint(0, length), "pet starts breating fire"],
    "pokemon": ["legendary", random.randint(0, length), "pet starts playing with pokeball"],
    "pigeon": ["common", random.randint(0, length), "pet starts pooping on cars"],
    "eagle": ["very rare", random.randint(0, length), "pet starts shouting america"],
    "turtle": ["common", random.randint(0, length), "pet starts nothing, cause they are too slow"],
    "cheetah": ["very rare", random.randint(0, length), "pet starts running very fast"],
    "hawk": ["rare", random.randint(0, length), "pet starts hunting rats"],
    "rabbit": ["common", random.randint(0, length), "pet starts eating carrots"],
    "lion": ["holy fish rare", random.randint(0, length), "pet starts roaring"],
    "shark": ["holy fish rare", random.randint(0, length), "pet starts intimidating people with it's fins"],
    "crocodile": ["very rare", random.randint(0, length), "pet starts being still until a prey comes to them"],
    "girraffe": ["rare", random.randint(0, length), "pet starts being tall"],
    "deer": ["rare", random.randint(0, length), "pet starts standing still infront of 3000 pounds of steel coming right at it"],
    "hyena": ["rare", random.randint(0, length), "pet starts eating other pet's hunt"],
    "frog": ["common", random.randint(0, length), "pet starts kissing a princess"],
    "panda": ["holy fish rare", random.randint(0, length), "pet starts being cute"],
    "sloth": ["rare", random.randint(0, length), "pet starts nothing"],
    "koala": ["rare", random.randint(0, length), "pet starts hanging on trees"],
    "lizard": ["common", random.randint(0, length), "pet starts camouflaging"],
    "horse": ["common", random.randint(0, length), "pet starts eating sugar"],
    "donkey": ["common", random.randint(0, length), "pet starts making \"hee-haw\" noises"],
    "whale": ["very rare", random.randint(0, length), "pet starts living forever"],
    "salmon": ["rare", random.randint(0, length), "pet starts transforming in to sushi"],
    "parrot": ["common", random.randint(0, length), "pet starts repeating"],
    "hamster": ["common", random.randint(0, length), "pet starts running around in a wheel"],
    "pig": ["common", random.randint(0, length), "pet starts oinking"],
    "rat": ["common", random.randint(0, length), "pet starts entering a french restraunt"],
    "snake": ["rare", random.randint(0, length), "pet starts eating something 100 times it's size"],
    "Anaconda": ["holy fish rare", random.randint(0, length), "Nicki Minaj appears"],
    "chimpanzee": ["common", random.randint(0, length), "pet starts stealing your personal items"],
    "orangutan": ["holy fish rare", random.randint(0, length), "pet starts staring menacingly"],
    "sheep": ["common", random.randint(0, length), "pet starts baaaaaaaing"],
    "goat": ["common", random.randint(0, length), "pet starts baaaaaaaing"],
    "unicorn": ["legendary", random.randint(0, length), "pet starts healing with it's horn"],
    "sphinix": ["legendary", random.randint(0, length), "pet starts losing it's nose"],
    "bee": ["common", random.randint(0, length), "pet starts making honey"],
    "camel": ["rare", random.randint(0, length), "pet starts holding grudges for people who hurt them"],
    "bull": ["rare", random.randint(0, length), "pet starts ramming into red things"],
    "racoon": ["rare", random.randint(0, length), "pet starts eating your food"],
    "wolf": ["common", random.randint(0, length), "pet starts howling"],
    "cow": ["common", random.randint(0, length), "pet starts mooing"],
    "elephant": ["common", random.randint(0, length), "pet starts taking a mud path"],
    "peacock": ["holy fish rare", random.randint(0, length), "pet starts showing it's feathers elegantly"],
    "fox": ["rare", random.randint(0, length), "pet starts making a brand new noise no one has ever heard before"],
    "rooster": ["rare", random.randint(0, length), "pet starts waking up people in the morning"],
    "bear": ["rare", random.randint(0, length), "pet starts attacking people"],
    "tiger": ["very rare", random.randint(0, length), "pet starts playing in water"],
    "duck": ["common", random.randint(0, length), "pet starts floating in a pond"],
    "human": ["legendary", random.randint(0, length), "pet starts destroying for no reason"],
    "kangroo": ["rare", random.randint(0, length), "pet starts speaking in an australian accent"],
    "swan": ["rare", random.randint(0, length), "pet starts catching fish"],
    "goose": ["rare", random.randint(0, length), "pet starts picking up a knife"],
    "hoopoes": ["very rare", random.randint(0, length), "pet starts looking badass"],
    "seal": ["rare", random.randint(0, length), "pet starts diving down into the depths of the ocean"],
    "polar bear": ["rare", random.randint(0, length), "pet starts attacking seals"],
    "chicken": ["commom", random.randint(0, length), "pet starts laying eggs"],
    "squirrel": ["common", random.randint(0, length), "pet starts shoving nuts in their mouth"],
    "hedgehog": ["rare", random.randint(0, length), "pet starts running fast"],
    "moose": ["rare", random.randint(0, length), "pet starts saying sorry and drinking maple syrup"],
    "ostrich": ["rare", random.randint(0, length), "pet starts ducking their head in the dirt"],
    "bison": ["rare", random.randint(0, length), "pet starts saying bye to his son"], # the joke came from ahmed don't blame me
    "wolverine": ["very rare", random.randint(0, length), "pet starts getting mad at deadpool"],
    "ant eater": ["rare", random.randint(0, length), "pet starts eating ants"],
    "comodo dragon": ["very rare", random.randint(0, length), "pet starts licking the air"],
    "orca": ["holy fish rare", random.randint(0, length), "pet starts being a bully"],
    "zebra": ["common", random.randint(0, length), "pet starts sticking to other zebras"],
    "turkey": ["rare", random.randint(0, length), "pet starts getting stuffed in thanksgiving"],
    "llama": ["rare", random.randint(0, length), "pet starts spitting on you"],
    "peppa": ["legendary", random.randint(0, length), "pet starts 55555555"],
    "octupus-chan": ["legendary", random.randint(0, length), "pet starts approaches an anime girl"],
    "rhino": ["rare", random.randint(0, length), "pet starts getting sun-burnt"],
    "pegasus": ["legendary", random.randint(0, length), "pet starts flying"],
}

def getDetails(spec, list_choice):
    if list_choice == "rarity":
        print(AnimalsToDetails[spec][0])
    if list_choice == "ability":
        print(AnimalsToDetails[spec][1])


# just to list out how many pets of each rarites are available
def num_of_rarities():
    common_count = 0
    rare_count = 0
    very_rare_count = 0
    holy_fish_rare_count = 0
    legendary_count = 0

    for key in AnimalsToDetails: 
        if "common" in AnimalsToDetails[key]:
            common_count += 1
        if "rare" in AnimalsToDetails[key]:
            rare_count += 1
        if "very rare" in AnimalsToDetails[key]:
            very_rare_count += 1
        if "holy fish rare" in AnimalsToDetails[key]:
            holy_fish_rare_count += 1
        if "legendary" in AnimalsToDetails[key]:
            legendary_count += 1



    print(f"common: {common_count}")
    print(f"rare: {rare_count}")
    print(f"very rare: {very_rare_count}")
    print(f"holy fish rare: {holy_fish_rare_count}")
    print(f"legendary: {legendary_count}")


num_of_rarities() 


