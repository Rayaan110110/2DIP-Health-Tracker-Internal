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