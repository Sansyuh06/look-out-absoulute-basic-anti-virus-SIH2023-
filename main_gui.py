import tkinter as tk
from tkinter import font, filedialog

def button_click(button_number):
    message_text.config(state=tk.NORMAL)  
    message_text.delete(1.0, tk.END)  
    message_text.configure(font=("Unispcae", 12, "bold"))  
    if button_number == 0:
        message = """
        Missing files are being fixed  \n 






"""
    elif button_number == 1:
        message = """
Scanning The Files.... \n


    elif button_number == 2:
        
        file_path = filedialog.askopenfilename()
        if file_path:
            message = f"Selected file: {file_path}"
            message = message+'''


    message_text.insert(tk.END, message + "\n")
    message_text.config(state=tk.DISABLED)  


def toggle_theme():
    global dark_theme
    dark_theme = not dark_theme
    if dark_theme:
        root.configure(bg="black")
        instructions_frame.configure(bg="black")
        instructions_label.configure(bg="black", fg="white")
        string_frame.configure(bg="black")
        string_label.configure(bg="black", fg="white")
        buttons_frame.configure(bg="black")
        message_text.configure(bg="black", fg="white")
        for button in button_labels:
            button.configure(bg="black", fg="white", activebackground="black", activeforeground="white")
    else:
        root.configure(bg="white")
        instructions_frame.configure(bg="lightgray")
        instructions_label.configure(bg="lightgray", fg="black")
        string_frame.configure(bg="white")
        string_label.configure(bg="white", fg="black")
        buttons_frame.configure(bg="white")
        message_text.configure(bg="white", fg="black")
        for button in button_labels:
            button.configure(bg="white", fg="black", activebackground="white", activeforeground="black")

root = tk.Tk()
root.title("Instructions, String, and Buttons App")
root.geometry("600x400")
instructions_frame = tk.Frame(root, width=240, bg="lightgray")
instructions_frame.pack(side="left", fill="both")
instructions_font = font.Font(family="Arial", size=14)  
instructions_text = 
"""Instructions:
1. Fix missing files
2. Complete Scan
3. Scan a specific file

Have a great day!"""
instructions_label = tk.Label(instructions_frame, text=instructions_text, wraplength=220, justify="left", font=instructions_font)
instructions_label.pack(padx=20, pady=20)
theme_button = tk.Button(instructions_frame, text="Themes", command=toggle_theme, font=("Arial", 16))
theme_button.pack(padx=20, pady=5)
string_frame = tk.Frame(root, width=240)
string_frame.pack(side="right", fill="both")
string_text = """

"""
string_label = tk.Label(string_frame, text=string_text, font=font.nametofont("TkFixedFont"), justify="left")
string_label.pack(padx=20, pady=20)

buttons_frame = tk.Frame(string_frame)
buttons_frame.pack(padx=20, pady=10)
button_labels = []
button_names = ["Fix Missing Files", "Complete Scan", "Scan a Specific File"]
for i in range(3):
    button = tk.Button(buttons_frame, text=button_names[i], command=lambda i=i: button_click(i))
    button.pack(side="left", padx=5)
    button_labels.append(button)
message_text = tk.Text(string_frame, wrap="none", height=5, width=30)
message_text.pack(side="right", padx=20, pady=(0, 20), fill="both", expand=True)
message_text.config(state=tk.DISABLED)  
dark_theme = False
root.mainloop()
