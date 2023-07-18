# Function to create the tracking metrics frame
def track_metrics():
    global name
    menu_frame.pack_forget()
    track_frame = tk.Frame(window)
    track_frame.pack(padx=20, pady=20)

    # Function to track exercise metrics
    def track_exercise():
        exercise_calories = exercise_entry.get()
        
        if not exercise_calories:
            messagebox.showerror("Error", "Please enter the number of calories burned.")
            return
        
        try:
            exercise_calories = float(exercise_calories)
        except ValueError:
            messagebox.showerror("Error", "Calories burned must be a number.")
            return
        
        metrics["Exercise"] = {"calories": exercise_calories}
        messagebox.showinfo("Success", "Exercise metrics tracked successfully.")
    
    # Function to track sleep metrics
    def track_sleep():
        sleep_hours = sleep_entry.get()
        
        if not sleep_hours:
            messagebox.showerror("Error", "Please enter the number of hours slept.")
            return
        
        try:
            sleep_hours = float(sleep_hours)
        except ValueError:
            messagebox.showerror("Error", "Hours slept must be a number.")
            return
        
        metrics["Sleep"] = {"hours": sleep_hours}
        messagebox.showinfo("Success", "Sleep metrics tracked successfully.")
    
    # Function to track diet metrics
    def track_diet():
        diet_calories = diet_entry.get()
        
        if not diet_calories:
            messagebox.showerror("Error", "Please enter the number of calories consumed.")
            return
        
        try:
            diet_calories = float(diet_calories)
        except ValueError:
            messagebox.showerror("Error", "Calories consumed must be a number.")
            return
        
        metrics["Diet"] = {"calories": diet_calories}
        messagebox.showinfo("Success", "Diet metrics tracked successfully.")   

    # Function to go back to the menu
    def back_to_menu():
        track_frame.pack_forget()
        show_menu()

    # Create and pack the header
    header_track = tk.Label(track_frame, text=f"{name}'s Metrics Tracking", font=("Arial", 16))
    header_track.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

    # Create and pack the exercise tracking section
    exercise_label = tk.Label(track_frame, text="Enter Calories Burned:")
    exercise_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    exercise_entry = tk.Entry(track_frame, width=10)
    exercise_entry.grid(row=1, column=1, padx=10, pady=5)

    exercise_button = tk.Button(track_frame, text="Track", command=track_exercise)
    exercise_button.grid(row=1, column=2, padx=10, pady=5)

    # Create and pack the sleep tracking section
    sleep_label = tk.Label(track_frame, text="Enter Hours Slept:")
    sleep_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    sleep_entry = tk.Entry(track_frame, width=10)
    sleep_entry.grid(row=2, column=1, padx=10, pady=5)

    sleep_button = tk.Button(track_frame, text="Track", command=track_sleep)
    sleep_button.grid(row=2, column=2, padx=10, pady=5)

    # Create and pack the diet tracking section
    diet_label = tk.Label(track_frame, text="Enter Calories Consumed:")
    diet_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    diet_entry = tk.Entry(track_frame, width=10)
    diet_entry.grid(row=3, column=1, padx=10, pady=5)

    diet_button = tk.Button(track_frame, text="Track", command=track_diet)
    diet_button.grid(row=3, column=2, padx=10, pady=5)

    # Create and pack the back button
    back_button = tk.Button(track_frame, text="Back", command=back_to_menu)
    back_button.grid(row=4, column=0, columnspan=3, pady=10)