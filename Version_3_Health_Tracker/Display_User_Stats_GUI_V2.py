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