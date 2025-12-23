# Crate class represents the crate that is located in the final chamber
# The crate is the gatekeeper of the combination to unlock the door
class Crate:
    def __init__(self):
        self._smashed = False
        self._paperRevealed = False

    # Player smashes the crate once they are in the final chamber
    def smash(self):
        # Allow player to smash if not already smashed
        if not self._smashed:
            self._smashed = True
            # Allow the player to begin attempting the combination lock to unlock the door
            self._paperRevealed = True
            # Reveal the paper inside the crate
            print("You smash the crate. Inside is a folded piece of paper.")
        # Player tries to smash crate after it has been smashed
        else:
            print("The crate is already smashed open.")

    # Player examines the crate or the paper
    # They cannot be in the dark room to examine these objects
    def examine(self, item):
        # Player examines crate
        if item == "crate":
            print("A wooden crate sits in the corner of the room.")
        # Player examines paper
        elif item == "paper":
            if self._paperRevealed:
                print("The paper says: 'Combination: 12345'") # reveal the combination
            else:
                print("You don't see any paper here.")
        else:
            print("You don't see that item here.")

    # Player attempts to open crate
    # The crate must be smashed to reveal the paper inside
    def open(self):
        print("The crate won't open normally. It's sealed tight.")

    # When player looks around the surroundings
    def look(self):
        print("You notice a wooden crate tucked away under rubble.")
