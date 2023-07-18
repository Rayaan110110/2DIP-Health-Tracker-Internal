# Global variables
goals = {}
metrics = {}
activity_level = " "

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
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Age should be an integer, and height/weight should be numbers.")
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
            activity_level = activity_var.get()
        
            gender_display = "Male" if gender == "M" else "Female"
        
            confirm_msg = f"Name: {name}\nAge: {age}\nHeight: {height}\nWeight: {weight}\nGender: {gender_display}\nActivity Level: {activity_level}"
            confirmed = messagebox.askokcancel("User Information", confirm_msg)
        
            if confirmed:
                # Save the user information or perform any desired action with the data
                # For now, let's just display a message box
                messagebox.showinfo("Success", "User information saved!")
                activity_level_window.destroy()  # Close the activity level window
                show_menu()
            else:
                # User clicked "Cancel"
                messagebox.showinfo("Cancelled", "User information not saved.")

    save_button = tk.Button(activity_level_window, text="Save", command=save_user_information)
    save_button.pack(pady=10)