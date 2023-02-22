# Create a Mad Libs game
print("Welcome to Mad Libs! \nLet's create a story.")

answer = input("Do yo want to start the game now? (yes/no) \n")

# Set variables for the background of inserted words
backgr_color = '\033[46m'
reset_backgr_color = '\033[49m'

# Starting the game
if answer.lower().strip() == "yes":
    # Choose a story
    while True:
        answer1 = input('Please, select your story entering the numbers 1, 2 or 3.\n'
                        'To exit, enter "quit" \n')
        if answer1.lower().strip() == "quit":
            break
        elif answer1 == "1":
            # Prompt the user for various words
            number1 = input("Input a number: ")
            noun1 = input("Input measure of time (plural): ")
            noun2 = input("Input a mode of transportation: ")
            adjective1 = input("Input an adjective: ")
            adjective2 = input("Input another adjective: ")
            noun3 = input("Input a noun (plural): ")
            adjective3 = input("Input a color: ")
            noun4 = input("Input a part of the body (plural): ")
            verb1 = input("Input a verb: ")
            number2 = input("Input a number: ")
            noun5 = input("Input a noun (plural): ")
            noun6 = input("Input another noun (plural): ")
            noun7 = input("Input a part of the body (plural): ")
            verb2 = input("Input a verb: ")
            noun8 = input("Input a noun: ")
            adjective4 = input("Input an adjective: ")
            noun9 = input("Input a silly word: ")
            noun10 = input("Input a noun: ")
            # Use the collected words to construct the story
            story1 = (f"\n"
                      f"        It was about {backgr_color + number1 + reset_backgr_color} {backgr_color + noun1 + reset_backgr_color} ago when I arrived at the hospital in a(n) {backgr_color + noun2 + reset_backgr_color}.\n"
                      f"        The hospital is a(n) {backgr_color + adjective1 + reset_backgr_color} place, there are a lot of {backgr_color + adjective2 + reset_backgr_color} {backgr_color + noun3 + reset_backgr_color} here.\n"
                      f"        There are nurses here who have {backgr_color + adjective3 + reset_backgr_color} {backgr_color + noun4 + reset_backgr_color}. \n"
                      f"        If someone wants to come into my room I told them that they have to {backgr_color + verb1 + reset_backgr_color} first. \n"
                      f"        I've decorated my room with {backgr_color + number2 + reset_backgr_color} {backgr_color + noun5 + reset_backgr_color}.\n"
                      f"        Today I talked to doctors and they were wearing {backgr_color + noun6 + reset_backgr_color} on their {backgr_color + noun7 + reset_backgr_color}.\n"
                      f"        I heard that all doctors {backgr_color + verb2 + reset_backgr_color} {backgr_color + noun8 + reset_backgr_color} every day for breakfast. \n"
                      f"        The most {backgr_color + adjective4 + reset_backgr_color} thing about being in the hospital is the {backgr_color + noun9 + reset_backgr_color} {backgr_color + noun10 + reset_backgr_color}!\n"
                      f"        ")

            # Display the story
            print("\nHere's your story:")
            print(story1)

        elif answer1 == "2":
            noun1 = input("Input a person's name: ")
            noun2 = input("Input a noun: ")
            adjective1 = input("Input an adjective (feeling): ")
            verb1 = input("Input a verb: ")
            adjective2 = input("Input an adjective (feeling): ")
            noun3 = input("Input an animal: ")
            verb2 = input("Input a verb: ")
            adjective3 = input("Input a color: ")
            verb3 = input("Input a verb (ending in ing): ")
            adverb1 = input("Input an adverb (ending in ly): ")
            number1 = input("Input a number: ")
            noun4 = input("Input measure of time (plural): ")
            adjective4 = input("Input a color: ")
            noun5 = input("Input an animal: ")
            number2 = input("Input a number: ")
            noun6 = input("Input a silly word: ")
            noun7 = input("Input a noun (plural): ")

            story2 = (f"\n"
                      f"        This weekend I am going camping with {backgr_color + noun1 + reset_backgr_color}. \n"
                      f"        I packed my lantern, sleeping bag and {backgr_color + noun2 + reset_backgr_color}. \n"
                      f"        I am so {backgr_color + adjective1 + reset_backgr_color} to {backgr_color + verb1 + reset_backgr_color} in a tent. \n"
                      f"        I am {backgr_color + adjective2 + reset_backgr_color} we might see a(n) {backgr_color + noun3 + reset_backgr_color}. \n"
                      f"        I hear they're kind of dangerous. While we're camping, we are going to hike, fish and {backgr_color + verb2 + reset_backgr_color}. \n"
                      f"        I have heard that the {backgr_color + adjective3 + reset_backgr_color} lake is great for {backgr_color + verb3 + reset_backgr_color}. \n"
                      f"        Then we will {backgr_color + adverb1 + reset_backgr_color} hike through the forest for {backgr_color + number1 + reset_backgr_color} {backgr_color + noun4 + reset_backgr_color}.\n"
                      f"        If I see a {backgr_color + adjective4 + reset_backgr_color} {backgr_color + noun5 + reset_backgr_color} while hiking, I am going to bring it home as a pet! \n"
                      f"        At night we will tell {backgr_color + number2 + reset_backgr_color} {backgr_color + noun6 + reset_backgr_color} stories and roast {backgr_color + noun7 + reset_backgr_color} around the campfire!\n"
                      f"        ")

            print("\nHere's your story:")
            print(story2)

        elif answer1 == "3":

            noun1 = input("Input a person's name: ")
            adjective1 = input("Input an adjective: ")
            adjective2 = input("Input a color: ")
            noun2 = input("Input an animal: ")
            noun3 = input("Input a place: ")
            adjective3 = input("Input an adjective: ")
            noun4 = input("Input a magical creature (plural): ")
            adjective4 = input("Input an adjective: ")
            noun5 = input("Input a magical creature (plural): ")
            noun6 = input("Input name of a room in a house: ")
            noun7 = input("Input noun (plural): ")
            noun8 = input("Input a noun: ")
            noun9 = input("Input noun (plural): ")
            adjective5 = input("Input an adjective: ")
            noun10 = input("Input noun (plural): ")
            number1 = input("Input a number: ")
            noun11 = input("Input measure of time (plural): ")
            verb1 = input("Input a verb (ending in ing): ")
            adjective6 = input("Input an adjective: ")
            noun12 = input("Input a noun: ")

            story3 = (f"\n"
                      f"        Dear {backgr_color + noun1 + reset_backgr_color}! \n"
                      f"        I am writing to you from a(n) {backgr_color + adjective1 + reset_backgr_color} castle in an enchanted forest. \n"
                      f"        I found myself here one day after going for a ride on a(n) {backgr_color + adjective2 + reset_backgr_color} {backgr_color + noun2 + reset_backgr_color} in {backgr_color + noun3 + reset_backgr_color}. \n"
                      f"        There are {backgr_color + adjective3 + reset_backgr_color} {backgr_color + noun4 + reset_backgr_color} and {backgr_color + adjective4 + reset_backgr_color} {backgr_color + noun5 + reset_backgr_color} here! \n"
                      f"        In the {backgr_color + noun6 + reset_backgr_color} there is a pool full of {backgr_color + noun7 + reset_backgr_color}. \n"
                      f"        I fall asleep each night on a(n) {backgr_color + noun8 + reset_backgr_color} of {backgr_color + noun9 + reset_backgr_color} and dream of {backgr_color + adjective5 + reset_backgr_color} {backgr_color + noun10 + reset_backgr_color}. \n"
                      f"        It feels as though I have lived here for {backgr_color + number1 + reset_backgr_color} {backgr_color + noun11 + reset_backgr_color}. \n"
                      f"        I hope one day you can visit me, although the only way to get here now is {backgr_color + verb1 + reset_backgr_color} on a {backgr_color + adjective6 + reset_backgr_color} {backgr_color + noun12 + reset_backgr_color}!\n"
                      f"        ")

            print("\nHere's your story:")
            print(story3)

else:
    print("Goodbye!")