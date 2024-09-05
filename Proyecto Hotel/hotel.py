import tkinter as tk
from tkinter import ttk, messagebox


class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reservaciones de Hotel")
        self.root.geometry("800x400")

        # Estructuras de datos
        self.clientes = {}  # Diccionario para almacenar clientes
        self.reservaciones = {}  # Diccionario para almacenar reservaciones
        self.habitaciones = {}  # Diccionario para almacenar habitaciones

        # Crear el control de pestañas
        self.tab_control = ttk.Notebook(root)

        # Crear las pestañas
        self.tab_clientes = ttk.Frame(self.tab_control)
        self.tab_reservaciones = ttk.Frame(self.tab_control)
        self.tab_habitaciones = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_clientes, text="Clientes")
        self.tab_control.add(self.tab_reservaciones, text="Reservaciones")
        self.tab_control.add(self.tab_habitaciones, text="Habitación")

        self.tab_control.pack(expand=1, fill="both")

        # Interfaz de Clientes
        self.clientes_ui()

        # Interfaz de Reservaciones
        self.reservaciones_ui()

        # Interfaz de Habitaciones
        self.habitaciones_ui()

    def clientes_ui(self):
        # Labels y entradas para clientes
        tk.Label(self.tab_clientes, text="Ingrese Id del Cliente:").grid(row=0, column=0, padx=5, pady=5)
        self.cliente_id_entry = tk.Entry(self.tab_clientes)
        self.cliente_id_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.tab_clientes, text="Buscar", command=self.buscar_cliente).grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self.tab_clientes, text="ID:").grid(row=1, column=0, padx=5, pady=5)
        self.cliente_id_label = tk.Entry(self.tab_clientes)
        self.cliente_id_label.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab_clientes, text="Nombre:").grid(row=2, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(self.tab_clientes)
        self.nombre_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab_clientes, text="Dirección:").grid(row=3, column=0, padx=5, pady=5)
        self.direccion_entry = tk.Entry(self.tab_clientes)
        self.direccion_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab_clientes, text="Email:").grid(row=2, column=2, padx=5, pady=5)
        self.email_entry = tk.Entry(self.tab_clientes)
        self.email_entry.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(self.tab_clientes, text="Teléfono:").grid(row=3, column=2, padx=5, pady=5)
        self.telefono_entry = tk.Entry(self.tab_clientes)
        self.telefono_entry.grid(row=3, column=3, padx=5, pady=5)

        # Botones
        tk.Button(self.tab_clientes, text="Nuevo", command=self.nuevo_cliente).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.tab_clientes, text="Salvar", command=self.salvar_cliente).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(self.tab_clientes, text="Cancelar", command=self.limpiar_campos_cliente).grid(row=4, column=2, padx=5,
                                                                                                pady=5)
        tk.Button(self.tab_clientes, text="Editar", command=self.editar_cliente).grid(row=4, column=3, padx=5, pady=5)
        tk.Button(self.tab_clientes, text="Eliminar", command=self.eliminar_cliente).grid(row=4, column=4, padx=5,
                                                                                          pady=5)

    def buscar_cliente(self):
        cliente_id = self.cliente_id_entry.get()
        if cliente_id in self.clientes:
            cliente = self.clientes[cliente_id]
            self.cliente_id_label.delete(0, tk.END)
            self.cliente_id_label.insert(0, cliente_id)
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, cliente['nombre'])
            self.direccion_entry.delete(0, tk.END)
            self.direccion_entry.insert(0, cliente['direccion'])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, cliente['email'])
            self.telefono_entry.delete(0, tk.END)
            self.telefono_entry.insert(0, cliente['telefono'])
        else:
            messagebox.showwarning("Error", "Cliente no encontrado")

    def nuevo_cliente(self):
        self.limpiar_campos_cliente()

    def salvar_cliente(self):
        cliente_id = self.cliente_id_label.get()
        nombre = self.nombre_entry.get()
        direccion = self.direccion_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()

        if cliente_id and nombre:
            self.clientes[cliente_id] = {
                'nombre': nombre,
                'direccion': direccion,
                'email': email,
                'telefono': telefono
            }
            messagebox.showinfo("Éxito", "Cliente guardado exitosamente")
        else:
            messagebox.showwarning("Error", "El ID y Nombre son obligatorios")

    def editar_cliente(self):
        cliente_id = self.cliente_id_entry.get()
        if cliente_id in self.clientes:
            nombre = self.nombre_entry.get()
            direccion = self.direccion_entry.get()
            email = self.email_entry.get()
            telefono = self.telefono_entry.get()

            self.clientes[cliente_id] = {
                'nombre': nombre,
                'direccion': direccion,
                'email': email,
                'telefono': telefono
            }
            messagebox.showinfo("Éxito", "Cliente editado exitosamente")
        else:
            messagebox.showwarning("Error", "Cliente no encontrado")

    def eliminar_cliente(self):
        cliente_id = self.cliente_id_entry.get()
        if cliente_id in self.clientes:
            del self.clientes[cliente_id]
            messagebox.showinfo("Éxito", "Cliente eliminado exitosamente")
            self.limpiar_campos_cliente()
        else:
            messagebox.showwarning("Error", "Cliente no encontrado")

    def limpiar_campos_cliente(self):
        self.cliente_id_label.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.cliente_id_entry.delete(0, tk.END)

    def reservaciones_ui(self):
        # Labels y entradas para reservaciones
        tk.Label(self.tab_reservaciones, text="Ingrese Reservación:").grid(row=0, column=0, padx=5, pady=5)
        self.reservacion_id_entry = tk.Entry(self.tab_reservaciones)
        self.reservacion_id_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.tab_reservaciones, text="Buscar Reservación", command=self.buscar_reservacion).grid(row=0,
                                                                                                           column=2,
                                                                                                           padx=5,
                                                                                                           pady=5)

        tk.Label(self.tab_reservaciones, text="Reservacion ID:").grid(row=1, column=0, padx=5, pady=5)
        self.reservacion_id_label = tk.Entry(self.tab_reservaciones)
        self.reservacion_id_label.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab_reservaciones, text="Cliente ID:").grid(row=2, column=0, padx=5, pady=5)
        self.cliente_id_reservacion = tk.Entry(self.tab_reservaciones)
        self.cliente_id_reservacion.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab_reservaciones, text="Habitacion ID:").grid(row=3, column=0, padx=5, pady=5)
        self.habitacion_id_reservacion = tk.Entry(self.tab_reservaciones)
        self.habitacion_id_reservacion.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.tab_reservaciones, text="Fecha Reservación:").grid(row=2, column=2, padx=5, pady=5)
        self.fecha_reservacion_entry = tk.Entry(self.tab_reservaciones)
        self.fecha_reservacion_entry.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(self.tab_reservaciones, text="Fecha Salida:").grid(row=3, column=2, padx=5, pady=5)
        self.fecha_salida_entry = tk.Entry(self.tab_reservaciones)
        self.fecha_salida_entry.grid(row=3, column=3, padx=5, pady=5)

        tk.Label(self.tab_reservaciones, text="Costo:").grid(row=4, column=0, padx=5, pady=5)
        self.costo_entry = tk.Entry(self.tab_reservaciones)
        self.costo_entry.grid(row=4, column=1, padx=5, pady=5)

        # Botones para las acciones
        tk.Button(self.tab_reservaciones, text="Nueva Reservación", command=self.nueva_reservacion).grid(row=5,
                                                                                                         column=0,
                                                                                                         padx=5, pady=5)
        tk.Button(self.tab_reservaciones, text="Reservar", command=self.reservar).grid(row=5, column=1, padx=5, pady=5)
        tk.Button(self.tab_reservaciones, text="Cancelar Reservación", command=self.cancelar_reservacion).grid(row=5,
                                                                                                               column=2,
                                                                                                               padx=5,
                                                                                                               pady=5)
        tk.Button(self.tab_reservaciones, text="Editar", command=self.editar_reservacion).grid(row=5, column=3, padx=5,
                                                                                               pady=5)

    def buscar_reservacion(self):
        reservacion_id = self.reservacion_id_entry.get()
        if reservacion_id in self.reservaciones:
            reservacion = self.reservaciones[reservacion_id]
            self.reservacion_id_label.delete(0, tk.END)
            self.reservacion_id_label.insert(0, reservacion_id)
            self.cliente_id_reservacion.delete(0, tk.END)
            self.cliente_id_reservacion.insert(0, reservacion['cliente_id'])
            self.habitacion_id_reservacion.delete(0, tk.END)
            self.habitacion_id_reservacion.insert(0, reservacion['habitacion_id'])
            self.fecha_reservacion_entry.delete(0, tk.END)
            self.fecha_reservacion_entry.insert(0, reservacion['fecha_reservacion'])
            self.fecha_salida_entry.delete(0, tk.END)
            self.fecha_salida_entry.insert(0, reservacion['fecha_salida'])
            self.costo_entry.delete(0, tk.END)
            self.costo_entry.insert(0, reservacion['costo'])
        else:
            messagebox.showwarning("Error", "Reservación no encontrada")

    def cancelar_reservacion(self):
        reservacion_id = self.reservacion_id_label.get()
        if reservacion_id in self.reservaciones:
            habitacion_id = self.reservaciones[reservacion_id]['habitacion_id']
            del self.reservaciones[reservacion_id]
            self.habitaciones[habitacion_id]['estado'] = 'Libre'
            messagebox.showinfo("Éxito", "Reservación cancelada exitosamente")
            self.nueva_reservacion()
        else:
            messagebox.showwarning("Error", "Reservación no encontrada")

    def nueva_reservacion(self):
        self.reservacion_id_label.delete(0, tk.END)
        self.cliente_id_reservacion.delete(0, tk.END)
        self.habitacion_id_reservacion.delete(0, tk.END)
        self.fecha_reservacion_entry.delete(0, tk.END)
        self.fecha_salida_entry.delete(0, tk.END)
        self.costo_entry.delete(0, tk.END)

    def reservar(self):
        reservacion_id = self.reservacion_id_label.get()
        cliente_id = self.cliente_id_reservacion.get()
        habitacion_id = self.habitacion_id_reservacion.get()
        fecha_reservacion = self.fecha_reservacion_entry.get()
        fecha_salida = self.fecha_salida_entry.get()
        costo = self.costo_entry.get()

        if reservacion_id and cliente_id and habitacion_id:
            if habitacion_id in self.habitaciones:
                if self.habitaciones[habitacion_id]['estado'] == 'Libre':
                    self.reservaciones[reservacion_id] = {
                        'cliente_id': cliente_id,
                        'habitacion_id': habitacion_id,
                        'fecha_reservacion': fecha_reservacion,
                        'fecha_salida': fecha_salida,
                        'costo': costo
                    }
                    self.habitaciones[habitacion_id]['estado'] = 'Ocupado'
                    messagebox.showinfo("Éxito", "Reservación guardada exitosamente")
                else:
                    messagebox.showwarning("Error", "La habitación está ocupada")
            else:
                messagebox.showwarning("Error", "Habitación no encontrada")
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")

    def cancelar_reservacion(self):
        reservacion_id = self.reservacion_id_label.get()
        if reservacion_id in self.reservaciones:
            habitacion_id = self.reservaciones[reservacion_id]['habitacion_id']
            del self.reservaciones[reservacion_id]
            self.habitaciones[habitacion_id]['estado'] = 'Libre'
            messagebox.showinfo("Éxito", "Reservación cancelada exitosamente")
            self.nueva_reservacion()
        else:
            messagebox.showwarning("Error", "Reservación no encontrada")

    def editar_reservacion(self):
        reservacion_id = self.reservacion_id_label.get()
        cliente_id = self.cliente_id_reservacion.get()
        habitacion_id = self.habitacion_id_reservacion.get()
        fecha_reservacion = self.fecha_reservacion_entry.get()
        fecha_salida = self.fecha_salida_entry.get()
        costo = self.costo_entry.get()

        if reservacion_id in self.reservaciones:
            self.reservaciones[reservacion_id] = {
                'cliente_id': cliente_id,
                'habitacion_id': habitacion_id,
                'fecha_reservacion': fecha_reservacion,
                'fecha_salida': fecha_salida,
                'costo': costo
            }
            messagebox.showinfo("Éxito", "Reservación editada exitosamente")
        else:
            messagebox.showwarning("Error", "Reservación no encontrada")

    def habitaciones_ui(self):
        # Labels y entradas para habitaciones
        tk.Label(self.tab_habitaciones, text="Ingrese Numero de Habitación:").grid(row=0, column=0, padx=5, pady=5)
        self.habitacion_num_entry = tk.Entry(self.tab_habitaciones)
        self.habitacion_num_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.tab_habitaciones, text="Buscar", command=self.buscar_habitacion).grid(row=0, column=2, padx=5,
                                                                                             pady=5)

        tk.Label(self.tab_habitaciones, text="Habitacion ID:").grid(row=1, column=0, padx=5, pady=5)
        self.habitacion_id_entry = tk.Entry(self.tab_habitaciones)
        self.habitacion_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.tab_habitaciones, text="Numero:").grid(row=2, column=0, padx=5, pady=5)
        self.habitacion_num_label = tk.Entry(self.tab_habitaciones)
        self.habitacion_num_label.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.tab_habitaciones, text="Seleccione Estado Habitación:").grid(row=1, column=2, padx=5, pady=5)
        self.estado_habitacion = ttk.Combobox(self.tab_habitaciones, values=["Libre", "Ocupada"])
        self.estado_habitacion.grid(row=1, column=3, padx=5, pady=5)

        # Botones para las acciones
        tk.Button(self.tab_habitaciones, text="Nueva Habitación", command=self.nueva_habitacion).grid(row=3, column=0,
                                                                                                      padx=5, pady=5)
        tk.Button(self.tab_habitaciones, text="Salvar", command=self.salvar_habitacion).grid(row=3, column=1, padx=5,
                                                                                             pady=5)
        tk.Button(self.tab_habitaciones, text="Editar", command=self.editar_habitacion).grid(row=3, column=2, padx=5,
                                                                                             pady=5)

    def salvar_habitacion(self):
        habitacion_id = self.habitacion_id_entry.get()
        numero = self.habitacion_num_label.get()
        estado = self.estado_habitacion.get()

        if habitacion_id and numero:
            self.habitaciones[habitacion_id] = {
                'numero': numero,
                'estado': estado
            }
            messagebox.showinfo("Éxito", "Habitación guardada exitosamente")
        else:
            messagebox.showwarning("Error", "El ID y Número son obligatorios")

    def buscar_habitacion(self):
        habitacion_num = self.habitacion_num_entry.get()
        for habitacion_id, habitacion in self.habitaciones.items():
            if habitacion['numero'] == habitacion_num:
                self.habitacion_id_entry.delete(0, tk.END)
                self.habitacion_id_entry.insert(0, habitacion_id)
                self.habitacion_num_label.delete(0, tk.END)
                self.habitacion_num_label.insert(0, habitacion_num)
                self.estado_habitacion.set(habitacion['estado'])
                return
        messagebox.showwarning("Error", "Habitación no encontrada")

    def nueva_habitacion(self):
        self.habitacion_id_entry.delete(0, tk.END)
        self.habitacion_num_label.delete(0, tk.END)
        self.estado_habitacion.set('Libre')

    def editar_habitacion(self):
        habitacion_id = self.habitacion_id_entry.get()
        if habitacion_id in self.habitaciones:
            numero = self.habitacion_num_label.get()
            estado = self.estado_habitacion.get()
            self.habitaciones[habitacion_id] = {
                'numero': numero,
                'estado': estado
            }
            messagebox.showinfo("Éxito", "Habitación editada exitosamente")
        else:
            messagebox.showwarning("Error", "Habitación no encontrada")


if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()
