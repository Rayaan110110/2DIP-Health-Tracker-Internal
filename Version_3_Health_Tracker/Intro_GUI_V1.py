# Function for the intro component
def intro():
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

    # Create a confirmation message box
    confirm_msg = f"Name: {name}\nAge: {age}\nHeight: {height}\nWeight: {weight}\nGender: {gender}"
    confirmed = messagebox.askokcancel("User Information", confirm_msg)

    if confirmed:
        # Save the user information or perform any desired action with the data
        # For now, let's just display a message box
        messagebox.showinfo("Success", "User information saved!")
        show_menu()
    else:
        # User clicked "Cancel"
        messagebox.showinfo("Cancelled", "User information not saved.")