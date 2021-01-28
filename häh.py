from tkinter import*
from PyQt5.QtWidgets import *
from psutil import*
import platform
import GPUtil
from cpuinfo import get_cpu_info


uname = platform.uname()
cpu = get_cpu_info()
threads = cpu_count()
cores = cpu_count(logical=False)
gpus = GPUtil.getGPUs()


app = QApplication([])
button = QPushButton('Click')
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
app.exec_()
print(threads)
print(cores)
for gpu in gpus:
    gpu_id = gpu.id
    gpu_name = gpu.name
    canvas1.create_text(100,100,text=gpu_id, fill="white", width=150)
    print(gpu_name)

app.exec_()