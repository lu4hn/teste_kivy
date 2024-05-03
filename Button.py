from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class MyApp(App):
    def build(self):
        return Button(text="Clique aqui", font_size=50, background_color=('#3894db'), size_hint=(0.5, 0.2))
if __name__ == '__main__':
    MyApp().run()