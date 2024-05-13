import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        
        self.current_path = tk.StringVar()
        self.current_path.set(os.getcwd())
        
        self.create_widgets()
        self.update_file_list()

    def create_widgets(self):
        self.path_label = tk.Label(self.root, text="Current Directory:")
        self.path_label.pack()

        self.path_entry = tk.Entry(self.root, textvariable=self.current_path, width=50)
        self.path_entry.pack()

        self.file_listbox = tk.Listbox(self.root, width=80, height=20)
        self.file_listbox.pack()

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_directory)
        self.browse_button.pack()

        self.copy_button = tk.Button(self.root, text="Copy", command=self.copy_file)
        self.copy_button.pack()

        self.move_button = tk.Button(self.root, text="Move", command=self.move_file)
        self.move_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_file)
        self.delete_button.pack()

    def update_file_list(self):
        self.file_listbox.delete(0, tk.END)
        files = os.listdir(self.current_path.get())
        for file in files:
            self.file_listbox.insert(tk.END, file)

    def browse_directory(self):
        selected_path = filedialog.askdirectory()
        if selected_path:
            self.current_path.set(selected_path)
            self.update_file_list()

    def copy_file(self):
        selected_file = self.file_listbox.get(tk.ACTIVE)
        if selected_file:
            src = os.path.join(self.current_path.get(), selected_file)
            dst = filedialog.askdirectory()
            if dst:
                shutil.copy(src, dst)
                messagebox.showinfo("Success", f"{selected_file} copied successfully.")
                self.update_file_list()

    def move_file(self):
        selected_file = self.file_listbox.get(tk.ACTIVE)
        if selected_file:
            src = os.path.join(self.current_path.get(), selected_file)
            dst = filedialog.askdirectory()
            if dst:
                shutil.move(src, dst)
                messagebox.showinfo("Success", f"{selected_file} moved successfully.")
                self.update_file_list()

    def delete_file(self):
        selected_file = self.file_listbox.get(tk.ACTIVE)
        if selected_file:
            src = os.path.join(self.current_path.get(), selected_file)
            if os.path.isfile(src):
                os.remove(src)
                messagebox.showinfo("Success", f"{selected_file} deleted successfully.")
                self.update_file_list()
            elif os.path.isdir(src):
                shutil.rmtree(src)
                messagebox.showinfo("Success", f"{selected_file} deleted successfully.")
                self.update_file_list()

# Create and run the app
root = tk.Tk()
app = FileManagerApp(root)
root.mainloop()
