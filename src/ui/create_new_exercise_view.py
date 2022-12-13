from tkinter import ttk
from services.app_service import app_service

class CreateNewExerciseView:
    def __init__(self, root, handle_save_exercise):
        self._root = root
        self._frame = None
        self._user = app_service.get_logged_user()
        self._handle_save_exercise = handle_save_exercise

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _handle_save_onClick(self):
        name = self._exercise_name_input.get()
        reps = self._exercise_reps_input.get()
        sets = self._exercise_sets_input.get()
        weight = self._exercise_weight_input.get()

        app_service.create_exercise(name,reps,sets,weight)
        self._handle_save_exercise()

    def _initialize_header(self):
        view_header = ttk.Label(master=self._frame,text="Create new exercise")
        view_header.grid(row=0, column=0, columnspan=2)

    def _initialize_exercise_name_input(self):
        exercise_name_label = ttk.Label(master=self._frame, text="Exercise name: ")
        self._exercise_name_input = ttk.Entry(master=self._frame)
        exercise_name_label.grid(row=1, column=0)
        self._exercise_name_input.grid(row=1, column=1)

    def _initialize_exercise_weight_input(self):
        exercise_weight_label = ttk.Label(master=self._frame, text="Weight: ")
        self._exercise_weight_input = ttk.Entry(master=self._frame)
        exercise_weight_label.grid(row=2, column=0)
        self._exercise_weight_input.grid(row=2, column=1)

    def _initialize_exercise_reps_input(self):
        exercise_reps_label = ttk.Label(master=self._frame, text="Reps: ")
        self._exercise_reps_input = ttk.Entry(master=self._frame)
        exercise_reps_label.grid(row=3, column=0)
        self._exercise_reps_input.grid(row=3, column=1)

    def _initialize_exercise_sets_input(self):
        exercise_sets_label = ttk.Label(master=self._frame, text="Sets: ")
        self._exercise_sets_input = ttk.Entry(master=self._frame)
        exercise_sets_label.grid(row=4, column=0)
        self._exercise_sets_input.grid(row=4, column=1)

    def _initialize_save_exercise_button(self):
        create_exercise_button = ttk.Button(master=self._frame, text="Save", command= self._handle_save_onClick)
        create_exercise_button.grid(row=5, column=0)

    def _initialize_cancel_button(self):
        cancel_button = ttk.Button(master=self._frame, text="Cancel")
        cancel_button.grid(row=5, column=1)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_header()
        self._initialize_exercise_name_input()
        self._initialize_exercise_weight_input()
        self._initialize_exercise_reps_input()
        self._initialize_exercise_sets_input()
        self._initialize_save_exercise_button()
        self._initialize_cancel_button()
