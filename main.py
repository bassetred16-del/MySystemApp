from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = """
MDScreen:
    md_bg_color: [0, 0, 0, 1]
    MDLabel:
        text: "ZE8C - SYSTEM ACTIVE"
        halign: "center"
        theme_text_color: "Custom"
        text_color: [0, 1, 0.8, 1]
"""

class SovereignApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    SovereignApp().run()
