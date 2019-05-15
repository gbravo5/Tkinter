# mainApp() hereda de Tk()

from tkinter import *

class mainApp(Tk):
    
    # assumptions:
    
    # 1.- screen:
    size_screen         = '640x480'
    window_title        = 'my_screen'
    background_screen   = 'blue'
    
    
    def __init__(self):
        # 1.- screen:
            # a) invocar al constructor de Tk
        Tk.__init__(self)
            # b) customize
        self.geometry(self.size_screen)
        self.title(self.window_title)
        self.configure(bg = self.background_screen)



    def maincycle(self):
        # manage events
        self.mainloop()
               





if __name__ == '__main__':
    app = mainApp()
    app.maincycle()
    