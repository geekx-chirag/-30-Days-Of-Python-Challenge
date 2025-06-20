from kivy.app import App
from kivy.uix.button import Button

class IronManApp(App):
    def build(self):
        return Button(text="Avengers Assemble")

if __name__ == '__main__':
    IronManApp().run()
