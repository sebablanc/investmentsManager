# This Python file uses the following encoding: utf-8
from datetime import datetime
from PySide6.QtCore import Qt, QAbstractTableModel

class CaucionTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(CaucionTableModel, self).__init__()
        self._data = data

        self.hheaders = ["Fecha Inversión", "Monto Invertido", "Cantidad de días", "TNA %", "Derecho de mercado", "ID"]

    def data(self, index, role):
        value = self._data[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
           if isinstance(value, datetime):
               value = value.strftime("%d/%m/%Y")
           elif(isinstance(value, float) and index.column() == 1):
               value = "%.2f" % value
               value = "$" + value.replace(".", ",")
           elif(isinstance(value, float) and (index.column() == 3 or index.column() == 4)):
               value = "%.2f" % value
               value = value.replace(".", ",") + "%"
           elif isinstance(value, str):
               value = '"%s"' % value

           return value

        elif role == Qt.ItemDataRole.TextAlignmentRole:
           if isinstance(value, int) or isinstance(value, float) or isinstance(value, datetime):
               return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignRight

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.hheaders[section]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            pass
        return super().headerData(section, orientation, role)

    def rowCount(self, index):
            return len(self._data)

    def columnCount(self, index):
        return len(self._data[0]) - 1
