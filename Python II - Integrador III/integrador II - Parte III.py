import tkinter as tk
from tkinter import messagebox, simpledialog, font
import sqlite3
import time

# ─────────────────────────────────────────────
# BASE DE DATOS
# ─────────────────────────────────────────────
def conectar_db():
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS venta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            fecha TEXT,
            ComboS INTEGER,
            ComboD INTEGER,
            ComboT INTEGER,
            Flurby INTEGER,
            total REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encargado TEXT,
            fecha TEXT,
            evento TEXT,
            caja REAL
        )
    """)
    conn.commit()
    return conn

# ─────────────────────────────────────────────
# CLASE PRINCIPAL
# ─────────────────────────────────────────────

class SistemaCaja:
    def __init__(self, ventana_principal):
        self.ventana = ventana_principal
        self.ventana.title("VIDEOJUEGOS IT")
        self.ventana.geometry("420x420")
        self.ventana.config(bg="#0d0d0d")
        self.ventana.resizable(False, False)
        self.ventana.protocol("WM_DELETE_WINDOW", self.salir)

        # Fuentes
        self.fuente_titulo = font.Font(family="Courier New", size=20, weight="bold")
        self.fuente_normal = font.Font(family="Courier New", size=10, weight="bold")
        self.fuente_chica  = font.Font(family="Courier New", size=9)
        self.conn = conectar_db()
        self.encargado  = ""
        self.total_caja = 0
        self.pedir_encargado()
        if not self.encargado:
            self.ventana.destroy()
            return
        self.registrar_entrada()
        self.armar_menu()

    # ─────────────────────────────────────────
    # PEDIR ENCARGADO
    # ─────────────────────────────────────────
    
    def pedir_encargado(self):
        while True:
            nombre = simpledialog.askstring(
                "INICIO DE SESIÓN",
                "Ingresá el nombre del encargad@:",
                parent=self.ventana
            )
            if nombre is None:
                # El usuario apretó Cancelar
                break
            elif nombre.strip() == "" or nombre.strip().isdigit():
                messagebox.showerror("ERROR", "El nombre debe contener letras.")
            else:
                self.encargado = nombre.strip().upper()
                break

    # ─────────────────────────────────────────
    # REGISTRAR ENTRADA / SALIDA
    # ─────────────────────────────────────────
   
    def registrar_entrada(self):
        fecha = time.ctime()
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO registro (encargado, fecha, evento, caja) VALUES (?, ?, ?, ?)",
            (self.encargado, fecha, "IN", 0)
        )
        self.conn.commit()

    def registrar_salida(self):
        fecha = time.ctime()
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO registro (encargado, fecha, evento, caja) VALUES (?, ?, ?, ?)",
            (self.encargado, fecha, "OUT", self.total_caja)
        )
        self.conn.commit()

    # ─────────────────────────────────────────
    # MENÚ PRINCIPAL
    # ─────────────────────────────────────────
  
    def armar_menu(self):
        for elemento in self.ventana.winfo_children():
            elemento.destroy()

        # Título
        tk.Label(
            self.ventana, text="VIDEOJUEGOS IT",
            font=self.fuente_titulo, bg="#0d0d0d", fg="#00FF41"
        ).pack(pady=(20, 5))

        # Nombre del encargado activo
        tk.Label(
            self.ventana, text=f"Encargad@: {self.encargado}",
            font=self.fuente_normal, bg="#0d0d0d", fg="#00FF41"
        ).pack(pady=(0, 5))

        # Total de caja del turno actual
        self.label_caja = tk.Label(
            self.ventana, text=f"Caja del turno: ${self.total_caja}",
            font=self.fuente_chica, bg="#0d0d0d", fg="#888888"
        )
        self.label_caja.pack(pady=(0, 20))

        estilo = {
            "font": self.fuente_normal,
            "bg": "#00FF41",
            "fg": "#0d0d0d",
            "activebackground": "#00cc33",
            "activeforeground": "#0d0d0d",
            "width": 28,
            "bd": 0,
            "pady": 8,
            "cursor": "hand2"
        }

        tk.Button(self.ventana, text="NUEVO PEDIDO",
                  command=self.nuevo_pedido, **estilo).pack(pady=6)
        tk.Button(self.ventana, text="HISTORIAL DE VENTAS",
                  command=self.ver_historial, **estilo).pack(pady=6)
        tk.Button(self.ventana, text="CAMBIO DE TURNO",
                  command=self.cambio_turno, **estilo).pack(pady=6)

      
        tk.Button(
            self.ventana, text="SALIR",
            command=self.salir,
            font=self.fuente_normal,
            bg="#FF3333", fg="#ffffff",
            activebackground="#cc0000",
            width=28, bd=0, pady=8, cursor="hand2"
        ).pack(pady=6)

    # ─────────────────────────────────────────
    # NUEVO PEDIDO
    # ─────────────────────────────────────────
    def nuevo_pedido(self):
        pantalla = tk.Toplevel(self.ventana)
        pantalla.title("NUEVO PEDIDO")
        pantalla.geometry("400x540")
        pantalla.config(bg="#0d0d0d")
        pantalla.resizable(False, False)

        estilo_label = {"bg": "#0d0d0d", "fg": "#00FF41", "font": self.fuente_normal}
        estilo_entry = {"bg": "#1a1a1a", "fg": "#ffffff", "font": self.fuente_normal,
                        "insertbackground": "white", "bd": 1, "relief": "solid"}

        tk.Label(pantalla, text="NUEVO PEDIDO", font=self.fuente_titulo,
                 bg="#0d0d0d", fg="#00FF41").pack(pady=(15, 10))

        tk.Label(pantalla, text="Nombre del cliente:", **estilo_label).pack()
        entrada_cliente = tk.Entry(pantalla, **estilo_entry, width=30)
        entrada_cliente.pack(pady=4)

        tk.Label(pantalla, text="─" * 40, bg="#0d0d0d", fg="#333333").pack()

        productos = [
            ("Juego básico   ($15)", "basico"),
            ("Juego premium  ($25)", "premium"),
            ("DLC            ($5) ", "dlc"),
            ("Pase temporada ($10)", "pase"),
        ]

        entradas = {}
        for nombre_prod, clave in productos:
            tk.Label(pantalla, text=nombre_prod, **estilo_label).pack()
            e = tk.Entry(pantalla, **estilo_entry, width=10)
            e.insert(0, "0")  # Arranca en 0 por defecto
            e.pack(pady=2)
            entradas[clave] = e

        label_total = tk.Label(pantalla, text="TOTAL: $0",
                               font=self.fuente_titulo, bg="#0d0d0d", fg="#FFD700")
        label_total.pack(pady=8)

        tk.Label(pantalla, text="Dinero entregado:", **estilo_label).pack()
        entrada_pago = tk.Entry(pantalla, **estilo_entry, width=15)
        entrada_pago.pack(pady=4)

        def calcular():
            try:
                basico  = int(entradas["basico"].get())
                premium = int(entradas["premium"].get())
                dlc     = int(entradas["dlc"].get())
                pase    = int(entradas["pase"].get())
                if any(v < 0 for v in [basico, premium, dlc, pase]):
                    messagebox.showerror("ERROR", "Las cantidades no pueden ser negativas.", parent=pantalla)
                    return None
                total = basico * 15 + premium * 25 + dlc * 5 + pase * 10
                label_total.config(text=f"TOTAL: ${total}")
                return total, basico, premium, dlc, pase
            except ValueError:
                messagebox.showerror("ERROR", "Ingresá solo números en cantidades.", parent=pantalla)
                return None

        def confirmar():
            datos = calcular()
            if not datos:
                return
            total, basico, premium, dlc, pase = datos
            cliente = entrada_cliente.get().strip()
            if cliente == "" or cliente.isdigit():
                messagebox.showerror("ERROR", "Nombre de cliente no válido.", parent=pantalla)
                return
            try:
                pago = float(entrada_pago.get())
            except ValueError:
                messagebox.showerror("ERROR", "El dinero entregado debe ser un número.", parent=pantalla)
                return
            if pago < total:
                messagebox.showerror("ERROR", f"El pago (${pago}) no alcanza (${total}).", parent=pantalla)
                return
            vuelto = pago - total

            # Guarda en la tabla venta
            fecha = time.ctime()
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO venta (cliente, fecha, ComboS, ComboD, ComboT, Flurby, total) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (cliente.upper(), fecha, basico, premium, dlc, pase, total)
            )
            self.conn.commit()

            # Suma al total de caja del turno y actualiza el label del menú
            self.total_caja += total
            self.label_caja.config(text=f"Caja del turno: ${self.total_caja}")

            messagebox.showinfo("PEDIDO CONFIRMADO", f"Venta guardada.\nVuelto: ${vuelto:.2f}", parent=pantalla)
            pantalla.destroy()

        tk.Button(pantalla, text="CALCULAR TOTAL", command=calcular,
                  font=self.fuente_normal, bg="#00FF41", fg="#0d0d0d",
                  activebackground="#00cc33", bd=0, pady=6, width=20, cursor="hand2").pack(pady=4)

        tk.Button(pantalla, text="CONFIRMAR PEDIDO", command=confirmar,
                  font=self.fuente_normal, bg="#FFD700", fg="#0d0d0d",
                  activebackground="#ccaa00", bd=0, pady=6, width=20, cursor="hand2").pack(pady=4)

    # ─────────────────────────────────────────
    # HISTORIAL DE VENTAS 
    # ─────────────────────────────────────────

    def ver_historial(self):
        pantalla = tk.Toplevel(self.ventana)
        pantalla.title("HISTORIAL DE VENTAS")
        pantalla.geometry("500x420")
        pantalla.config(bg="#0d0d0d")

        tk.Label(pantalla, text="HISTORIAL DE VENTAS",
                 font=self.fuente_titulo, bg="#0d0d0d", fg="#00FF41").pack(pady=10)

        # Consulta todas las ventas de la base de datos
        cursor = self.conn.cursor()
        cursor.execute("SELECT cliente, fecha, total FROM venta ORDER BY id DESC")
        ventas = cursor.fetchall()

        # Suma todos los totales de la tabla
        cursor.execute("SELECT SUM(total) FROM venta")
        resultado = cursor.fetchone()[0]
        total_dia = resultado if resultado else 0

        tk.Label(pantalla, text=f"Total vendido: ${total_dia:.2f}",
                 font=self.fuente_normal, bg="#0d0d0d", fg="#FFD700").pack(pady=(0, 10))

        frame = tk.Frame(pantalla, bg="#0d0d0d")
        frame.pack(fill="both", expand=True, padx=10, pady=5)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        texto = tk.Text(frame, bg="#1a1a1a", fg="#00FF41",
                        font=self.fuente_chica, yscrollcommand=scrollbar.set, bd=0)
        texto.pack(fill="both", expand=True)
        scrollbar.config(command=texto.yview)

        if not ventas:
            texto.insert("end", "No hay ventas registradas aún.")
        else:
            for venta in ventas:
                cliente, fecha, total = venta
                texto.insert("end", f"Cliente: {cliente}\nFecha: {fecha}\nTotal: ${total}\n{'─'*40}\n")

        # Solo lectura para que no se pueda editar
        texto.config(state="disabled")

    # ─────────────────────────────────────────
    # CAMBIO DE TURNO
    # ─────────────────────────────────────────
    
    def cambio_turno(self):
        self.registrar_salida()
        self.total_caja = 0
        messagebox.showinfo("TURNO CERRADO", "Datos de caja guardados.")
        self.encargado = ""
        self.pedir_encargado()
        if self.encargado:
            self.registrar_entrada()
            self.armar_menu()
        else:
            self.ventana.destroy()

    # ─────────────────────────────────────────
    # SALIR
    # ─────────────────────────────────────────

    def salir(self):
        self.registrar_salida()
        self.conn.close()
        self.ventana.destroy()


# ─────────────────────────────────────────────
# ARRANQUE DEL PROGRAMA
# ─────────────────────────────────────────────

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    aplicacion = SistemaCaja(ventana_principal)
    ventana_principal.mainloop()
