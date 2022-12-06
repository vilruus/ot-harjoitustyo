from tkinter import ttk
from services.user_service import user_service

class ExercisesOverview:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._user = user_service.get_logged_user()

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize_header(self):
        view_header = ttk.Label(master=self._frame,text="Your Exercises")
        view_header.grid(row=0, column=0, columnspan=2)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_header()
        wip_label = ttk.Label(master=self._frame,text=f"Welcome {self._user.username} , This view is WIP")
        wip_label.grid(row=1, column=0, columnspan=2)

