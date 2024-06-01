import random
import sys
import tkinter as tk
from tkinter import messagebox

def create_user_file():
    users = [
            ('Alice', 'apass', 1),
            ('Bob', 'bpass', 2),
            ('Chase', 'cpass', 3),
            ('Dany', 'dpass', 4)
    ]
    with open('shadow.txt', 'w') as file:
        [file.write(f"{user}:{password}:{level}\n") for user, password, level in users]

def generate_file_permissions():
    file_array = [(f'file_{i}', random.randint(1, 4)) for i in range(100, 150)]
    with open('file_permissions.txt', 'w') as file:
        [file.write(f"{file_name}:{permission}\n") for file_name, permission in file_array]

def get_user_data():
    with open('shadow.txt', 'r') as file:
        lines = file.readlines()
    return [line.strip().split(':') for line in lines]

class SecurityLevelsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bell-La-Paluda Security Model")

        self.create_user_file()
        self.generate_file_permissions()

        self.user_data = self.get_user_data()

        self.user_label = tk.Label(root, text="Select a user to login:")
        self.user_label.pack()

        self.user_listbox = tk.Listbox(root)
        for user, _, _ in self.user_data:
            self.user_listbox.insert(tk.END, user)

        self.user_listbox.pack()

        self.login_button = tk.Button(root, text="Login", command=self.user_login)
        self.login_button.pack()

    def create_user_file(self):
        users = [
            ('Alice', 'apass', 1),
            ('Bob', 'bpass', 2),
            ('Chase', 'cpass', 3),
            ('Dany', 'dpass', 4)
        ]
        with open('shadow.txt', 'w') as file:
            [file.write(f"{user}:{password}:{level}\n") for user, password, level in users]

    def generate_file_permissions(self):
        file_array = [(f'file_{i}', random.randint(1, 4)) for i in range(100, 150)]
        with open('file_permissions.txt', 'w') as file:
            [file.write(f"{file_name}:{permission}\n") for file_name, permission in file_array]

    def get_user_data(self):
        with open('shadow.txt', 'r') as file:
            lines = file.readlines()
        return [line.strip().split(':') for line in lines]

    def user_login(self):
        selected_index = self.user_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a user.")
            return

        user_number = selected_index[0] + 1
        user_input = tk.simpledialog.askstring("Password", f"Enter {self.user_data[user_number - 1][0]}'s password:")
        if user_input != self.user_data[user_number - 1][1]:
            messagebox.showerror("Error", "Invalid password.")
        else:
            self.show_user_actions(self.user_data[user_number - 1][0], int(self.user_data[user_number - 1][2]))

    def show_user_actions(self, user, level):
        self.user_label.config(text=f"{user}, you are Security Level {level}")

        self.user_listbox.pack_forget()
        self.login_button.pack_forget()

        self.action_label = tk.Label(self.root, text="Select an option:")
        self.action_label.pack()

        self.actions_listbox = tk.Listbox(self.root)
        self.actions_listbox.insert(tk.END, "Show READABLE files")
        self.actions_listbox.insert(tk.END, "Show WRITABLE files")
        self.actions_listbox.insert(tk.END, "LOGOUT")
        self.actions_listbox.pack()

        self.actions_listbox.bind('<Double-Button-1>', self.perform_user_action)

    def perform_user_action(self, event):
        selected_index = self.actions_listbox.curselection()
        if not selected_index:
            return

        action_number = selected_index[0] + 1

        if action_number == 1:
            self.display_readable_files()
        elif action_number == 2:
            self.display_writable_files()
        elif action_number == 3:
            self.logout()

    def display_readable_files(self):
        with open('file_permissions.txt', 'r') as file:
            lines = file.readlines()

        readable_files = [f"{line.strip().split(':')[0]}\t\t{line.strip().split(':')[1]}" for line in lines
                          if int(line.strip().split(':')[1]) <= int(self.user_data[2])]
        messagebox.showinfo("Readable Files", '\n'.join(readable_files))

    def display_writable_files(self):
        with open('file_permissions.txt', 'r') as file:
            lines = file.readlines()

        writable_files = [f"{line.strip().split(':')[0]}\t\t{line.strip().split(':')[1]}" for line in lines
                          if int(line.strip().split(':')[1]) >= int(self.user_data[2])]
        messagebox.showinfo("Writable Files", '\n'.join(writable_files))

    def logout(self):
        self.action_label.pack_forget()
        self.actions_listbox.pack_forget()
        self.user_listbox.pack()
        self.login_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityLevelsApp(root)
    root.mainloop()
