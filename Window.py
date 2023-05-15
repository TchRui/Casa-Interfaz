import serial
import serial.tools.list_ports
from tkinter import *
from tkinter import messagebox

class Interface:
    def __init__(self):
        ports = list(serial.tools.list_ports.comports())
        print(ports)
        #* Creamos una excepción si no se puede conectar al puerto serial
        try:
            self.arduino = serial.Serial(ports[0].device, 9600)
            self.ventana()
        except:
            messagebox.showerror("Casa inteligente - Arduino", "No se pudo identificar al puerto serial. No se encontraron dispositivos conectados.")
            exit()

    
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
        fondo = Label(root, image=imagen).place(x=0, y=0, relwidth=1, relheight=1)

        self.boton_encender = Button(root, text="Encender LED", command=self.encender_led, )
        self.boton_encender.pack()
        self.boton_apagar = Button(root, text="Apagar LED", command=self.apagar_led)
        self.boton_apagar.pack()

        root.mainloop()
    
    def encender_led(self):
        self.arduino.write(b'H')

    def apagar_led(self):
        self.arduino.write(b'L')

if __name__ == "__main__":
    interface_object = Interface()