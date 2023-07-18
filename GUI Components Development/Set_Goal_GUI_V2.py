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
    day_spinbox = tk.Spinbox(deadline_frame, width=5)
    day_spinbox.pack(side=tk.LEFT)

    month_label = tk.Label(deadline_frame, text="Month:")
    month_label.pack(side=tk.LEFT, padx=5)
    month_spinbox = tk.Spinbox(deadline_frame, width=5)
    month_spinbox.pack(side=tk.LEFT)

    year_label = tk.Label(deadline_frame, text="Year:")
    year_label.pack(side=tk.LEFT, padx=5)
    year_spinbox = tk.Spinbox(deadline_frame, width=8)
    year_spinbox.pack(side=tk.LEFT)

    # Function to process the goal input and save it
    def process_goal_input():
        goal_name = goal_name_entry.get().strip()
    
        if not goal_name:
            return
    
        if goal_name in goals:
            return
    
        priority = priority_var.get()
        deadline = f"{day_spinbox.get()}-{month_spinbox.get()}-{year_spinbox.get()}"
    
        goals[goal_name] = {
            "priority": priority,
            "deadline": deadline
        }
    
        set_goal_frame.pack_forget()
        show_menu()