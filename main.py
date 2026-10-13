from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class ScamSimulatorApp(App):
    def build(self):
        self.title = "AI Quantitative Analytics"
        
        # State variables
        self.balance = 0
        self.tasks = 0
        self.activated = False
        self.premium = False
        self.referrals = 0

        # Main Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Dashboard Header
        layout.add_widget(Label(text="[b]🌟 AI QUANTITATIVE ANALYTICS 🌟[/b]", markup=True, font_size='20sp', size_hint_y=None, height=40))
        
        # Status Display Label
        self.status_label = Label(
            text=self.get_status_text(),
            markup=True,
            font_size='16sp',
            halign='left',
            valign='middle'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        layout.add_widget(self.status_label)

        # Action Buttons
        btn_task = Button(text="▶️ Complete Task (Watch Video)", background_color=(0.1, 0.6, 0.3, 1), font_size='16sp')
        btn_task.bind(on_press=self.do_task)
        layout.add_widget(btn_task)

        btn_withdraw = Button(text="💸 Request Withdrawal", background_color=(0.8, 0.2, 0.2, 1), font_size='16sp')
        btn_withdraw.bind(on_press=self.request_withdrawal)
        layout.add_widget(btn_withdraw)

        return layout

    def get_status_text(self):
        return (
            f"💰 Current Balance: [b]{self.balance:,} ETB[/b]\n"
            f"✅ Completed Tasks: {self.tasks}\n"
            f"🔒 Account Status: {'ACTIVATED' if self.activated else 'FREE TIER'}\n"
            f"⭐ Membership: {'PREMIUM' if self.premium else 'STANDARD'}\n"
            f"👥 Active Referrals: {self.referrals}/5"
        )

    def update_ui(self):
        self.status_label.text = self.get_status_text()

    def do_task(self, instance):
        self.tasks += 1
        self.balance += 5000
        self.update_ui()
        self.show_popup("Task Complete!", "+5,000 ETB added to dashboard balance.")

    def request_withdrawal(self, instance):
        if self.balance < 35000:
            self.show_popup("Withdrawal Failed", f"Minimum limit is 35,000 ETB.\nCurrent: {self.balance:,} ETB.")
            return

        if not self.activated:
            self.show_popup("Gate 1: Activation Required", "Pay 35,000 ETB Activation Fee to unlock funds.")
            self.activated = True
            self.update_ui()
            return

        if not self.premium:
            self.show_popup("Gate 2: Premium Subscription", "Upgrade to Premium (5,000 ETB/month) required.")
            self.premium = True
            self.update_ui()
            return

        if self.referrals < 5:
            self.show_popup("Gate 3: Referral Quota", "You must invite 5 active friends first.")
            self.referrals = 5
            self.update_ui()
            return

        self.show_popup("Gate 4: Final Security Check", "BLOCKED: One of your referrals must deposit 35,000 ETB first!")

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message, halign='center'))
        close_btn = Button(text="OK", size_hint_y=None, height=40)
        content.add_widget(close_btn)

        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    ScamSimulatorApp().run()
