from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    def build(self):
        return Label(text='Olá SENAI!', font_size=100, font_name='Arial',color=get_color_from_hex('#c9d3ff'))
    
if __name__ == "__main__":
    MinhaApp().run()