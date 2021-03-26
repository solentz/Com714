from tkinter import *
from tkinter import messagebox

from universe import Universe

from planet_gui import PlanetGui


class UniverseGui(Tk):

    def __init__(self):
        super().__init__()

        # universe to populate
        self.universe = Universe()

        # declare components
        self.planet_label = Label()
        self.planet_list = Listbox()
        self.planet_button = Button()

        # set window attributes
        self.title("Universe GUI")

        # add components
        self.add_planet_label()
        self.add_planet_list()
        self.add_planets_button()

    def add_planet_label(self):
        # add component to window
        self.planet_label.grid(row=0, column=0)

        # style the components
        self.planet_label.configure(text="Existing Planet")

    def add_planet_list(self):
        # add component to window
        self.planet_list.grid(row=1, column=0)

        # style the component

    def add_planets_button(self):
        # add component to window
        self.planet_button.grid(row=2, column=0)

        # style the component
        self.planet_button.configure(text="Add Planet")

        # assign events
        self.planet_button.bind("<ButtonRelease-1>", self.planet_button_clicked)

    def planet_button_clicked(self, event):
        self.destroy()
        self.add_planet_gui = PlanetGui()
        self.add_planet_gui.mainloop()


if __name__ == '__main__':
    gui = UniverseGui()
    gui.mainloop()
