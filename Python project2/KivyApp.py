# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
#
#
# class SunidhiApp(App):
#
#     def build(self):
#
#         return Label(text="Sunidhi python!!!")
#
# if __name__=="__main__":
#     SunidhiApp().run()


import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class AakashGrid(GridLayout):
    def __init__(self,**kwargs):
        super(AakashGrid,self).__init__()
        self.cols = 2
        self.add_widget(Label(text="Student Name:"))

        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Student Marks:"))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="Student Gender:"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

class AakashApp(App):
    def build(self):
        return AakashGrid()


if __name__=="__main__":
    AakashApp().run()