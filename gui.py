import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from video_to_audio import decode_audio
from translated import transcribe_and_translate
from end_video import stitch_video

class DubbingApp:
    def __init__(self, root, dub_function, indian_languages):
        self.root = root
        self.root.title("AI Dubbing Tool")
        self.dub_function = dub_function
        self.indian_languages = indian_languages

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Create and configure a progress bar
        self.progress_bar = ttk.Progressbar(
            self.root, length=200, mode='determinate')
        self.progress_bar.grid(row=0, column=0, padx=10, pady=10)

        # Create a label and dropdown menu for selecting the target language
        ttk.Label(self.root, text="Select Target Language:").grid(
            row=1, column=0, padx=10, pady=5)
        self.target_language_var = tk.StringVar()
        self.target_language_var.set("Hindi")  # Default language
        target_language_menu = ttk.OptionMenu(
            self.root, self.target_language_var, *self.indian_languages.keys())
        target_language_menu.grid(row=1, column=1, padx=10, pady=5)

        # Create a Start Dubbing button
        self.start_button = ttk.Button(
            self.root, text="Start Dubbing", command=self.start_dubbing)
        self.start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def start_dubbing(self):
        # Get the selected target language
        target_language = self.indian_languages[self.target_language_var.get()]

        # Replace with your dubbing logic
        input_video_path = filedialog.askopenfilename(
            title="Select a video file", filetypes=[("Video files", "*.mp4 *.avi")])

        if not input_video_path:
            messagebox.showerror("Error", "Please select a video file.")
            return

        # Perform dubbing
        self.dub_function(input_video_path, target_language)

        messagebox.showinfo("Dubbing Complete", "Dubbing process completed.")

def create_gui(root, dub_function, indian_languages):
    app = DubbingApp(root, dub_function, indian_languages)

if __name__ == "__main__":
    # Language codes for Indian regional languages
    indian_languages = {
        "Hindi": "hi",
        "Tamil": "ta",
        "Telugu": "te",
        "Kannada": "kn",
        "Bengali": "bn",
        "Marathi": "mr",
        "Gujarati": "gu",
        "Punjabi": "pa",
        "Odia": "or",
        "Malayalam": "ml"
    }

    root = tk.Tk()
    create_gui(root, None, indian_languages)
    root.mainloop()

