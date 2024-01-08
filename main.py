from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kanisanav import screen_helper
from kivy.core.window import Window

Window.size =(350, 580)



class MenuScreen(Screen):
    pass

class AmaniScreen(Screen):
    pass

class UpendoScreen(Screen):
    pass

class UzalishajiScreen(Screen):
    pass

class KaziScreen(Screen):
    pass

sm=ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(AmaniScreen(name='amani'))
sm.add_widget(UpendoScreen(name='upendo'))
sm.add_widget(UzalishajiScreen(name='uzalishaji'))
sm.add_widget(KaziScreen(name='kazi'))

class KanisaHalisiApp(MDApp):

    def build(self):
        
        screen=Builder.load_string(screen_helper)
        return screen
        
    
        

KanisaHalisiApp().run()  

