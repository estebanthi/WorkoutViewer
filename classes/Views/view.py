from PyQt5 import QtWidgets
import shutil
import datetime as dt


from classes.pyqt5_utils import PyQt5Utils
from classes.ui.mplwidget import MplWidget
from ui.main_window import Ui_MainWindow
from classes.daterange import Daterange


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
        self.exoSelect.currentIndexChanged.connect(self.updateSelect)

    def getFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Choisissez un fichier')[0]
        if filename:
            shutil.copy(filename, 'data/data.sv')
            self.controller.load_data()

    def updateData(self):
        PyQt5Utils.clearLayout(self.allSessionsLayout)
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

        workoutsNb = len(self.controller.model.sessions)
        self.totalSessionsInput.setValue(workoutsNb)

        self.lundi.setValue(self.controller.get_sessions_for_day(0))
        self.mardi.setValue(self.controller.get_sessions_for_day(1))
        self.mercredi.setValue(self.controller.get_sessions_for_day(2))
        self.jeudi.setValue(self.controller.get_sessions_for_day(3))
        self.vendredi.setValue(self.controller.get_sessions_for_day(4))
        self.samedi.setValue(self.controller.get_sessions_for_day(5))
        self.dimanche.setValue(self.controller.get_sessions_for_day(6))

        exercices = self.controller.get_exercices()
        self.exoSelect.addItems([exercice.name for exercice in exercices])

        allSessionsPlot = self.getAllSessionsPlot()
        self.allSessionsLayout.addWidget(allSessionsPlot)

        nbDays = len(Daterange(sessions[0].date, sessions[-1].date, resolution=60*60*24).to_list())
        self.totalDaysSpin.setValue(nbDays)
        self.averageWorkoutsPerWeek.setValue(workoutsNb/(nbDays/7))

    def postInit(self):
        if self.controller.model.sessions:
            self.updateData()

    def filter(self):
        self.controller.filter(self.startEdit.date(), self.endEdit.date())

    def reset_filter(self):
        self.controller.reset_filter()

    def updateSelect(self):
        PyQt5Utils.clearLayout(self.graphsLayout)
        for i in reversed(range(self.graphsLayout.count())):
            self.graphsLayout.itemAt(i).widget().setParent(None)

        mplWidget = MplWidget()
        exercices = self.controller.get_exercice(self.exoSelect.currentText())

        y = [exercice.value for exercice in exercices]

        if isinstance(y[0], tuple):

            y = [exercice[0]*exercice[1] for exercice in y]
        x = [exercice.date for exercice in exercices]

        mplWidget.plot(x, y)
        mplWidget.format(self.exoSelect.currentText(), 4)
        mplWidget.set_ylabel("Charge totale (charge x répétitions)")
        self.graphsLayout.addWidget(mplWidget)

    def getAllSessionsPlot(self):
        allSessionPlot = MplWidget()
        allSessionPlot.setTitle('Total séances')

        sessions = self.controller.get_sessions()

        start = sessions[0].date
        end = sessions[-1].date

        dates = Daterange(start, end, resolution=60*60*24).to_list()

        x = dates
        y = []
        total = 0
        for date in dates:
            for session in sessions:
                if session.date == date:
                    total += 1
            y.append(total)

        allSessionPlot.plot(x, y)
        allSessionPlot.format('Total séances', 3)
        allSessionPlot.setMinimumSize(500, 300)
        return allSessionPlot
