import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

class DesqueezeApp:
    def __init__(self, master):
        self.master = master
        master.title("Desqueeze-App")
        master.iconbitmap('logo.ico')  # Stelle sicher, dass logo.ico im gleichen Ordner liegt

        self.input_files = []
        self.output_dir = ""

        self.factors = ["1.25", "1.33", "1.5", "1.8", "Benutzerdefiniert"]
        self.selected_factor = tk.StringVar(value="1.33")
        self.custom_factor = tk.DoubleVar(value=1.33)

        tk.Button(master, text="Bilder auswählen", command=self.select_images).pack(pady=5)
        self.input_label = tk.Label(master, text="Keine Bilder ausgewählt.")
        self.input_label.pack(pady=5)

        tk.Button(master, text="Ausgabeordner wählen", command=self.select_output_folder).pack(pady=5)
        self.output_label = tk.Label(master, text="Kein Ausgabeordner gewählt.")
        self.output_label.pack(pady=5)

        tk.Label(master, text="Desqueeze-Faktor wählen:").pack(pady=5)
        self.factor_menu = tk.OptionMenu(master, self.selected_factor, *self.factors, command=self.on_factor_change)
        self.factor_menu.pack(pady=5)

        self.custom_entry = tk.Entry(master, textvariable=self.custom_factor, state="disabled")
        self.custom_entry.pack(pady=5)

        tk.Button(master, text="Desqueeze starten", command=self.process_images).pack(pady=10)

    def select_images(self):
        files = filedialog.askopenfilenames(filetypes=[("Bilddateien", "*.jpg *.jpeg *.png *.bmp")])
        if files:
            self.input_files = files
            self.input_label.config(text=f"{len(files)} Bilder ausgewählt.")

    def select_output_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_dir = folder
            self.output_label.config(text=f"Ausgabe: {folder}")

    def on_factor_change(self, selection):
        if selection == "Benutzerdefiniert":
            self.custom_entry.config(state="normal")
        else:
            self.custom_entry.config(state="disabled")
            self.custom_factor.set(float(selection))

    def process_images(self):
        if not self.input_files:
            messagebox.showwarning("Warnung", "Bitte zuerst Bilder auswählen!")
            return
        if not self.output_dir:
            messagebox.showwarning("Warnung", "Bitte zuerst Ausgabeordner wählen!")
            return

        factor = self.custom_factor.get()

        for path in self.input_files:
            try:
                img = Image.open(path)
                new_width = int(img.width * factor)
                new_img = img.resize((new_width, img.height), Image.LANCZOS)
                base_name = os.path.basename(path)
                name, ext = os.path.splitext(base_name)
                new_img.save(os.path.join(self.output_dir, f"{name}_Desq{ext}"))
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler bei {path}: {e}")

        messagebox.showinfo("Fertig", "Alle Bilder wurden erfolgreich verarbeitet!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DesqueezeApp(root)
    root.mainloop()
