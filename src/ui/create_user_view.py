from tkinter import ttk
from services.app_service import app_service

class CreateUserView:
    def __init__(self, root, handle_show_login_view, handle_create_user):
        self._root = root
        self._frame = None
        self._username_input = None
        self._password_input = None
        self._handle_show_login_view = handle_show_login_view
        self._handle_create_user = handle_create_user

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _handle_create_user_onClick(self):
        username = self._username_input.get()
        password = self._password_input.get()
        app_service.create_user(username,password)
        self._handle_create_user()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")

        self._username_input = ttk.Entry(master=self._frame)

        username_label.grid(row=1, column=0, columnspan=1)
        self._username_input.grid(row=1, column=1, columnspan=2)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_input = ttk.Entry(master=self._frame)

        password_label.grid(row=2, column=0, columnspan=1)
        self._password_input.grid(row=2, column=1, columnspan=2)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_username_field()
        self._initialize_password_field()

        create_button = ttk.Button(
            master=self._frame,
            text="Create",
            command= self._handle_create_user_onClick
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command= self._handle_show_login_view 
        )

        create_button.grid(row=3, column=1)
        login_button.grid(row=3, column=2)
