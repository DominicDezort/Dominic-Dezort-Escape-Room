# The door class represents the door in the final chamber separating the player from their victory
# The door is locked and requires the correct combination in order to be unlocked
class Door:
    def __init__(self, lock):
        self._openDoor = False
        self._closeDoor = True
        self._lock = lock

    # Player can see door when looking at their surroundings
    def look(self):
        print("A sturdy door with a glowing combination lock blocks your exit.")

    # Describe the door and let the player know the door has a combination lock
    def examine(self):
        print("The door has ancient carvings and a combination lock.")

    # Player correctly inputs the correct combination for the lock
    def unlock(self, combo):
        # Interpret the input from the combination, if correct the door is no longer locked
        self._lock.unlock(combo)
        # Player unlocks door
        if self._lock.unlocked:
            self._openDoor = True # Door can be opened
            self._closeDoor = False # door is no longer locked, player can escape

    # Player can open door once it is unlocked
    def open(self):
        if self._openDoor:
            print("The door creaks open, revealing freedom ahead.")
        # Player attempts to open door when it is still locked
        else:
            print("The door won't budge. It must be locked.")

    # Player may exit the temple and win the game if the door is unlocked
    def exit(self):
        # Player leaves the temple
        if self._openDoor:
            print("You step through the door and escape the cursed temple. You win!")
            return True # Door is open
        # Player tries to leave while the door is locked
        else:
            print("You can't exit. The door is still locked.")
            return False # Door is not open
