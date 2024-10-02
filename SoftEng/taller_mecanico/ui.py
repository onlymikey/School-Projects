import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

# User imports
from Controllers.user_controller import UserController
from Models.user_model import User
from Services.user_service import UserService

# Customer imports
from Models.customer_model import Customer
from Services.customer_service import CustomerService

# Vehicle imports
from Services.vehicle_service import VehicleService
from Models.vehicle_model import Vehicle

global editing_mode
global logged_in_user_id

# Función para validar que los campos no estén vacíos
def validate_fields(entries):
    for entry in entries:
        if not entry.get().strip():
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return False
    return True

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.user_controller = UserController()
        self.user_service = UserService()
        self.root.title("Login")

        # Crear el contenedor principal
        self.frame = ttk.Frame(self.root, padding="100 50 100 50")
        self.frame.grid(row=0, column=0, padx=50, pady=50, sticky="nsew")

        # Ajustar redimensionamiento
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Campos de entrada para nombre de usuario y contraseña
        ttk.Label(self.frame, text="User Name:").grid(row=0, column=0, sticky=tk.W)
        self.username_entry = ttk.Entry(self.frame, width=30)
        self.username_entry.grid(row=0, column=1, pady=5)

        ttk.Label(self.frame, text="Password:").grid(row=1, column=0, sticky=tk.W)
        self.password_entry = ttk.Entry(self.frame, show="*", width=30)
        self.password_entry.grid(row=1, column=1, pady=5)

        # Botón para acceder (centrado)
        self.login_button = ttk.Button(self.frame, text="Acceder", command=self.on_login, width=15)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10, sticky=tk.EW)

    def check_empty_fields(self):
        """Verificar que los campos no estén vacíos."""
        if not self.username_entry.get() or not self.password_entry.get():
            return False
        return True

    def check_password_format(self, password):
        """Verificar que la contraseña tenga mayúsculas, minúsculas, números y caracteres especiales."""
        if (len(password) < 8 or not re.search(r'[A-Z]', password) or 
                not re.search(r'[a-z]', password) or 
                not re.search(r'\d', password) or 
                not re.search(r'[\W_]', password)):
            return False
        return True

    def on_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Verificar que los campos no estén vacíos
        if not self.check_empty_fields():
            messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
            return
        #esto si quedara, solo la omito para hacer pruebas
        # Verificar que la contraseña cumpla con el formato adecuado
        # if not self.check_password_format(password):
        #     messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres, incluyendo mayúsculas, minúsculas, números y caracteres especiales.")
        #     return

        # Si pasa las verificaciones, intentar verificar en la base de datos
        if self.check_credentials(username, password):
            global logged_in_user_id
            user = self.user_service.get_user_by_username(username)
            if user:
                logged_in_user_id = user.id
                messagebox.showinfo("Éxito", "Login exitoso")
                # Ocultar ventana de login y mostrar la ventana de menú
                self.frame.grid_forget()
                MenuWindow(self.root)
                #DEBUG (Security Risk)
                print(logged_in_user_id)
            else:
                messagebox.showerror("Error", "Usuario no encontrado.")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    def check_credentials(self, username, password):
        """Verificar si el usuario y la contraseña son válidos en la base de datos."""
        return self.user_controller.verify_credentials(username, password)


class MenuWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal")

        # Ajustar el tamaño de la ventana a 1000x500 píxeles (relación 100x50)
        self.root.geometry("700x350")

        # Crear un contenedor
        self.frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Ajustar redimensionamiento
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Crear el menú
        self.create_menu()

    def create_menu(self):
        # Crear la barra de menú
        menu_bar = tk.Menu(self.root)

        # Crear el menú desplegable "File"
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Users", command=self.open_users)
        file_menu.add_command(label="Customers", command=self.open_customers)
        file_menu.add_command(label="Vehicles", command=self.open_vehicles)
        file_menu.add_command(label="Service")
        file_menu.add_command(label="Parts")
        file_menu.add_separator()  # Línea separadora
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Añadir el menú "File" a la barra de menú
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Configurar la barra de menú en la ventana
        self.root.config(menu=menu_bar)

    def open_users(self):
        # Aquí abrirás la interfaz de usuarios (lógica aún por implementar)
        self.frame.grid_forget()
        UsersWindow(self.root)

    def open_customers(self):
        # Aquí abrirás la interfaz de clientes (lógica aún por implementar)
        self.frame.grid_forget()
        CustomersWindow(self.root)

    def open_vehicles(self):
        # Aquí abrirás la interfaz de vehículos (lógica aún por implementar)
        self.frame.grid_forget()
        VehicleWindow(self.root)


class UsersWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Users")
        self.user_service = UserService()
        global editing_mode
        editing_mode = False

        # Crear un contenedor principal
        self.frame = ttk.Frame(self.root, padding="5 5 5 5")
        self.frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Ajustar redimensionamiento
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Fila 1: Label "Ingrese ID a buscar:" + Entry + Botón "Buscar"
        ttk.Label(self.frame, text="Ingrese ID a buscar:").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        self.id_entry = ttk.Entry(self.frame, width=20)
        self.id_entry.grid(row=0, column=1, padx=2, pady=2, sticky="ew")  # Se ajusta el `sticky` para expandir Entry
        self.search_button = ttk.Button(self.frame, text="Buscar", command=self.search_user)
        self.search_button.grid(row=0, column=2, padx=2, pady=2)

        # Fila 2: Label "Usuario ID:"
        ttk.Label(self.frame, text="Usuario ID:").grid(row=1, column=0, sticky="w", padx=2, pady=2)
        self.user_id_label = ttk.Label(self.frame, text="")
        self.user_id_label.grid(row=1, column=1, padx=2, pady=2, sticky="ew")

        # Fila 3: Label "Nombre" + Entry
        ttk.Label(self.frame, text="Nombre:").grid(row=2, column=0, sticky="w", padx=2, pady=2)
        self.name_entry = ttk.Entry(self.frame, width=30)
        self.name_entry.grid(row=2, column=1, padx=2, pady=2, sticky="ew")

        # Fila 4: Label "UserName" + Entry
        ttk.Label(self.frame, text="UserName:").grid(row=3, column=0, sticky="w", padx=2, pady=2)
        self.username_entry = ttk.Entry(self.frame, width=30)
        self.username_entry.grid(row=3, column=1, padx=2, pady=2, sticky="ew")

        # Fila 5: Label "Password" + Entry
        ttk.Label(self.frame, text="Password:").grid(row=4, column=0, sticky="w", padx=2, pady=2)
        self.password_entry = ttk.Entry(self.frame, show="*", width=30)
        self.password_entry.grid(row=4, column=1, padx=2, pady=2, sticky="ew")

        # Fila 6: Label "Perfil" + ComboBox
        ttk.Label(self.frame, text="Perfil:").grid(row=5, column=0, sticky="w", padx=2, pady=2)
        self.profile_combobox = ttk.Combobox(self.frame, values=["Administrador", "Secretaria", "Mecanico"], state="readonly")
        self.profile_combobox.grid(row=5, column=1, padx=2, pady=2, sticky="ew")
        self.profile_combobox.current(0)

        # Fila 7: Botones "Nuevo", "Salvar", "Cancelar", "Editar"
        button_frame = ttk.Frame(self.frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=10)

        self.new_button = ttk.Button(button_frame, text="Nuevo", command=self.on_new)
        self.new_button.grid(row=0, column=0, padx=5)

        self.save_button = ttk.Button(button_frame, text="Salvar", command=self.create_user)
        self.save_button.grid(row=0, column=1, padx=5)

        self.cancel_button = ttk.Button(button_frame, text="Cancelar", command=self.on_cancel)
        self.cancel_button.grid(row=0, column=2, padx=5)

        self.edit_button = ttk.Button(button_frame, text="Editar", command=self.on_edit)
        self.edit_button.grid(row=0, column=3, padx=5)

        # Ajuste de redimensionamiento de columnas
        self.frame.grid_columnconfigure(0, weight=0)  # Evitamos que se expanda demasiado
        self.frame.grid_columnconfigure(1, weight=1)  # Solo la columna 1 se expandirá
        self.frame.grid_columnconfigure(2, weight=0)  # Evitamos que la columna del botón Buscar se expanda

        # Ajustar tamaño de la ventana
        self.root.geometry("600x250")

        # Desactivar campos de texto y botones por defecto
        self.disable_fields()
        self.save_button.config(state='disabled')
        self.cancel_button.config(state='disabled')

    def create_user(self):
        global editing_mode
        if not validate_fields([self.name_entry, self.username_entry, self.password_entry, self.profile_combobox]):
            return
        name = self.name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        profile = self.profile_combobox.get()
        user = User(id=None, name=name, username=username, password=password, profile=profile)

        try:
            if editing_mode:
                user.id = int(self.user_id_label.cget("text"))
                self.user_service.update_user(user)
                messagebox.showinfo("Éxito", "Usuario actualizado exitosamente.")

            else:
                self.user_service.create_user(user)
                messagebox.showinfo("Éxito", "Usuario creado exitosamente.")

            self.limpiar_campos()
            self.disable_fields()
            self.search_button.config(state='enabled')
            self.edit_button.config(state='enabled')
            self.save_button.config(state='disabled')
            self.cancel_button.config(state='disabled')
            self.new_button.config(state='enabled')
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear el usuario: {e}")
            self.limpiar_campos()
            self.disable_fields()
            self.search_button.config(state='enabled')
            self.edit_button.config(state='enabled')
            self.save_button.config(state='disabled')
            self.cancel_button.config(state='disabled')
            editing_mode = False

    def on_edit(self):
        global editing_mode
        if not self.user_id_label.cget("text"):
            messagebox.showwarning("Advertencia", "Primero debe buscar un usuario antes de editar.")
            return
        editing_mode = True
        self.enable_fields()
        self.search_button.config(state='disabled')
        self.edit_button.config(state='disabled')
        self.save_button.config(state='enabled')
        self.cancel_button.config(state='enabled')
        self.new_button.config(state='disabled')

    def limpiar_campos(self):
        self.name_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.profile_combobox.set(self.profile_combobox['values'][0])

    def on_cancel(self):
        self.limpiar_campos()
        self.disable_fields()
        self.search_button.config(state='enabled')
        self.edit_button.config(state='enabled')

    def on_new(self):
        self.enable_fields()
        self.limpiar_campos()
        self.search_button.config(state='disabled')
        self.edit_button.config(state='disabled')
        self.save_button.config(state='enabled')
        self.cancel_button.config(state='enabled')

    def search_user(self):
        user_id = self.id_entry.get()
        if user_id:
            try:
                user = self.user_service.get_user(int(user_id))
                if user:
                    self.user_id_label.config(text=user.id)
                    self.name_entry.config(state='normal')
                    self.name_entry.delete(0, tk.END)
                    self.name_entry.insert(0, user.name)
                    self.name_entry.config(state='disabled')

                    self.username_entry.config(state='normal')
                    self.username_entry.delete(0, tk.END)
                    self.username_entry.insert(0, user.username)
                    self.username_entry.config(state='disabled')

                    self.password_entry.config(state='normal')
                    self.password_entry.delete(0, tk.END)
                    self.password_entry.insert(0, user.password)
                    self.password_entry.config(state='disabled')

                    self.profile_combobox.config(state='readonly')
                    self.profile_combobox.set(user.profile)
                    self.profile_combobox.config(state='disabled')
                else:
                    messagebox.showerror("Error", "Usuario no encontrado.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al buscar el usuario: {e}")
        else:
            messagebox.showerror("Error", "Por favor ingrese un ID de usuario.")

    def enable_fields(self):
        self.name_entry.config(state='normal')
        self.username_entry.config(state='normal')
        self.password_entry.config(state='normal')
        self.profile_combobox.config(state='readonly')

    def disable_fields(self):
        self.name_entry.config(state='disabled')
        self.username_entry.config(state='disabled')
        self.password_entry.config(state='disabled')
        self.profile_combobox.config(state='disabled')


class CustomersWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Customers")
        self.customer_service = CustomerService()
        self.user_service = UserService()
        self.user_controller = UserController()
        global editing_mode
        editing_mode = False

        # Crear un contenedor principal
        self.frame = ttk.Frame(self.root, padding="5 5 5 5")
        self.frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Ajustar redimensionamiento
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Fila 1: Label "Ingrese ID a buscar:" + Entry + Botón "Buscar"
        ttk.Label(self.frame, text="Ingrese ID a buscar:").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        self.id_entry = ttk.Entry(self.frame, width=20)
        self.id_entry.grid(row=0, column=1, padx=2, pady=2, sticky="ew")  # Se ajusta el `sticky` para expandir Entry
        self.search_button = ttk.Button(self.frame, text="Buscar", command= self.search_customer)
        self.search_button.grid(row=0, column=2, padx=2, pady=2)

        # Fila 2: Label "Cliente ID:"
        ttk.Label(self.frame, text="Cliente ID:").grid(row=1, column=0, sticky="w", padx=2, pady=2)
        self.client_id_label = ttk.Label(self.frame, text="")
        self.client_id_label.grid(row=1, column=1, padx=2, pady=2, sticky="ew")

        # Fila 3: Label "UserName" + Entry + Label "User ID" + Entry
        ttk.Label(self.frame, text="UserName:").grid(row=2, column=0, sticky="w", padx=2, pady=2)
        self.username_entry = ttk.Entry(self.frame, width=30)
        self.username_entry.grid(row=2, column=1, padx=2, pady=2, sticky="ew")

        ttk.Label(self.frame, text="User ID:").grid(row=2, column=2, sticky="w", padx=2, pady=2)
        self.user_id_entry = ttk.Entry(self.frame, width=30)
        self.user_id_entry.grid(row=2, column=3, padx=2, pady=2, sticky="ew")

        # Fila 4: Label "Nombre Cliente" + Entry
        ttk.Label(self.frame, text="Nombre Cliente:").grid(row=3, column=0, sticky="w", padx=2, pady=2)
        self.client_name_entry = ttk.Entry(self.frame, width=30)
        self.client_name_entry.grid(row=3, column=1, padx=2, pady=2, sticky="ew")

        # Fila 5: Label "Teléfono" + Entry
        ttk.Label(self.frame, text="Teléfono:").grid(row=4, column=0, sticky="w", padx=2, pady=2)
        self.phone_entry = ttk.Entry(self.frame, width=30)
        self.phone_entry.grid(row=4, column=1, padx=2, pady=2, sticky="ew")

        # Fila 7: Botones "Nuevo", "Salvar", "Cancelar", "Editar"
        button_frame = ttk.Frame(self.frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=10)

        self.new_button = ttk.Button(button_frame, text="Nuevo", command=self.on_new)
        self.new_button.grid(row=0, column=0, padx=5)

        self.save_button = ttk.Button(button_frame, text="Salvar", command=self.create_client)
        self.save_button.grid(row=0, column=1, padx=5)

        self.cancel_button = ttk.Button(button_frame, text="Cancelar", command=self.on_cancel)
        self.cancel_button.grid(row=0, column=2, padx=5)

        self.edit_button = ttk.Button(button_frame, text="Editar", command=self.on_edit)
        self.edit_button.grid(row=0, column=3, padx=5)

        # Ajuste de redimensionamiento de columnas
        self.frame.grid_columnconfigure(0, weight=0)  # Evitamos que se expanda demasiado
        self.frame.grid_columnconfigure(1, weight=1)  # Solo la columna 1 se expandirá
        self.frame.grid_columnconfigure(2, weight=0)  # Evitamos que la columna del botón Buscar se expanda

        # Ajustar tamaño de la ventana
        self.root.geometry("600x250")

        # Desactivar campos de texto y botones por defecto
        self.disable_fields()
        self.save_button.config(state='disabled')
        self.cancel_button.config(state='disabled')

        self.populate_user_info()

    def populate_user_info(self):
        global logged_in_user_id
        user = self.user_service.get_user(logged_in_user_id)
        if user:
            self.username_entry.config(state='normal')
            self.username_entry.insert(0, user.username)
            self.username_entry.config(state='disabled')

            self.user_id_entry.config(state='normal')
            self.user_id_entry.insert(0, user.id)
            self.user_id_entry.config(state='disabled')


    def search_customer(self):
        customer_id = self.id_entry.get()
        if customer_id:
            try:
                customer = self.customer_service.get_customer(int(customer_id))
                if customer:
                    self.client_id_label.config(text=customer.id)
                    self.client_name_entry.config(state='normal')
                    self.client_name_entry.delete(0, tk.END)
                    self.client_name_entry.insert(0, customer.name)
                    self.client_name_entry.config(state='disabled')

                    self.phone_entry.config(state='normal')
                    self.phone_entry.delete(0, tk.END)
                    self.phone_entry.insert(0, customer.phone)
                    self.phone_entry.config(state='disabled')
                else:
                    messagebox.showerror("Error", "Cliente no encontrado.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al buscar el cliente: {e}")
        else:
            messagebox.showerror("Error", "Por favor ingrese un ID de cliente.")

    def on_new(self):
        self.enable_fields()
        self.clear_fields()
        self.search_button.config(state='disabled')
        self.edit_button.config(state='disabled')
        self.save_button.config(state='enabled')
        self.cancel_button.config(state='enabled')

    def create_client(self):
        global editing_mode
        if not validate_fields([self.client_name_entry, self.phone_entry, self.user_id_entry]):
            return
        name = self.client_name_entry.get()
        phone = self.phone_entry.get()
        userid = self.user_id_entry.get()
        customer = Customer(id=None, name=name, phone=phone, userid=userid)

        try:
            if editing_mode:
                customer.id = int(self.client_id_label.cget("text"))
                self.customer_service.update_customer(customer)
                messagebox.showinfo("Éxito", "Cliente actualizado exitosamente.")
            else:
                self.customer_service.create_customer(customer)
                messagebox.showinfo("Éxito", "Cliente creado exitosamente.")

            self.clear_fields()
            self.disable_fields()
            self.search_button.config(state='enabled')
            self.edit_button.config(state='enabled')
            self.save_button.config(state='disabled')
            self.cancel_button.config(state='disabled')
            self.new_button.config(state='enabled')
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear el cliente: {e}")
            self.clear_fields()
            self.disable_fields()
            self.search_button.config(state='enabled')
            self.edit_button.config(state='enabled')
            self.save_button.config(state='disabled')
            self.cancel_button.config(state='disabled')
            editing_mode = False

    def on_cancel(self):
        self.clear_fields()
        self.disable_fields()
        self.search_button.config(state='enabled')
        self.edit_button.config(state='enabled')
        self.save_button.config(state='disabled')
        self.cancel_button.config(state='disabled')
        self.new_button.config(state='enabled')

    def on_edit(self):
        global editing_mode
        if not self.client_id_label.cget("text"):
            messagebox.showwarning("Advertencia", "Primero debe buscar un cliente antes de editar.")
            return
        editing_mode = True
        self.enable_fields()
        self.search_button.config(state='disabled')
        self.edit_button.config(state='disabled')
        self.save_button.config(state='enabled')
        self.cancel_button.config(state='enabled')
        self.new_button.config(state='disabled')

    def clear_fields(self):
        self.client_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def enable_fields(self):
        self.client_name_entry.config(state='normal')
        self.phone_entry.config(state='normal')

    def disable_fields(self):
        self.client_name_entry.config(state='disabled')
        self.phone_entry.config(state='disabled')


class VehicleWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle")
        self.vehicle_service = VehicleService()
        self.customer_service = CustomerService()
        global editing_mode
        editing_mode = False

        # Crear un contenedor principal
        self.frame = ttk.Frame(self.root, padding="5 5 5 5")
        self.frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Ajustar redimensionamiento
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Fila 1: Label "Ingrese Matricula a buscar:" + Entry + Botón "Buscar"
        ttk.Label(self.frame, text="Ingrese Matricula a buscar:").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        self.registration_search_entry = ttk.Entry(self.frame, width=20)
        self.registration_search_entry.grid(row=0, column=1, padx=2, pady=2, sticky="ew")  # Se ajusta el `sticky` para expandir Entry
        self.search_button = ttk.Button(self.frame, text="Buscar", command=self.search_vehicle)
        self.search_button.grid(row=0, column=2, padx=2, pady=2)

        # Fila 2: Label "Cliente ID:"
        ttk.Label(self.frame, text="Matricula:").grid(row=1, column=0, sticky="w", padx=2, pady=2)
        self.registration_entry = ttk.Entry(self.frame, width=20)
        self.registration_entry.grid(row=1, column=1, padx=2, pady=2, sticky="ew")

        # Fila 3: Label "Nombre Cliente" + ComboBox + Label "Cliente ID" + Entry
        ttk.Label(self.frame, text="Nombre Cliente:").grid(row=2, column=0, sticky="w", padx=2, pady=2)
        self.client_name_combobox = ttk.Combobox(self.frame, state="readonly")
        self.client_name_combobox.grid(row=2, column=1, padx=2, pady=2, sticky="ew")
        self.client_name_combobox.bind("<<ComboboxSelected>>", self.on_client_selected)

        ttk.Label(self.frame, text="Cliente ID:").grid(row=2, column=2, sticky="w", padx=2, pady=2)
        self.client_id_entry = ttk.Entry(self.frame, width=10, state="disabled")
        self.client_id_entry.grid(row=2, column=3, padx=2, pady=2, sticky="ew")

        # Fila 4: Label "Marca" + Entry
        ttk.Label(self.frame, text="Marca:").grid(row=3, column=0, sticky="w", padx=2, pady=2)
        self.brand_entry = ttk.Entry(self.frame, width=30)
        self.brand_entry.grid(row=3, column=1, padx=2, pady=2, sticky="ew")

        # Fila 5: Label "Modelo" + Entry
        ttk.Label(self.frame, text="Modelo:").grid(row=4, column=0, sticky="w", padx=2, pady=2)
        self.model_entry = ttk.Entry(self.frame, width=30)
        self.model_entry.grid(row=4, column=1, padx=2, pady=2, sticky="ew")

        # Fila 7: Botones "Nuevo", "Salvar", "Cancelar", "Editar"
        button_frame = ttk.Frame(self.frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=10)

        self.new_button = ttk.Button(button_frame, text="Nuevo", command=self.on_new)
        self.new_button.grid(row=0, column=0, padx=5)

        self.save_button = ttk.Button(button_frame, text="Salvar", command=self.create_vehicle)
        self.save_button.grid(row=0, column=1, padx=5)

        self.cancel_button = ttk.Button(button_frame, text="Cancelar", command=self.on_cancel)
        self.cancel_button.grid(row=0, column=2, padx=5)

        self.edit_button = ttk.Button(button_frame, text="Editar", command=self.on_edit)
        self.edit_button.grid(row=0, column=3, padx=5)

        # Ajuste de redimensionamiento de columnas
        self.frame.grid_columnconfigure(0, weight=0)  # Evitamos que se expanda demasiado
        self.frame.grid_columnconfigure(1, weight=1)  # Solo la columna 1 se expandirá
        self.frame.grid_columnconfigure(2, weight=0)  # Evitamos que la columna del botón Buscar se expanda

        # Ajustar tamaño de la ventana
        self.root.geometry("600x250")

        # Desactivar campos de texto y botones por defecto
        self.save_button.config(state='disabled')
        self.cancel_button.config(state='disabled')

        # Desactivar campos de texto y botones por defecto
        self.disable_fields()
        self.save_button.config(state='disabled')
        self.cancel_button.config(state='disabled')

        # Populate customer names in the combobox
        self.populate_customer_names()

    def populate_customer_names(self):
        customer_names = self.customer_service.get_all_customer_names()
        self.client_name_combobox['values'] = customer_names
        print(f"Combobox populated with: {customer_names}")

    def on_client_selected(self, event):
        print("on_client_selected function executed")  # Debug print
        selected_name = self.client_name_combobox.get()
        print(f"Selected client name: {selected_name}")  # Debug print
        customer = self.customer_service.get_customer_by_name(selected_name)
        if customer:
            self.client_id_entry.config(state='normal')
            self.client_id_entry.delete(0, tk.END)
            self.client_id_entry.insert(0, customer.id)
            self.client_id_entry.config(state='disabled')
            print(f"Debug: client_id_entry type: {type(customer.id)}")  # Debug print to verify data type

    def search_vehicle(self):
        registration = self.registration_search_entry.get()
        if registration:
            try:
                vehicle = self.vehicle_service.get_vehicle_by_registration(registration)
                if vehicle:
                    self.registration_entry.config(state='normal')
                    self.registration_entry.delete(0, tk.END)
                    self.registration_entry.insert(0, vehicle.registration)
                    self.registration_entry.config(state='disabled')

                    # Debug print to show the clientid being sent
                    print(f"Debug: clientid sent to get_customer: {vehicle.clientid}")

                    customer = self.customer_service.get_customer(vehicle.clientid)
                    print(f"Debug: Customer found: {customer}") # Debug print
                    if customer:
                        self.client_name_combobox.set(customer.name)
                        self.client_id_entry.config(state='normal')
                        self.client_id_entry.delete(0, tk.END)
                        self.client_id_entry.insert(0, customer.id)
                        self.client_id_entry.config(state='disabled')
                        print(f"Debug: client_id_entry type: {type(customer.id)}")  # Debug print to verify data type
                    else:
                        messagebox.showerror("Error", "Cliente no encontrado.")

                    self.brand_entry.config(state='normal')
                    self.brand_entry.delete(0, tk.END)
                    self.brand_entry.insert(0, vehicle.brand)
                    self.brand_entry.config(state='disabled')

                    self.model_entry.config(state='normal')
                    self.model_entry.delete(0, tk.END)
                    self.model_entry.insert(0, vehicle.model)
                    self.model_entry.config(state='disabled')
                else:
                    messagebox.showerror("Error", "Vehículo no encontrado.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al buscar el vehículo: {e}")
        else:
            messagebox.showerror("Error", "Por favor ingrese una matrícula.")

    def on_new(self):
        self.clear_fields()
        self.enable_fields()
        self.search_button.config(state='disabled')
        self.edit_button.config(state='disabled')
        self.save_button.config(state='enabled')
        self.cancel_button.config(state='enabled')

    def create_vehicle(self):
        global editing_mode
        if not validate_fields([self.registration_entry, self.client_name_combobox, self.brand_entry, self.model_entry]):
            return
        registration = self.registration_entry.get()
        client_id = self.client_id_entry.get()
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        vehicle = Vehicle(registration, client_id, brand, model)

        try:
            if editing_mode:
                vehicle.registration = self.registration_entry.get()
                self.vehicle_service.update_vehicle(vehicle)
                messagebox.showinfo("Éxito", "Vehículo actualizado exitosamente.")
            else:
                self.vehicle_service.create_vehicle(vehicle)
                messagebox.showinfo("Éxito", "Vehículo creado exitosamente.")

            self.clear_fields()
            self.disable_fields()
            self.search_button.config(state='enabled')
            self.edit_button.config(state='enabled')
            self.save_button.config(state='disabled')
            self.cancel_button.config(state='disabled')
            self.new_button.config(state='enabled')
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear el vehículo: {e}")
            self.clear_fields()
            self.disable_fields()
            self.search_button.config(state='enabled')
            self.edit_button.config(state='enabled')
            self.save_button.config(state='disabled')
            self.cancel_button.config(state='disabled')
            editing_mode = False

    def on_cancel(self):
        self.clear_fields()
        self.disable_fields()
        self.search_button.config(state='enabled')
        self.edit_button.config(state='enabled')
        self.save_button.config(state='disabled')
        self.cancel_button.config(state='disabled')
        self.new_button.config(state='enabled')

    def on_edit(self):
        global editing_mode
        client_id_text = self.client_id_entry.get()
        if not client_id_text or int(client_id_text) == 0:
            messagebox.showwarning("Advertencia", "Primero debe buscar un vehículo antes de editar.")
            return
        editing_mode = True
        self.enable_fields()
        self.registration_entry.config(state='disabled')
        self.search_button.config(state='disabled')
        self.edit_button.config(state='disabled')
        self.save_button.config(state='enabled')
        self.cancel_button.config(state='enabled')
        self.new_button.config(state='disabled')

    def clear_fields(self):
        self.registration_entry.config(state='normal')  # Ensure the entry is editable
        self.registration_entry.delete(0, tk.END)  # Clear the entry field
        self.registration_entry.config(state='disabled')  # Optionally, disable the entry again if needed
        self.client_name_combobox.delete(0, tk.END)
        self.client_id_entry.config(state='normal')  # Ensure the entry is editable
        self.client_id_entry.delete(0, tk.END)  # Clear the entry field
        self.client_id_entry.config(state='disabled')  # Optionally, disable the entry again if needed
        self.brand_entry.delete(0, tk.END)
        self.model_entry.delete(0, tk.END)

    def enable_fields(self):
        self.registration_entry.config(state='normal')
        self.client_name_combobox.config(state='normal')
        self.brand_entry.config(state='normal')
        self.model_entry.config(state='normal')

    def disable_fields(self):
        self.registration_entry.config(state='disabled')
        self.client_name_combobox.config(state='disabled')
        self.client_id_entry.config(state='disabled')
        self.brand_entry.config(state='disabled')
        self.model_entry.config(state='disabled')

