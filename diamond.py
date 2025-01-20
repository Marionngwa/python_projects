print('''
            .
             _\____
            |_===__`.        ==/
            \/  '---"\ _ _ _ _/
      ______/_______/_|_|_|_|_|
    _|--------------------==."
     \____________________.'   ''')

print("🌊 Welcome to Beri Voyage! Your mission is to find the missing diamond hidden overseas.")

choice1 = input("Which city will you like to sail to first? 'Dubai', 'Italy', or 'Greece'? ").lower()

if choice1 == "dubai":
    print("🏜️ You arrive in Dubai, a city of towering skyscrapers and hidden treasures.")
    swim_or_wait = input("Do you want to swim through the lagoon or wait for the tide? "
                         "\nType 'swim' to swim or 'wait' to wait: ").lower()
    if swim_or_wait == "wait":
        print("⏳ You patiently wait as the tide reveals a hidden cave entrance!")
        door = input("Inside the cave, you see three glowing doors. Which door will you choose? "
                     "'Red', 'Blue', or 'Yellow'? ").lower()
        if door == "yellow":
            print("💎 Congratulations! You've found the diamond. You win!")
        elif door == "red":
            print("🔥 The red door bursts into flames! Game over.")
        elif door == "blue":
            print("❄️ The blue door traps you in ice. Game over.")
        else:
            print("🚪 You chose a door that doesn't exist. Game over. 😒")
    else:
        print("🐊 Oh no! A crocodile attacks you in the water. Game over.")
elif choice1 == "italy":
    print("🍝 You dock in Italy and enjoy some pasta, but the diamond isn't here. Game over.")
elif choice1 == "greece":
    print("🏛️ You explore ancient ruins in Greece, but a trapdoor sends you falling. Game over.")
else:
    print("❌ You didn't choose a valid city. Game over.")
