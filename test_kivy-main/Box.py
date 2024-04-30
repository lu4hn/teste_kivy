from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RotuloApp(App):
    def build(self):
        Layout=BoxLayout(orientation='vertical')
        self.lab1=Label(
                text='SENAI', color=[1, 0, 0, 1],
                 font_size=40, bold=True
        )
        self.lab2=Label(
                text='SESI', color=[0, 1, 0, 1],
                font_size=40, italic=True
        )
        self.lab3=Label(
            text='ENEM', color=[0, 0, 1, 1],
            font_size=40, font_name='Arial',
            underline=True
        )
        Layout.add_widget(self.lab1)
        Layout.add_widget(self.lab2)
        Layout.add_widget(self.lab3)
        return Layout
    
if __name__ == '__main__':
    RotuloApp().run()
        
