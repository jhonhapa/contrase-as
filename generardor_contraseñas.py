import tkinter as tk
from tkinter import ttk, messagebox
import string
import secrets # prueba camilo de actualizacion


def generar_contrasena():
    """Genera una contraseña segura según las opciones seleccionadas."""
    try:
        longitud = int(entry_longitud.get())

        if longitud <= 0:
            messagebox.showerror("Error", "La longitud debe ser mayor que cero.")
            return

        caracteres = ""

        if var_mayusculas.get():
            caracteres += string.ascii_uppercase
        if var_minusculas.get():
            caracteres += string.ascii_lowercase
        if var_numeros.get():
            caracteres += string.digits
        if var_simbolos.get():
            caracteres += string.punctuation

        if not caracteres:
            messagebox.showwarning(
                "Advertencia",
                "Seleccione al menos un tipo de carácter."
            )
            return

        # Garantizar al menos un carácter de cada tipo seleccionado
        contrasena = []

        if var_mayusculas.get():
            contrasena.append(secrets.choice(string.ascii_uppercase))
        if var_minusculas.get():
            contrasena.append(secrets.choice(string.ascii_lowercase))
        if var_numeros.get():
            contrasena.append(secrets.choice(string.digits))
        if var_simbolos.get():
            contrasena.append(secrets.choice(string.punctuation))

        # Completar la longitud restante
        while len(contrasena) < longitud:
            contrasena.append(secrets.choice(caracteres))

        # Mezclar los caracteres para mayor seguridad
        secrets.SystemRandom().shuffle(contrasena)

        resultado = "".join(contrasena)
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)

    except ValueError:
        messagebox.showerror("Error", "Ingrese una longitud válida.")


def copiar_portapapeles():
    """Copia la contraseña generada al portapapeles."""
    contrasena = entry_resultado.get()
    if contrasena:
        ventana.clipboard_clear()
        ventana.clipboard_append(contrasena)
        ventana.update()
        messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles.")
    else:
        messagebox.showwarning("Advertencia", "No hay contraseña para copiar.")


def limpiar():
    """Limpia los campos de la interfaz."""
    entry_resultado.delete(0, tk.END)
    entry_longitud.delete(0, tk.END)
    entry_longitud.insert(0, "12")
    var_mayusculas.set(True)
    var_minusculas.set(True)
    var_numeros.set(True)
    var_simbolos.set(True)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("420x420")
ventana.resizable(False, False)

# Título
titulo = ttk.Label(
    ventana,
    text="Generador de Contraseñas",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

# Marco principal
frame = ttk.Frame(ventana, padding=15)
frame.pack(fill="both", expand=True)

# Longitud
ttk.Label(frame, text="Longitud de la contraseña:").grid(
    row=0, column=0, sticky="w", pady=5
)
entry_longitud = ttk.Entry(frame, width=10)
entry_longitud.grid(row=0, column=1, pady=5)
entry_longitud.insert(0, "12")

# Opciones
ttk.Label(frame, text="Tipos de caracteres:").grid(
    row=1, column=0, sticky="w", pady=5
)

var_mayusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

ttk.Checkbutton(frame, text="Mayúsculas (A-Z)",
                variable=var_mayusculas).grid(row=2, column=0, sticky="w")
ttk.Checkbutton(frame, text="Minúsculas (a-z)",
                variable=var_minusculas).grid(row=3, column=0, sticky="w")
ttk.Checkbutton(frame, text="Números (0-9)",
                variable=var_numeros).grid(row=4, column=0, sticky="w")
ttk.Checkbutton(frame, text="Símbolos (!@#$)",
                variable=var_simbolos).grid(row=5, column=0, sticky="w")

# Resultado
ttk.Label(frame, text="Contraseña generada:").grid(
    row=6, column=0, sticky="w", pady=10
)
entry_resultado = ttk.Entry(frame, width=30, font=("Arial", 12))
entry_resultado.grid(row=7, column=0, columnspan=2, pady=5)

# Botones
ttk.Button(frame, text="Generar",
           command=generar_contrasena).grid(
    row=8, column=0, pady=10, sticky="ew"
)

ttk.Button(frame, text="Copiar",
           command=copiar_portapapeles).grid(
    row=8, column=1, pady=10, sticky="ew"
)

ttk.Button(frame, text="Limpiar",
           command=limpiar).grid(
    row=9, column=0, columnspan=2, pady=5, sticky="ew"
)

# Ejecutar la aplicación
ventana.mainloop()