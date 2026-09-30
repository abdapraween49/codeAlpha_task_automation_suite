import os
import re
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path


class AutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Task Automation Suite")
        self.root.geometry("520x420")
        self.root.resizable(False, False)

        # Apply Modern Styling
        style = ttk.Style()
        style.theme_use("clam")

        # Main Title Label
        title_label = ttk.Label(
            root, 
            text="⚡ Python Task Automation Tool", 
            font=("Helvetica", 14, "bold")
        )
        title_label.pack(pady=15)

        # Tab Control
        self.tabControl = ttk.Notebook(root)
        
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text=" Image Organizer (.jpg) ")
        self.tabControl.add(self.tab2, text=" Email Extractor (.txt) ")
        self.tabControl.pack(expand=1, fill="both", padx=10, pady=5)

        # Setup Tabs
        self.setup_organizer_tab()
        self.setup_extractor_tab()

    # ================= TAB 1: FILE ORGANIZER =================
    def setup_organizer_tab(self):
        # Source Directory
        ttk.Label(self.tab1, text="Source Folder:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.src_entry = ttk.Entry(self.tab1, width=38)
        self.src_entry.grid(row=0, column=1, padx=5, pady=10)
        ttk.Button(self.tab1, text="Browse", command=self.browse_src).grid(row=0, column=2, padx=5, pady=10)

        # Target Directory
        ttk.Label(self.tab1, text="Destination Folder:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.dest_entry = ttk.Entry(self.tab1, width=38)
        self.dest_entry.grid(row=1, column=1, padx=5, pady=10)
        ttk.Button(self.tab1, text="Browse", command=self.browse_dest).grid(row=1, column=2, padx=5, pady=10)

        # Action Button
        run_btn = ttk.Button(self.tab1, text="Organize Images", command=self.run_organizer)
        run_btn.grid(row=2, column=0, columnspan=3, pady=25)

    def browse_src(self):
        folder = filedialog.askdirectory()
        if folder:
            self.src_entry.delete(0, tk.END)
            self.src_entry.insert(0, folder)

    def browse_dest(self):
        folder = filedialog.askdirectory()
        if folder:
            self.dest_entry.delete(0, tk.END)
            self.dest_entry.insert(0, folder)

    def run_organizer(self):
        src = self.src_entry.get().strip()
        dest = self.dest_entry.get().strip()

        if not src or not dest:
            messagebox.showwarning("Warning", "Please select both Source and Destination folders.")
            return

        source_path = Path(src)
        target_path = Path(dest)

        if not source_path.exists():
            messagebox.showerror("Error", "Source directory does not exist.")
            return

        target_path.mkdir(parents=True, exist_ok=True)
        moved_count = 0

        for file_path in source_path.glob("*"):
            if file_path.suffix.lower() in [".jpg", ".jpeg"]:
                destination = target_path / file_path.name
                try:
                    shutil.move(str(file_path), str(destination))
                    moved_count += 1
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to move {file_path.name}: {e}")
                    return

        messagebox.showinfo("Success", f"Task Complete!\n{moved_count} image(s) moved successfully.")

    # ================= TAB 2: EMAIL EXTRACTOR =================
    def setup_extractor_tab(self):
        # Input Text File
        ttk.Label(self.tab2, text="Input Text File:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.input_entry = ttk.Entry(self.tab2, width=38)
        self.input_entry.grid(row=0, column=1, padx=5, pady=10)
        ttk.Button(self.tab2, text="Browse", command=self.browse_input).grid(row=0, column=2, padx=5, pady=10)

        # Output Text File
        ttk.Label(self.tab2, text="Save Emails To:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.output_entry = ttk.Entry(self.tab2, width=38)
        self.output_entry.grid(row=1, column=1, padx=5, pady=10)
        ttk.Button(self.tab2, text="Browse", command=self.browse_output).grid(row=2 if False else 1, column=2, padx=5, pady=10)

        # Action Button
        extract_btn = ttk.Button(self.tab2, text="Extract & Save Emails", command=self.run_extractor)
        extract_btn.grid(row=2, column=0, columnspan=3, pady=25)

    def browse_input(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, file_path)

    def browse_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, file_path)

    def run_extractor(self):
        input_file = self.input_entry.get().strip()
        output_file = self.output_entry.get().strip()

        if not input_file or not output_file:
            messagebox.showwarning("Warning", "Please specify both Input and Output file paths.")
            return

        input_path = Path(input_file)
        if not input_path.is_file():
            messagebox.showerror("Error", "Selected input file does not exist.")
            return

        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        try:
            with open(input_path, "r", encoding="utf-8") as f:
                content = f.read()

            emails = sorted(set(re.findall(email_pattern, content)))

            if not emails:
                messagebox.showinfo("No Emails Found", "No email addresses were found in the file.")
                return

            with open(output_file, "w", encoding="utf-8") as f:
                for email in emails:
                    f.write(f"{email}\n")

            messagebox.showinfo("Success", f"Successfully extracted {len(emails)} unique email(s).")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationApp(root)
    root.mainloop()