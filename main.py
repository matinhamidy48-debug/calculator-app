from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorApp(App):

    def calculate(self, operation):
        try:
            a = float(self.num1.text)
            b = float(self.num2.text)

            if operation == "+":
                result = a + b
            elif operation == "-":
                result = a - b
            elif operation == "*":
                result = a * b
            elif operation == "/":
                if b == 0:
                    self.result.text = "تقسیم بر صفر ممکن نیست"
                    return
                result = a / b

            self.result.text = "نتیجه: " + str(result)

        except:
            self.result.text = "لطفاً عدد وارد کن"

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        title = Label(
            text="ماشین حساب عبدالمتین",
            font_size=25
        )
        layout.add_widget(title)

        self.num1 = TextInput(
            hint_text="عدد اول",
            input_filter="float",
            multiline=False,
            font_size=20
        )
        layout.add_widget(self.num1)

        self.num2 = TextInput(
            hint_text="عدد دوم",
            input_filter="float",
            multiline=False,
            font_size=20
        )
        layout.add_widget(self.num2)

        for operation in ["+", "-", "*", "/"]:
            button = Button(
                text=operation,
                font_size=25
            )
            button.bind(
                on_press=lambda x, op=operation:
                self.calculate(op)
            )
            layout.add_widget(button)

        self.result = Label(
            text="نتیجه:",
            font_size=22
        )
        layout.add_widget(self.result)

        return layout


CalculatorApp()
