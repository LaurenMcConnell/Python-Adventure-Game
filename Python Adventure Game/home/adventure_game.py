import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def intro():
    print_pause("You find yourself in an unfamiliar town square")
    print_pause("A man in sandals approaches from a doorway")
    print_pause("\"What village are you from, horse thief?\" he asks")
    print_pause("You answer the villager by saying:")
    print_pause("1. \"Sorry, I don't know your horse, "
                "but I do know who stole them.\" ")
    print_pause("2. \"Hey now! Let's go to the taven and "
                "talk about this over a mead.\" ")
    print_pause("3. You draw your dagger and prepare for a fight.")


def answer_villager(items):
    response = input("Choose your move: 1, 2, or 3 \n")
    if response == "1":
        snitch(items)
    elif response == "2":
        tavern(items)
    elif response == "3":
        fight(items)
    else:
        print_pause("I'm sorry, I don't understand.")
        answer_villager(items)


def snitch(items):
    print_pause("You say to the villager, \"You can't ride a horse "
                "in sandals, why would you want him back?\"")
    print_pause("\"Sentimental value,\" the villager says. \"That "
                "horse meant everything to me.\"")
    print_pause("\"I'll talk to the man who took your horse. I'll "
                "reason with him,\" you say.")
    print_pause("The villager, teary eyed, hands you a halter.")
    items.append("halter")
    print_pause("\"You'll need to find his bridle too. He's a headstrong "
                "son of a gun.\"")
    print_pause("The villager thanks you and gives you directions "
                "to the town stables.")
    stables(items)


def stables(items):
    print_pause("The air smells of fresh hay.")
    print_pause("A big, chestnut color horse with a white front "
                "stands in a far stall.")
    print_pause("The horse turns his head to give you the side "
                "eye and a long snort.")
    print_pause("You hear a pair of boots on the floor behind you "
                "and turn around.")
    print_pause("A tall man stands there with a bridle in his hands.")
    print_pause("\"That's not your horse,\" he says.")
    print_pause("\"Or mine either for that matter.\"")
    print_pause("You:")
    print_pause("1. Draw your dagger. \"It doesn't matter whose he "
                "is, that horse is mine now.\"")
    print_pause("2. Tell the man, \"The villager who owns this horse "
                "is terribly upset. Please, I have the horse's halter."
                "If you'll let me have that bridle, I'll get him back "
                "to his owner safe.\"")
    print_pause("3. Jump the gate of the stall, swinging your leg "
                "up and over the horse. You back the big animal out "
                "of the stable as you buckle the bridel under it's muzzle"
                "like the horse theif you are. You head off on horseback "
                "in the direction of the tavern")
    while True:
        response = input("Choose your move: 1, 2, or 3 \n")
        if response == "1":
            fight(items)
            break
        elif response == "2":
            items.append("bridle")
            items.append("horse")
            hero(items)
            break
        elif response == "3":
            items.append("horse")
            tavern(items)
            break
        else:
            print_pause("I'm sorry, I don't understand.")


def hero(items):
    print_pause("The man motions to a saddle in the corner "
                "of the stables. \"Please take that too if it"
                "helps. I didn't steal this horse, the horse "
                "showed up hungry and I just gave him a place "
                "to stay.\"")
    print_pause("You put on the halter, bridle, and saddle up the"
                "horse, riding it triumphantly back to it's rightful "
                "owner.")
    print_pause("You win, congratulations.")
    play_again()


def tavern(items):
    print_pause("It's dark inside, a few villagers sit at "
                "scattered tables.")
    print_pause("You find the barmaid and order a mead for "
                "you and your new friend.")
    gwent_setUp(items)


def gwent_setUp(items):
    print_pause("\"Would you like to play a friendly game of "
                "gwent for a small wager?\" he asks as you sit "
                "down at one of the tables.")
    response = input("Yes or No?\n").lower()
    if response == "yes":
        wager(items)
    elif response == "no":
        print_pause("\"No? Then prepare to fight, I know a horse "
                    "thief when I see one!\"")
        print_pause("You draw your dagger and ready yourself")
        fight(items)
    else:
        print_pause("\"I'm sorry, I don't understand. "
                    "Let me ask you again,\" he says.")
        gwent_setUp(items)


def wager(items):
    if "change_purse" in items:
        items.remove("change_purse")
        gwent_cardGame(items)
    elif "winnings" in items:
        items.remove("winnings")
        gwent_cardGame(items)
    elif "horse" in items:
        print_pause("\"What a fine wager,\" the villager says.")
        print_pause("\"What I've been after all along, my friend.\"")
        print_pause("\"Now that I've got my horse back, prepare to die.\"")
        fight(items)
    else:
        print_pause("\"You're out of money,\" he says, \"I guess"
                    "you could bet a horse.\"")
        print_pause("\"That is, if you had one.\"")
        print_pause("\"Where would I get one of those?\" you ask.")
        print_pause("\"My guess is as good as yours,\" he says.")
        print_pause("\"I might know of one, you say.\"")
        print_pause("\"If I fetch him, you'll let me bet again?\" you ask.")
        print_pause("The villager pauses for a second.")
        print_pause("Depends on the quality of the wager,\" "
                    "he answers.")
        print_pause("You get up from the table. Leaving the tavern,"
                    "you head for the town stables")
        stables(items)


def gwent_cardGame(items):
    print_pause("You push your wager to the middle of the table.")
    print_pause("\"I'll even give you the advantage,\" he says. \"In case of "
                "a tie, you win.\"")
    deck = ["catapult", "torrential rain", "medic", "spy"]
    card = deck[random.randint(0, len(deck) - 1)]
    villagers_card = deck[random.randint(0, len(deck) - 1)]
    print_pause("Your card is: ")
    print(card)
    print_pause("The villager's card is: ")
    print(villagers_card)
    if len(card) >= len(villagers_card):
        print_pause("\"Ahh looks like you beat me! Here are some winnings.\"")
        items.append("winnings")
        items.append("winnings")
    else:
        print_pause("\"Better luck next time, buddy. I won't be"
                    "returning that wager of yours.\"")
    while True:
        print_pause("Would you like to bet again?")
        response = input("Yes or No?").lower()
        if response == "yes":
            wager(items)
            break
        elif response == "no":
            print_pause("The villager looks you up and down.")
            print_pause("\"You seem like an alright fella. Guess you "
                        "didn't take my horse,\" he says. You two shake "
                        "hands and you tell him,\"I sure do hope you find "
                        "who did.\"")
            print_pause("You win. Thanks for playing.")
            play_again()
            break
        else:
            print_pause("Sorry I don't understand")


def fight(items):
    print_pause("You died, don't start knife fights. Or steal horses.")
    play_again()


def play_again():
    response = input("Would you like to play again?\n").lower()
    if response == "yes":
        play_game()
    elif response == "no":
        print_pause("The End. Thank you for playing")
    else:
        print_pause("Sorry I don't understand")
        play_again()


def play_game():
    items = ["dagger", "change_purse"]
    intro()
    answer_villager(items)


play_game()
