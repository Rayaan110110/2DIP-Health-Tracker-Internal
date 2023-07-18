def edit_user_information():
    global activity_level

    # Hide the menu frame
    menu_frame.pack_forget()

    edit_frame = tk.Frame(window)
    edit_frame.pack(padx=20, pady=20)

    # Display current user information for editing
    age_label = tk.Label(edit_frame, text="Age:")
    age_label.pack(pady=5)
    age_entry = tk.Entry(edit_frame)
    age_entry.insert(0, str(age))
    age_entry.pack(pady=5)

    height_label = tk.Label(edit_frame, text="Height (cm):")
    height_label.pack(pady=5)
    height_entry = tk.Entry(edit_frame)
    height_entry.insert(0, str(height))
    height_entry.pack(pady=5)

    weight_label = tk.Label(edit_frame, text="Weight (kg):")
    weight_label.pack(pady=5)
    weight_entry = tk.Entry(edit_frame)
    weight_entry.insert(0, str(weight))
    weight_entry.pack(pady=5)

    activity_label = tk.Label(edit_frame, text="Activity Level:")
    activity_label.pack(pady=5)

    # Create activity level radio buttons using the global activity_levels list
    activity_var = tk.StringVar(value=activity_level)
    for level in activity_levels:
        activity_radio = tk.Radiobutton(edit_frame, text=level, variable=activity_var, value=level)
        activity_radio.pack(pady=5)

    def submit_updated_information():
        new_age = age_entry.get().strip()
        new_height = height_entry.get().strip()
        new_weight = weight_entry.get().strip()
        new_activity_level = activity_var.get()

        if new_age:
            try:
                new_age = int(new_age)
                global age
                age = new_age
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Age should be an integer.")
                return

        if new_height:
            try:
                new_height = float(new_height)
                global height
                height = new_height
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Height should be a number.")
                return

        if new_weight:
            try:
                new_weight = float(new_weight)
                global weight
                weight = new_weight
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Weight should be a number.")
                return

        if new_activity_level:
            global activity_level
            activity_level = new_activity_level

        messagebox.showinfo("Success", "User information updated!")
        edit_frame.pack_forget()
        show_menu()

    submit_button = tk.Button(edit_frame, text="Submit", command=submit_updated_information)
    submit_button.pack(pady=10)

    def back_to_menu():
        edit_frame.pack_forget()
        show_menu()

    back_button = tk.Button(edit_frame, text="Back", command=back_to_menu)
    back_button.pack(pady=10)