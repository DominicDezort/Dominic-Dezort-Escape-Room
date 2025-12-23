# Lever class reveals the dark room when pulled.
# Player must reveal the dark room before entering or interacting with snake statue
class Lever:
    def __init__(self):
        self._pulled = False

    # Player pulls lever that moves a large rock away from the door
    def pull(self):
        if not self._pulled:
            self._pulled = True
            print("You pull the lever. A large rock rolls aside, revealing a dark room.")
        else:
            print("The lever has already been pulled. The dark room has been revealed.")

    # Player examines the lever
    def examine(self):
        print("The lever looks ancient. You feel it might do something important.")

    # Player looks around surroundings
    def look(self):
        print("You spot a lever on the wall.")
