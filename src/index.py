from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database

def main():
    window = Tk()
    window.title("Progressive overloader")

    ui_view = UI(window)
    ui_view.start()
    window.mainloop()

if __name__ == "__main__":
    main()