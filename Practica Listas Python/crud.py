import tkinter as tk
from tkinter import END, messagebox, ttk

libros = []

def deshabilitar_componentes():
    txId.delete(0, END)
    txTitulo.delete(0, END)
    txAutor.delete(0, END)
    txEditorial.delete(0, END)
    cbClasificacion.set('')

def salvar_libro():
    try:
        if not txId.get().strip():
            raise ValueError("ID vacío")
        libro_id = int(txId.get())
        if any(libro['id'] == libro_id for libro in libros):
            messagebox.showerror(message="ID ya existe", title="Error")
            return
        libro = {
            'id': libro_id,
            'titulo': txTitulo.get(),
            'autor': txAutor.get(),
            'editorial': txEditorial.get(),
            'clasificacion': cbClasificacion.get()
        }
        libros.append(libro)
        deshabilitar_componentes()
        btnNuevo.config(state="normal")
        btnSalvar.config(state="disabled")
        btnCancelar.config(state="disabled")
        print(f"Libro guardado: {libro}")  # Debugging
    except ValueError as e:
        messagebox.showerror(message=str(e), title="Error")

def buscar_libro():
    try:
        if not txId.get().strip():
            raise ValueError("ID vacío")
        id_buscar = int(txId.get())
        print(f"Buscando libro con ID: {id_buscar}")  # Debugging
        deshabilitar_componentes()
        for libro in libros:
            if libro['id'] == id_buscar:
                txTitulo.insert(0, libro['titulo'])
                txAutor.insert(0, libro['autor'])
                txEditorial.insert(0, libro['editorial'])
                cbClasificacion.set(libro['clasificacion'])
                btnEditar.config(state="normal")
                btnEliminar.config(state="normal")
                print(f"Libro encontrado: {libro}")  # Debugging
                return
        messagebox.showinfo(message="Libro no encontrado", title="Info")
    except ValueError as e:
        messagebox.showerror(message=str(e), title="Error")

def nuevo_libro():
    deshabilitar_componentes()
    btnNuevo.config(state="disabled")
    btnSalvar.config(state="normal")
    btnCancelar.config(state="normal")

def cancelar_operacion():
    deshabilitar_componentes()
    btnNuevo.config(state="normal")
    btnSalvar.config(state="disabled")
    btnCancelar.config(state="disabled")
    btnEditar.config(state="disabled")
    btnEliminar.config(state="disabled")

def editar_libro():
    try:
        if not txId.get().strip():
            raise ValueError("ID vacío")
        id_editar = int(txId.get())
        for libro in libros:
            if libro['id'] == id_editar:
                libro['titulo'] = txTitulo.get()
                libro['autor'] = txAutor.get()
                libro['editorial'] = txEditorial.get()
                libro['clasificacion'] = cbClasificacion.get()
                deshabilitar_componentes()
                cancelar_operacion()
                return
        messagebox.showinfo(message="Libro no encontrado", title="Info")
    except ValueError as e:
        messagebox.showerror(message=str(e), title="Error")

def eliminar_libro():
    try:
        if not txId.get().strip():
            raise ValueError("ID vacío")
        id_eliminar = int(txId.get())
        for libro in libros:
            if libro['id'] == id_eliminar:
                libros.remove(libro)
                deshabilitar_componentes()
                cancelar_operacion()
                return
        messagebox.showinfo(message="Libro no encontrado", title="Info")
    except ValueError as e:
        messagebox.showerror(message=str(e), title="Error")

root = tk.Tk()
root.config(width=500, height=400)
root.title("Biblioteca")

tk.Label(root, text="ID:").place(x=10, y=10)
txId = tk.Entry(root)
txId.place(x=10, y=30)

tk.Label(root, text="Titulo Libro").place(x=10, y=50)
txTitulo = tk.Entry(root, width=30)
txTitulo.place(x=10, y=70)

tk.Label(root, text="Autor:").place(x=10, y=90)
txAutor = tk.Entry(root, width=30)
txAutor.place(x=10, y=110)

tk.Label(root, text="Editorial:").place(x=10, y=130)
txEditorial = tk.Entry(root, width=30)
txEditorial.place(x=10, y=150)

tk.Label(root, text="Clasificacion:").place(x=10, y=185)
cbClasificacion = ttk.Combobox(root, state="normal", values=["Novela", "Cuento", "Finanzas", "Economia"])
cbClasificacion.place(x=10, y=205)

btnNuevo = tk.Button(root, text="Nuevo", command=nuevo_libro)
btnNuevo.place(x=10, y=250)

btnSalvar = tk.Button(root, text="Guardar", command=salvar_libro, state="disabled")
btnSalvar.place(x=80, y=250)

btnCancelar = tk.Button(root, text="Cancelar", command=cancelar_operacion, state="disabled")
btnCancelar.place(x=150, y=250)

btnBuscar = tk.Button(root, text="Buscar", command=buscar_libro)
btnBuscar.place(x=220, y=250)

btnEditar = tk.Button(root, text="Editar", command=editar_libro, state="disabled")
btnEditar.place(x=290, y=250)

btnEliminar = tk.Button(root, text="Eliminar", command=eliminar_libro, state="disabled")
btnEliminar.place(x=360, y=250)

root.mainloop()