# mainApp() hereda de Tk()

from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    
    data_input      = None
    temperature     = None
    conversion_type = None
    __previous_value = ''
    
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
        self.temperature. trace('w', self.validatetemperature)         # 'w'- write, 'r'- read, 'u'- unset (borrar); 'w' cada vez que se introduzca/borre/.../modifique una temperatura en el interfaz gráfico, se llamará al método 'validatetemperature'
        self.conversion_type  = StringVar(value = 'F')                 # objeto que se inicializa con valor 'C'
        
        self.createlayout()
        
    
    def createlayout(self):
        # layout + screen interaction-capture
        self.data_input            = ttk.Entry(self, textvariable = self.temperature).place(x = 10, y = 10)                                                # entry temperature on screen --> value ---> gotofeature = self.temperature
        self.label_conversion_type = ttk.Label(self, text = 'degrees:').place(x = 10 , y = 45)
        self.conversion_type_f     = ttk.Radiobutton(self, text = 'fahrenheit', variable = self.conversion_type, value = 'F').place(x = 20, y = 70)        # click radiobutton on screen --> value, F, gotofeature = self.conversion_type   
        self.conversion_type_c     = ttk.Radiobutton(self, text = 'celsius', variable = self.conversion_type, value = 'C').place(x = 20, y = 95)           # click radiobutton on screen --> value, C, gotofeature = self.conversion_type


    def validatetemperature(self, *args):
        value = self.temperature.get()                                 # screen interaction: capturamos del interfaz gráfico data introducido y acumulamos
        try:
            float(value)
            self.__previous_value = value
        except:
            self.temperature.set(self.__previous_value)                # screen interaction: devolvemos al interfaz gráfico último valor validado introducido
    
     
     #def converter(self, temperature, conversion_type):
        
        
    
    def maincycle(self):
        # manage events
        self.mainloop()    

if __name__ == '__main__':
    app = mainApp()
    app.maincycle()