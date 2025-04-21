import tkinter as tk
from tkinter import ttk

class AgenteCreateWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu de criação de personagens")
        self.geometry("450x600")

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(expand=1, fill="both")

        # Importar as abas (depois você cria elas)
        from .agente.agente_create_frame import AgenteCreateFrame

        self.tabs.add(AgenteCreateFrame(self.tabs), text="Criação de personagem")