# Function to create the tracking metrics frame
def track_metrics():
    menu_frame.pack_forget()
    tracking_metrics = tk.Frame(window)
    tracking_metrics.pack(padx=20, pady=20)

    # Function to process the metric input and save it
    def process_metric_input(metric):
        calories_entry = calories_entry_dict[metric].get().strip()
        hours_entry = hours_entry_dict[metric].get().strip()

        if not calories_entry or not hours_entry:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        try:
            calories = float(calories_entry)
            hours = float(hours_entry)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Calories and hours should be numbers.")
            return

        # Save the metric values or perform any desired action with the data
        # For now, let's display a message box
        messagebox.showinfo("Success", f"{metric} tracked successfully!")
        calories_entry_dict[metric].delete(0, tk.END)
        hours_entry_dict[metric].delete(0, tk.END)

    # Function to show the metric input fields
    def show_metric_input(metric, calories_label_text, hours_label_text):
        # Clear any previous input
        calories_entry.delete(0, tk.END)
        hours_entry.delete(0, tk.END)
    
        # Adjust the entry labels and fields based on the metric
        if metric == "Exercise":
            calories_label.configure(text=calories_label_text)
            hours_label.pack_forget()
            hours_entry.pack_forget()
            calories_label.pack()
            calories_entry.pack()
        elif metric == "Diet":
            calories_label.configure(text=calories_label_text)
            hours_label.configure(text=hours_label_text)
            calories_label.pack()
            calories_entry.pack()
            hours_label.pack_forget()
            hours_entry.pack_forget()
        elif metric == "Sleep":
            calories_label.configure(text=calories_label_text)
            hours_label.configure(text=hours_label_text)
            calories_label.pack_forget()
            calories_entry.pack_forget()
            hours_label.pack()
            hours_entry.pack()

        # Update the submit button command
        submit_button.configure(command=lambda: process_metric_input(metric))

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

    # Create and pack the submit button
    submit_button = tk.Button(tracking_metrics_frame, text="Submit")
    submit_button.pack(pady=10)