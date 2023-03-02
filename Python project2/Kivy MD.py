# from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel
#
# class HelloApp(MDApp):
#     def build(self):
#         txt=MDLabel(text="Lokesh..",halign="center",font_style="H1",
#                        theme_text_color="Custom",
#                        text_color=(2,0,1))
#         return txt
#
# HelloApp().run()



from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Main_App(MDApp):
    def build(self):
        return MDLabel(text="Welcome to Aayam",halign="center")
if __name__=='__main__':
    Main_App().run()
    