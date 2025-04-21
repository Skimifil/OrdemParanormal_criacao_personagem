from app.models.personagem import Personagem

def criar_personagem_interativo():
    print('Criar personagem interativo')

    nome = input('Digite o nome do personagem: ')
    agilidade = int(input('Digite a Agilidade do personagem: '))
    forca = int(input('Digite a Força do personagem: '))
    intelectp = int(input('Digite o Intelecto do personagem: '))
    vida = int(input('Digite a Vida do personagem: '))
    vigor = int(input('Digite o Vigor do personagem: '))

    personagem = Personagem(nome, agilidade, forca, intelectp, vida, vigor)
    print(type(personagem))

    return personagem