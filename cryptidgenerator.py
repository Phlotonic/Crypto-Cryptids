import random
import uuid
from cryptidnamelibrary import prefixes, suffixes

# Expansive trait library for crypto cryptids
traits_library = {
    "biome": ["forest", "mountain", "desert", "arctic", "swamp", "ocean"],
    "type": ["grass", "fire", "water", "electric", "rock", "ground", "flying", "poison", "bug", "normal", "ghost", "psychic", "dragon", "dark", "steel", "fairy", "space", "fungal", "hominid"],
    "social": ["solitary", "pack", "family"],
    "activity": ["diurnal", "nocturnal", "crepuscular"],
    "rarity": ["common", "uncommon", "rare", "epic", "legendary"],
    "size": ["tiny", "small", "medium", "large", "giant"],
    # Stats are now generated based on type and biome
    # ... (removed the "stats" key from traits_library)
}

def generate_cryptid():
    """Generates a unique crypto cryptid with cohesive name, stats, and description."""

    cryptid = {}
    cryptid["id"] = uuid.uuid4().hex

 # Generate all traits
    for trait, values in traits_library.items():
        if trait == "type":  # Handle multiple types
            if random.random() < 1/3:
                cryptid["type"] = random.sample(values, 2)
            else:
                cryptid["type"] = [random.choice(values)]
        else:
            cryptid[trait] = random.choice(values)

    # Generate type(s)
    if random.random() < 1/3:  # 1/3 chance of having two types
        cryptid["type"] = random.sample(traits_library["type"], 2)
    else:
        cryptid["type"] = [random.choice(traits_library["type"])]  # Single type as a list
    
    # Generate biome
    cryptid["biome"] = random.choice(traits_library["biome"])

    # Generate name based on type and biome
    cryptid["name"] = generate_name(cryptid)

    # Generate stats based on type and biome
    cryptid["stats"] = generate_stats(cryptid)

    # Generate description based on all generated traits
    cryptid["description"] = generate_description(cryptid)

    cryptid["species_name"] = generate_species_name(cryptid)

    return cryptid

def generate_name(cryptid):
    """Generates a name based on the cryptid's type(s) and biome."""

    prefix = random.choice(prefixes.get(cryptid["biome"], ["Cryp-", "Xeno-", "Mytho-"]))

    # Handle multiple types in the name
    if len(cryptid["type"]) == 2:
        suffix1 = random.choice(suffixes.get(cryptid["type"][0], ["fang"]))
        suffix2 = random.choice(suffixes.get(cryptid["type"][1], ["wing"]))
        suffix = f"{suffix1}-{suffix2}"
    else:
        suffix = random.choice(suffixes.get(cryptid["type"][0], ["fang", "wing", "maw"]))

    return f"{prefix}{suffix}"


def generate_stats(cryptid):
    """Generates stats based on the cryptid's type(s) and biome."""

    base_stats = {
        "grass": {"hp": 70, "attack": 70, "defense": 70, "speed": 70},
        "fire": {"hp": 65, "attack": 90, "defense": 60, "speed": 85},
        "water": {"hp": 75, "attack": 75, "defense": 80, "speed": 60},
        # ... (add base stats for other types)
    }
    biome_modifiers = {
        "forest": {"hp": 1.1, "attack": 1.0, "defense": 1.1, "speed": 0.9},
        "mountain": {"hp": 1.2, "attack": 0.9, "defense": 1.2, "speed": 0.8},
        "desert": {"hp": 0.9, "attack": 1.1, "defense": 0.9, "speed": 1.1},
        # ... (add biome modifiers for other biomes)
    }

    stats = {"hp": 0, "attack": 0, "defense": 0, "speed": 0}
    for t in cryptid["type"]:  # Calculate stats for each type
        type_stats = base_stats.get(t, {"hp": 70, "attack": 70, "defense": 70, "speed": 70}).copy()
        for stat, value in type_stats.items():
            stats[stat] += value

    # Average the stats if there are two types
    if len(cryptid["type"]) == 2:
        for stat in stats:
            stats[stat] = int(stats[stat] / 2)

    # Apply biome modifiers
    for stat, modifier in biome_modifiers.get(cryptid["biome"], {}).items():
        stats[stat] = int(stats[stat] * modifier)

    # Add some randomness to the stats
    for stat in stats:
        stats[stat] += random.randint(-10, 10)

    return stats

def generate_species_name(cryptid):
    """Generates a species name like 'The Electric Mouse Cryptid'."""

    species_names = {
        "grass": ["Plant", "Vine", "Flower", "Tree", "Fern"],
        "fire": ["Salamander", "Phoenix", "Dragon", "Wyvern", "Drake"],
        "water": ["Fish", "Squid", "Crab", "Serpent", "Whale"],
        "electric": ["Rodent", "Bird", "Eel", "Bug", "Elemental"],
        "rock": ["Golem", "Gargoyle", "Elemental", "Giant", "Dinosaur"],
        "ground": ["Mole", "Snake", "Worm", "Badger", "Elemental"],
        "flying": ["Bird", "Bat", "Wyvern", "Insect", "Dragon"],
        "poison": ["Snake", "Spider", "Insect", "Frog", "Slime"],
        "bug": ["Ant", "Bee", "Beetle", "Mantis", "Spider"],
        "normal": ["Mammal", "Bird", "Reptile", "Fish", "Insect"],
        "ghost": ["Spirit", "Phantom", "Wraith", "Ghoul", "Specter"],
        "psychic": ["Humanoid", "Feline", "Bird", "Cephalopod", "Elemental"],
        "dragon": ["Dragon", "Wyvern", "Drake", "Serpent", "Wyrm"],
        "dark": ["Bat", "Wolf", "Raven", "Shadow", "Wraith"],
        "steel": ["Golem", "Robot", "Machine", "Construct", "Elemental"],
        "fairy": ["Pixie", "Sprite", "Nymph", "Fae", "Butterfly"],
        "space": ["Alien", "Star", "Comet", "Nebula", "Entity"],
        "fungal": ["Mushroom", "Mold", "Fungus", "Spore", "Mycelium"],
        "hominid": ["Ape", "Humanoid", "Giant", "Shaman", "Warrior"],
    }

    # Handle multiple types
    if len(cryptid["type"]) == 2:
        species_name1 = random.choice(species_names.get(cryptid["type"][0], ["Cryptid"]))
        species_name2 = random.choice(species_names.get(cryptid["type"][1], ["Cryptid"]))
        species_name = f"The {species_name1}-{species_name2} Cryptid"
    else:
        species_name = f"The {random.choice(species_names.get(cryptid['type'][0], ['Cryptid']))} Cryptid"

    return species_name

def generate_description(cryptid):
    """Generates a cohesive description that aligns with the cryptid's traits,
    including its name, stats, and type(s)."""

    descriptions = {
        "biome": {
            "forest": [
                f"Often mistaken for Bigfoot, this {cryptid['type']} cryptid lurks in the dense forests, leaving behind only large footprints and eerie howls.",
                f"A master of camouflage, this {cryptid['type']} cryptid blends seamlessly with the forest undergrowth, its glowing eyes the only indication of its presence.",
                f"This elusive {cryptid['type']} cryptid dwells in the heart of old-growth forests, its presence often heralded by the rustling of leaves and snapping of twigs.",
                f"Legends speak of a creature that protects the forest, a guardian spirit with the power to control nature. This {cryptid['type']} cryptid is believed to be the embodiment of that legend."
            ],
            "mountain": [
                f"Similar to the Yeti, this {cryptid['type']} cryptid is adapted to the harsh mountain environment, its thick fur protecting it from the cold and its powerful limbs allowing it to navigate treacherous terrain.",
                f"Legends speak of a creature that roams the high peaks, leaving behind unidentifiable tracks in the snow. This {cryptid['type']} cryptid is believed to be the source of these tales.",
                f"This solitary {cryptid['type']} cryptid makes its home in the high altitudes, its keen eyesight allowing it to spot prey from miles away.",
                f"Perched atop the highest peaks, this majestic {cryptid['type']} cryptid surveys its domain, its powerful wings carrying it effortlessly through the thin mountain air."
            ],
            "desert": [
                f"This {cryptid['type']} cryptid is a rare sight, emerging from its underground burrows only during the cooler hours of the day to hunt for prey.",
                f"With its ability to withstand extreme heat and lack of water, this {cryptid['type']} cryptid is a true survivor of the harsh desert environment.",
                f"Camouflaged against the sand and rock, this {cryptid['type']} cryptid is a master of stealth, ambushing its prey with lightning speed.",
                f"This resilient {cryptid['type']} cryptid wanders the vast deserts, its tough hide protecting it from the sun and sand."
            ],
            "arctic": [
                f"A solitary predator, this {cryptid['type']} cryptid roams the frozen wastes, its white fur providing perfect camouflage against the snow and ice.",
                f"Rarely seen by humans, this {cryptid['type']} cryptid is said to possess incredible strength and endurance, allowing it to survive in the harshest conditions on Earth.",
                f"This elusive {cryptid['type']} cryptid is a master of survival in the frozen north, its thick blubber and specialized blood allowing it to thrive in sub-zero temperatures.",
                f"Legends speak of a creature that guards the arctic, a spirit of the ice with the power to control blizzards and ice storms. This {cryptid['type']} cryptid is believed to be that guardian."
            ],
            "swamp": [
                f"Legends of swamp monsters come to life with this {cryptid['type']} cryptid, its murky form emerging from the depths to snatch unsuspecting prey.",
                f"This {cryptid['type']} cryptid is perfectly adapted to the swampy environment, its webbed feet and powerful tail allowing it to navigate the murky waters with ease.",
                f"This amphibious {cryptid['type']} cryptid lurks in the murky swamps, its glowing eyes piercing the darkness.",
                f"A master of disguise, this {cryptid['type']} cryptid blends seamlessly with the swamp vegetation, its presence betrayed only by the ripples in the water."
            ],
            "ocean": [
                f"Said to be the inspiration for tales of sea serpents, this massive {cryptid['type']} cryptid lurks in the deepest parts of the ocean, its glowing eyes piercing the darkness.",
                f"This elusive {cryptid['type']} cryptid is rarely seen, but its haunting calls can sometimes be heard echoing across the waves.",
                f"This majestic {cryptid['type']} cryptid glides effortlessly through the ocean depths, its bioluminescent markings illuminating the darkness.",
                f"A creature of myth and legend, this colossal {cryptid['type']} cryptid is said to rule the oceans, its power unmatched by any other creature."
            ],
        },
        "type": {
            "grass": [
                f"This cryptid draws its power from nature, harnessing the energy of plants and trees.",
                f"Its body is covered in lush vegetation, providing natural camouflage and a connection to the earth.",
                f"This cryptid is known for its healing abilities and its affinity for nature."
            ],
            "fire": [
                f"This fiery cryptid is known for its explosive temper and powerful flames.",
                f"Its body burns with an intense heat, making it a formidable opponent in battle.",
                f"This cryptid is a master of fire, able to conjure flames and control them with ease."
            ],
            "water": [
                f"This aquatic cryptid is a graceful swimmer, often found near rivers, lakes, or oceans.",
                f"Its ability to control water makes it a master of its domain.",
                f"This cryptid is known for its calming presence and its connection to the water element."
            ],
            "electric": [
                f"This electrifying cryptid crackles with energy, its body charged with raw power.",
                f"Its speed and agility are unmatched, allowing it to strike with lightning speed.",
                f"This cryptid is a master of electricity, able to generate powerful shocks and control electrical currents."
            ],
            "rock": [
                f"This sturdy cryptid is as tough as the mountains it inhabits, its rocky hide providing impenetrable defense.",
                f"Its strength and endurance are unmatched, making it a formidable opponent in any battle.",
                f"This cryptid is known for its unwavering determination and its connection to the earth."
            ],
            "ground": [
                f"This cryptid is deeply connected to the earth, drawing strength and stability from the ground beneath its feet.",
                f"Its powerful limbs can tunnel through solid rock and create tremors with a single stomp.",
                f"This cryptid is known for its resilience and its ability to withstand even the most powerful attacks."
            ],
            "flying": [
                f"This graceful cryptid soars through the skies with effortless ease, its wings carrying it to great heights.",
                f"Its keen eyesight allows it to spot prey from miles away, and its sharp talons make it a formidable predator.",
                f"This cryptid is known for its freedom and its connection to the sky."
            ],
            "poison": [
                f"This venomous cryptid secretes toxins from its skin, its touch capable of inflicting debilitating pain.",
                f"Its vibrant colors serve as a warning to potential predators, signaling its deadly nature.",
                f"This cryptid is known for its cunning and its ability to adapt to any environment."
            ],
            "bug": [
                f"This adaptable cryptid thrives in a variety of environments, its exoskeleton providing protection and camouflage.",
                f"Its swift movements and sharp senses make it a skilled hunter, able to capture even the most elusive prey.",
                f"This cryptid is known for its resilience and its ability to work together in swarms."
            ],
            "normal": [
                f"This adaptable cryptid thrives in a variety of environments, its versatility allowing it to adapt to any situation.",
                f"Its balanced stats make it a well-rounded fighter, capable of both offense and defense.",
                f"This cryptid is known for its resilience and its ability to learn a wide range of moves."
            ],
            "ghost": [
                f"This ethereal cryptid exists between the realms of the living and the dead, its ghostly form phasing through walls and objects.",
                f"Its chilling presence can drain the life force of its opponents, leaving them weakened and vulnerable.",
                f"This cryptid is known for its mystery and its connection to the spirit world."
            ],
            "psychic": [
                f"This intelligent cryptid possesses powerful psychic abilities, capable of manipulating objects with its mind and reading the thoughts of others.",
                f"Its heightened senses allow it to perceive the world in ways that others cannot, giving it an edge in battle.",
                f"This cryptid is known for its wisdom and its connection to the mind."
            ],
            "dragon": [
                f"This majestic cryptid is a creature of myth and legend, its powerful wings carrying it across the skies.",
                f"Its fiery breath and sharp claws make it a fearsome opponent, capable of devastating attacks.",
                f"This cryptid is known for its pride and its connection to ancient powers."
            ],
            "dark": [
                f"This shadowy cryptid lurks in the darkness, its presence shrouded in mystery and fear.",
                f"Its cunning and stealth make it a formidable predator, able to strike from the shadows without warning.",
                f"This cryptid is known for its ruthlessness and its ability to exploit its opponents' weaknesses."
            ],
            "steel": [
                f"This resilient cryptid is protected by a tough metallic hide, its defenses nearly impenetrable.",
                f"Its strength and endurance are unmatched, allowing it to withstand even the most powerful attacks.",
                f"This cryptid is known for its unwavering resolve and its connection to technology."
            ],
            "fairy": [
                f"This enchanting cryptid possesses a magical aura, its presence bringing joy and wonder to those around it.",
                f"Its playful nature and mischievous spirit make it a beloved companion, but its powers should not be underestimated.",
                f"This cryptid is known for its kindness and its connection to the fairy realm."
            ],
            "space": [
                f"This enigmatic cryptid is believed to have originated from beyond the stars, its body composed of celestial energy and cosmic dust.",
                f"Its powers are shrouded in mystery, capable of manipulating gravity, bending light, and traversing the vast expanse of space.",
                f"This cryptid is known for its otherworldly presence and its connection to the cosmos."
            ],
            "fungal": [
                f"This bizarre cryptid is a living embodiment of the fungal kingdom, its body composed of interwoven mycelial networks.",
                f"Its spores can induce hallucinations, manipulate the growth of plants, and even decompose organic matter with astonishing speed.",
                f"This cryptid is known for its adaptability and its connection to the natural world."
            ],
            "hominid": [
                f"This intelligent cryptid walks upright, displaying a remarkable level of sentience and social complexity.",
                f"Its strength, cunning, and ability to use tools make it a formidable predator and a master of survival.",
                f"This cryptid is known for its resourcefulness and its connection to the evolutionary history of humankind."
            ]
        },
        "stats": {
            "hp": {
                "high": [
                    "It possesses incredible resilience and can endure significant damage.",
                    "Its robust constitution makes it a formidable opponent."
                ],
                "low": [
                    "It is quite fragile and susceptible to injury.",
                    "Its delicate frame requires caution in battles."
                ]
            },
            "attack": {
                "high": [
                    "Its powerful attacks can cleave through even the toughest defenses.",
                    "It is known for its ferocious strikes and devastating blows."
                ],
                "low": [
                    "Its attacks are rather weak and may struggle to inflict significant damage.",
                    "It relies more on strategy and cunning than brute force."
                ]
            },
            "defense": {
                "high": [
                    "Its impenetrable defenses can withstand even the most powerful attacks.",
                    "It is renowned for its resilience and ability to shrug off damage."
                ],
                "low": [
                    "Its defenses are quite weak, leaving it vulnerable to attacks.",
                    "It must rely on agility and evasion to avoid harm."
                ]
            },
            "speed": {
                "high": [
                    "Its blinding speed allows it to outmaneuver and strike before its opponents can react.",
                    "It is known for its swift movements and lightning-fast reflexes."
                ],
                "low": [
                    "It is quite slow and may struggle to keep up with faster opponents.",
                    "Its sluggish movements make it a predictable target."
                ]
            }
        }
    }



    description_parts = []  # List to store description parts

    # Biome-specific description
    if cryptid["biome"] in descriptions["biome"]:
        description_parts.append(random.choice(descriptions["biome"][cryptid["biome"]]))

    # Type-specific description
    type_descriptions = []
    for t in cryptid["type"]:
        if t in descriptions["type"]:
            type_descriptions.append(random.choice(descriptions["type"][t]))
    description_parts.append(" ".join(type_descriptions))

    # Add descriptions based on other traits
    description_parts.append(f"This {cryptid['size']} cryptid is {cryptid['rarity']} and is most active during the {cryptid['activity']} hours.")
    if cryptid['social'] == 'solitary':
        description_parts.append("It prefers to live alone.")
    elif cryptid['social'] == 'pack':
        description_parts.append("It lives in packs and hunts cooperatively.")
    elif cryptid['social'] == 'family':
        description_parts.append("It forms strong family bonds and protects its young fiercely.")

    # Find the highest and lowest stat values
    stats = cryptid["stats"]
    highest_stat = max(stats, key=stats.get)
    lowest_stat = min(stats, key=stats.get)

    # Add descriptions based on highest and lowest stats, referencing the name if possible
    description_parts.append(f"The {cryptid['name']} is known for its {highest_stat},")
    description_parts.append(random.choice(descriptions["stats"][highest_stat]["high"]) + ".")
    description_parts.append(f"However, its {lowest_stat} is its weakness,")
    description_parts.append(random.choice(descriptions["stats"][lowest_stat]["low"]) + ".")

    # Join the description parts with improved flow
    description = " ".join(description_parts)
    description = description.replace(", and", ",")  # Remove unnecessary "and" after commas
    description = description.replace(", but", ",")  # Remove unnecessary "but" after commas

    return description

def main():
    """Generates a unique crypto cryptid and displays its information."""

    print("Welcome to the Crypto Cryptids Generator!")

    cryptid = generate_cryptid()

    print("Generated Cryptid:")
    print(f"Name: {cryptid['name']}")
    print(f"Species: {cryptid['species_name']}")
    print(f"Description: {cryptid['description']}")
    print(f"Stats: {cryptid['stats']}")
    print(f"ID: {cryptid['id']}")

if __name__ == "__main__":
    main()