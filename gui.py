import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from data_converter.core import convert
from data_converter.registry import FORMAT_REGISTRY


class ConverterGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("FrCnv - Data Format Converter")
        self.root.geometry("600x350")

        self.create_widgets()

    def create_widgets(self):

        tk.Label(self.root, text="Input Path:").pack(pady=5)

        self.input_entry = tk.Entry(self.root, width=70)
        self.input_entry.pack()

        tk.Button(self.root, text="Browse File/Folder",
                  command=self.select_input).pack(pady=5)

        tk.Label(self.root, text="Output Folder:").pack(pady=5)

        self.output_entry = tk.Entry(self.root, width=70)
        self.output_entry.pack()

        tk.Button(self.root, text="Browse Output Folder",
                  command=self.select_output).pack(pady=5)

        tk.Label(self.root, text="Target Format:").pack(pady=5)

        self.format_var = tk.StringVar(self.root)
        formats = list(FORMAT_REGISTRY.keys())
        self.format_var.set("csv")

        tk.OptionMenu(self.root, self.format_var, *formats).pack()

        tk.Button(self.root, text="Convert",
                  command=self.run_conversion,
                  bg="green",
                  fg="white").pack(pady=15)

        self.log_text = tk.Text(self.root, height=6)
        self.log_text.pack(fill="both", expand=True)

    def select_input(self):
        path = filedialog.askopenfilename() or filedialog.askdirectory()
        if path:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, path)

    def select_output(self):
        path = filedialog.askdirectory()
        if path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, path)

    def run_conversion(self):
        input_path = self.input_entry.get()
        output_path = self.output_entry.get()
        target_format = self.format_var.get()

        if not input_path or not output_path:
            messagebox.showerror("Error", "Please select input and output paths.")
            return

        thread = threading.Thread(
            target=self.execute_conversion,
            args=(input_path, output_path, target_format)
        )
        thread.start()

    def execute_conversion(self, input_path, output_path, target_format):
        try:
            self.log("Starting conversion...")
            convert(input_path, output_path, target_format)
            self.log("Conversion complete.")
            messagebox.showinfo("Success", "Conversion finished successfully!")

        except Exception as e:
            self.log(f"Error: {e}")
            messagebox.showerror("Error", str(e))

    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterGUI(root)
    root.mainloop()
