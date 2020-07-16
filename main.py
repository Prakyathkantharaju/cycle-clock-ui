# general imports
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# GUI has to have
class UI(object):
    def __init__(self):
        self.window = tk.Tk()
        self.width = int(self.window.winfo_screenwidth() / 2)
        self.height = int(self.window.winfo_screenheight() / 2)
        self.UI_loc = (self.height/2,self.width /2)
        self.main()

    def main(self):
        self.add_info()
        self._draw_cirle()
        self.window.geometry(f'{self.width}x{self.height}')
        self.window.mainloop()

    def add_info(self):
        self._info_b = tk.Button(self.window, text = 'Info', command = self.info)
        # self._info_b.place(x = int(self.width * 0.75), y = int(self.height/4))
        self._info_b.pack(side = 'left', padx = int(self.width * 0.5 * 0.7), pady = int(self.height/4), expand = 1)

    def info(self):
        info = tk.Tk()
        info.geometry(f'{int(self.width/2)}x{int(self.height/2)}')
        label = tk.Label(info, text = "cycle time").grid(row = 0)
        label1 = tk.Label(info, text = "rest time").grid(row = 1)
        label2 = tk.Label(info, text = "number of squats").grid(row = 2)
        # order
        # 1. cycle time
        # 2. rest time
        # 3. number of squat
        self.e1 = tk.Entry(info)
        self.e2 = tk.Entry(info)
        self.e3 = tk.Entry(info)
        self.e1.grid(row = 0, column = 1)
        self.e2.grid(row = 1, column = 1)
        self.e3.grid(row = 2, column = 1)


        tk.Button(info, text = "Enter", command = self._get_value).grid(row = 5,
                                                                       column= 0,
                                                                       sticky = tk.W,
                                                                       pady = 4)
        tk.Button(info, text = "Quit", command = info.destroy).grid(row = 5,
                                                                 column = 1,
                                                                 sticky = tk.W,
                                                                 pady = 4)
        self.info_window = info

    # code for the getting the value
    def _get_value(self):
        self.cycle_time = self.e1.get()
        self.rest_time = self.e2.get()
        self.no_squat = self.e3.get()
        print(self.cycle_time, self.rest_time, self.no_squat)
        self.info_window.destroy()


    def _draw_cirle(self):
        self.canvas = tk.Canvas(self.window)
        bbox = 0, 0, 100, 100
        print(bbox)
        self.canvas.create_oval(bbox,fill = 'black')
        self.canvas.place()



















if __name__ == '__main__':
    UI()
