import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox


# Load elements from the CSV file
def load_elements(filename):
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row if there is one
        return {row[1]: row for row in reader}  # Create a dictionary with the symbol as a key


# Main UI class for the Periodic Table
class PeriodicTableUI(QMainWindow):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Periodic Table of Elements')
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a button for each element and add it to the layout
        for symbol in self.elements:
            btn = QPushButton(f'{self.elements[symbol][2]} ({symbol})', self)
            btn.clicked.connect(lambda ch, symbol=symbol: self.show_element_info(symbol))
            layout.addWidget(btn)

    def show_element_info(self, element_symbol):
        element = self.elements[element_symbol]
        info_text = '\n'.join([f"{key}: {value}" for key, value in zip(headers, element)])
        QMessageBox.information(self, f"{element[2]} Details", info_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Define your CSV headers - adjust according to your CSV file structure
    headers = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
               'Group', 'Period', 'Atomic weight', 'Density',
               'Melting point', 'Boiling point',
               'Specific heat capacity', 'Electronegativity',
               'Abundance in earth\'s crust']

    # Replace 'periodictable.csv' with the actual path to your CSV file
    elements_dict = load_elements('periodictable.csv')

    # Create and show the main window
    main_window = PeriodicTableUI(elements_dict)
    main_window.show()

    # Start the event loop
    sys.exit(app.exec())
