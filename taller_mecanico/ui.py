import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

from Controllers.user_controller import UserController
from Models.user_model import User
from Services.user_service import UserService

from Models.customer_model import Customer
from Services.customer_service import CustomerService

global editing_mode
global logged_in_user_id

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
        file_menu.add_command(label="Cars")
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
