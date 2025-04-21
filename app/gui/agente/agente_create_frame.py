import tkinter as tk
from app.models.personagem import Personagem
from tkinter import ttk, Text, Button
from app.database.connection import get_connection, insert_personagem

class AgenteCreateFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        label = ttk.Label(self, text="Criação de personagem")
        label.pack(pady=10)

        # Dicionário para armazenar os campos de texto com seus respectivos nomes
        self.text_fields = {}

        # Campos de entrada com nomes específicos
        fields = ["Nome", "Agilidade", "Força", "Intelecto", "Presença", "Vigor"]

        for field in fields:
            field_label = ttk.Label(self, text=field)
            field_label.pack(pady=5)  # Rótulo para o campo

            text_box = Text(self, height=1, width=30)
            text_box.pack(pady=5)  # Campo de texto

            self.text_fields[field] = text_box  # Adicionar ao dicionário

        # Botão Commit
        buttonCommit = Button(self, text="Salvar e Fechar", command=self.commit_and_close)
        buttonCommit.pack(pady=10)

    def commit(self):
        # Coletar os valores de cada campo pelo nome
        field_values = {field: textbox.get("1.0", "end-1c") for field, textbox in self.text_fields.items()}

        personagem = Personagem(field_values["Nome"], field_values["Agilidade"], field_values["Força"], field_values["Intelecto"], field_values["Presença"], field_values["Vigor"])

        conn = get_connection()
        insert_personagem(conn, personagem)

    def commit_and_close(self):
        self.commit()
        self.on_close()