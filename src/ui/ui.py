from tkinter import Tk, ttk

class UI:    
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        app_header = ttk.Label(master=self._root, text="Progressive Overloader")
        view_header = ttk.Label(master=self._root, text="Login")

        username_label = ttk.Label(master=self._root, text="Username: ")
        username_input = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Password: ")
        password_input = ttk.Entry(master=self._root)

        login_button = ttk.Button(master=self._root, text="Login")
        create_user_button = ttk.Button(master=self._root, text="New user")

        app_header.grid(row=0, column=0, columnspan=3)
        view_header.grid(row=1, column=0, columnspan=2)
        username_label.grid(row=2, column=0, columnspan=1)
        username_input.grid(row=2, column=1, columnspan=2)
        password_label.grid(row=3, column=0, columnspan=1)
        password_input.grid(row=3, column=1, columnspan=2)
        login_button.grid(row=4, column=1, columnspan=1)
        create_user_button.grid(row=4, column=2, columnspan=1)