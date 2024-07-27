# This imports The time library.
import time
# This imports The random library.
import random

# This creates the total score variable, and stets it to 0.
global Total_score
Total_score = 0
# This sets a (Welcome_massages) list item.
welcome_massage1 = (
    "Welcome, wanderer, to the depths of the Whispering Woods. \n"
    "The trees around you seem to whisper secrets from an ancient past, "
    "\nand the path ahead is shrouded in mystery. Your journey begins here,"
    "\n where every step could lead to adventure or peril.\n"
    "Are you ready to unravel the secrets of the forest and find your way out?"
)
# This sets a (Welcome_massages) list item.
welcome_massage2 = (
    "You've entered the enigmatic realm of the Lost Woods, "
    "\nwhere shadows play tricks on your mind and the air is thick \n"
    "with mystery. Every corner hides a story,"
    "\n every rustle of leaves hints at hidden dangers. Trust your \n"
    "instincts and be prepared for anything. "
    "\nWelcome to the adventure that awaits you."
)
# This sets a (Welcome_massages) list item.
welcome_massage3 = (
    "Hello, brave explorer! Welcome to the Lost in the Woods game,\n"
    "where your courage and wits will be your greatest allies."
    "\nThe forest may seem daunting, but fear not! With each step, "
    "\nyou'll discover new paths, uncover hidden treasures,\n"
    "and face exciting challenges. Let's embark on this thrilling \n"
    "journey together. Good luck!"
)
# This sets a (Welcome_massages) list item.
welcome_massage4 = (
    "Welcome to the Lost Woods, a place where light barely pierces\n"
    "the canopy and danger lurks behind every tree. "
    "\nThe forest is alive with secrets, and it has been waiting \n"
    "for someone like you. The path is treacherous, "
    "\nand only the brave will survive. Step carefully, \n"
    "for the woods have a way of claiming those who wander too far."
    "\nAre you ready to face the unknown?"
)
# This makes the (Welcome_massages) list
Welcome_massages = [
    welcome_massage1, welcome_massage2, welcome_massage3, welcome_massage4
]
# This sets the variable options1
options1 = ["a", "b", "c"]
# This sets the massage1 variable
massage1 = (
    " A: Stay put and continue to wait for rescue."
    "\n B: Venture out to search for food and water."
    "\n C: Try to climb a tree to get a \n"
    "better view of your surroundings."
    "\n(Please enter A,B or C)\n"
)


# This function defines a print with a delay-after of 2 seconds.
def print_pause(print_statement):
    print(
        print_statement
    )
    time.sleep(2)


# This function defines the (climb the tallest tree nearby) decision
# and what follows this decision.
def climb_the_tallest_tree_nearby():
    global Total_score
    print_pause(
        "You decide to climb the tallest tree nearby to get "
        "\na better view of your surroundings."
        "\nThe climb is challenging, but you manage to reach "
        "\na sturdy branch high above the forest floor."
        "\nFrom your vantage point, you see a few key landmarks:"
        "\nTo the north, you spot a distant mountain peak."
        "\nTo the east, you catch a glimpse of sunlight "
        "\nreflecting off a river."
        "\nTo the west, the forest seems to thin out slightly, "
        "\nhinting at possible civilization."
    )
    Total_score += 40
    print(
        f"Your score is {Total_score}"
    )
    while True:
        print_pause(
            "What do you do next?"
        )
        break
    player_choice2 = input(
        massage1
    )
    player_choice2 = player_choice2.lower()
    player_choice2 = valid_input(player_choice2, massage1, options1)
    print(
        f"You chose: {player_choice2}"
    )
    if player_choice2 == "a":
        print_pause(
            "You decide to head north towards the mountain peak to gain "
            "\na better perspective of your surroundings. "
            "\nAs you trek through the dense forest, you encounter:"
            "\n A steep incline that tests your endurance."
            "\n Wildlife that seems curious but non-threatening."
            "\n An old, weathered trail that leads upwards."
        )
        print_pause(
            "After a challenging climb, you reach the peak. From here, "
            "\nyou can see the vast expanse of the forest below, "
            "\nand in the distance, you spot a faint trail leading towards "
            "\na small village nestled at the edge of the woods."
        )
        print_pause(
            "Congratulations! You've successfully navigated out of the forest."
        )
        print(
            "Victory"
        )
        Total_score += 60
    elif player_choice2 == "b":
        print_pause(
            "As you decide to follow the river in hopes of "
            "\nfinding a settlement,"
            "\nthe journey starts off promisingly."
            "\nThe soothing sound of flowing water guides your path "
            "\nthrough dense forests and rugged terrain."
            "\nThe day wears on, and you become immersed in the beauty of "
            "\nnature around you, feeling confident "
            "\nthat civilization is just around the bend."
        )
        print_pause(
            "However, as the river narrows into a steep gorge, your progress "
            "\ncomes to an abrupt halt. There's no safe way to cross, "
            "\nforcing you to find an alternate route through the thick, "
            "\nunfamiliar forest. The canopy above blocks out the sun, "
            "\nmaking it difficult to discern directions."
        )
        print_pause(
            "Hours pass as you push deeper into the wilderness, "
            "\ntrying to circumvent the gorge. But with each step, "
            "\nyou feel more disoriented. Night creeps in swiftly, "
            "\nbringing with it a chilling reminder of your vulnerability. "
            "\nAttempting to start a fire for warmth proves futile with "
            "\ndamp wood and no proper tools."
        )
        print(
            "Days blur into each other as you desperately search for familiar "
            "\nlandmarks or signs of human presence. "
            "\nHunger gnaws at your stomach, and fatigue weighs heavily "
            "\non your limbs. Every attempt to follow the river seems to"
            "\n lead to dead ends or treacherous terrain."
        )
        print_pause(
            "With each passing day, your hope dims. Exhausted, weakened by "
            "\nhunger, and unable to find a way out, you realize you're \n"
            "lost beyond rescue. In the harsh embrace of the wilderness, "
            "\nsurrounded by the relentless sounds of nature, "
            "\nyou succumb to the elements."
        )
        print_pause(
            "Your journey following the river, filled with initial "
            "\nhope and determination, ends tragically in the "
            "\nheart of the unforgiving wild."
        )
        print(
            "Game Over"
        )
        Total_score += 0
        print(
            f"Your score is {Total_score}"
        )
    elif player_choice2 == "c":
        print_pause(
            "You carefully descend from the tree, your movements slow and "
            "\ndeliberate to avoid making any noise. "
            "\nThe dense foliage above gives way to a more open part of "
            "\nthe forest to the west, \n"
            "where sunlight filters through the trees in dappled patches."
        )
        print_pause(
            "As you move through the thinner part of the forest, "
            "\nthe underbrush becomes sparser, \n"
            "and you can see further ahead. The air feels lighter, "
            "\nbut an uneasy silence hangs around you. \n"
            "Your decision to take this path lingers in your mind, \n"
            "a choice that has led you deeper into the unknown."
        )
        print_pause(
            "Suddenly, the forest around you seems to close in. "
            "\nThe rustling of leaves grows louder, "
            "\nand shadows dance at the edge of your vision. "
            "\nYou sense movement behind you and quicken your pace, "
            "\nbut it's too late. Out of the shadows, a pack \n"
            "of wolves emerges, their eyes glinting with hunger."
        )
        print_pause(
            "Your heart races as you realize the gravity of your situation."
            "\n The decision to venture west, "
            "\naway from the denser forest, has led you into their territory."
            "\n There's no escape. "
            "\nYou brace yourself, but the pack closes in swiftly."
        )
        print_pause(
            "The forest falls silent once more, the decision that led you here"
            "\nmarking the end of your journey."
        )
        print(
            "Game Over"
        )
        Total_score += 0
        print(
            f"Your score is {Total_score}"
        )


# This sets the variable massage2
massage2 = (
    " A: Investigate the campsite for clues about who might have been here."
    "\n B: Drink from the stream and rest for a while."
    "\n C: Explore the cave entrance to see where it leads."
    "\n(Please enter A,B or C)\n"
)


# This function defines the (climb the tallest tree nearby) decision
# and what follows this decision.
def follow_a_faint_animal_trail():
    global Total_score
    print_pause(
        "You decide to follow a faint animal trail that leads deeper "
        "\ninto the woods. The trail winds through thick underbrush and"
        "\nover fallen logs, but it seems to be leading somewhere."
        "\nAfter a while, you stumble upon:\nA small clearing with a "
        "\nmakeshift campsite. A stream with clear, drinkable water."
        "\nA cave entrance partially hidden by bushes."
    )
    Total_score += 40
    print(
        f"Your score is {Total_score}"
    )
    while True:
        print_pause(
            "What do you do next?"
        )
        break
    player_choice2 = input(
        massage2
    )
    player_choice2 = player_choice2.lower()
    player_choice2 = valid_input(player_choice2, massage2, options1)
    print(
        f"You chose: {player_choice2}"
    )
    if player_choice2 == "a":
        print_pause(
            "You cautiously approach the abandoned campsite, \n"
            "the remains of a fire still smoldering faintly. "
            "\nThe area is eerily quiet, and the surrounding trees "
            "\nseem to loom closer, casting long shadows. "
            "\nYour task is to investigate the campsite for any clues"
            "\nabout who might have been here."
        )
        print_pause(
            "As you sift through the remnants, you find scattered belongings:"
            "\n a torn backpack, some food wrappers,\n"
            "and a journal partially buried in the dirt. \n"
            "Flipping through the pages, you find cryptic notes and \n"
            "hastily drawn maps. The entries speak of a group who \n"
            "ventured too far and became hopelessly lost."
        )
        print_pause(
            "Suddenly, you recall the decision you made earlier—to \n"
            "split off from your group and explore this part of the \n"
            "forest alone. It seemed like a good idea at the time, \n"
            "a way to cover more ground and increase your chances of finding"
            "\n help. But now, as the pieces come together, "
            "\nyou realize the gravity of your mistake."
        )
        print_pause(
            "A rustling sound pulls your attention. You look up to see shadows"
            "\nmoving between the trees. Your heart races as you remember the "
            "\nwarnings in the journal about strange figures \n"
            "watching from the darkness. Panic sets in as \n"
            "you realize you’ve been surrounded."
        )
        print_pause(
            "You try to back away, but it’s too late. The figures emerge \n"
            "from the shadows, revealing themselves to be hostile forest \n"
            "dwellers, their eyes glinting with malice. \n"
            "You made a critical error by "
            "\nventuring here alone, and now there is no escape."
        )
        print_pause(
            "The campsite falls silent once more, the decision that \n"
            "led you here marking the end of your journey."
        )
        print(
            "Game Over"
        )
        Total_score += 0
        print(
            f"Your score is {Total_score}"
        )
    elif player_choice2 == "b":
        print_pause(
            "You find a clear, bubbling stream and decide to take \n"
            "a break from your exhausting journey through the forest.\n"
            "The cool water looks inviting, and you kneel down to drink,"
            "\nfeeling a sense of relief as the refreshing liquid \n"
            "quenches your thirst. Deciding to rest for a while, \n"
            "you sit by the stream, letting the sound of \n"
            "flowing water soothe your weary mind."
        )
        print_pause(
            "As you relax, you think back to the decision you made \n"
            "earlier—to leave the path and venture deeper into the \n"
            "forest in search of a shortcut. It seemed like a good \n"
            "idea at the time, a way to save time and reach \n"
            "safety quicker. But now, as you sit by the stream, \n"
            "a creeping sense of unease begins to settle in."
        )
        print_pause(
            "Suddenly, your stomach churns, and a wave of dizziness "
            "\nwashes over you. You try to stand but find \n"
            "yourself too weak. The realization hits you: \n"
            "the water from the stream was contaminated. \n"
            "Panic sets in as you remember the warnings you \n"
            "ignored about drinking from unknown sources."
        )
        print_pause(
            "Your vision blurs, and you feel yourself growing weaker "
            "\nby the moment. The decision to drink from the stream, "
            "\ndriven by desperation and exhaustion, \n"
            "has sealed your fate. With no strength left to move, "
            "\nyou succumb to the effects of the poisoned water."
        )
        print_pause(
            "The forest remains silent, the decision that \n"
            "led you here marking the end of your journey."
        )
        print(
            "Game Over"
        )
        Total_score += 0
        print(
            f"Your score is {Total_score}"
        )
    elif player_choice2 == "c":
        print_pause(
            "Intrigued by the cave entrance, you decide to explore its depths."
            "\nYou carefully navigate through the dark passages, \n"
            "relying on your senses and whatever light filters in "
            "\nfrom the entrance."
        )
        print_pause(
            "Inside the cave, you discover:\n Ancient carvings on the walls "
            "\ndepicting local wildlife and rituals. A narrow passage "
            "\nleading deeper underground.\n A chamber with a \n"
            "glimmer of what looks like treasure."
        )
        print_pause(
            "As you venture further, you hear echoing sounds of water \n"
            "dripping and faint murmurs. Eventually, you emerge from \n"
            "another opening on the other side of the hill."
        )
        print_pause(
            "You've found a shortcut through the mountain! "
            "\nCongratulations on your adventurous discovery."
        )
        Total_score += 60


# This sets the variable massage3
massage3 = (
    " A: Stay put and continue to wait for rescue."
    "\n B: Venture out to search for food and water."
    "\n C: Try to climb a tree to get a better view of your surroundings."
    "\n(Please enter A,B or C)\n"
)


# This function defines the (climb the tallest tree nearby) decision
# and what follows this decision.
def build_a_makeshift_shelter():
    global Total_score
    print_pause(
        "You decide to build a makeshift shelter using branches and leaves, "
        "hoping that someone will come looking for you soon."
        "\nAs you gather materials and construct your shelter, "
        "\nthe forest grows darker and colder."
        "\nEventually, you settle in for the night."
    )
    Total_score += 40
    print(
        f"Your score is {Total_score}"
    )
    while True:
        print_pause(
            "What do you do the next morning?"
        )
        break
    player_choice2 = input(
        massage3
    )
    player_choice2 = player_choice2.lower()
    player_choice2 = valid_input(player_choice2, massage3, options1)
    print(
        f"You chose: {player_choice2}"
    )
    if player_choice2 == "a":
        print_pause(
            "You decide to build a makeshift shelter and wait for rescue. "
            "\nAs you settle in for the night, you keep a small fire burning"
            "\n for warmth and safety."
        )
        print_pause(
            "The next morning, you hear distant voices and shouts. "
            "\nYou rush out of your shelter and wave your arms to get \n"
            "their attention. A search party sent by your friends \n"
            "finds you safe and sound."
        )
        print_pause(
            "You've been rescued! "
            "\nCongratulations on surviving the night in the wilderness."
        )
        Total_score += 60
    elif player_choice2 == "b":
        print_pause(
            "You find a small clearing and decide it’s best to stay put, "
            "\nhoping that rescue will come soon. You gather some branches "
            "\nand leaves to create a makeshift shelter and sit down to wait."
            "\nThe forest around you is still, with only the occasional \n"
            "rustling of leaves and distant bird calls breaking the silence."
        )
        print_pause(
            "As time passes, you recall the decision you made earlier—to \n"
            "stay in one place instead of continuing to search for a way out. "
            "\nIt seemed like a sensible choice, conserving your energy and "
            "\nincreasing your chances of being found by a rescue team."
        )
        print_pause(
            "Hours turn into days. Your supplies dwindle, and the isolation "
            "\nweighs heavily on you. The forest, once a place of hopeful "
            "\nanticipation, now feels like a prison. Your calls for help go "
            "\nunanswered, and the sky above remains stubbornly clear, "
            "\nwith no signs of rescue."
        )
        print_pause(
            "Weakness sets in from lack of food and clean water. \n"
            "The decision to stay put, driven by hope and caution, \n"
            "has left you stranded. Your strength fades as you realize \n"
            "no one is coming. The forest's stillness becomes oppressive, "
            "\nand you finally succumb to exhaustion and despair."
        )
        print_pause(
            "The clearing remains silent, \n"
            "the decision that led you here marking the end of your journey."
        )
        print(
            "Game Over"
        )
        Total_score += 0
        print(
            f"Your score is {Total_score}"
        )
    elif player_choice2 == "c":
        print_pause(
            "You decide to climb a tall tree to get a better view of your "
            "\nsurroundings, hoping to spot a way out of the dense forest. "
            "\nYou carefully select a sturdy tree with low branches and "
            "\nbegin your ascent, each step bringing you higher above the "
            "\nforest floor.As you climb, you feel a mix of hope and "
            "\ntrepidation, thinking that this decision "
            "\nmight be the turning point in your journey."
        )
        print_pause(
            "Reaching a high branch, you pause to catch your breath and \n"
            "survey the landscape. The view is impressive; you can see the "
            "\nexpanse of the forest stretching out in all directions.\n"
            "However, as you scan for any signs of civilization, \n"
            "your foot slips. You grasp for a branch, but it's too late."
        )
        print_pause(
            "You lose your grip and fall, branches snapping beneath you "
            "\nas you plummet towards the ground. The world becomes \n"
            "a blur of green and brown, and you hit the ground hard, \n"
            "pain shooting through your body. The impact leaves you \n"
            "disoriented and unable to move. The decision to climb the tree, "
            "\ndriven by the hope of finding a way out, "
            "\nhas resulted in a catastrophic fall."
        )
        print_pause(
            "As you lie on the forest floor, the pain intensifies and \n"
            "your vision begins to fade. The forest around you falls silent, "
            "\nthe decision that led you here marking the end of your journey."
        )
        print(
            "Game Over"
        )
        Total_score += 0
        print(
            f"Your score is {Total_score}"
        )


# This function defines the game end (victory)
def game_end():
    # Game ends if score reaches 100
    if Total_score >= 100:
        print(
            "Game Over! You won!"
        )
        print(
            f"Your score is {Total_score}"
        )

    else:
        game_should_continue()


# This function obligates the player to giv a valid input.
def valid_input(prompt, massage, options):
    while prompt not in options:
        print("Invalid choice. Please try again.")
        prompt = input(
            massage
        )
        prompt = prompt.lower().strip()
    return prompt


# This list sets the argument option in the valid_input's arguments.
options2 = [
    "y", "n"
]
# This sets the massage4 variable
massage4 = "Do you want to play again Y/N \n(Please enter Y or N)\n"


# This function defines the condition were the game asks if the
# user wants to play again or no.
def game_should_continue():
    while True:
        prompt = input(
            "Do you want to play again Y/N \n(Please enter Y or N)\n"
        )
        prompt = prompt.lower().strip()
        user_choice = valid_input(prompt, massage4, options2)
        print(
            f"You chose: {user_choice}"
        )
        if user_choice == "y":
            lost_in_the_woods_game()
        elif user_choice == "n":
            break


# This sets the variable massage
massage = (
    "Do you:\n A: Climb a tall tree to get a better view."
    "\n B: Follow a faint animal trail deeper into the woods."
    "\n C: Build a shelter and wait for rescue.\n(Please enter A,B or C)\n"
)


# This function is where I gather the code together.
def main():
    # This below welcomes the player.
    print_pause(random.choice(Welcome_massages))
    # This describes what is happening to the player.
    print_pause(
        "\nYou find yourself deep in a dense forest with no clear path out..."
    )
    # This asks the user to mke a decision.
    while True:
        player_choice = input(
            massage
        )
        # This makes the player_choice lowercase.
        player_choice = player_choice.lower()
        player_choice = valid_input(player_choice, massage, options1)
        print(
            f"You chose: {player_choice}"
        )
        if player_choice == "a":
            climb_the_tallest_tree_nearby()
        elif player_choice == "b":
            follow_a_faint_animal_trail()
        elif player_choice == "c":
            build_a_makeshift_shelter()
        break


# This function is where I gathered the (main, game_end) functions.
def lost_in_the_woods_game():
    main()
    game_end()


# This code runs the hole game.
lost_in_the_woods_game()
