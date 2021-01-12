from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text='Name: '))

        # Add input Box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        # Submit button
        self.submit = Button(text='submit', font_size=20)

        # Binding the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        self.add_widget(Label(text=f'Hi there, {name}'))


class HelloWorldApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    HelloWorldApp().run()
