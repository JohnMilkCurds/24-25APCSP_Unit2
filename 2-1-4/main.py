import tkinter as tk
# Main Window
root = tk.Tk()
root.wm_geometry("200x200")
# Create empty frame (new window for components in root)

frame_login = tk.Frame(root)
# Create empty frame

frame_login.grid()
# Widgets for Frame-login

lbl_username = tk.Label(frame_login, text="Username", font = 'times 14')
lbl_username.pack(padx=50, pady=50)
# text Box for Username

ent_username = tk.Entry(frame_login, bd =3)
ent_username.pack()
root.mainloop()