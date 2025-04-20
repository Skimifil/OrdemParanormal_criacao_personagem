import tkinter as tk
from tkinter import ttk

class AgenteFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        label = ttk.Label(self, text="Lista de agentes cadastrados")
        label.pack(pady=20)

        # Aqui virá: listagem de personagens, botão criar novo, visualizar ficha, deletar...
