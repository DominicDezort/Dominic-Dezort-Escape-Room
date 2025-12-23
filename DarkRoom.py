# Dark room is only revealed when the boulder is moved by pulling the lever
# Since the room is dark, a torch is needed to see (enter the room)
class DarkRoom:
    def __init__(self):
        self._revealed = False
        self._dark = True

    # Once lever is pulled, the room is revealed
    def reveal(self):
        self._revealed = True

    # Player may enter the room only if they have obtained the torch
    def enter(self, hasTorch):
        # Player cannot enter room before pulling lever
        if not self._revealed:
            print("You can't enter. The room hasn't been revealed.")
        # Player cannot enter without torch
        elif not hasTorch:
            print("It's too dark to enter safely without a torch.")
        # Player enters the room after it has been revealed and they have obtained a torch
        else:
            self._dark = False
            print("You step into the dark room, your torch casting eerie shadows.")

    # Player may examine the dark room
    def examine(self,hasTorch):
        if not self._revealed:
            print("You do not see a secret room.")
        elif self._revealed and not hasTorch:
            print("It's too dark to see anything.")
        else:
            print("You see a mysterious snake statue in the center of the room.")


        # # Player tries to examine the room from the outside without a torch
        # if self._dark and self._revealed:
        #     print("It's too dark to see anything.")
        # # Player examines the room after they obtained a torch
        # elif not self._dark and not self._revealed:
        #     print("You do not see a secret room.")
        # elif self._dark and not self._revealed:
        #     print("You do not see a secret room.")
        # else:
        #     print("You see a mysterious snake statue in the center of the room.")

    # Player must leave room once key is acquired to continue their journey
    # Player can leave room at any time after they have already entered the dark room
    def leave(self):
        print("You return to the original room.")