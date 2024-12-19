import tkinter as tk

window = tk.Tk()

for i in range(4):
    for j in range(4):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=5
        )
        frame.grid(row=i, column=j, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()