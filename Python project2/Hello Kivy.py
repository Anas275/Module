# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.core.window import Window
#
# Window.clearcolor=(1,1,1,1,)
#
# class LokeshApp(App):
#     def build(self):
#         label=Label(text="Hello Kivy",font_size="120sp",bold=True,italic=True,color=(1,0,1))
#         return label
#
# LokeshApp().run()



import kivy
from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        btn=Button(text="Click Me",size_hint=(0.3,0.4),pos_hint={"center_x":0.5,"center_y":0.5}
                   ,font_size="44sp",on_release=self.btn_click)
        return btn

    def btn_click(self, btn):
        print("Button.clicked")

ButtonApp().run()