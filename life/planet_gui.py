from tkinter import *
from tkinter import messagebox


class PlanetGui(Tk):

    def __init__(self):
        super().__init__()

        # declare components
        self.name_label = Label()
        self.name_entry = Entry()
        self.submit_button = Button()

        # set window attributes
        self.title("Planet GUI")

        # add components
        self.add_name_label()
        self.add_name_entry()
        self.add_submit_button()

    def add_name_label(self):
        # add component to window
        self.name_label.grid(row=0, column=0)

        # style the components
        self.name_label.configure(text="Enter Planet Name:")

    def add_name_entry(self):
        # add component to window
        self.name_entry.grid(row=1, column=0)

        # style the component

    def add_submit_button(self):
        # add component to window
        self.submit_button.grid(row=2, column=0)

        # style the component
        self.submit_button.configure(text="Submit")


if __name__ == '__main__':
    gui = PlanetGui()
    gui.mainloop()
