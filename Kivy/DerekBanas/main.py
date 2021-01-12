import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.button import Label


class HelloKivyApp(App):

    def build(self):
        return Label()


hello_kivy = HelloKivyApp()
hello_kivy.run()
