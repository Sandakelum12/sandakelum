import random
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("My Software")
        self.setWindowIcon(QIcon('icon.png'))

        # Create a button that runs the simulation when clicked
        def on_button_click():
            cross_section_photo_effect =0.8  # Material properties as a percent
            cross_section_scattering =0.2# Material properties 

            n_simulating_incidents = 100 # Simulation parameter which means how many times simulating 

            # Counter for photoelectric and scattering events from 0
            n_photo = 0
            n_scatter = 0

            for r in range(n_simulating_incidents):
                # Generate a random number between 0 and 1
                r = random.random()

                # Compare the random number to the probability of the photoelectric effect
                if r < cross_section_photo_effect / (cross_section_photo_effect + cross_section_scattering):
                    n_photo += 1

                else:
                    n_scatter += 1

            # Append the results to the text edit widget
            self.text_edit.append("Number of photoelectric events: {}".format(n_photo))
            self.text_edit.append("Number of scattering events: {}".format(n_scatter))

        button = QPushButton("Run Simulation", self)
        button.setGeometry(10, 10, 280, 30)
        button.clicked.connect(on_button_click)
        
       
        
        # Create a text edit widget to display the results of the simulation
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 50, 280, 220)
        self.text_edit.setReadOnly(True)
        self.setCentralWidget(self.text_edit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
    

