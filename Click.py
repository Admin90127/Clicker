import tkinter as tk

# function that will execute on button click
def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title('Application Window')

# Create a button and bind it to the on_button_click function
button = tk.Button(root, text='Click me', command=on_button_click)
button.pack()

root.mainloop()
