import kivy
from kivy.app import App
from kivy.uix.image import Image

class MyImageApp(App):
    def build(self):
        img=Image(source="Sun.png",size_hint=(None,None),
                  width=200,height=100,pos_hint={"center_x":0.5,
                  "center_y":0.5})
        return img

MyImageApp().run()