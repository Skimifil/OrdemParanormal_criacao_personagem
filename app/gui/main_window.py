import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Menu de Personagens")
        self.geometry("900x600")

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(expand=1, fill="both")

        # Importar as abas (depois você cria elas)
        from .agente_frame import AgenteFrame
        from .classe_frame import ClasseFrame
        from .origem_frame import OrigemFrame
        from .equipamento_frame import EquipamentoFrame
        from .ritual_frame import RitualFrame

        self.tabs.add(AgenteFrame(self.tabs), text="Agentes")
        self.tabs.add(ClasseFrame(self.tabs), text="Classes")
        self.tabs.add(OrigemFrame(self.tabs), text="Origens")
        self.tabs.add(EquipamentoFrame(self.tabs), text="Equipamento")
        self.tabs.add(RitualFrame(self.tabs), text="Rituais")
