# The Trap class represents barrier between the main room and the final chamber
# The trap is deactivated using a key obtained from the snake statue
class Trap:
    def __init__(self):
        self._closedTrap = True
        self._openTrap = False

    # Prompted when player looks at the surroundings
    # Give a hint that it can be deactivated
    def look(self):
        print("You see a large trap blocking the path. It looks mechanical.")

    # Player examines trap
    # Indicate the key can deactivate the trap
    def examine(self):
        # When player has not deactivated the trap
        if self._closedTrap:
            print("This trap appears dangerous, but there's a slot for a key. That must be how you deactivate the trap.")
        # The key has been used and the trap is deactivated
        # Allows player to continue forward
        else:
            print("The trap has been safely deactivated.")

    # Player deactivates trap using the key
    def deactivate(self, hasKey):
        # Player must have key to deactivate the trap
        if hasKey:
            self._closedTrap = False # trap is no longer active
            self._openTrap = True # trap is now deactivated
            print("You insert the key and deactivate the trap. A path opens to the  final chamber.") # let player know the trap has been deactivated
        # Indicate the trap is still active and the player may not pass
        else:
            print("You need a key to deactivate the trap.")