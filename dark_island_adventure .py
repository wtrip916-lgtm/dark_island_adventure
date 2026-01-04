import time
import random
import os

# ---------- UTIL ----------
def slow(text):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.02)
    print()

def line():
    print("-" * 40)

# ---------- CHARACTER SETUP ----------
slow("🌑 DARK ISLAND ADVENTURE – ULTRA EDITION 🌑\n")
name = input("Enter your name: ")

slow("\nChoose your class:")
slow("1. Warrior (High Health)")
slow("2. Mage (High Magic)")
slow("3. Rogue (Critical Hits)")

cls = input("Choose 1/2/3: ")

if cls == "1":
    player_class = "Warrior"
    health = 150
    attack = 25
    magic = 10
    crit = 10
elif cls == "2":
    player_class = "Mage"
    health = 110
    attack = 20
    magic = 30
    crit = 10
else:
    player_class = "Rogue"
    health = 120
    attack = 22
    magic = 15
    crit = 25

level = 1
xp = 0
coins = 20
inventory = ["Potion"]
day = 1

slow(f"\n{name} the {player_class}, your journey begins...\n")

# ---------- LEVEL UP ----------
def level_up():
    global level, xp, health, attack, magic
    if xp >= level * 60:
        level += 1
        xp = 0
        health += 20
        attack += 5
        magic += 5
        slow(f"\n⬆️ LEVEL UP! You are now Level {level}")

# ---------- INVENTORY ----------
def show_inventory():
    slow("\n🎒 Inventory:")
    if inventory:
        for item in inventory:
            slow(f"- {item}")
    else:
        slow("Empty")

# ---------- FIGHT SYSTEM ----------
def fight(enemy):
    global health, xp, coins, magic

    enemy_hp = enemy["hp"]
    enemy_attack = enemy["atk"]

    slow(f"\n⚔️ {enemy['name']} appears!")

    while enemy_hp > 0 and health > 0:
        slow(f"\nYour HP:{health} | Magic:{magic} | Enemy HP:{enemy_hp}")
        slow("1.Attack  2.Skill  3.Potion  4.Inventory")
        c = input("Choose: ")

        if c == "1":
            dmg = random.randint(10, attack)
            if random.randint(1, 100) <= crit:
                dmg *= 2
                slow("💥 CRITICAL HIT!")
            enemy_hp -= dmg
            slow(f"You dealt {dmg} damage")

        elif c == "2" and magic >= 5:
            magic -= 5
            dmg = random.randint(25, 40)
            enemy_hp -= dmg
            slow(f"🔥 Skill attack dealt {dmg}")

        elif c == "3" and "Potion" in inventory:
            health += 35
            inventory.remove("Potion")
            slow("🧪 Potion used +35 HP")

        elif c == "4":
            show_inventory()
            continue
        else:
            slow("Invalid move!")

        if enemy_hp > 0:
            ed = random.randint(5, enemy_attack)
            health -= ed
            slow(f"Enemy hit you for {ed}")

    if health <= 0:
        slow("\n❌ You died... GAME OVER")
        exit()

    slow(f"\n✅ {enemy['name']} defeated!")
    xp += enemy["xp"]
    coins += enemy["coins"]
    slow(f"+{enemy['xp']} XP | +{enemy['coins']} Coins")
    level_up()

# ---------- ENEMIES ----------
forest_enemy = {"name": "Forest Beast", "hp": 70, "atk": 15, "xp": 30, "coins": 10}
cave_enemy = {"name": "Cave Stalker", "hp": 90, "atk": 18, "xp": 40, "coins": 15}
boss_enemy = {"name": "👹 ISLAND KING 👹", "hp": 100, "atk": 10, "xp": 80, "coins": 45}

# ---------- MAIN GAME LOOP ----------
while True:
    line()
    slow(f"🌞 Day {day}")
    slow("🗺️ Choose Location:")
    slow("1. Forest")
    slow("2. Cave")
    slow("3. Shop")
    slow("4. Rest (Next Day)")
    slow("5. Final Boss")

    choice = input("Go to: ")

    if choice == "1":
        fight(forest_enemy)

    elif choice == "2":
        fight(cave_enemy)

    elif choice == "3":
        slow(f"\n🏪 Coins: {coins}")
        slow("1. Buy Potion (10)")
        slow("2. Buy Skill Book (20)")
        s = input("Choose: ")

        if s == "1" and coins >= 10:
            inventory.append("Potion")
            coins -= 10
            slow("Potion bought")
        elif s == "2" and coins >= 20:
            magic += 10
            coins -= 20
            slow("Skill improved!")
        else:
            slow("Not enough coins")

    elif choice == "4":
        day += 1
        health += 20
        magic += 10
        slow("\n😴 You rested and recovered")
        slow("+20 HP | +10 Magic")

    elif choice == "5":
        fight(boss_enemy)
        slow("\n🚁 You escaped the island!")
        slow("🏆 TRUE ENDING UNLOCKED 🏆")
        break

    else:
        slow("Invalid choice")

# ---------- FINAL STATS ----------
line()
slow("📊 FINAL STATS")
slow(f"Name: {name}")
slow(f"Class: {player_class}")
slow(f"Level: {level}")
slow(f"Health: {health}")
slow(f"Attack: {attack}")
slow(f"Magic: {magic}")
slow(f"Coins: {coins}")
slow(f"Inventory: {inventory}")
# ================== CHAPTER 2 ==================
slow("\n📖 CHAPTER 2: THE LOST TRUTH\n")
slow("The helicopter takes you away from the island...")
slow("But your heart feels heavy.")
slow("You look down and see the island burning in darkness.\n")

slow("Days later...")
slow("You wake up in a quiet hospital room 🏥")
slow("Your body survived, but your mind is not at peace.\n")

slow("A man enters the room.")
slow("\"You were not supposed to escape,\" he says softly.")
slow("\"That island was an experiment...\"\n")

# Choice 1
slow("💔 Truth is revealed:")
slow("You were sent to the island on purpose.")
slow("Many others like you never returned.\n")

slow("1. Get angry and shout")
slow("2. Stay silent and listen")

c2_choice1 = input("Choose 1 or 2: ")

if c2_choice1 == "1":
    slow("\nYou shout in anger.")
    slow("Your heart rate increases.")
    health -= 20
    slow("Pain returns to your body.")
else:
    slow("\nYou stay silent.")
    slow("The truth hurts more than pain.")

slow("\nThe man continues...")
slow("\"Your survival changed everything.\"")
slow("\"The island will be destroyed, but the souls lost there...\"\n")

# Choice 2
slow("You feel guilt.")
slow("1. Accept the guilt")
slow("2. Deny everything")

c2_choice2 = input("Choose 1 or 2: ")

if c2_choice2 == "1":
    slow("\nTears roll down your face.")
    slow("You remember the enemies you killed.")
    slow("They were victims too.")
    magic += 10
    slow("Your pain turned into wisdom (+10 Magic)")
else:
    slow("\nYou turn away.")
    slow("But the memories follow you.")

# Ending
slow("\n🌧️ FINAL SCENE")
slow("That night, rain falls outside the hospital window.")
slow("You hold the island map in your hand.")
slow("Freedom has a cost.\n")

slow("🏆 SAD ENDING UNLOCKED: 'THE SURVIVOR'S GUILT' 🏆")

# Final Chapter 2 stats
slow("\n📊 CHAPTER 2 STATS")
slow(f"Health: {health}")
slow(f"Magic: {magic}")
slow(f"Level: {level}")
# ================== CHAPTER 3 ==================
slow("\n📖 CHAPTER 3: ASHES OF REVENGE\n")

slow("Weeks pass after the hospital incident...")
slow("You cannot sleep. Faces from the island haunt you.")
slow("You discover secret files about the experiment.\n")

slow("The truth is clear:")
slow("A private group ran the island to test human survival.")
slow("They are still active.\n")

slow("You make a choice.\n")
slow("1. Train in secret and hunt them down")
slow("2. Try to expose them legally")

c3_choice1 = input("Choose 1 or 2: ")

if c3_choice1 == "1":
    slow("\nYou disappear from public life.")
    slow("Months of brutal training follow.")
    attack += 15
    health += 20
    slow("Your body hardens. (+15 Attack, +20 Health)")
else:
    slow("\nYou try to expose them.")
    slow("Your evidence is erased.")
    slow("They notice you.")
    health -= 15
    slow("You are attacked in the shadows (-15 Health)")

slow("\nA location is revealed: an offshore facility 🏢")
slow("You infiltrate it at night.\n")

# MINI-BOSS FIGHT
slow("⚔️ MINI-BOSS: EXPERIMENT ENFORCER ⚔️")
mini_boss = {"name": "Enforcer", "hp": 120, "atk": 22, "xp": 50, "coins": 30}
fight(mini_boss)

slow("\nInside the facility, you find prisoners.")
slow("They recognize you.")
slow("\"You escaped the island... help us,\" they beg.\n")

slow("1. Free the prisoners")
slow("2. Ignore them and go for the leader")

c3_choice2 = input("Choose 1 or 2: ")

if c3_choice2 == "1":
    slow("\nYou free them.")
    slow("Alarms blare, but lives are saved.")
    magic += 10
    slow("Your rage turns into purpose (+10 Magic)")
else:
    slow("\nYou walk past them.")
    slow("Your goal is clear, but your heart grows colder.")
    attack += 10
    slow("Pure rage fuels you (+10 Attack)")

# FINAL REVENGE BOSS
slow("\n👹 FINAL REVENGE BOSS: THE ARCHITECT 👹")
revenge_boss = {"name": "The Architect", "hp": 220, "atk": 30, "xp": 120, "coins": 60}
fight(revenge_boss)

# ENDINGS
slow("\n🔥 FINAL DECISION")
slow("The Architect is defeated.")
slow("1. End him")
slow("2. Arrest and expose him")

c3_final = input("Choose 1 or 2: ")

if c3_final == "1":
    slow("\nYou end his life.")
    slow("The experiment dies with him.")
    slow("Peace never fully returns.")
    slow("🏆 REVENGE ENDING UNLOCKED: 'BLOOD PAID IN FULL' 🏆")
else:
    slow("\nYou spare him.")
    slow("The world finally learns the truth.")
    slow("Justice replaces revenge.")
    slow("🏆 JUSTICE ENDING UNLOCKED: 'TRUTH OVER HATE' 🏆")

# CHAPTER 3 STATS
slow("\n📊 CHAPTER 3 STATS")
slow(f"Health: {health}")
slow(f"Attack: {attack}")
slow(f"Magic: {magic}")
slow(f"Level: {level}")
# ================== FINAL ENDING ==================
slow("\n🌅 FINAL MOMENT\n")
slow("Everything is finally over.")
slow("You stand alone, thinking about the journey.\n")

slow("Choose your final path:")
slow("1. Let go of the past and live peacefully")
slow("2. Stay trapped in memories of pain")

final_choice = input("Choose 1 or 2: ")

if final_choice == "1":
    slow("\nYou take a deep breath.")
    slow("You decide to forgive yourself.")
    slow("The pain slowly fades away.")
    slow("You help others who suffered like you.")
    slow("🌈 HAPPY ENDING UNLOCKED: 'A NEW BEGINNING' 🌈")
else:
    slow("\nYou sit alone in silence.")
    slow("Even after revenge, peace never came.")
    slow("The memories never leave you.")
    slow("Rain falls as the screen fades to black.")
    slow("🌧️ SAD ENDING UNLOCKED: 'SCARS THAT REMAIN' 🌧️")

# ================== GAME COMPLETE ==================
slow("\n🏁 GAME COMPLETED 🏁")
slow("Thank you for playing DARK ISLAND ADVENTURE")
slow("Your choices shaped the story.")