import tkinter as tk
import random

root = tk.Tk()
root.title("Tk Restaurant Picker")
root.iconbitmap("icon\\chef-hat.ico")

window_height = 300
window_width = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

root.configure(background="#3884c7", highlightthickness=10, highlightcolor="#226199")
root.resizable(False, False)  # This code helps to disable windows from resizing

# Global vars
restaurant_var = tk.StringVar()
restaurantes = []

def submit(event=None):  # Allow for the event parameter from the key binding
    name = restaurant_var.get()
    if name != "":
        restaurantes.append(name)
        restaurant_var.set("")
    else:
        pass
    
def finish():
    if not restaurantes:
        pass  
    else:
        finish_label = tk.Label(frame1, background="#3884c7", fg="#e8e6e6",
                                font=("Lato", 13, "bold"),
                                text=f"Your result is: {random.choice(restaurantes)}", pady=20)
        finish_label.pack()

        stop_btn.config(state=tk.DISABLED)
        sub_btn.config(state=tk.DISABLED)
        restaurantes_entry.config(state=tk.DISABLED,
        disabledbackground="#21598a",
        disabledforeground="#6d6d6d")
        
frame1 = tk.Frame(root, background="#3884c7")
frame1.pack()

restaurantes_label = tk.Label(
    frame1, fg="#e8e6e6", text="Restaurant Picker", font=("Lato", 17, "bold"), background="#3884c7"
)
restaurantes_entry = tk.Entry(
    frame1, textvariable=restaurant_var, fg="#d6d6d6", font=("Lato", 11, "bold"), 
    justify="center", background="#21598a", bd=4, insertbackground="#d6d6d6"
)
sub_btn = tk.Button(
    frame1, text="Add", font=("Lato", 13), fg="#f5f0f0", command=submit, 
    background="#21598a", highlightthickness=4, highlightcolor="#226199", 
    width=18, height=1, activebackground="#133e63"
)
stop_btn = tk.Button(
    frame1, text="Finish", font=("Lato", 13), fg="#f5f0f0", command=finish, 
    background="#21598a", highlightthickness=4, highlightcolor="#226199", 
    width=18, height=1, activebackground="#133e63"
)

restaurantes_label.pack(pady=(10, 10))
restaurantes_entry.pack(pady=10)
sub_btn.pack(pady=(20, 0))
stop_btn.pack(pady=(10))

restaurantes_entry.bind("<Return>", submit)

root.mainloop()
