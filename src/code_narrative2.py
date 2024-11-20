# ChatGPT Code

# === THE DEFENSE BEGINS ===
# Three warriors stand against waves of enemies to protect their village.
# Each wave tests their courage, skills, and unity as they battle together.

# Step 1: Define the warriors and their traits
class Warrior:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

# Meet the defenders
defenders = [
    Warrior("Aric", "Mastery of the sword"),
    Warrior("Thalia", "Unerring archery"),
    Warrior("Kael", "Mystical barrier creation"),
]

# Step 2: The enemy waves
# Each wave represents a more formidable challenge.
enemy_waves = {
    "Wave 1": "A band of marauding raiders",
    "Wave 2": "A charging beast of steel and fury",
    "Wave 3": "A shadowy figure controlling the storm",
}

# Step 3: The defenders face the waves
def fight_wave(wave, warrior):
    print(f"{warrior.name} uses their skill ({warrior.skill}) to confront '{wave}'.")

# Step 4: Begin the defense
print("=== THE BATTLE BEGINS ===")
for wave, enemy in enemy_waves.items():
    # Each warrior takes a turn leading the defense
    lead = defenders.pop(0)  # Rotate leader
    fight_wave(enemy, lead)
    defenders.append(lead)  # Leader returns to the back of the line

# Step 5: The aftermath
# The village is saved, but at great cost.
print("\n=== THE VILLAGE STANDS ===")
victory_message = """
Through their bravery and sacrifice, the village is safe for another day. 
The warriors stand together, battered but unbroken, as the sun rises over the horizon.
"""
print(victory_message.strip())

# Step 6: Reflection on the conflict
# The warriors reflect on the strength they drew from one another.
print("\n=== REFLECTION ===")
for warrior in defenders:
    print(f"{warrior.name} says, 'Without {warrior.skill}, the village might have fallen.'")

# === THE BATTLE ENDS ===

