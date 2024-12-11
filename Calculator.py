from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class StandardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_expression = "0"

        layout = BoxLayout(orientation='vertical')
        self.display = Label(text=self.current_expression, size_hint=(1, 0.2), halign='right', valign='middle')
        self.display.bind(size=self.display.setter('text_size'))
        layout.add_widget(self.display)

        buttons_layout = GridLayout(cols=4, size_hint=(1, 0.8))
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        for btn_text in buttons:
            buttons_layout.add_widget(Button(text=btn_text, on_press=self.on_button_press))

        buttons_layout.add_widget(Button(text='DEL', on_press=self.delete_last))
        buttons_layout.add_widget(Button(text='(', on_press=self.on_button_press))
        buttons_layout.add_widget(Button(text=')', on_press=self.on_button_press))

        layout.add_widget(buttons_layout)
        layout.add_widget(
            Button(text="Switch to Programmer Mode", size_hint=(1, 0.1), on_press=self.switch_to_programmer))
        self.add_widget(layout)

    def on_button_press(self, instance):
        if self.current_expression == "0" or self.current_expression == "Error":
            self.current_expression = ""
        if instance.text == "=":
            try:
                self.current_expression = str(eval(self.current_expression))
            except Exception:
                self.current_expression = "Error"
        else:
            self.current_expression += instance.text
        self.update_display()

    def delete_last(self, instance):
        if self.current_expression == "Error":
            self.current_expression = "0"
        else:
            self.current_expression = self.current_expression[:-1] or "0"
        self.update_display()

    def update_display(self):
        self.display.text = self.current_expression

    def switch_to_programmer(self, instance):
        self.manager.current = 'programmer'


class ProgrammerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_input = "0"

        layout = BoxLayout(orientation='vertical')
        self.display = Label(text=self.current_input, size_hint=(1, 0.2), halign='right', valign='middle')
        self.display.bind(size=self.display.setter('text_size'))
        layout.add_widget(self.display)

        self.mode = "DEC"
        mode_buttons = BoxLayout(size_hint=(1, 0.1))
        mode_buttons.add_widget(Button(text="DEC", on_press=self.set_mode))
        mode_buttons.add_widget(Button(text="HEX", on_press=self.set_mode))
        mode_buttons.add_widget(Button(text="BIN", on_press=self.set_mode))
        layout.add_widget(mode_buttons)

        self.buttons_layout = GridLayout(cols=4, size_hint=(1, 0.6))
        self.update_buttons()

        layout.add_widget(self.buttons_layout)
        control_buttons = BoxLayout(size_hint=(1, 0.1))
        control_buttons.add_widget(Button(text="DEL", on_press=self.delete_last))
        control_buttons.add_widget(Button(text="CLR", on_press=self.clear_input))
        control_buttons.add_widget(Button(text="Switch to Standard Mode", on_press=self.switch_to_standard))
        layout.add_widget(control_buttons)
        self.add_widget(layout)

    def update_buttons(self):
        self.buttons_layout.clear_widgets()
        if self.mode == "DEC":
            buttons = [str(i) for i in range(10)]
        elif self.mode == "HEX":
            buttons = [str(i) for i in range(10)] + list("ABCDEF")
        elif self.mode == "BIN":
            buttons = ["0", "1"]

        for btn_text in buttons:
            self.buttons_layout.add_widget(Button(text=btn_text, on_press=self.on_button_press))

    def on_button_press(self, instance):
        if self.current_input == "0":
            self.current_input = ""
        self.current_input += instance.text
        self.update_display()

    def delete_last(self, instance):
        self.current_input = self.current_input[:-1] or "0"
        self.update_display()

    def clear_input(self, instance):
        self.current_input = "0"
        self.update_display()

    def update_display(self):
        if self.mode == "DEC":
            value = int(self.current_input)
            display_value = f"DEC: {value}\nHEX: {hex(value)[2:].upper()}\nBIN: {bin(value)[2:]}"
        elif self.mode == "HEX":
            value = int(self.current_input, 16)
            display_value = f"DEC: {value}\nHEX: {self.current_input}\nBIN: {bin(value)[2:]}"
        elif self.mode == "BIN":
            value = int(self.current_input, 2)
            display_value = f"DEC: {value}\nHEX: {hex(value)[2:].upper()}\nBIN: {self.current_input}"
        self.display.text = display_value

    def set_mode(self, instance):
        self.mode = instance.text
        self.update_buttons()
        self.clear_input(None)

    def switch_to_standard(self, instance):
        self.manager.current = 'standard'


class CalculatorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StandardScreen(name='standard'))
        sm.add_widget(ProgrammerScreen(name='programmer'))
        return sm


if __name__ == '__main__':
    CalculatorApp().run()
