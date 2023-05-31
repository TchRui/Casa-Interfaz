import serial
import serial.tools.list_ports
from tkinter import *
from tkinter import messagebox

class Interface:
    def __init__(self):
        self.arduino = serial.Serial('COM7', 9600)
        self.ventana()
        """ ports = list(serial.tools.list_ports.comports())
        print(ports)
        #* Creamos una excepción si no se puede conectar al puerto serial
        try:
            self.arduino = serial.Serial(ports[0].device, 9600)
            self.ventana()
        except:
            messagebox.showerror("Casa inteligente - Arduino", "No se pudo identificar al puerto serial. No se encontraron dispositivos conectados.")
            exit() """

    
    def ventana(self):
        root = Tk()
        root.title("Casa inteligente - Arduino")

        width_root = 879
        height_root = 348
        x_root = root.winfo_screenwidth() // 2 - width_root // 2
        y_root = root.winfo_screenheight()// 2 - height_root // 2 - 42
        position = str(width_root) + "x" + str(height_root) + "+" + str(x_root) + "+" + str(y_root)
        root.geometry(position)

        root.iconbitmap("icono.ico")
        root.config(bg='#7FADA9')

        #Coloca la imágen de fondo
        imagen = PhotoImage(file="fondo.png")
        fondo = Label(root, image=imagen)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.boton_encender_a = Button(root, text="E", width=1, command=self.encender_led1)
        self.boton_encender_a.place(x=863, y=321)
        self.boton_apagar_a = Button(root, text="A", width=1, command=self.apagar_led1)
        self.boton_apagar_a.place(x=863, y=293)
        
        self.boton_encender_b = Button(root, text="E", width=1, command=self.encender_led2)
        self.boton_encender_b.place(x=765, y=321)
        self.boton_apagar_b = Button(root, text="A", width=1, command=self.apagar_led2)
        self.boton_apagar_b.place(x=783, y=321)

        self.boton_encender_c = Button(root, text="E", width=1, command=self.encender_led3)
        self.boton_encender_c.place(x=635, y=321)
        self.boton_apagar_c = Button(root, text="A", width=1, command=self.apagar_led3)
        self.boton_apagar_c.place(x=653, y=321)

        self.boton_encender_d = Button(root, text="E", width=1, command=self.encender_led4)
        self.boton_encender_d.place(x=560, y=158)
        self.boton_apagar_d = Button(root, text="A", width=1, command=self.apagar_led4)
        self.boton_apagar_d.place(x=578, y=158)

        self.boton_encender_e = Button(root, text="E", width=1, command=self.encender_led5)
        self.boton_encender_e.place(x=350, y=228)
        self.boton_apagar_e = Button(root, text="A", width=1, command=self.apagar_led5)
        self.boton_apagar_e.place(x=368, y=228)

        self.boton_encender_f = Button(root, text="E", width=1, command=self.encender_led6)
        self.boton_encender_f.place(x=290, y=152)
        self.boton_apagar_f = Button(root, text="A", width=1, command=self.apagar_led6)
        self.boton_apagar_f.place(x=290, y=180)

        self.boton_encender_g = Button(root, text="E", width=1, command=self.encender_led7)
        self.boton_encender_g.place(x=200, y=321)
        self.boton_apagar_g = Button(root, text="A", width=1, command=self.apagar_led7)
        self.boton_apagar_g.place(x=218, y=321)
        root.mainloop()
    
    def encender_led1(self):
        self.arduino.write(b'A')

    def apagar_led1(self):
        self.arduino.write(b'a')

    def encender_led2(self):
        self.arduino.write(b'B')
    
    def apagar_led2(self):
        self.arduino.write(b'b')
    
    def encender_led3(self):
        self.arduino.write(b'C')
    
    def apagar_led3(self):
        self.arduino.write(b'c')
    
    def encender_led4(self):
        self.arduino.write(b'D')
    
    def apagar_led4(self):
        self.arduino.write(b'd')
    
    def encender_led5(self):
        self.arduino.write(b'E')
    
    def apagar_led5(self):
        self.arduino.write(b'e')
    
    def encender_led6(self):
        self.arduino.write(b'F')
    
    def apagar_led6(self):
        self.arduino.write(b'f')
    
    def encender_led7(self):
        self.arduino.write(b'G')
    
    def apagar_led7(self):
        self.arduino.write(b'g')
    
if __name__ == "__main__":
    interface_object = Interface()