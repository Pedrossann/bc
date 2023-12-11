from blueprints.ScreenBllueprint import ScreenBllueprint


# First Frame, that lets user to choose which variables he wants to calculate.
# @window CTkFrame - Parent of the frame.
# @mathHandler -connection to mathematic logic of the application.
class ChooseScreen(ScreenBllueprint):
    def __init__(self, window, formulas_handler):
        super().__init__(window, formulas_handler)

        button_frame = self.create_button_frame(True, False)
        main_frame = self.create_main_frame()
        self.formulas_handler.create_formulas(main_frame)

        main_frame.pack()
        button_frame.pack(fill="x", expand=True)

    # Gets the data(on = true/ off = false) of the switches and saves chosed formulas into the math handler.
    def get_states_of_formulas(self):
        states = {}
        for name in list(self.formulas_handler.formulas.keys()):
            states[name] = self.formulas_handler.formulas[name].switch
        self.formulas_handler.switches_wanted_formulas(states)

    # Switches the screen and loads the data for the next screen.
    def next_screen(self):
        self.get_states_of_formulas()
        self.window.screens["ImportScreen"].grid_needed_variables()
        self.window.screens["ImportScreen"].tkraise()
