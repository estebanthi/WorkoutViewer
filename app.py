import sys


from PyQt5.QtWidgets import QApplication


from classes.Models.model import Model
from classes.Views.view import View
from classes.Controllers.controller import Controller
from classes.config import Config


class App:

    def __init__(self):
        qapp = QApplication(sys.argv)

        Config.initial_config()

        controller = Controller()
        model = Model(controller)
        controller.model = model

        try:
            view = View(controller)
            controller.view = view
            controller.connect()

            view.postInit()
            view.show()

            sys.exit(qapp.exec())
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = App()
