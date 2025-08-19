from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.datepicker import DatePicker
from kivy.clock import Clock
import csv
import os
from datetime import datetime
from plyer import filechooser, share

class ScannerApp(App):
    def build(self):
        self.data = []
        self.store_code_input = TextInput(hint_text="Enter Store Code", multiline=False)
        self.date_input = TextInput(hint_text="Enter Date YYYY-MM-DD", multiline=False)
        self.scan_input = TextInput(hint_text="Scan Barcode or enter manually", multiline=False)
        self.status_label = Label(text="Ready")

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(self.store_code_input)
        layout.add_widget(self.scan_input)
        layout.add_widget(self.date_input)

        btn_add = Button(text="Add Scan")
        btn_add.bind(on_press=self.add_scan)
        layout.add_widget(btn_add)

        btn_save = Button(text="Save CSV")
        btn_save.bind(on_press=self.save_csv)
        layout.add_widget(btn_save)

        layout.add_widget(self.status_label)

        return layout

    def add_scan(self, instance):
        store_code = self.store_code_input.text.strip()
        barcode = self.scan_input.text.strip()
        date_text = self.date_input.text.strip()
        if not store_code or not barcode or not date_text:
            self.status_label.text = "Fill all fields!"
            return
        self.data.append([store_code, barcode, date_text])
        self.scan_input.text = ""
        self.status_label.text = f"{len(self.data)} scans added."

    def save_csv(self, instance):
        if not self.data:
            self.status_label.text = "No data to save!"
            return
        filename = f"StoreScans_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        folder = filechooser.choose_dir(title="Select Folder to Save CSV")[0]
        path = os.path.join(folder, filename)
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Store Code", "Barcode", "Date"])
            writer.writerows(self.data)
        self.status_label.text = f"Saved: {path}"
        share.share(path)  # open share dialog (WhatsApp, Gmail, etc.)

if __name__ == "__main__":
    ScannerApp().run()
