import json
from PyQt6 import QtWidgets

PAIRS_IN_ROW = 6

def adjust_table(data_len: int, table_widget) -> None:
    num_rows = (data_len + PAIRS_IN_ROW - 1) // PAIRS_IN_ROW 
    
    table_widget.setRowCount(num_rows)
    table_widget.setColumnCount(PAIRS_IN_ROW * 2)

    headers = []
    for i in range(PAIRS_IN_ROW):
        headers.append(f'Монета {i + 1}')
        headers.append(f'Цена {i + 1}')
    table_widget.setHorizontalHeaderLabels(headers)


def render_data(table_widget, data: dict) -> None:
    adjust_table(len(data), table_widget)
    index = 0
    for key, value in data.items():
        row = index // PAIRS_IN_ROW
        col = (index % PAIRS_IN_ROW) * 2
        table_widget.setItem(
            row, col, QtWidgets.QTableWidgetItem(key))
        table_widget.setItem(
            row, col+1, QtWidgets.QTableWidgetItem(str(value))) 
        index+=1
