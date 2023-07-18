import tkinter as tk
from tkinter import messagebox
import json


# Global variables
goals = {}
metrics = {}
activity_level = " "
# Global dictionary to store user information
user_info = {}

# Function for the intro component
def intro():
    global name, age, height, weight, gender, activity_levels
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    height = height_entry.get().strip()
    weight = weight_entry.get().strip()
    gender = gender_entry.get().strip().upper()

    if not name or not age or not height or not weight or not gender:
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    try:
        age = int(age)
        height = float(height)
        weight = float(weight)
        if age <= 0 or height <= 0 or weight <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Age should be a positive integer, and height/weight should be positive numbers.")
        return

    if gender not in ("M", "F"):
        messagebox.showerror("Error", "Invalid gender. Please enter 'M' for male or 'F' for female.")
        return

    activity_level_window = tk.Toplevel(window)
    activity_level_window.title("Activity Level")

    activity_label = tk.Label(activity_level_window, text="Select your activity level:")
    activity_label.pack(padx=20, pady=10)

    activity_var = tk.StringVar()
    activity_var.set("1. Sedentary (little to no exercise)")
    activity_levels = [
        "1. Sedentary (little to no exercise)",
        "2. Lightly active (light exercise/sports 1-3 days/week)",
        "3. Moderately active (moderate exercise/sports 3-5 days/week)",
        "4. Very active (hard exercise/sports 6-7 days/week)",
        "5. Super active (very hard exercise/sports & physical job or 2x training)"
    ]

    for level in activity_levels:
        activity_radio = tk.Radiobutton(activity_level_window, text=level, variable=activity_var, value=level)
        activity_radio.pack(padx=20, anchor="w")

    def save_user_information():
        global user_info
        activity_level = activity_var.get()

        gender_display = "Male" if gender == "M" else "Female"

        # Store the user information in the dictionary
        user_info = {
            "Name": name,
            "Age": age,
            "Height": height,
            "Weight": weight,
            "Gender": gender_display,
            "Activity Level": activity_level
        }

        confirm_msg = f"Name: {name}\nAge: {age}\nHeight: {height}\nWeight: {weight}\nGender: {gender_display}\nActivity Level: {activity_level}"
        confirmed = messagebox.askokcancel("User Information", confirm_msg)

        if confirmed:
            # Save the user information as JSON
            with open("user_info.json", "w") as file:
                json.dump(user_info, file)
    
            messagebox.showinfo("Success", "User information saved!")
            activity_level_window.destroy()  # Close the activity level window
            show_menu()
        else:
            # Handle the case if the user cancels the saving of information
            pass
        
    save_button = tk.Button(activity_level_window, text="Save", command=save_user_information)
    save_button.pack(pady=10)


# Function to display the menu options
def show_menu():
    intro_frame.pack_forget()
    menu_frame.pack()


# Function to set the user's goals
def set_goal():
    menu_frame.pack_forget()
    set_goal_frame = tk.Frame(window)
    set_goal_frame.pack(padx=20, pady=20)

    # Create and pack the goal name label and entry
    goal_name_label = tk.Label(set_goal_frame, text="Goal Name:")
    goal_name_label.pack(pady=5)
    goal_name_entry = tk.Entry(set_goal_frame)
    goal_name_entry.pack(pady=5)

    # Create and pack the priority label
    priority_label = tk.Label(set_goal_frame, text="Priority:")
    priority_label.pack(pady=5)

    # Create a StringVar to store the selected priority
    priority_var = tk.StringVar()

    # Function to set the selected priority
    def set_priority(value):
        priority_var.set(value)

    # Create and pack the priority radio buttons
    priority_frame = tk.Frame(set_goal_frame)
    priority_frame.pack(pady=5)

    priorities = ["High", "Medium", "Low"]
    for priority in priorities:
        priority_radio = tk.Radiobutton(priority_frame, text=priority, variable=priority_var, value=priority)
        priority_radio.pack(side=tk.LEFT, padx=5)
    
    # Create and pack the deadline label
    deadline_label = tk.Label(set_goal_frame, text="Deadline:")
    deadline_label.pack(pady=5)

    # Create and pack the spin boxes for day, month, and year
    deadline_frame = tk.Frame(set_goal_frame)
    deadline_frame.pack(pady=5)

    day_label = tk.Label(deadline_frame, text="Day:")
    day_label.pack(side=tk.LEFT, padx=5)
    day_spinbox = tk.Spinbox(deadline_frame, from_=1, to=31, width=5)
    day_spinbox.pack(side=tk.LEFT)

    month_label = tk.Label(deadline_frame, text="Month:")
    month_label.pack(side=tk.LEFT, padx=5)
    month_spinbox = tk.Spinbox(deadline_frame, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"), width=5)
    month_spinbox.pack(side=tk.LEFT)

    year_label = tk.Label(deadline_frame, text="Year:")
    year_label.pack(side=tk.LEFT, padx=5)
    year_spinbox = tk.Spinbox(deadline_frame, from_=2023, to=2100, width=8)
    year_spinbox.pack(side=tk.LEFT)

    # Function to process the goal input and save it
    def process_goal_input():
        goal_name = goal_name_entry.get().strip()

        if not goal_name:
            messagebox.showerror("Error", "Goal name cannot be empty. Please try again.")
            return

        if goal_name in goals:
            messagebox.showerror("Error", "Goal with the same name already exists. Please choose a different name.")
            return

        priority = priority_var.get()
        deadline = f"{day_spinbox.get()}-{month_spinbox.get()}-{year_spinbox.get()}"

        goals[goal_name] = {
            "priority": priority,
            "deadline": deadline
        }

        messagebox.showinfo("Success", "Goal successfully set!")
        set_goal_frame.pack_forget()
        show_menu()

    # Create and pack the submit button
    submit_button = tk.Button(set_goal_frame, text="Submit", command=process_goal_input)
    submit_button.pack(pady=10)

    # Function to go back to the menu
    def back_to_menu():
        set_goal_frame.pack_forget()
        show_menu()

    # Create and pack the back button
    back_button = tk.Button(set_goal_frame, text="Back", command=back_to_menu)
    back_button.pack(pady=10)



# Function to create the tracking metrics frame
def track_metrics():
    global name
    menu_frame.pack_forget()
    track_frame = tk.Frame(window)
    track_frame.pack(padx=20, pady=20)

    # Function to track exercise metrics
    def track_exercise():
        exercise_calories = exercise_entry.get()

        if not exercise_calories:
            messagebox.showerror("Error", "Please enter the number of calories burned.")
            return

        try:
            exercise_calories = float(exercise_calories)
        except ValueError:
            messagebox.showerror("Error", "Calories burned must be a number.")
            return

        metrics["Exercise"] = {"calories": exercise_calories}
        messagebox.showinfo("Success", "Exercise metrics tracked successfully.")

    # Function to track sleep metrics
    def track_sleep():
        sleep_hours = sleep_entry.get()

        if not sleep_hours:
            messagebox.showerror("Error", "Please enter the number of hours slept.")
            return

        try:
            sleep_hours = float(sleep_hours)
        except ValueError:
            messagebox.showerror("Error", "Hours slept must be a number.")
            return

        metrics["Sleep"] = {"hours": sleep_hours}
        messagebox.showinfo("Success", "Sleep metrics tracked successfully.")

    # Function to track diet metrics
    def track_diet():
        diet_calories = diet_entry.get()

        if not diet_calories:
            messagebox.showerror("Error", "Please enter the number of calories consumed.")
            return

        try:
            diet_calories = float(diet_calories)
        except ValueError:
            messagebox.showerror("Error", "Calories consumed must be a number.")
            return

        metrics["Diet"] = {"calories": diet_calories}
        messagebox.showinfo("Success", "Diet metrics tracked successfully.")

    # Function to go back to the menu
    def back_to_menu():
        track_frame.pack_forget()
        show_menu()

    # Create and pack the header
    header_track = tk.Label(track_frame, text=f"{name}'s Metrics Tracking", font=("Arial", 16))
    header_track.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

    # Create and pack the exercise tracking section
    exercise_label = tk.Label(track_frame, text="Enter Calories Burned:")
    exercise_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    exercise_entry = tk.Entry(track_frame, width=10)
    exercise_entry.grid(row=1, column=1, padx=10, pady=5)

    exercise_button = tk.Button(track_frame, text="Track", command=track_exercise)
    exercise_button.grid(row=1, column=2, padx=10, pady=5)

    # Create and pack the sleep tracking section
    sleep_label = tk.Label(track_frame, text="Enter Hours Slept:")
    sleep_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    sleep_entry = tk.Entry(track_frame, width=10)
    sleep_entry.grid(row=2, column=1, padx=10, pady=5)

    sleep_button = tk.Button(track_frame, text="Track", command=track_sleep)
    sleep_button.grid(row=2, column=2, padx=10, pady=5)

    # Create and pack the diet tracking section
    diet_label = tk.Label(track_frame, text="Enter Calories Consumed:")
    diet_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    diet_entry = tk.Entry(track_frame, width=10)
    diet_entry.grid(row=3, column=1, padx=10, pady=5)

    diet_button = tk.Button(track_frame, text="Track", command=track_diet)
    diet_button.grid(row=3, column=2, padx=10, pady=5)

    # Create and pack the back button
    back_button = tk.Button(track_frame, text="Back", command=back_to_menu)
    back_button.grid(row=4, column=0, columnspan=3, pady=10)


    
# Function to show the main menu
def show_main_menu(tracking_metrics_frame, menu_frame):
    tracking_metrics_frame.pack_forget()
    menu_frame.pack()

# Function to display the users tracked metrics
def display_metrics():
    global name
    menu_frame.pack_forget()
    metric_frame = tk.Frame(window)
    metric_frame.pack(padx=20, pady=20)

    # Function to update the priority and deadline for a goal
    def update_goal(goal):
        new_priority = priority_vars[goal].get()
        new_deadline = deadline_entries[goal].get()

        # Update the priority and deadline for the goal
        goals[goal]["priority"] = new_priority
        goals[goal]["deadline"] = new_deadline

        messagebox.showinfo("Success", "Goal updated successfully.")
        
        
        
    # Function to go back to the menu
    def back_to_menu():
        metric_frame.pack_forget()
        show_menu()
            
    # Create and pack the header
    header_metrics = tk.Label(metric_frame, text=f"{name}'s Metrics", font=("Arial", 16))
    header_metrics.grid(row=0, column=0, columnspan=6, padx=20, pady=10)

    # Check if any goals are set
    if len(goals) == 0:
        no_goals_label = tk.Label(metric_frame, text="No goals set. Please set a goal before viewing metrics.")
        no_goals_label.grid(row=1, column=0, columnspan=6, padx=20, pady=10)

        back_button = tk.Button(metric_frame, text="Back", command=back_to_menu)
        back_button.grid(row=2, column=0, columnspan=6, pady=10)
        return

    # Create dictionaries to store the entry fields for priority and deadline
    priority_vars = {}
    deadline_entries = {}

    # Iterate over the goals and display the metrics
    row = 1
    for goal, data in goals.items():
        goal_frame = tk.Frame(metric_frame)
        goal_frame.grid(row=row, column=0, columnspan=7, padx=20, pady=10)

        goal_name_label = tk.Label(goal_frame, text=goal + ":")
        goal_name_label.grid(row=0, column=0, padx=10)

        exercise_label = tk.Label(goal_frame, text="Exercise: " + str(metrics.get("Exercise", {}).get("calories", "-")) + " Calories Burned")
        exercise_label.grid(row=0, column=1, padx=10)

        sleep_label = tk.Label(goal_frame, text="Sleep: " + str(metrics.get("Sleep", {}).get("hours", "-")) + " Hours Slept")
        sleep_label.grid(row=0, column=2, padx=10)

        diet_label = tk.Label(goal_frame, text="Diet: " + str(metrics.get("Diet", {}).get("calories", "-")) + " Calories Consumed")
        diet_label.grid(row=0, column=3, padx=10)

        # Create and grid radio buttons for priority
        priority_label = tk.Label(goal_frame, text="Priority:")
        priority_label.grid(row=1, column=0, padx=10, sticky="w")

        priority_var = tk.StringVar(value=data.get("priority", ""))
        priority_vars[goal] = priority_var

        low_radio = tk.Radiobutton(goal_frame, text="Low", variable=priority_var, value="Low")
        low_radio.grid(row=1, column=1, padx=10, sticky="w")

        medium_radio = tk.Radiobutton(goal_frame, text="Medium", variable=priority_var, value="Medium")
        medium_radio.grid(row=1, column=2, padx=10, sticky="w")

        high_radio = tk.Radiobutton(goal_frame, text="High", variable=priority_var, value="High")
        high_radio.grid(row=1, column=3, padx=10, sticky="w")

        # Create and grid entry box for deadline
        deadline_label = tk.Label(goal_frame, text="Deadline:")
        deadline_label.grid(row=2, column=0, padx=10, sticky="w")

        deadline_entry = tk.Entry(goal_frame, width=10)
        deadline_entry.insert(tk.END, data.get("deadline", ""))
        deadline_entries[goal] = deadline_entry
        deadline_entry.grid(row=2, column=1, padx=5, sticky="w")

        # Create and grid update button
        update_button = tk.Button(goal_frame, text="Update", command=lambda g=goal: update_goal(g))
        update_button.grid(row=2, column=2, padx=10, sticky="w")

        row += 1

    back_button = tk.Button(metric_frame, text="Back", command=back_to_menu)
    back_button.grid(row=row, column=0, columnspan=6, pady=10)


# Function to allow user to edit their information
def edit_user_information():
    global activity_level

    # Hide the menu frame
    menu_frame.pack_forget()

    edit_frame = tk.Frame(window)
    edit_frame.pack(padx=20, pady=20)

    # Display current user information for editing
    age_label = tk.Label(edit_frame, text="Age:")
    age_label.pack(pady=5)
    age_entry = tk.Entry(edit_frame)
    age_entry.insert(0, str(age))
    age_entry.pack(pady=5)

    height_label = tk.Label(edit_frame, text="Height (cm):")
    height_label.pack(pady=5)
    height_entry = tk.Entry(edit_frame)
    height_entry.insert(0, str(height))
    height_entry.pack(pady=5)

    weight_label = tk.Label(edit_frame, text="Weight (kg):")
    weight_label.pack(pady=5)
    weight_entry = tk.Entry(edit_frame)
    weight_entry.insert(0, str(weight))
    weight_entry.pack(pady=5)

    activity_label = tk.Label(edit_frame, text="Activity Level:")
    activity_label.pack(pady=5)

    # Create activity level radio buttons using the global activity_levels list
    activity_var = tk.StringVar(value=activity_level)
    for level in activity_levels:
        activity_radio = tk.Radiobutton(edit_frame, text=level, variable=activity_var, value=level)
        activity_radio.pack(pady=5)

    def submit_updated_information():
        new_age = age_entry.get().strip()
        new_height = height_entry.get().strip()
        new_weight = weight_entry.get().strip()
        new_activity_level = activity_var.get()
    
        if new_age:
            try:
                new_age = int(new_age)
                global age
                age = new_age
                user_info["Age"] = new_age
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Age should be an integer.")
                return
    
        if new_height:
            try:
                new_height = float(new_height)
                global height
                height = new_height
                user_info["Height"] = new_height
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Height should be a number.")
                return
    
        if new_weight:
            try:
                new_weight = float(new_weight)
                global weight
                weight = new_weight
                user_info["Weight"] = new_weight
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Weight should be a number.")
                return
    
        if new_activity_level:
            global activity_level
            activity_level = new_activity_level
            user_info["Activity Level"] = new_activity_level
    
        messagebox.showinfo("Success", "User information updated!")
        edit_frame.pack_forget()
        show_menu()


    submit_button = tk.Button(edit_frame, text="Submit", command=submit_updated_information)
    submit_button.pack(pady=10)

    def back_to_menu():
        edit_frame.pack_forget()
        show_menu()

    back_button = tk.Button(edit_frame, text="Back", command=back_to_menu)
    back_button.pack(pady=10)


# Function to create the Display User Statistics frame
def display_user_stats():
    global user_info
    menu_frame.pack_forget()
    display_frame = tk.Frame(window)
    display_frame.pack(padx=20, pady=20)

    # Retrieve the user's information from the dictionary
    name = user_info.get("Name")
    age = user_info.get("Age")
    height = user_info.get("Height")
    weight = user_info.get("Weight")
    gender = user_info.get("Gender")
    activity_level = user_info.get("Activity Level")

    # Calculate BMI
    bmi = weight / ((height/100) ** 2)

    # Create and pack the BMI label
    bmi_label = tk.Label(display_frame, text=f"BMI: {bmi:.2f}")
    bmi_label.pack(pady=5)

    # Determine BMI category
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif 18.5 <= bmi < 25:
        bmi_category = "Normal weight"
    elif 25 <= bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # Create and pack the BMI category label
    bmi_category_label = tk.Label(display_frame, text=f"BMI Category: {bmi_category}")
    bmi_category_label.pack(pady=5)

    # Print additional messages based on BMI category
    if bmi_category == "Normal weight":
        bmi_message = "You are within a healthy weight range."
    else:
        bmi_message = "You may want to consult a healthcare professional for guidance on maintaining a healthy weight."
    bmi_message_label = tk.Label(display_frame, text=bmi_message)
    bmi_message_label.pack(pady=5)

    # Calculate BMR using the appropriate equation based on gender
    if gender == "Male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "Female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    # Create and pack the BMR label
    bmr_label = tk.Label(display_frame, text=f"BMR: {bmr:.2f} calories")
    bmr_label.pack(pady=5)

    # Calculate recommended daily calorie intake based on activity level
    if activity_level == "1. Sedentary (little to no exercise)":
        calorie_intake = bmr * 1.2
    elif activity_level == "2. Lightly active (light exercise/sports 1-3 days/week)":
        calorie_intake = bmr * 1.375
    elif activity_level == "3. Moderately active (moderate exercise/sports 3-5 days/week)":
        calorie_intake = bmr * 1.55
    elif activity_level == "4. Very active (hard exercise/sports 6-7 days/week)":
        calorie_intake = bmr * 1.725
    elif activity_level == "5. Super active (very hard exercise/sports & physical job or 2x training)":
        calorie_intake = bmr * 1.9

    # Create and pack the recommended calorie intake label
    calorie_intake_label = tk.Label(display_frame, text=f"Recommended Daily Calorie Intake: {calorie_intake:.2f} calories")
    calorie_intake_label.pack(pady=5)

    # Determine exercise duration recommendation based on age
    if age < 6:
        exercise_duration = "Engage in physical activity throughout the day, the more the better"
    elif 6 <= age <= 17:
        exercise_duration = "At least 60 minutes of moderate to vigorous physical activity daily"
    elif 18 <= age <= 64:
        exercise_duration = "At least 150 minutes of moderate-intensity aerobic activity or 75 minutes of vigorous-intensity aerobic activity per week"
    else:
        exercise_duration = "Follow adult guidelines if possible; engage in activities to enhance balance and prevent falls if not possible"

    # Create and pack the exercise duration label
    exercise_duration_label = tk.Label(display_frame, text=f"Exercise Recommendation: {exercise_duration}")
    exercise_duration_label.pack(pady=5)

    # Function to go back to the menu
    def back_to_menu():
        display_frame.pack_forget()
        show_menu()

    # Create and pack the back button
    back_button = tk.Button(display_frame, text="Back", command=back_to_menu)
    back_button.pack(pady=10)




# Function to load the users information
def load_user_information():
    global name, age, height, weight, gender, activity_level

    try:
        with open("user_info.json", "r") as file:
            data = json.load(file)

        # Load user information
        name = data.get("Name", "")
        age = data.get("Age", "")
        height = data.get("Height", "")
        weight = data.get("Weight", "")
        gender = data.get("Gender", "")
        activity_level = data.get("Activity Level", "")

        # Update the entry fields
        name_entry.delete(0, tk.END)
        name_entry.insert(tk.END, name)
        age_entry.delete(0, tk.END)
        age_entry.insert(tk.END, str(age))
        height_entry.delete(0, tk.END)
        height_entry.insert(tk.END, str(height))
        weight_entry.delete(0, tk.END)
        weight_entry.insert(tk.END, str(weight))
        gender_entry.delete(0, tk.END)
        gender_entry.insert(tk.END, gender)

        # Save the user information
        user_info = {
            "Name": name,
            "Age": age,
            "Height": height,
            "Weight": weight,
            "Gender": gender,
            "Activity Level": activity_level
        }

        with open("user_info.json", "w") as file:
            json.dump(user_info, file)

        # Show success message
        messagebox.showinfo("Success", "User information loaded and saved successfully.")

        # Move to the menu frame
        intro_frame.pack_forget()
        show_menu()

    except FileNotFoundError:
        messagebox.showerror("Error", "User information file not found.")






def exit_program():
    # Perform any cleanup actions here if needed
    window.destroy()


# Create the window
window = tk.Tk()
window.title("Health Tracker")

# Create the intro frame
intro_frame = tk.Frame(window)
intro_frame.pack(padx=20, pady=20)

# Create and pack the intro label
intro_label = tk.Label(intro_frame, text="Welcome to Health Tracker!", font=("Arial", 16))
intro_label.pack()

# Create and pack the name label and entry
name_label = tk.Label(intro_frame, text="Name:")
name_label.pack(pady=5)
name_entry = tk.Entry(intro_frame)
name_entry.pack(pady=5)

# Create and pack the age label and entry
age_label = tk.Label(intro_frame, text="Age:")
age_label.pack(pady=5)
age_entry = tk.Entry(intro_frame)
age_entry.pack(pady=5)

# Create and pack the height label and entry
height_label = tk.Label(intro_frame, text="Height (cm):")
height_label.pack(pady=5)
height_entry = tk.Entry(intro_frame)
height_entry.pack(pady=5)

# Create and pack the weight label and entry
weight_label = tk.Label(intro_frame, text="Weight (kg):")
weight_label.pack(pady=5)
weight_entry = tk.Entry(intro_frame)
weight_entry.pack(pady=5)

# Create and pack the gender label and entry
gender_label = tk.Label(intro_frame, text="Gender (M/F):")
gender_label.pack(pady=5)
gender_entry = tk.Entry(intro_frame)
gender_entry.pack(pady=5)

# Create and pack the load button
Load_button = tk.Button(intro_frame, text="Load User Information", command=load_user_information)
Load_button.pack(pady=10)

# Create and pack the submit button
submit_button = tk.Button(intro_frame, text="Submit", command=intro)
submit_button.pack(pady=10)

# Create the menu frame
menu_frame = tk.Frame(window)

# Create and pack the menu label
menu_label = tk.Label(menu_frame, text="What would you like to do?", font=("Arial", 15))
menu_label.pack(pady=20)

# Create and pack the menu options
option1_button = tk.Button(menu_frame, text="1. Set Goal", command=set_goal)
option1_button.pack(pady=5)

option2_button = tk.Button(menu_frame, text="2. Track Metrics", command=track_metrics)
option2_button.pack(pady=5)

option3_button = tk.Button(menu_frame, text="3. Display Metrics", command=display_metrics)
option3_button.pack(pady=5)

option4_button = tk.Button(menu_frame, text="4. Update User Information", command=edit_user_information)
option4_button.pack(pady=5)

option5_button = tk.Button(menu_frame, text="5. Display User Statistics", command=display_user_stats)
option5_button.pack(pady=5)

option6_button = tk.Button(menu_frame, text="6. Exit", command=exit_program)
option6_button.pack(pady=5)

# Hide the menu frame initially
menu_frame.pack_forget()

# Start the main event loop
window.mainloop()
