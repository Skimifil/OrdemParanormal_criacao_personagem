import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu de criação de personagens")
        self.geometry("900x600")

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(expand=1, fill="both")

        # Importar as abas (depois você cria elas)
        from .agente_frame import AgenteFrame
        from .classe_frame import ClasseFrame

        self.tabs.add(AgenteFrame(self.tabs), text="Agentes")
        self.tabs.add(ClasseFrame(self.tabs), text="Classes")
        # Adicionar depois: Origens, Equipamentos, Rituais
