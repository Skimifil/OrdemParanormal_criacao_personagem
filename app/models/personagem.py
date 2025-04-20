

class Personagem:
    def __init__(self, nome, agilidade, forca, intelecto, presenca, vigor, classe_id=None, trilha_id=None, origem_id=None, domo_id=None, inventario_id=None):
        self.nome = nome
        self.agilidade = agilidade
        self.forca = forca
        self.intelecto = intelecto
        self.presenca = presenca
        self.vigor = vigor

        self.classe_id = classe_id
        self.trilha_id = trilha_id
        self.origem_id = origem_id
        self.domo_id = domo_id
        self.inventario_id = inventario_id


    def exibir_ficha(self):
        print(f"\nSeu personagem {self.nome} tem os seguintes atributos:\nAgilidade: {self.agilidade}\nForça: {self.forca}\nIntelecto: {self.intelecto}\nPresença: {self.presenca}\nVigor: {self.vigor}\nClasse ID: {self.classe_id}\nTrilha ID: {self.trilha_id}\nOrigem ID: {self.origem_id}\nDomo ID: {self.domo_id}\nInventario ID: {self.inventario_id}")


    def exportar_json(self):
        pass