import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="estetica unisex"
)

if conexion.is_connected():
  print("Conexión exitosa a la base de datos")

cursor = conexion.cursor()
consulta = "SELECT * FROM citas"
cursor.execute(consulta)

for fila in cursor.fetchall():
  print(fila)

conexion.close()

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Estetica tec" and password == "1234programacion":
        message_label.config(text="Inicio de sesión exitoso, cierre la ventana porfavor", fg="white")
    else:
        message_label.config(text="Datos incorrectos, verifique porfavor", fg="red")
        
root = tk.Tk()
root.title("Inicio de sesión")
root.geometry("600x400")
root.config(bg="blue")

username_label = tk.Label(root, text="Nombre de usuario:", font=("Arial", 16), bg="blue", fg="white")
username_label.pack(pady=10)

username_entry = tk.Entry(root, font=("Arial", 16))
username_entry.pack(pady=10)

password_label = tk.Label(root, text="Contraseña:", font=("Arial", 16), bg="blue", fg="white")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", font=("Arial", 16))
password_entry.pack(pady=10)


login_button = tk.Button(root, text="Iniciar sesión", font=("Arial", 16), command=login)
login_button.pack(pady=10)

message_label = tk.Label(root, font=("Arial", 16), bg="blue", fg="white")
message_label.pack(pady=10)
root.mainloop()

# AGRAGAMOS LA FUNCION PARA AGREGAR LOS DATOS DENTRO DE LA BASE
def agregar_datos():
    nombre = campo_nombre.get()
    edad = campo_edad.get()
    tipo_servicio = campo_servicio.get()
    sexo = campo_sexo.get()
    fecha = campo_fecha.get()
    telefono = campo_telefono.get()

    tabla.insert("", END, values=(nombre, edad, tipo_servicio, sexo, fecha, telefono))

    campo_nombre.delete(0, END)
    campo_edad.delete(0, END)
    campo_servicio.delete(0, END)
    campo_sexo.delete(0, END)
    campo_fecha.delete(0, END)
    campo_telefono.delete(0, END)

# VENTANA PRINCIPAL
ventana = Tk()
ventana.title("Tabla de citas")

tabla = ttk.Treeview(ventana, columns=("Nombre", "Edad", "Tipo de servicio", "Sexo", "Fecha agendada", "Teléfono"))
tabla.heading("#0", text="")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")
tabla.heading("Tipo de servicio", text="Tipo de servicio")
tabla.heading("Sexo", text="Sexo")
tabla.heading("Fecha agendada", text="Fecha agendada")
tabla.heading("Teléfono", text="Teléfono")
tabla.pack()

# ENTRADA DE LOS DATOS
etiqueta_nombre = Label(ventana, text="Nombre:")
etiqueta_nombre.pack()
campo_nombre = Entry(ventana)
campo_nombre.pack()

etiqueta_edad = Label(ventana, text="Edad:")
etiqueta_edad.pack()
campo_edad = Entry(ventana)
campo_edad.pack()

etiqueta_servicio = Label(ventana, text="Tipo de servicio:")
etiqueta_servicio.pack()
campo_servicio = Entry(ventana)
campo_servicio.pack()

etiqueta_sexo = Label(ventana, text="Sexo:")
etiqueta_sexo.pack()
campo_sexo = Entry(ventana)
campo_sexo.pack()

etiqueta_fecha = Label(ventana, text="Fecha agendada:")
etiqueta_fecha.pack()
campo_fecha = Entry(ventana)
campo_fecha.pack()

etiqueta_telefono = Label(ventana, text="Teléfono:")
etiqueta_telefono.pack()
campo_telefono = Entry(ventana)
campo_telefono.pack()

# BOTON PARA AGREGAR LOS DATOS FINALES
boton_agregar = Button(ventana, text="Agregar", command=agregar_datos)
boton_agregar.pack()

ventana.mainloop()