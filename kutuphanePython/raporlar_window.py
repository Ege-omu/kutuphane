from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout,
    QTableWidget, QTableWidgetItem
)
from raporlar import (
    rapor_oduncte_olanlar,
    rapor_gecikmeler,
    rapor_en_cok_odunc
)


class RaporWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Raporlar")
        self.setFixedSize(700, 400)

        self.init_ui()

    def init_ui(self):
        btn1 = QPushButton("Ödünçte Olan Kitaplar")
        btn2 = QPushButton("Gecikmiş Kitaplar")
        btn3 = QPushButton("En Çok Ödünç Alınan Kitaplar")

        btn1.clicked.connect(self.show_oduncte)
        btn2.clicked.connect(self.show_gecikme)
        btn3.clicked.connect(self.show_populer)

        self.table = QTableWidget()

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def fill_table(self, cols, rows):
        self.table.clear()
        self.table.setColumnCount(len(cols))
        self.table.setRowCount(len(rows))
        self.table.setHorizontalHeaderLabels(cols)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(value))
                )

    def show_oduncte(self):
        cols, rows = rapor_oduncte_olanlar()
        self.fill_table(cols, rows)

    def show_gecikme(self):
        cols, rows = rapor_gecikmeler()
        self.fill_table(cols, rows)

    def show_populer(self):
        cols, rows = rapor_en_cok_odunc()
        self.fill_table(cols, rows)
