def track_metrics_frame():
    menu_frame.pack_forget()
    tracking_metrics_frame = tk.Frame(window)
    tracking_metrics_frame.pack(padx=20, pady=20)

    # Dictionary to store the metric labels
    metric_labels = {}

    def process_metric_input(metric):
        calories_entry = calories_entry_dict[metric].get().strip()
        hours_entry = hours_entry_dict[metric].get().strip()
    
        if not calories_entry and not hours_entry:
            messagebox.showerror("Error", "Please fill in at least one field.")
            return
    
        try:
            calories = float(calories_entry) if calories_entry else 0.0
            hours = float(hours_entry) if hours_entry else 0.0
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Calories and hours should be numbers.")
            return
    
        # Update the metrics dictionary with user input
        metrics[metric] = {"calories": calories, "hours": hours}
    
        # Save the metric values or perform any desired action with the data
        if calories_entry and hours_entry:
            messagebox.showinfo("Success", f"{metric} successfully tracked. Calories: {calories}, Hours: {hours}")
        elif calories_entry:
            messagebox.showinfo("Success", f"{metric} calories successfully tracked. Calories: {calories}")
        else:
            messagebox.showinfo("Success", f"{metric} hours successfully tracked. Hours: {hours}")
    
        calories_entry_dict[metric].delete(0, tk.END)
        hours_entry_dict[metric].delete(0, tk.END)
    
        # Update the metric labels
        update_metric_labels()
    
        # Update the goals with the tracked metrics
        for goal in goals.values():
            goal[metric.lower()] = metrics[metric]    


    def update_metric_labels():
        # Update the metric labels based on the tracked metrics
        for metric, data in metrics.items():
            calories = data.get("calories", "-")
            hours = data.get("hours", "-")
            metric_labels[metric].configure(text=f"{metric}: {calories} Calories, {hours} Hours")

    def show_metric_input(metric, calories_label_text, hours_label_text):
        # Clear any previous input
        calories_entry.delete(0, tk.END)
        hours_entry.delete(0, tk.END)

        # Hide both the calories and hours labels and entry boxes
        calories_label.pack_forget()
        calories_entry.pack_forget()
        hours_label.pack_forget()
        hours_entry.pack_forget()

        # Adjust the entry labels and fields based on the metric
        if metric == "Exercise":
            calories_label.configure(text=calories_label_text)
            calories_label.pack()
            calories_entry.pack()
        elif metric == "Diet":
            calories_label.configure(text=calories_label_text)
            hours_label.configure(text=hours_label_text)
            calories_label.pack()
            calories_entry.pack()
        elif metric == "Sleep":
            hours_label.configure(text=hours_label_text)
            hours_label.pack()
            hours_entry.pack()

        # Update the submit button command
        submit_button.configure(command=lambda: process_metric_input(metric))
        submit_button.pack(side=tk.BOTTOM, pady=5)  # Show the submit button below the entry box

    # Create and pack the track exercise button
    track_exercise_button = tk.Button(tracking_metrics_frame, text="Track Exercise",
                                      command=lambda: show_metric_input("Exercise",
                                                                        "Enter Calories Burned:",
                                                                        "Enter Hours Slept:"))
    track_exercise_button.pack(pady=5)

    # Create and pack the track sleep button
    track_sleep_button = tk.Button(tracking_metrics_frame, text="Track Sleep",
                                   command=lambda: show_metric_input("Sleep",
                                                                     "Enter Calories Burned:",
                                                                     "Enter Hours Slept:"))
    track_sleep_button.pack(pady=5)

    # Create and pack the track diet button
    track_diet_button = tk.Button(tracking_metrics_frame, text="Track Diet",
                                  command=lambda: show_metric_input("Diet",
                                                                    "Enter Calories Consumed:",
                                                                    "Enter Hours Slept:"))
    track_diet_button.pack(pady=5)

    # Create and pack the entry boxes for calories and hours
    calories_label = tk.Label(tracking_metrics_frame, text="Calories:")
    calories_label.pack_forget()  # Hide initially
    calories_entry = tk.Entry(tracking_metrics_frame)
    calories_entry.pack_forget()  # Hide initially

    hours_label = tk.Label(tracking_metrics_frame, text="Hours:")
    hours_label.pack_forget()  # Hide initially
    hours_entry = tk.Entry(tracking_metrics_frame)
    hours_entry.pack_forget()  # Hide initially

    # Create dictionaries to store the entry fields for each metric
    calories_entry_dict = {"Exercise": calories_entry, "Diet": calories_entry, "Sleep": calories_entry}
    hours_entry_dict = {"Exercise": hours_entry, "Diet": hours_entry, "Sleep": hours_entry}

    # Create and pack the submit button (initially hidden)
    submit_button = tk.Button(tracking_metrics_frame, text="Submit")

    # Create and pack the back button
    back_button = tk.Button(tracking_metrics_frame, text="Back to Main Menu", command=lambda: show_main_menu(tracking_metrics_frame, menu_frame))
    back_button.pack(pady=10)