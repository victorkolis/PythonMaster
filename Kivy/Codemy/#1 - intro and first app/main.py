from kivy.app import App
from kivy.uix.label import Label


class HelloWorldApp(App):
    def build(self):
        return Label(text='Hello World!', font_size=72)


if __name__ == '__main__':
    HelloWorldApp().run()
