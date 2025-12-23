# Vines Class represent vines covering a hidden clue on the wall
# Vines can be moved, examined, and looked at
class Vines:
    def __init__(self):
        self._moved = False # Vines have not been moved yet
    # Move vines if prompted by the player
    def move(self):
        if not self._moved:
            self._moved = True # Vines have been moved
            # Reveal a clue to obtain key from snake statue
            # Player will not know how to overcome statue puzzle without a clue/hint
            print("You move the vines to reveal the following message: 'You must push the button, turn the knob, and pull the handle to defeat the snake.'")
        else:
            print("You already moved the vines. The message is still visible.")
    # Examine vines - Handles the case when players examines vines after they have been moved
    def examine(self):
        if self._moved:
            print("The vines have been moved. The message has been revealed.") # vines moved
        else:
            print("Vines cover something on the wall.") # Vines have not been moved yet

    # Prompted when player looks around surroundings
    def look(self):
        print("You see thick vines hanging suspiciously over part of the wall.")