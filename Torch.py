# Torch class represents a light source required to enter the dark room.
# Player does not start with a torch but can acquire one from the wall
class Torch:
    def __init__(self):
        self._taken = False

    # Take torch from wall
    def take(self):
        if not self._taken:
            self._taken = True
            print("You take a lit torch from the wall. It illuminates your path.")
        else:
            print("You have already taken the torch.")
    # Player decides to examine torch
    def examine(self):
        print("It's a torch mounted on the wall. You can take it with you.")

    # Prompted when player looks around surroundings
    def look(self):
        print("A torch flickers on the wall. It could be useful in dark places.")