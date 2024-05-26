from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
import random
import string

class PasswordGeneratorApp(App):
    def build(self):

        self.title = "Password Generator"
        Window.clearcolor = (1, 1, 1, 1)  # Set the background color to white

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title layout
        title_layout = BoxLayout(size_hint_y=None, height='50dp')
        self.label = Label(
            text="Password Generator",
            font_size='24sp',
            color=(0.2, 0.6, 0.86, 1),  # Set the text color
            size_hint=(1, None),
            height='50dp'
        )
        title_layout.add_widget(self.label)

        # Content layout
        content_layout = BoxLayout(orientation='vertical', spacing=10, pos_hint={'top': 0.9})

        self.password_box = TextInput(
            text="",
            font_size='20sp',
            readonly=True,
            background_color=(1, 1, 1, 1),
            foreground_color=(0.2, 0.6, 0.86, 1),
            size_hint=(1, None),
            height='50dp'
        )

        self.length_label = Label(
            text="Password Length: 10",
            font_size='18sp',
            color=(0.2, 0.6, 0.86, 1),
            size_hint=(1, None),
            height='40dp'
        )

        self.slider = Slider(
            min=10, max=20, value=10, step=1,
            value_track=True,
            value_track_color=(0.2, 0.6, 0.86, 1),
            size_hint=(1, None),
            height='40dp'
        )
        self.slider.bind(value=self.on_slider_value_change)

        self.uppercase_checkbox = CheckBox(size_hint=(None, None), size=(40, 40))
        self.lowercase_checkbox = CheckBox(active=True, size_hint=(None, None), size=(40, 40))

        self.numbers_toggle = BoxLayout(size_hint_y=None, height='40dp')
        self.numbers_yes = ToggleButton(text='Include Numbers', group='numbers', state='down')
        self.numbers_no = ToggleButton(text='No Numbers', group='numbers')
        self.numbers_toggle.add_widget(self.numbers_yes)
        self.numbers_toggle.add_widget(self.numbers_no)

        self.symbols_toggle = BoxLayout(size_hint_y=None, height='40dp')
        self.symbols_yes = ToggleButton(text='Include Symbols', group='symbols')
        self.symbols_no = ToggleButton(text='No Symbols', group='symbols', state='down')
        self.symbols_toggle.add_widget(self.symbols_yes)
        self.symbols_toggle.add_widget(self.symbols_no)

        options_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height='200dp')
        options_layout.add_widget(Label(text='Uppercase Letters:', font_size='18sp', color=(0.2, 0.6, 0.86, 1)))
        options_layout.add_widget(self.uppercase_checkbox)
        options_layout.add_widget(Label(text='Lowercase Letters:', font_size='18sp', color=(0.2, 0.6, 0.86, 1)))
        options_layout.add_widget(self.lowercase_checkbox)
        options_layout.add_widget(Label(text='Numbers:', font_size='18sp', color=(0.2, 0.6, 0.86, 1)))
        options_layout.add_widget(self.numbers_toggle)
        options_layout.add_widget(Label(text='Symbols:', font_size='18sp', color=(0.2, 0.6, 0.86, 1)))
        options_layout.add_widget(self.symbols_toggle)

        self.button_generate = Button(
            text="Generate Password",
            size_hint=(1, None),
            height='60dp',  # Increase the button height
            pos_hint={'center_x': 0.5},
            background_color=(0.2, 0.6, 0.86, 1),  # Set the button color
            color=(1, 1, 1, 1)  # Set the text color to white
        )
        self.button_generate.bind(on_press=self.generate_password)

        self.button_copy = Button(
            text="Copy Password",
            size_hint=(1, None),
            height='60dp',  # Increase the button height
            pos_hint={'center_x': 0.5},
            background_color=(0.2, 0.6, 0.86, 1),  # Set the button color
            color=(1, 1, 1, 1)  # Set the text color to white
        )
        self.button_copy.bind(on_press=self.copy_password)

        content_layout.add_widget(self.password_box)
        content_layout.add_widget(self.length_label)
        content_layout.add_widget(self.slider)
        content_layout.add_widget(options_layout)
        content_layout.add_widget(self.button_generate)
        content_layout.add_widget(self.button_copy)

        main_layout.add_widget(title_layout)
        main_layout.add_widget(content_layout)

        return main_layout

    def on_slider_value_change(self, instance, value):
        self.length_label.text = f"Password Length: {int(value)}"

    def generate_password(self, instance):
        length = int(self.slider.value)
        characters = ''
        if self.uppercase_checkbox.active:
            characters += string.ascii_uppercase
        if self.lowercase_checkbox.active:
            characters += string.ascii_lowercase
        if self.numbers_yes.state == 'down':
            characters += string.digits
        if self.symbols_yes.state == 'down':
            characters += string.punctuation

        if not characters:
            self.password_box.text = "Please select at least one option."
        else:
            password = ''.join(random.choices(characters, k=length))
            self.password_box.text = password

    def copy_password(self, instance):
        Clipboard.copy(self.password_box.text)
        # print("Password copied to clipboard!")

if __name__ == "__main__":
    PasswordGeneratorApp().run()
