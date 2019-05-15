# mainApp() hereda de Tk()

from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    
    data_input      = None
    temperature     = None
    conversion_type = None
    
    # assumptions:

    size_screen         = '210x150'
    window_title        = 'termómetro_tkinter'
    background_screen   = '#ECECEC'
    
    
    def __init__(self):
        
        # 1.- screen:
            # a) invocar al constructor de Tk
        Tk.__init__(self)
            # b) customize
        self.geometry(self.size_screen)
        self.title(self.window_title)
        self.configure(bg = self.background_screen)
        self.resizable(0,0)                                            # pantalla fija
        
        # 2.- widgets: features 
        self.temperature      = StringVar(value = '')                  # objeto que se inicializa con valor ''
        self.conversion_type  = StringVar(value = 'C')                 # objeto que se inicializa con valor 'C'
        
        self.createLayout()
        
    
    def createLayout(self):
        # layout + screen interaction-capture
        self.data_input            = ttk.Entry(self, textvariable = self.temperature).place(x = 10, y = 10)                                                # entry temperature on screen --> value ---> gotofeature = self.temperature
        self.label_conversion_type = ttk.Label(self, text = 'degrees:').place(x = 10 , y = 45)
        self.conversion_type_f     = ttk.Radiobutton(self, text = 'fahrenheit', variable = self.conversion_type, value = 'F').place(x = 20, y = 70)    # click radiobutton on screen --> value, F, gotofeature = self.conversion_type   
        self.conversion_type_c     = ttk.Radiobutton(self, text = 'celsius', variable = self.conversion_type, value = 'C').place(x = 20, y = 95)       # click radiobutton on screen --> value, C, gotofeature = self.conversion_type


    def maincycle(self):
        # manage events
        self.mainloop()    

if __name__ == '__main__':
    app = mainApp()
    app.maincycle()