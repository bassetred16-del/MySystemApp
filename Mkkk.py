from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import random

# جعل التطبيق يغطي الشاشة بالكامل
Window.fullscreen = 'auto'

class XiinVirusApp(MDApp):
    def build(self):
        # إعدادات الستيل (Neon Green & Dark)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        
        self.screen = MDScreen()
        self.count = 0

        # واجهة "الكلحة" (الواجهة الاحترافية)
        self.main_card = MDCard(
            orientation='vertical',
            padding=25,
            spacing=20,
            size_hint=(0.8, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[25, 25, 25, 25],
            elevation=4
        )

        self.main_card.add_widget(MDLabel(
            text="XIIN OPTIMIZER",
            halign="center",
            font_style="H4",
            bold=True,
            theme_text_color="Primary"
        ))

        self.main_card.add_widget(MDLabel(
            text="Boost your phone performance now.",
            halign="center",
            theme_text_color="Secondary"
        ))

        self.start_btn = MDFillRoundFlatButton(
            text="START BOOSTING",
            pos_hint={"center_x": 0.5},
            on_release=self.launch_terror
        )
        self.main_card.add_widget(self.start_btn)

        self.screen.add_widget(self.main_card)
        return self.screen

    def launch_terror(self, *args):
        # مسح الواجهة القديمة وتحويل الشاشة للأسود
        self.screen.clear_widgets()
        Window.clearcolor = (0, 0, 0, 1)

        # تشغيل الصوت المرعب اللي بعتهولي
        self.sound = SoundLoader.load('ghost_voice.mp3')
        if self.sound:
            self.sound.volume = 1.0
            self.sound.loop = True
            self.sound.play()

        # إظهار الصورة اللي تخلع (الفوطو تاعك)
        self.horror_img = Image(source='horror.jpg', allow_stretch=True, keep_ratio=False)
        self.screen.add_widget(self.horror_img)

        # إضافة نص "الاختراق" هابط
        self.status_label = MDLabel(
            text="SYSTEM COMPROMISED!",
            halign="center",
            font_style="H5",
            theme_text_color="Error",
            pos_hint={"center_y": 0.2},
            bold=True
        )
        self.screen.add_widget(self.status_label)

        # تشغيل تأثير الفيروسات الهابطة
        Clock.schedule_interval(self.virus_messages, 0.3)

    def virus_messages(self, dt):
        msgs = ["UPLOADING DATA...", "ERASING OS...", "HACKED BY XIIN", "CHEK YOUR GALLERY..."]
        self.status_label.text = random.choice(msgs)

if __name__ == "__main__":
    XiinVirusApp().run()
