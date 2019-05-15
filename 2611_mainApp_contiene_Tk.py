
# Tk() contenido en mainApp()

from tkinter import *

class mainApp():
    
    # assumptions:
    
    # 1.- screen:
    size_screen         = '640x480'
    window_title        = 'my_screen'
    background_screen   = 'lightgray'
    
    
    def __init__(self):
        
        # 1.- screen --> root (main_window)
            # a) create
        self.root = Tk()
            # b) customize
                # size
        self.root.geometry(self.size_screen)
                # title
        self.root.title(self.window_title)
                # backgroud
        self.root.configure(bg = self.background_screen)

    def maincycle(self):
        self.root.mainloop()
               





if __name__ == '__main__':
    app = mainApp()
    app.maincycle()
    
    