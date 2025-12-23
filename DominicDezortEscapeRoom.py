# Driver to run the game
# Allow access to classes from driver
from Vines import *
from Torch import *
from Lever import *
from DarkRoom import *
from SnakeStatue import *
from Trap import *
from LastRoom import *
from Crate import *
from CombinationLock import *
from Door import *
from CountdownTimer import *


# Main function
def main():
    # Print Welcome message
    print("""
Welcome to the Jungle Temple Escape Room!
You are an archaeologist in the heart of the Amazon Rainforest, 
and you stumbled upon an ancient temple with a team of explorers. Upon arrival to the entrance of the temple, 
you and your team are knocked unconscious by an evil spirit that is standing guard. When you regain consciousness, 
you are locked in what looks to be the dungeon of the temple and realize that the rest of your team is missing. 
Use the clues and your instinct to figure a way out of the temple and reunite with your team before the time runs out! 
Type 'look' to observe your surroundings, 'examine <object>' to inspect something,
or 'quit' to give up your adventure.
""")

    # Instantiate the Classes
    vines = Vines()
    torch = Torch()
    lever = Lever()
    darkRoom = DarkRoom()
    statue = SnakeStatue()
    trap = Trap()
    finalRoom = LastRoom()
    crate = Crate()
    lock = CombinationLock(argCombination="12345",argHint="") # Prompt constructor with correct combination
    door = Door(lock)
    timer = CountdownTimer(600)  # 10 minutes to complete the game

    # Initialize Methods
    global gameWon
    torchTaken = False
    inDarkRoom = False
    inFinalRoom = False
    hasKey = False
    gameWon = False
    lookUsed = False


    while True:
        # Time runs out before the game has been completed or before player quits
        if timer.isTimeUp():
            # Print message if player runs out of time
            print("Time’s up! The temple seals shut and you are lost forever... Game over.")
            break

        # Interpret commands that player enters throughout the game
        # Handles the case of extra spacing or capital letters
        cmd = input("\n> ").strip().lower()

        # Handles the case when player is in the dark room
        # Player cannot interact with things outside the dark room
        if inDarkRoom:
            allowedInDark = [
                "look", "examine statue", "push button", "turn knob", "pull handle",
                "open statue", "take key", "leave room", "quit"]
            if cmd not in allowedInDark:
                print("You are in a dark room. You must leave the room or interact with the statue.")
                continue

        # Handles the case when player is in the final chamber
        # Player can only interact with objects in the final chamber
        if inFinalRoom:
            allowedInRoom = ["look","examine chamber","examine crate","smash crate","examine door","unlock door","exit","open door","examine paper","leave chamber"]
            if cmd not in allowedInRoom:
                print("You are in the final chamber. You must leave the room to interact with that.")
                continue


        # If player does not start with 'look' the only acceptable command is 'quit'
        # Handles the case if player tries to begin their escape without looking around
        # Countdown will begin when 'look' is entered. Player must 'look' first before anything else
        if not lookUsed:
            if cmd == "quit":
                print("You sit down and accept your fate in the ancient temple without even trying.")
                break
            elif cmd != "look":
                print("You must look around before doing anything else. You cannot blindly begin your escape! Type 'look' or 'quit'")
                continue

        # Handles case if player decides to quit the game before finishing
        if cmd == "quit":
            print("You sit down and accept your fate in the ancient temple. Game over.")
            break

        # Player looks at surroundings (player does not know surroundings without this input)
        # Initializes the countdown timer (10 minutes to escape)
        elif cmd == "look":
            lookUsed = True
            timer.look() # Begin timer
            # Player uses command while in dark room
            # Cannot see surroundings other than what is in the room
            if inDarkRoom:
                print("You are in a dark room. You can see a snake statue with various mechanisms. They look ancient, but they seem to be operational.")
            # Player uses command while in the final chamber
            # Can only see the surroundings in the final chamber when in the final chamber
            elif inFinalRoom:
                print("You are in the final chamber. You see a crate and a locked door.")
            # Player uses command in main room
            # Can see surroundings in main room but cannot see inside the dark room
            # Player is still able to see objects in final chamber
            else:
                vines.look()
                torch.look()
                lever.look()
                darkRoom.look() if hasattr(darkRoom, "look") else None
                trap.look()
                finalRoom.look()
                crate.look()
                door.look()

        # Player examines an object
        elif cmd.startswith("examine"): # Checks to see if examine is first word
            # If examine first word, splits string at the space
            parts = cmd.split()
            # If player entered a two word phrase (ensures player only examines one object at a time)
            if len(parts) == 2:
                # Analyze second word of the command input
                obj = parts[1]
                if inDarkRoom: # If player is in dark room
                    # Player can only examine statue while in the dark room
                    if obj == "statue":
                        statue.examine()
                    # Player cannot examine any other object besides statue while in dark room
                    else:
                        print("You cannot examine that while in the dark room")
                # Player attempts to examine objects in final chamber
                # If not in final chamber, the player cannot examine the objects in the chamber
                # The objects not in final chamber cannot be examined while in final chamber
                elif inFinalRoom:
                    if obj == "crate":
                        crate.examine("crate")
                    elif obj == "paper":
                        crate.examine("paper")
                    elif obj == "door":
                        door.examine()
                    else:
                        print("You don't see anything like that to examine here.")
                # If the player is in main room, they can examine the following objects
                else:
                    if obj == "vines":
                        vines.examine() # examine the vines
                    elif obj == "torch":
                        torch.examine() # examine the torch
                    elif obj == "lever":
                        lever.examine() # examine the lever
                    # Cannot examine statue unless player in dark room
                    elif obj == "statue":
                        print("You cannot examine the statue. You are not in the dark room")
                    elif obj == "trap":
                        trap.examine() # examine trap
                    # Cannot examine the objects in final chamber from main room
                    elif obj == "crate":
                        print("You cannot examine the crate. You are too far away")
                    elif obj == "paper":
                        print("You cannot examine the paper. You're too far away")
                    elif obj == "door":
                        print("You cannot examine the door. You're too far away")
                    # Player wants to examine the final room or dark room
                    elif obj == "room":
                        darkRoom.examine(torchTaken) # player must have torch to see inside dark room
                    # Player can examine the chamber if the trap is deactivated
                    elif obj == "chamber":
                        finalRoom.examine()
                    # Handles case if player enters an invalid object to examine
                    else:
                        print("You don't see anything like that to examine.")
            # Handles the case where a player tries to examine more than one object at a time
            else:
                print("Please examine one object at a time.")

        # Player moves vines
        elif cmd == "move vines":
            vines.move()

        # Player takes the torch
        elif cmd == "take torch":
            torch.take()
            torchTaken = True

        # Player pulls lever to reveal a dark room
        elif cmd == "pull lever":
            lever.pull()
            if not darkRoom._revealed:
                darkRoom.reveal()

        # Player attempts to enter the dark room
        elif cmd == "enter room":
            # Player can only enter room if they have taken the torch
            darkRoom.enter(torchTaken)
            if torchTaken:
                inDarkRoom = True # Player has torch so they may enter the room

        # Player must exit the room once key has been obtained
        # Returns player to the main room
        elif cmd == "leave room":
            darkRoom.leave()
            inDarkRoom = False

        # Player pushes button on snake statue
        # Can only push button if in the dark room
        elif cmd == "push button":
            # Checks to see if player is in the dark room
            if inDarkRoom:
                statue.pushButton()
            # Handles when player is too far away from the statue
            else:
                print("You're not near the statue.")

        # Player turns knob on snake statue
        # Can only be turned if in the dark room
        elif cmd == "turn knob":
            if inDarkRoom:
                statue.turnKnob()
            # Handles when the player is too far away from the statue
            else:
                print("You're not near the statue.")

        # Player pulls the handle on the statue
        # Can only be pulled if in the dark room
        elif cmd == "pull handle":
            if inDarkRoom:
                statue.pullHandle()
            # Handles if player is too far away from the statue
            else:
                print("You're not near the statue.")

        # Player can open statue when they correctly interact with button, handle, knob
        # Statue will not open if player is too far away or did not interact with mechanisms
        elif cmd == "open statue":
            # Player must be in dark room to interact with statue
            if inDarkRoom:
                statue.open()
            else:
                print("You're not near the statue.")

        # Once player opens statue they may take the key
        # Can only take key if statue is open and in the dark room
        elif cmd == "take key":
            if inDarkRoom:
                statue.take()
                hasKey = True
            else:
                print("You're not near the statue.")

        # Player may use key to deactivate trap
        # Must be in main room to deactivate trap (player should leave dark room)
        elif cmd == "deactivate trap":
            trap.deactivate(hasKey) # Trap only deactivated if player has obtained the key

        # Once trap is deactivated, player may enter the final chamber
        # Player can only enter chamber if the trap is deactivated
        elif cmd == "enter chamber":
            if trap._openTrap:
                finalRoom.enter(trap._openTrap) # Trap is deactivated so the final chamber is accessible
                inFinalRoom = True
                inDarkRoom = False
            else:
                print("The path to the chamber is still blocked by the trap. You must deactivate the trap!")

        # Player may leave the final chamber
        # If they choose to do so, they will return to the main room
        elif cmd == "leave chamber":
            if inFinalRoom:
                inFinalRoom = False
                print("You return to the main room")
            else:
                print("You're not in the chamber")
        # Player must smash crate in order to reveal paper with combination
        # Must be in the final chamber in order to interact with crate
        elif cmd == "smash crate":
            if finalRoom._open:
                crate.smash() # Player is in final chamber
            else:
                print("You're not in the final chamber.") # Player is not in the final chamber

        # Player attempts to open crate
        # Can only interact with crate if the final chamber has been opened (and trap deactivated)
        elif cmd == "open crate":
            if finalRoom._open:
                crate.open()
            else:
                print("You're not in the final chamber")

        # Player is in final chamber and attempts to unlock door
        # Player must at least have the crate smashed and paper revealed in order to enter a password
        elif cmd == "unlock door":
            if crate._paperRevealed:
                success = lock.unlock()
                # Player successfully enters the combination
                if success:
                    door._openDoor = True
                    door._closeDoor = False
                    print("You hear the door click open. You may now 'open door' and 'exit'")
                # Player enters the wrong combination
                else:
                    print("Combination incorrect. You are still stuck!")
            # Paper containing combination has not been revealed yet
            else:
                print("You don't know the combination yet.")

        # Player can open door once the combination has been correctly entered
        elif cmd == "open door":
            door.open()

        # Player may exit the temple and the game is over once the door is unlocked and opened
        elif cmd == "exit":
            gameWon = door.exit()

            if gameWon:
                break

        # Player may pause game if break is needed and player wants to continue
        elif cmd == "pause":
            timer.pause()

        # Player can resume the paused game
        elif cmd == "resume":
            timer.resume()

        # Player enters an invalid command
        else:
            print("That command isn't recognized. Try something else.")

    # Print goodbye message whether player wins, loses, or quits
    print("\nThanks for playing the Jungle Temple Escape Room!")


if __name__ == "__main__":
    main()