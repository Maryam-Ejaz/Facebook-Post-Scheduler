import sys
import psutil  # Import psutil module for process management
import platform  # Import platform module to get the current platform

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from UI.Ui_MainWindow import Ui_MainWindow


def kill_chrome_processes():
    for proc in psutil.process_iter():
        try:
            # Check if the process name contains 'chrome'
            if 'chrome' in proc.name().lower():
                # Terminate the process
                proc.kill()
                print(f"Terminated Chrome process with PID {proc.pid}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        kill_chrome_processes()  # Kill Chrome processes before starting the application
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()
