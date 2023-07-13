# Function to create the Set Goal frame
def set_goal():
    menu_frame.pack_forget()
    set_goal_frame = tk.Frame(window)
    set_goal_frame.pack(padx=20, pady=20)

    # Create and pack the goal name label and entry
    goal_name_label = tk.Label(set_goal_frame, text="Goal Name:")
    goal_name_label.pack(pady=5)
    goal_name_entry = tk.Entry(set_goal_frame)
    goal_name_entry.pack(pady=5)

    # Create and pack the deadline label and entry
    deadline_label = tk.Label(set_goal_frame, text="Deadline (optional):")
    deadline_label.pack(pady=5)
    deadline_entry = tk.Entry(set_goal_frame)
    deadline_entry.pack(pady=5)

    # Create and pack the priority label and entry
    priority_label = tk.Label(set_goal_frame, text="Priority (high/medium/low):")
    priority_label.pack(pady=5)
    priority_entry = tk.Entry(set_goal_frame)
    priority_entry.pack(pady=5)

    # Function to process the goal input and save it
    def process_goal_input():
        goal_name = goal_name_entry.get().strip()

        if not goal_name:
            messagebox.showerror("Error", "Goal name cannot be empty. Please try again.")
            return

        if goal_name in goals:
            messagebox.showerror("Error", "Goal with the same name already exists. Please choose a different name.")
            return

        name = name_entry.get().strip()
        age = age_entry.get().strip()
        height = height_entry.get().strip()
        weight = weight_entry.get().strip()
        deadline = deadline_entry.get().strip()
        priority = priority_entry.get().strip()

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