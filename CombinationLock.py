# required - must use this class at least once
# When instantiating this object within your game, the lock will initially be locked.
# You will give it the combination and optionally a hint (via the constructor).
# Call the unlock() method when the player is trying to unlock it.
#   This will prompt them to enter the combination (and the hint if you have provided one).
#   You do not need to prompt yourself.  This will take care of prompting and possibly unlocking if the combination is correct.
#   The unlock() method will return True or False, depending on whether or not the player successfully unlocked it.
# Use the method isUnlocked() to check the status of the lock.

class CombinationLock:
    # Constructor
    # The combination is required when creating this object
    # Leave the hint blank if you do not want to use it
    # If you want to use the hint, use the other constructor.
    def __init__(self,argCombination,argHint=""):
        # Set the combination and hint.
        self.__combination = argCombination
        self.__hint = argHint

        # This starts out being locked.
        self.__openFlag = False

    # This method will prompt the player for the combination and possibly unlock the combination lock.
    # It will return true if successful, false if not.
    def unlock(self):
        # If the lock is already open, nothing should be done.
        if (self.__openFlag):
            return self.__openFlag
        # Prompt the player for the combination
        enteredCombination = input("Please enter the combination " + self.__hint + ":  ")

        # Check if the combination is correct
        if (enteredCombination == self.__combination):
            # The combination is correct.
            self.__openFlag = True

        # Return the status of the lock.
        return self.__openFlag

    # This method will return the status of the lock.
    # TRUE if unlocked, FALSE if locked.
    def isUnlocked(self):
        return self.__openFlag
