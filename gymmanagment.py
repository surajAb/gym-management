
import tkinter as tk
from tkinter import messagebox
members = []

def show_members():
    """Display all gym members in a listbox."""
    listbox.delete(0, tk.END)  # Clear previous items
    
    for member in members:
        listbox.insert(tk.END, f"{member['id']}: {member['name']} ({member['email']})")

def add_member():
    """Add a new gym member."""
    name = name_entry.get()
    email = email_entry.get()
    
    if name and email:
        new_member = {
            "id": len(members) + 1,
            "name": name,
            "email": email
        }
        members.append(new_member)
        show_members()  # Update the listbox
        messagebox.showinfo("Success", "Member added successfully!")
    else:
         messagebox.showerror("Error", "Please provide both name and email")

        
        

# Create main window
root = tk.Tk()
root.title("Gym Management System")
root.iconbitmap('gym.ico')
root.maxsize(width=500,height=300)
root.configure(bg='skyblue')


# Create GUI components
tk.Label(root, text="Name:",bg="yellow", fg="red").pack()
name_entry = tk.Entry(root,fg="red")
name_entry.pack()

tk.Label(root, text="Email:",bg="red").pack()
email_entry = tk.Entry(root,fg="blue")
email_entry.pack()

add_button = tk.Button(root, text="Add Member", command=add_member,bg="lightgreen")
add_button.pack()

tk.Label(root, text="Gym Members:",bg="pink",fg="black").pack()
listbox = tk.Listbox(root, width=40,bg="pink",fg="green")
listbox.pack()

show_members()  # Display initial members

root.mainloop()
