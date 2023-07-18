# Function to create the Display User Statistics frame
def display_user_statistics():
    global gender, age, height, weight, activity_level
    menu_frame.pack_forget()
    display_frame = tk.Frame(window)
    display_frame.pack(padx=20, pady=20)

    # Calculate BMI
    bmi = weight / ((height/100) ** 2)

    # Create and pack the BMI label
    bmi_label = tk.Label(display_frame, text=f"BMI: {bmi:.2f}")
    bmi_label.pack(pady=5)

    # Calculate BMR using the appropriate equation based on gender
    if gender == "M":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "F":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    # Create and pack the BMR label
    bmr_label = tk.Label(display_frame, text=f"BMR: {bmr:.2f} calories")
    bmr_label.pack(pady=5)

    # Calculate recommended daily calorie intake based on activity level
    if activity_level == "little or no exercise":
        calorie_intake = bmr * 1.2
    elif activity_level == "light exercise":
        calorie_intake = bmr * 1.375
    elif activity_level == "moderate exercise":
        calorie_intake = bmr * 1.55
    elif activity_level == "very active":
        calorie_intake = bmr * 1.725
    elif activity_level == "extra active":
        calorie_intake = bmr * 1.9

    # Create and pack the recommended calorie intake label
    calorie_intake_label = tk.Label(display_frame, text=f"Recommended Daily Calorie Intake: {calorie_intake:.2f} calories")
    calorie_intake_label.pack(pady=5)

    # Calculate recommended exercise duration
    exercise_duration = calorie_intake / 7.0

    # Create and pack the recommended exercise duration label
    exercise_duration_label = tk.Label(display_frame, text=f"Recommended Exercise Duration: {exercise_duration:.2f} minutes")
    exercise_duration_label.pack(pady=5)

    # Function to go back to the menu
    def back_to_menu():
        display_frame.pack_forget()
        show_menu()

    # Create and pack the back button
    back_button = tk.Button(display_frame, text="Back", command=back_to_menu)
    back_button.pack(pady=10)