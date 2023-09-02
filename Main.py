import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from gui import create_gui
from dub import dub

def main():
    root = tk.Tk()
    root.title("AI Dubbing Tool")

    # Create the main GUI
    create_gui(root, dub)

    root.mainloop()

if __name__ == "__main__":
    main()
