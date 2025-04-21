import tkinter as tk
from tkinter import ttk

class EquipamentoFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        label = ttk.Label(self, text="Lista de equipamentos cadastrados")
        label.pack(pady=20)
