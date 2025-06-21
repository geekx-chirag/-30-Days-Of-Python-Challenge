from kivy.app import App
from kivy.uix.button import Button

class IronManApp(App):
    def build(self):
        return Button(text="Avengers Assemble")

if __name__ == '__main__':
    IronManApp().run()

# CHALLENGE : Convert the temperature converter CLI tool into a GUI tool

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TempConverterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input field
        self.input = TextInput(hint_text='Enter Celsius', multiline=False)

        # Button
        convert_button = Button(text='Convert to Fahrenheit')
        convert_button.bind(on_press=self.convert_temp)

        # Result label
        self.result_label = Label(text='')

        # Add widgets to layout
        layout.add_widget(self.input)
        layout.add_widget(convert_button)
        layout.add_widget(self.result_label)

        return layout

    def convert_temp(self, instance):
        try:
            celsius = float(self.input.text)
            fahrenheit = (celsius * 9/5) + 32
            self.result_label.text = f'{fahrenheit:.2f} °F'
        except:
            self.result_label.text = 'Invalid input!'

if __name__ == '__main__':
    TempConverterApp().run()
