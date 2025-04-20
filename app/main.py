from app.database.connection import get_connection, create_tables, insert_personagem, close_connection
from services.personagem_service import criar_personagem_interativo
from app.gui.main_window import MainWindow



if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
    # conn = get_connection()
    # create_tables(conn)
    #
    # personagem = criar_personagem_interativo()
    # personagem.exibir_ficha()
    #
    # resultado = insert_personagem(conn, personagem)
    # print(resultado)
    #
    # close_connection(conn)
