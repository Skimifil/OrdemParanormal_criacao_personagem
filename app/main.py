from app.database.connection import get_connection, create_tables, insert_personagem, close_connection
from services.personagem_service import criar_personagem_interativo
from app.gui.main_window import MainWindow



if __name__ == '__main__':
    # conn = get_connection()
    # p2_info = insert_personagem(conn, criar_personagem_interativo())
    # print(p2_info)
    # close_connection(conn)
    app = MainWindow()
    app.mainloop()
