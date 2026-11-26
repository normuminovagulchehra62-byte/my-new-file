from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MeningIlovam(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        self.label = Label(text='Salom, dunyo!', font_size='30sp')
        self.add_widget(self.label)

        btn = Button(text='Meni bos!', size_hint=(1, 0.3), font_size='24sp')
        btn.bind(on_press=self.bosildi)
        self.add_widget(btn)

    def bosildi(self, instance):
        self.label.text = 'Tugma bosildi!'

class MeningApp(App):
    def build(self):
        self.title = 'Mening Ilovam'
        return MeningIlovam()

if __name__ == '__main__':
    MeningApp().run()