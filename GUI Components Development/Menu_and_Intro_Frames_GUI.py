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