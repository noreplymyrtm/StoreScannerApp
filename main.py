from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.datepicker import DatePicker
from kivy.clock import Clock
from kivy.lang import Builder
from plyer import camera, filechooser, share
import csv
import os
from datetime import datetime

KV = '''
<ScannerUI>:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    Label:
        text: "Enter Store Code:"
    TextInput:
        id: store_code
        multiline: False
        hint_text: "E.g., ABC123"

    Button:
        text: "Scan Barcode"
        on_press: root.start_scan()

    TextInput:
        id: barcode_input
        multiline: False
        hint_text: "Manual barcode input if scan fails"

    Label:
        text: "Select / Enter Date:"
    TextInput:
        id: date_input
        multiline: False
        hint_text: "YYYY-MM-DD"

    Button:
        text: "Add Scan"
        on_press: root.add_scan()

    Button:
        text: "Save CSV"
        on_press: root.save_csv()

    Button:
        text: "Share CSV"
        on_press: root.share_csv()
'''

class ScannerUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scans = []

    def start_scan(self):
        try:
            camera.take_picture(filename='barcode.jpg', on_complete=self.on_scan_complete)
        except NotImplementedError:
            popup = Popup(title='Camera Error',
                          content=Label(text='Camera not supported. Use manual input.'),
                          size_hint=(0.7, 0.3))
            popup.open()

    def on_scan_complete(self, filepath):
        # Placeholder: real-time barcode scanning can be integrated here
        # For now, simulate reading a barcode from image filename
        barcode = os.path.basename(filepath).split('.')[0]
        self.ids.barcode_input.text = barcode

    def add_scan(self):
        store_code = self.ids.store_code.text.strip()
        barcode = self.ids.barcode_input.text.strip()
        date_text = self.ids.date_input.text.strip()

        if not store_code or not barcode:
            popup = Popup(title='Error', content=Label(text='Store Code and Barcode are required.'),
                          size_hint=(0.7, 0.3))
            popup.open()
            return

        # Default to today if date not provided
        if not date_text:
            date_text = datetime.now().strftime('%Y-%m-%d')

        self.scans.append({
            'Store Code': store_code,
            'Barcode': barcode,
            'Date': date_text
        })

        # Clear barcode input for next scan
        self.ids.barcode_input.text = ''

    def save_csv(self):
        if not self.scans:
            popup = Popup(title='Error', content=Label(text='No scans to save.'),
                          size_hint=(0.7, 0.3))
            popup.open()
            return

        path = os.path.join(os.getcwd(), 'store_scans.csv')
        with open(path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Store Code', 'Barcode', 'Date'])
            writer.writeheader()
            for scan in self.scans:
                writer.writerow(scan)

        popup = Popup(title='Saved', content=Label(text=f'CSV saved to {path}'),
                      size_hint=(0.7, 0.3))
        popup.open()

    def share_csv(self):
        path = os.path.join(os.getcwd(), 'store_scans.csv')
        if os.path.exists(path):
            share.share(path)
        else:
            popup = Popup(title='Error', content=Label(text='CSV file not found. Save first.'),
                          size_hint=(0.7, 0.3))
            popup.open()


class StoreScannerApp(App):
    def build(self):
        Builder.load_string(KV)
        return ScannerUI()


if __name__ == '__main__':
    StoreScannerApp().run()
