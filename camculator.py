from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon

app = QApplication([])
main_window = QWidget()

main_window.setWindowTitle("Calculator")
main_window.setWindowIcon(QIcon("images.jpg"))
main_window.resize(300 , 400)  
main_window.move(1200 , 200)

text_box = QLineEdit()
grid = QGridLayout()

buttons = ["7", "8", "9", '/',
           "4", "5", "6", '*',
           "1", "2", "3", '+',
           "0", ".", '=', '-']
clear = QPushButton("C")
delete = QPushButton("Del")

def button_click():
    button = app.sender()
    symbol = button.text()

    if symbol == '=':
        expression = text_box.text()
        try:
            result = eval(expression)
            text_box.setText(str(result))
        except:
            text_box.setText("Error")

    elif symbol == 'C':
        text_box.clear()

    elif symbol == 'Del':
        current_value = text_box.text()
        text_box.setText(current_value[:-1])

    else:
        current_value = text_box.text()
        text_box.setText(current_value + symbol)

#buttom yaratamiz
col = 0
row = 0
for text in buttons:
    button = QPushButton(text)
    button.setFixedSize(70, 70) 
    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)
    col += 1

    if col > 3:
        col = 0
        row += 1

master_layout = QVBoxLayout()
text_box.setFixedHeight(50)  
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row = QHBoxLayout()
clear.setFixedSize(70, 70)  
delete.setFixedSize(70, 70)  
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout.addLayout(button_row)

main_window.setLayout(master_layout)

delete.clicked.connect(button_click)
clear.clicked.connect(button_click)

# Dezayn => oynaga style sheet qoshamiz 
main_window.setStyleSheet("""
    QWidget {
        background-color: #2E2E2E;
    }
    QLineEdit {
        background-color: white;
        font-size: 20px;
        padding: 10px;
        border: 2px solid #CCCCCC;
        border-radius: 5px;
        color: black;
    }
    QPushButton {
        background-color: #4CAF50;
        font-size: 18px;
        padding: 15px;
        border: none;
        border-radius: 5px;
        color: white;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QPushButton:pressed {
        background-color: #3e8e41;
    }
    QPushButton#clear {
        background-color: #f44336;
    }
    QPushButton#delete {
        background-color: #ff9800;
    }
""")

clear.setObjectName("clear")
delete.setObjectName("delete")

main_window.show()
app.exec_()
