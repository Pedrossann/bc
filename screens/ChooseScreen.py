from widgets.customButton import customButton
import customtkinter as ctk


# First Frame, that lets user to choose which variables he wants to calculate.
# @window CTkFrame - Parent of the frame.
# @mathHandler -connection to mathematic logic of the application.
class ChooseScreen(ctk.CTkFrame):
    def __init__(self, window, formulas_handler):
        super().__init__(window, width=800, height=400)
        self.window = window
        self.formulas_handler = formulas_handler

        self.button_frame = self.create_button_frame()
        self.main_frame = self.create_main_frame()

        self.main_frame.pack()
        self.button_frame.pack(fill="x", expand=True)

    # Creates frame with next/back buttons.
    def create_button_frame(self) -> ctk.CTkFrame:
        button_frame = ctk.CTkFrame(self, width=720)
        next_button = customButton(
            button_frame,
            text="Další",
            command=lambda: self.next_screen(),
        )
        button_frame.grid_columnconfigure(1, weight=1)
        next_button.grid(row=0, column=1, sticky="e", pady=10, padx=10)

        return button_frame

    # Creates Scrollable frame with all formulas inside.
    # @return created frame with forulas.
    def create_main_frame(self):
        main_frame = ctk.CTkScrollableFrame(self, width=720, height=350)
        self.formulas_handler.create_formulas(main_frame)
        return main_frame

    # Gets the data(on = true/ off = false) of the switches and saves chosed formulas into the math handler.
    def get_states_of_formulas(self):
        states = {}
        for formula in self.formulas_handler.formulas:
            states[formula.name] = formula.switch
        self.formulas_handler.switches_wanted_formulas(states)

    # Switches the screen and loads the data for the next screen.
    def next_screen(self):
        self.get_states_of_formulas()
        self.window.screens["ImportScreen"].grid_needed_variables()
        self.window.screens["ImportScreen"].tkraise()
