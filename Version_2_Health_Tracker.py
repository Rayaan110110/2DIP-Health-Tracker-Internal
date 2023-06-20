# Version 2 Health Tracker

# Create Dictionary for Goals
goals = {}


# Function for the intro component
def intro():
    # Print welcome message
    print("Welcome to the Health Tracker program!")
    print("Let's get started.")

    # Loop until a valid name is entered
    while True:
        # Prompt the user to enter their name
        name = input("Enter your name: ")
        if not name:
            # If no name is entered, prompt again
            print("Invalid input. Please enter a valid name.")
        else:
            # Greet the user with their name and break the loop
            print("Hello, " + name + "!")
            break

    # Get user's age using a helper function
    age = get_positive_integer("Enter your age: ")

    # Get user's height in centimeters using a helper function
    height = get_positive_float("Enter your height in centimeters: ")

    # Get user's weight in kilograms using a helper function
    weight = get_positive_float("Enter your weight in kilograms: ")

    # Loop until a valid gender is entered
    while True:
        # Prompt the user to enter their gender
        gender = input("Enter your gender (M/F): ")
        if gender.upper() in ("M", "F"):
            # If a valid gender is entered, break the loop
            break
        else:
            # If an invalid gender is entered, prompt again
            print("Invalid gender. Please enter 'M' for male or 'F' for female.")

    # Store user's information in the goals dictionary
    goals["user"] = {"name": name, "age": age, "height": height, "weight": weight, "gender": gender.upper()}


# Function to get a positive integer from user input
def get_positive_integer(message):
    while True:
        try:
            # Prompt the user to enter an integer value
            value = int(input(message))
            if value <= 0:
                # If a non-positive integer is entered, prompt again
                print("Invalid input. Please enter a positive integer.")
                continue
            # Return the valid positive integer
            return value
        except ValueError:
            # If an invalid integer is entered, prompt again
            print("Invalid input. Please enter a valid integer.")


# Function to get a positive float from user input
def get_positive_float(message):
    while True:
        try:
            # Prompt the user to enter a float value
            value = float(input(message))
            if value <= 0:
                # If a non-positive float is entered, prompt again
                print("Invalid input. Please enter a positive number.")
                continue
            # Return the valid positive float
            return value
        except ValueError:
            # If an invalid float is entered, prompt again
            print("Invalid input. Please enter a valid number.")


# Function to set a new goal
def set_goal():
    print("What is your new goal?")
    goal_name = input()

    if not goal_name:
        # Check if the goal name is empty
        print("Goal name cannot be empty. Please try again.")
        return set_goal()
    if goal_name in goals:
        # Check if a goal with the same name already exists
        print("Goal with the same name already exists. Please choose a different name.")
        return set_goal()

    # Retrieve user information from goals dictionary
    name = goals["user"]["name"]
    age = goals["user"]["age"]
    height = goals["user"]["height"]
    weight = goals["user"]["weight"]
    deadline = input("Enter the deadline for your goal (optional): ")
    priority = input("Enter the priority of your goal (high, medium, low): ")

    # Add the new goal to the goals dictionary
    goals[goal_name] = {
        "name": name,
        "exercise": 0,
        "diet": 0,
        "sleep": 0,
        "age": age,
        "height": height,
        "weight": weight,
        "deadline": deadline,
        "priority": priority
    }
    
    print("Goal successfully set!")


# Function to track exercise
def track_exercise():
    if not goals or len(goals) == 1:
        # Check if goals dictionary is empty or only contains user information
        print("No goals have been set. Please set a goal before tracking exercise.")
        return

    print("How many calories did you burn during exercise?")
    calories_burned = get_positive_float("Calories burned: ")

    # Update exercise value for all goals (excluding user information)
    for goal in goals.values():
        if goal is not goals["user"]:
            if "exercise" in goal:
                goal["exercise"] += calories_burned     
            else:
                goal["exercise"] = calories_burned

    print("Exercise successfully tracked!")


# Function to track diet
def track_diet():
    if not goals or len(goals) == 1:
        # Check if goals dictionary is empty or only contains user information
        print("No goals have been set. Please set a goal before tracking diet.")
        return
    
    print("How many calories did you consume?")
    calories_consumed = get_positive_float("Calories consumed: ")
    
    # Update diet value for all goals (excluding user information)
    for goal in goals.values():
        if "diet" in goal:
            goal["diet"] += calories_consumed
        else:
            goal["diet"] = calories_consumed
    
    print("Diet successfully tracked!")


# Function to track sleep
def track_sleep():
    if not goals or len(goals) == 1:
        # Check if goals dictionary is empty or only contains user information
        print("No goals have been set. Please set a goal before tracking sleep.")
        return

    print("How many hours did you sleep?")
    hours_slept = get_positive_float("Hours slept: ")

    # Update sleep value for all goals (excluding user information)
    for goal in goals.values():
        if "sleep" in goal:
            goal["sleep"] += hours_slept
        else:
            goal["sleep"] = hours_slept

    print("Sleep successfully tracked!")
    


# Function to display metrics
def display_metrics():
    if not goals or len(goals) == 1:
        # Check if goals dictionary is empty or only contains user information
        print("No goals currently set, please set a goal before viewing metrics.")
        return

    # Iterate over goals and display exercise, diet, and sleep metrics for each goal
    for goal_name, goal in goals.items():
        if goal is not goals["user"]:
            print("Goal:", goal_name)
            print("Exercise:", goal.get("exercise", 0), "calories burned")
            print("Diet:", goal.get("diet", 0), "calories consumed")
            print("Sleep:", goal.get("sleep", 0), "hours slept")
            print()

    # Additional option to display BMI, recommended calorie intake, or recommended exercise duration
    print("Additional Metrics:")
    print("1. View BMI")
    print("2. View Recommended Daily Calorie Intake")
    print("3. View Recommended Exercise Duration")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid input. Please enter a numeric choice.")
            continue

        if choice == 1:
            height = goals["user"]["height"]
            weight = goals["user"]["weight"]
            view_bmi(height, weight)
            break
        elif choice == 2:
            view_calorie_intake(goals["user"]["gender"])
            break
        elif choice == 3:
            view_exercise_duration()
            break
        else: 
            print("Invalid choice. Please enter a valid option (1-3).")


# Function to calculate and display BMI
def view_bmi(height, weight):
    bmi = calculate_bmi(height, weight)
    category = get_bmi_category(bmi)
    
    print("Your BMI is: {:.2f}".format(bmi))
    print("Category: ", category)
    
    if category == "Normal weight":
        print("You are within a healthy weight range.")
    else:
        print("You may want to consult a healthcare professional for guidance on maintaining a healthy weight.")


# Function to calculate and display recommended daily calorie intake
def view_calorie_intake(gender):
    age = goals["user"]["age"]
    height = goals["user"]["height"]
    weight = goals["user"]["weight"]
    calorie_intake = calculate_calorie_intake(age, height, weight, gender)

    print("Recommended Daily Calorie Intake: {:.2f} calories".format(calorie_intake))


# Function to calculate and display recommended exercise duration
def view_exercise_duration():
    age = goals["user"]["age"]
    exercise_duration = calculate_exercise_duration(age)

    print("Recommended Exercise Duration:", exercise_duration)


# Function to calculate recommended daily calorie intake
def calculate_calorie_intake(age, height, weight, gender):
    if gender == "M":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "F":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    calorie_intake = bmr * 1.2  # Assuming a sedentary lifestyle

    return calorie_intake


# Function to calculate recommended exercise duration
def calculate_exercise_duration(age):
    if age < 6:
        return ("Engage in physical activity throughout the day, the more the better")
    elif 6 <= age <= 17:
        return ("At least 60 minutes of moderate to vigorous physical activity daily")
    elif 18 <= age <= 64:
        return ("At least 150 minutes of moderate-intensity aerobic activity or 75 minutes of vigorous-intensity aerobic activity per week")
    else:
        return ("Follow adult guidelines if possible; engage in activities to enhance balance and prevent falls if not possible")


# Function to calculate BMI
def calculate_bmi(height, weight):
    height_m = height / 100  # Convert height from centimeters to meters
    bmi = weight / (height_m ** 2)
    return bmi


# Function to determine BMI category
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Main routine
def main():
    intro()

    while True:
        print("\nWhat would you like to do?")
        print("1. Set a new goal")
        print("2. Track exercise")
        print("3. Track diet")
        print("4. Track sleep")
        print("5. Display metrics")
        print("6. Exit")

        try:
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter a numeric choice.")
            continue

        if choice == 1:
            set_goal()
        elif choice == 2:
            track_exercise()
        elif choice == 3:
            track_diet()
        elif choice == 4:
            track_sleep()
        elif choice == 5:
            display_metrics()
        elif choice == 6:
            print("Thank you for using the Health Tracker program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-6).")



# Run the program
main()
