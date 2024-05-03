from kivy.app import App 
from kivy.uix.video import Video 

class MinhaApp(App):
    def build(self):
        return Video(source='Documents/Não se machuque de manu silva')
    
if __name__ == "__main__":
    MinhaApp().run()