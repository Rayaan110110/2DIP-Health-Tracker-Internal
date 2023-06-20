#Version 1 Health Tracker

# Create Dictionary for Goals
goals = {}

print("Welcome to the Health Tracker program!")

# Function to set a new goal
def set_goal():
    while True:
        print("What is your new goal?")
        goal_name = input()
        
        if not goal_name:
            print("Goal name cannot be empty. Please try again.")
            continue
        
        try:
            int(goal_name)  # Check if the goal name is numeric
            print("Invalid goal name. Goal name cannot be a numeric value. Please try again.")
        except ValueError:
            if goal_name in goals:  # Check if the goal name already exists
                print("Goal with the same name already exists. Please choose a different name.")
            else:
                goals[goal_name] = {"exercise": 0, "diet": 0, "sleep": 0}  # Add the new goal to the goals dictionary
                print("Goal successfully set!")
                break
            

# Function to track exercise
def track_exercise():
    if not goals:
        print("No goals have been set. Please set a goal before tracking exercise.")
        return
    
    print("How many calories did you burn during exercise?")
    while True:
        try:
            calories_burned = float(input())  # Get the calories burned from the user
            if calories_burned < 0:  # Check if the input is valid (not negative)
                print("Invalid input. Calories burned cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for calories burned.")
    
    for goal in goals:  # Update the exercise calories for all goals
        goals[goal]["exercise"] += calories_burned
    
    print("Exercise successfully tracked!")


# Function to track diet
def track_diet():
    if not goals:
        print("No goals have been set. Please set a goal before tracking diet.")
        return
    
    print("How many calories did you consume?")
    while True:
        calories_consumed = input()  # Get the calories consumed from the user
        try:
            calories_consumed = float(calories_consumed)
            if calories_consumed < 0:  # Check if the input is valid (not negative)
                print("Invalid input. Calories consumed cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for calories consumed.")
    
    for goal in goals:  # Update the diet calories for all goals
        goals[goal]["diet"] += calories_consumed
    print("Diet successfully tracked!")


# Function to track sleep
def track_sleep():
    if not goals:
        print("No goals have been set. Please set a goal before tracking sleep.")
        return
    
    print("How many hours did you sleep?")
    while True:
        try:
            hours_slept = float(input())  # Get the hours slept from the user
            if hours_slept < 0:  # Check if the input is valid (not negative)
                print("Invalid input. Hours slept cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for hours slept.")
    
    for goal in goals:  # Update the sleep hours for all goals
        goals[goal]["sleep"] += hours_slept
    
    print("Sleep successfully tracked!")


# Function to display goals and metrics
def display_metrics():
    if not goals:
        print("No goals currently set.")
        return

    for goal in goals:  # Display the exercise, diet, and sleep metrics for each goal
        print(goal + ":")
        print("Exercise:", goals[goal]["exercise"], "calories burned")
        print("Diet:", goals[goal]["diet"], "calories consumed")
        print("Sleep:", goals[goal]["sleep"], "hours slept")

# Main routine
while True:
    print("What would you like to do?")
    print("1. Set a new goal")
    print("2. Track exercise")
    print("3. Track diet")
    print("4. Track sleep")
    print("5. Display metrics")
    print("6. Exit")
    
    try:
        choice = int(input())  # Get the user's choice
    except ValueError:
        print("Invalid input. Please enter a numeric choice.")
        continue

    if choice == 1:
        set_goal()  # Call the set_goal() function
    elif choice == 2:
        track_exercise()  # Call the track_exercise() function
    elif choice == 3:
        track_diet()  # Call the track_diet() function
    elif choice == 4:
        track_sleep()  # Call the track_sleep() function
    elif choice == 5:
        display_metrics()  # Call the display_metrics() function
    elif choice == 6:
        print("Thank you for using the Health Tracker program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-6).")
