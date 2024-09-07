import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer")
        
        self.label = tk.Label(root, text="Enter file name or folder path:")
        self.label.pack(pady=10)
        
        self.search_entry = tk.Entry(root, width=50)
        self.search_entry.pack(pady=5)
        
        self.search_button = tk.Button(root, text="Search", command=self.search_file)
        self.search_button.pack(pady=5)
        
        self.result_listbox = tk.Listbox(root, height=15, width=70)
        self.result_listbox.pack(pady=10)
        
        self.result_listbox.bind("<Double-1>", self.open_folder)
        
    def search_file(self):
        self.result_listbox.delete(0, tk.END)  # Clear previous results
        
        query = self.search_entry.get()
        if not query:
            messagebox.showerror("Error", "Please enter a file name or folder path.")
            return
        
        self._search_files(query)
    
    def _search_files(self, query):
        for root_dir, _, files in os.walk("C:\\"):  # Change the starting directory as needed
            for file in files:
                if query.lower() in file.lower():
                    self.result_listbox.insert(tk.END, os.path.join(root_dir, file))
                    
    def open_folder(self, event):
        selected_item = self.result_listbox.curselection()
        if selected_item:
            file_path = self.result_listbox.get(selected_item)
            folder_path = os.path.dirname(file_path)
            os.startfile(folder_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()
