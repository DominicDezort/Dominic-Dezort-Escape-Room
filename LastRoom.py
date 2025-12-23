# The LastRoom class represents the final chamber of the temple that has the locked door and crate
# Player must get to final chamber in order to unlock door from revealed combination
class LastRoom:
    def __init__(self):
        self._open = False

    # Handles case when player wants to examine the final chamber
    def examine(self):
        # Player examines chamber if the trap has been deactivated
        if self._open:
            print("You are in a large stone chamber. There is a wooden crate and a large door at the far end.")
        # Player examines chamber if trap is still active
        else:
            print("You can't examine the chamber. The way is blocked. You must deactivate the trap.")

    # Player may enter chamber if the trap is open
    def enter(self, trap_open):
        # Checks to see if trap is open
        if trap_open:
            # Trap is open, player may continue forward on their adventure
            self._open = True
            print("You step into the final chamber of the temple.")
        # Trap is not open, the last room is not accessible
        else:
            print("The trap is still active. You can't go any further.")

    # When player looks around the main room, they can see the final room
    # Player cannot enter without deactivating the trap
    def look(self):
        # If the trap is open, the player can see the crate and locked door
        if self._open:
            print("You see a dusty room with a crate and a locked door.")
        # Player sees the trap is blocking their path to the final chamber
        else:
            print("The final chamber is blocked off by a trap. There looks to be a path... if only there was a way "
                  "to deactivate the trap")
