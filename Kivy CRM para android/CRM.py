import kivy.app
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')
    TestApp().run()