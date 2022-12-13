from tkinter import ttk
import tkinter as tk
from services.app_service import app_service

class ExercisesOverview:
    def __init__(self, root, handle_show_create_new_exercise_view):
        self._root = root
        self._frame = None
        self._exercises = app_service.get_users_exercises()
        self._user = app_service.get_logged_user()
        self._handle_show_create_new_exercise_view = handle_show_create_new_exercise_view

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def handle_delete_exercise(self,id):
        print(id)
        self._exercises.remove
        app_service.delete_exercise(id)

    def _intialize_create_exercise_button(self):
        create_exercise_button = ttk.Button(master=self._frame, text="Create new exercise", command=self._handle_show_create_new_exercise_view)
        create_exercise_button.grid(column=0)

    def _initialize_exercise_card(self,exercise):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=f"{exercise.name} {exercise.weight}kg {exercise.sets}x{exercise.reps}" )
        editbutton = ttk.Button(master=item_frame, text="Edit")
        deletebutton =ttk.Button(master=item_frame, text="Delete", command=self.handle_delete_exercise(exercise.id))
        label.grid(row=0, column=2)
        editbutton.grid(row=0, column=0, sticky=tk.W)
        deletebutton.grid(row=0, column=1, padx=1)
        item_frame.grid(padx=2, pady=2, sticky=tk.W)
        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.grid_columnconfigure(1, weight=1)
        item_frame.grid_columnconfigure(2, weight=3)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        headerlabel = ttk.Label(master=self._frame,text=f"Welcome {self._user.username} , here are your exercises: ")
        headerlabel.grid(row=1, column=0)
        for exercise in self._exercises:
            self._initialize_exercise_card(exercise)
        self._intialize_create_exercise_button()
