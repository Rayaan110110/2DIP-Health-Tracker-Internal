# Function to display the metrics and goals
def display_metrics():
    global name
    metric_display = tk.Toplevel(window)
    metric_display.title("Tracked Metrics")
    
    # Create and pack the header
    header_metrics = tk.Label(metric_display, text=f"{name}'s Metrics", font=("Arial", 16))
    header_metrics.pack(padx=20, pady=10)

    # Check if any goals are set
    if len(goals) == 0:
        no_goals_label = tk.Label(metric_display, text="No goals set.")
        no_goals_label.pack(padx=20, pady=10)

        back_button = tk.Button(metric_display, text="Back", command=metric_display.destroy)
        back_button.pack(pady=10)
        return
    
    # Iterate over the goals and display the metrics
    for goal, data in goals.items():
        goal_frame = tk.Frame(metric_display)
        goal_frame.pack(padx=20, pady=10)

        goal_name_label = tk.Label(goal_frame, text=goal + ":")
        goal_name_label.pack(side=tk.LEFT, padx=10)

        exercise_label = tk.Label(goal_frame, text="Exercise: " + str(data.get("exercise", "-")) + " Calories Burned")
        exercise_label.pack(side=tk.LEFT, padx=10)

        sleep_label = tk.Label(goal_frame, text="Sleep: " + str(data.get("sleep", "-")) + " Hours Slept")
        sleep_label.pack(side=tk.LEFT, padx=10)

        diet_label = tk.Label(goal_frame, text="Diet: " + str(data.get("diet", "-")) + " Calories Consumed")
        diet_label.pack(side=tk.LEFT, padx=10)
        
    back_button = tk.Button(metric_display, text="Back", command=metric_display.destroy)
    back_button.pack(pady=10)