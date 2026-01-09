from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QComboBox, QTableWidget, QTableWidgetItem, QLabel
)
from dinamik_rapor import odunc_dinamik_ara


class DinamikRaporWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dinamik Ödünç Arama")
        self.setFixedSize(700, 400)
        self.init_ui()

    def init_ui(self):
        label = QLabel("Ödünç Durumu Seç:")

        self.cmb_durum = QComboBox()
        self.cmb_durum.addItems([
            "Hepsi",
            "Aktif",
            "TeslimEdildi",
            "Gecikmis"
        ])

        btn_ara = QPushButton("Ara")
        btn_ara.clicked.connect(self.ara)

        self.table = QTableWidget()

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.cmb_durum)
        layout.addWidget(btn_ara)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def ara(self):
        durum = self.cmb_durum.currentText()
        cols, rows = odunc_dinamik_ara(durum)

        self.table.clear()
        self.table.setColumnCount(len(cols))
        self.table.setRowCount(len(rows))
        self.table.setHorizontalHeaderLabels(cols)

        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(val))
                )
