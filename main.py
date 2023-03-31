# Import the Boxing and JiuJitsu classes from separate modules

from boxing import Boxing
from jiujitsu import JiuJitsu

# Define the main function which allows user to 
# input and log their jiu jitsu and boxing workouts

def main():
    while True:
        # Display the main menu
        print();
        print("------------The Combat Training Logger------------");
        print();
        print("Welcome to the Workout Log!\n")

        # Prompt the user to enter the type of workout they would like to log

        workout_type = input("\nEnter your workout type.  1 for boxing or 2 for jiujitsu: ")

        # Create an instance of the Boxing class and call the
        # log_workout method if boxing or jiujitsu options are selected

        if workout_type == "1":
            boxing = Boxing()
            boxing.log_workout()
            summary = boxing.get_summary()
        elif workout_type == "2":
            jiu_jitsu = JiuJitsu()
            jiu_jitsu.log_workout()
            summary = jiu_jitsu.get_summary()
        else:
            # Display an error message if the user enters an invalid option 
            # and continue the program
            print("Invalid input. Please enter 1 or 2.")
            continue
        # Write the summary of the workout to a file named "trainingSummary.txt"
        print(summary)
        with open("trainingSummary.txt", "a") as f:
            f.write(summary + "\n")
        # Prompt the user to log another workout
        another_workout = input("\nWould you like to log another workout? (y/n): ")
        if another_workout.lower() != "y":
            print()
            print("Great job...see you next time!")
            break

# Check if the program is being run as the main module
if __name__ == "__main__":
    main()
