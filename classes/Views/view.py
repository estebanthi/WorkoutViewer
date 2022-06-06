from PyQt5 import QtWidgets
import shutil
import datetime as dt


from ui.main_window import Ui_MainWindow


class View(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.controller = controller
        self.connect()

        self.validateButton.setDisabled(True)
        self.resetButton.setDisabled(True)

    def connect(self):
        self.importCSVButton.clicked.connect(self.getFile)
        self.validateButton.clicked.connect(self.filter)
        self.resetButton.clicked.connect(self.reset_filter)

    def getFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Choisissez un fichier')[0]
        if filename:
            shutil.copy(filename, 'data/data.sv')
            self.controller.load_data()

    def updateData(self):
        self.validateButton.setDisabled(False)
        self.resetButton.setDisabled(False)

        sessions = self.controller.model.sessions

        self.startEdit.setMaximumDate(dt.datetime.now()-dt.timedelta(days=1))
        self.endEdit.setMinimumDate(sessions[0].date)
        self.endEdit.setMaximumDate(dt.datetime.now())
        self.endEdit.setMinimumDate(sessions[0].date+dt.timedelta(days=1))

        self.startEdit.setDate(sessions[0].date)
        self.endEdit.setDate(sessions[-1].date)
        self.lastDateInput.setDate(sessions[-1].date)

        self.totalSessionsInput.setValue(len(self.controller.model.sessions))

        self.lundi.setValue(self.controller.get_sessions_for_day(0))
        self.mardi.setValue(self.controller.get_sessions_for_day(1))
        self.mercredi.setValue(self.controller.get_sessions_for_day(2))
        self.jeudi.setValue(self.controller.get_sessions_for_day(3))
        self.vendredi.setValue(self.controller.get_sessions_for_day(4))
        self.samedi.setValue(self.controller.get_sessions_for_day(5))
        self.dimanche.setValue(self.controller.get_sessions_for_day(6))

    def postInit(self):
        if self.controller.model.sessions:
            self.updateData()

    def filter(self):
        self.controller.filter(self.startEdit.date(), self.endEdit.date())

    def reset_filter(self):
        self.controller.reset_filter()
