# Countdown Timer class adds a time challenge to escape
# Timer is set to 10 minutes but can be adjusted in the driver if an extra challenge is desired
import time

class CountdownTimer:
    def __init__(self, duration):
        self._duration = duration
        self._remainingTime = duration
        self._paused = False
        self._startTime = None

    # Begin timer when player looks around the surroundings
    def look(self):
        # Begin countdown the first time look is used
        if self._startTime is None:
            self._startTime = time.time()
            # Player has 600 seconds from the time they input 'look'
            print(f"The countdown begins. You have {self._duration} seconds to escape!")
        # Update the timer with time remaining any time 'look' is used after the first time
        else:
            self.updateRemainingTime()
            print(f"Time remaining: {int(self._remainingTime)} seconds") # Provides the remaining time left

    # Keep track of time that has elapsed from the beginning of the game
    def updateRemainingTime(self):
        if self._startTime and not self._paused:
            elapsed = time.time() - self._startTime
            self._remainingTime = max(0, self._duration - elapsed) # Calculates remaining time

    # Handles if player chooses to pause the time
    def pause(self):
        # Time will not countdown if the timer is paused
        if not self._paused:
            self.updateRemainingTime()
            self._paused = True
            print("The countdown has been paused.") # stop counting down

    # Player must resume time after pausing for timer to continue counting down
    def resume(self):
        # Resumes the game when player prompts the pause to cease
        if self._paused:
            self._startTime = time.time() - (self._duration - self._remainingTime)
            self._paused = False
            print("The countdown resumes.") # resume counting down

    # Player runs out of time
    def isTimeUp(self):
        self.updateRemainingTime()
        return self._remainingTime <= 0 # Timer reaches zero (no more time left, game will end)