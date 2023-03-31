# Define JiuJitsu class
class JiuJitsu:
    # Define an init method and initialize instance variables 
    # with default values of 0
    def __init__(self):
        self.minutes = 0
        self.partners = 0
        self.submissions = 0
        self.weight = 0
    # Define a method named log_workout that prompts the user 
    # to input workout parameters
    def log_workout(self):
        self.minutes = input("Enter the number of minutes you rolled: ")
        self.partners = input("Enter the number of partners you trained with: ")
        self.submissions = input("Enter the number of submissions you got: ")
        self.weight = input("Enter your weight at the end of the workout: ")
    # Define a method named get_summary that calcules calories burned 
    # and returns a summary of the workout
    def get_summary(self):
        calories_burned = int(self.minutes) * 15
        summary = f"\nYou rolled for {self.minutes} minutes, trained with {self.partners} partners, got {self.submissions} submissions, and weighed {self.weight} pounds. You burned {calories_burned} calories."
        return summary
