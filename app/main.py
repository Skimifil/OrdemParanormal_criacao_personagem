from app.database.connection import get_connection, create_tables, insert_personagem, close_connection
from services.personagem_service import criar_personagem_interativo
from app.gui.main_window import MainWindow



if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
