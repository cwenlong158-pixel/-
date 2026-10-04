from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

Window.orientation = 'landscape'

class LoginLayout(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.spacing=20
        self.padding=50
        self.add_widget(Label(text="登录",font_size=30))
        self.user=TextInput(hint_text="账号",size_hint=(0.6,None),height=40)
        self.pwd=TextInput(hint_text="密码",password=True,size_hint=(0.6,None),height=40)
        self.add_widget(self.user)
        self.add_widget(self.pwd)
        bt=BoxLayout(spacing=20,size_hint=(0.6,None),height=40)
        bt.add_widget(Button(text="登录"))
        bt.add_widget(Button(text="退出"))
        self.add_widget(bt)

class LoginApp(App):
    def build(self):
        return LoginLayout()

if __name__=="__main__":
    LoginApp().run()
