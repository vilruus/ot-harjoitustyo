from tkinter import ttk
from services.app_service import app_service

class LoginView:
    def __init__(self, root, handle_show_create_user_view, handle_login):
        self._root = root
        self._frame = None
        self._handle_show_create_user_view = handle_show_create_user_view
        self._handle_login = handle_login

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize_header(self):
        app_header = ttk.Label(master=self._frame, text="Progressive Overloader")
        view_header = ttk.Label(master=self._frame,text="Login")
        app_header.grid(row=0, column=0, columnspan=3)
        view_header.grid(row=1, column=0, columnspan=2)

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=2, column=0, columnspan=1)
        self._username_entry.grid(row=2, column=1, columnspan=2)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(row=3, column=0, columnspan=1)
        self._password_entry.grid(row=3, column=1, columnspan=2)

    def _handle_login_onClick(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        app_service.login(username, password)
        self._handle_login()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(master=self._frame, text="Login", command= self._handle_login_onClick)
        create_user_button = ttk.Button(master=self._frame, text="New user", command= self._handle_show_create_user_view)

        login_button.grid(row=4, column=1, columnspan=1)
        create_user_button.grid(row=4, column=2, columnspan=1)

    

