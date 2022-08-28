#!/usr/bin/python3
import tkinter as tk
import random

class PasswordGen:
    def __init__(self, master=None):
        self.length = tk.IntVar()
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.configure(width=200)
        self.toplevel1.geometry("190x220")
        self.toplevel1.resizable(False, False)
        self.toplevel1.title("Password Generator")
        self.label1 = tk.Label(self.toplevel1)
        self.label1.configure(font="{calibri} 14 {bold}", text="Password Generator")
        self.label1.pack(padx=15, pady=10, side="top")
        self.entry1 = tk.Entry(self.toplevel1)
        self.entry1.pack(side="top")
        self.button1 = tk.Button(self.toplevel1, command=self.generate)
        self.button1.configure(text="Fill Password")
        self.button1.pack(pady=10, side="top")
        self.lbl_options = tk.Label(self.toplevel1)
        self.lbl_options.configure(font="{calibri} 14 {bold}", text="Options")
        self.lbl_options.pack(side="top")
        self.lbl_length = tk.Label(self.toplevel1)
        self.lbl_length.configure(text="Length")
        self.lbl_length.pack(pady=10, side="top")
        self.ent_length = tk.Entry(self.toplevel1, textvariable=self.length)
        self.ent_length.pack(side="top")
        self.chk_special = tk.Checkbutton(self.toplevel1)
        self.chk_special.configure(text="Special Characters")
        self.chk_special.pack(pady=10, side="top")

        # Main widget
        self.mainwindow = self.toplevel1

    def generate(self):
        self.entry1.delete(0, "end")
        lowerLetters = "qwertyuiopasdfghjklzxcvbnm"
        upperLetters = lowerLetters.upper()
        numbers = "1234567890"
        special_chars = '!@#$%^&*()[]{}/\\'

        combined = lowerLetters + upperLetters + numbers + special_chars
        output = ""
        for x in range(int(self.ent_length.get())):
            output = output + random.choice(combined)

        self.entry1.insert(0, output)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = PasswordGen()
    app.run()
