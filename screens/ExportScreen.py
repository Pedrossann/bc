from widgets.customButton import customButton
import customtkinter as ctk


# Frame that let user choose criteria about saving the output
# @window - Parent of the frame.
# @mathHandler -connection to mathematic logic of the application.
class ExportScreen(ctk.CTkFrame):
    def __init__(self, window, formulas_handler):
        super().__init__(window, width=800, height=400)

        self.window = window
        self.formulas_handler = formulas_handler

        self.button_frame = self.create_button_frame()
        main_frame = ctk.CTkScrollableFrame(self, width=720, height=350)

        self.name_entry = self.create_entry_frame(main_frame)

        main_frame.pack()
        self.button_frame.pack(fill="x", expand=True)

    # Creates Button frame for the screen.
    def create_button_frame(self) -> ctk.CTkFrame:
        button_frame = ctk.CTkFrame(self, width=720)
        back_button = customButton(
            button_frame,
            text="Zpět",
            command=lambda: self.window.screens["ImportScreen"].tkraise(),
        )
        done_button = customButton(
            button_frame,
            text="Hotovo",
            command=lambda: self.click_done(),
        )
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        back_button.grid(row=0, column=0, sticky="w", pady=10, padx=10)
        done_button.grid(row=0, column=1, sticky="e", pady=10, padx=10)

        return button_frame

    # Run final logic of the application.
    def click_done(self):
        self.formulas_handler.calculation(self.name_entry.get())

    def create_entry_frame(self, parent):
        entry_frame = ctk.CTkFrame(parent)
        text = ctk.CTkLabel(entry_frame, text="Output file name")
        entry = ctk.CTkEntry(entry_frame, placeholder_text="name")

        text.grid(row=0, column=0, padx=10)
        entry.grid(row=0, column=1, padx=10)
        entry_frame.pack()

        return entry
