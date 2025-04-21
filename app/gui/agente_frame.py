import tkinter as tk
from tkinter import ttk
from app.database.connection import get_connection, get_personagem_por_nome, get_all_personagens

class AgenteFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        label = ttk.Label(self, text="Lista de agentes cadastrados")
        label.pack(pady=20)

        conn = get_connection()
        nomes = get_all_personagens(conn)
        agente = ttk.Label(self, text=f"{nomes}")
        agente.pack(pady=20)
