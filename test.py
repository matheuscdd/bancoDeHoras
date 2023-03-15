import tkinter as tk

# Create a new root window using the Tk class
root = tk.Tk()
root.wm_attributes("-topmost",1)
# Set the title of the root window
root.title("Main Window")

# Create a new toplevel window
toplevel = tk.Toplevel(root)

# Set the title of the toplevel window
toplevel.title("Toplevel Window")

# Run the main event loop
root.mainloop()