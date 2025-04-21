import tkinter as tk
from tkinter import ttk
from app.gui.agente_crate_window import AgenteCreateWindow
from app.database.connection import get_connection, get_all_personagens

class AgenteFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        label = ttk.Label(self, text="Lista de agentes cadastrados")
        label.pack(pady=20)

        conn = get_connection()
        nomes = get_all_personagens(conn)
        print(nomes)

        # Certifique-se de que nomes é uma lista/iterável
        if not isinstance(nomes, list):
            raise ValueError("O retorno de get_all_personagens deve ser uma lista.")

        # Processa e exibe os agentes
        self.processar_agentes(nomes)

        #Botão de criar agente
        button = ttk.Button(self, text="Criar personagem", command=self.button_click)
        button.pack(pady=20)


    def processar_agentes(self, nomes):
        """
        Processa a lista de agentes e organiza a exibição lado a lado.
        """

        # Cria o frame para organizar os widgets horizontalmente
        row_frame = ttk.Frame(self)
        row_frame.pack(fill="x", pady=10)

        # Número máximo de agentes por linha (opcional)
        items_por_linha = 5
        for i, nome in enumerate(nomes):
            if isinstance(nome, tuple) and len(nome) >= 6:  # Verifica se `nome` é uma tupla com todos os campos
                formatado = self.formatar_agente_dados(nome)

                # Caso o índice seja múltiplo de `items_por_linha`, cria uma nova linha
                if i % items_por_linha == 0 and i != 0:
                    row_frame = ttk.Frame(self)
                    row_frame.pack(fill="x", pady=10)

                # Adiciona o novo agente ao frame
                self.criar_agente_label(row_frame, formatado)

    def criar_agente_label(self, frame, agente_info):
        """
        Cria o widget Label para exibir os dados de um agente.
        """
        label_text = "\n".join([f"{chave.capitalize()}: {valor}" for chave, valor in agente_info.items()])

        # Cria o widget do agente com bordas visuais
        agente_label = ttk.Label(frame, text=label_text, relief="solid", borderwidth=1, padding=10)
        agente_label.pack(side="left", padx=10, pady=1)  # Organiza-o lado a lado

    def formatar_agente_dados(self, nome):
        """
        Formata os dados de um agente retornando um dicionário.
        """
        return {
            "nome": nome[0],
            "AGI": nome[1],
            "FOR": nome[2],
            "INT": nome[3],
            "PRE": nome[4],
            "VIG": nome[5]
        }

    def button_click(self):
        AgenteCreateWindow()
