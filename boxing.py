# Define Boxing class
class Boxing:
    # Define an init method and initialize instance variables with default values of 0
    def __init__(self):
        self.minutes = 0
        self.stations = 0
        self.rounds = 0
        self.weight = 0
    # Define a method named log_workout that prompts 
    # the user to input workout parameters
    def log_workout(self):
        self.minutes = input("Enter the number of minutes you boxed: ")
        self.stations = input("Enter the number of stations you worked: ")
        self.rounds = input("Enter the number of rounds you went: ")
        self.weight = input("Enter your weight at the end of the workout: ")
    # Define a method named get_summary that calculates calories burned 
    # and returns a summary of the workout
    def get_summary(self):
        calories_burned = int(self.minutes) * 10
        summary = f"\nYou boxed for {self.minutes} minutes, worked {self.stations} stations, went {self.rounds} rounds, and weighed {self.weight} pounds. You burned {calories_burned} calories."
        return summary
