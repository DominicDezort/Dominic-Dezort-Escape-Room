# SnakeStatue represents the puzzle mechanism that must be solved to reveal a key.
# As long as all mechanisms are interacted with, the puzzle will allow the player to open the statue
class SnakeStatue:
    def __init__(self):
        self._handle = False
        self._button = False
        self._knob = False
        self._keyTaken = False

   # Mechanisms can be interacted with in any order there is not a specific pattern

   # Player pushes button on the statue (mechanism 1 of 3)
    def pushButton(self):
        self._button = True
        print("You push a button on the statue.")

    # Player pulls lever (mechanism 2 of 3)
    def pullHandle(self):
        self._handle = True
        print("You pull a tiny handle on the statue.")

    # Player turns knob (mechanism 3 of 3)
    def turnKnob(self):
        self._knob = True
        print("You turn a knob on the statue.")

    # Player may only open the statue once all mechanisms are completed
    def open(self):
        if self._button and self._knob and self._handle:
            # Player may open the statue if not already opened
            if not self._keyTaken:
                print("The statue opens to reveal a key!")
            else:
                print("The statue is already open.")
        # If player tries to open statue without fiddling with mechanisms
        else:
            print("Nothing happens. Maybe those mechanisms are supposed to do something?")

    # Once statue is opened, the player may take the key to continue their journey
    # Player can only take the key once
    def take(self):
        # Player does not have key and attempts to take it
        if self._button and self._knob and self._handle and not self._keyTaken:
            self._keyTaken = True
            print("You take the key from the opened statue.")
        # Player already took the key so the statue will be empty
        else:
            print("There is no key to take.")

    # In dark room, player may examine the statue
    # By examining the statue, the player will be able to make the connection to the message hidden by the vines
    def examine(self):
        # Description of the statue when player examines it
        print("The statue appears to be a large rattlesnake. It looks like the eye could be a button, the fang could be a knob, and the rattle looks to be a handle. Seems complex.")