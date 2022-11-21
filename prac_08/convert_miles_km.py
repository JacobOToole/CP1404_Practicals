"""
CP1404 Practical
Kivy GUI program to convert miles/km
Jacob O'Toole
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

CONVERSION_RATE = 1.60934


class MilesConverter(App):
    message = StringProperty()

    def build(self):
        Window.size = (500, 200)
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Type in the field & press Enter"
        return self.root

    def handle_calculate(self, value):
        self.message = self.root.ids.output_label.text
        try:
            result = float(value) * CONVERSION_RATE
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = '0.0'

    def handle_increment(self, input_miles, increment):
        if input_miles == '':
            input_miles = '0'
        try:
            result = int(input_miles) + increment
            self.root.ids.input_miles.text = str(result)
        except ValueError:
            pass


MilesConverter().run()
