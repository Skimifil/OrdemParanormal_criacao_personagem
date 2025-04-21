import sqlite3


def get_connection():
    try:
        conn = sqlite3.connect('database/ordem_paranormal.db')
        return conn

    except sqlite3.Error as e:
        raise RuntimeError(f"Erro ao conectar ao banco de dados: {e}")


def create_tables(conn):
    try:
        tabela_create_sql = ['''
              CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                descricao TEXT
            );''',
            '''
            CREATE TABLE IF NOT EXISTS trilhas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                descricao TEXT
            );''',
            '''
            CREATE TABLE IF NOT EXISTS origens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                descricao TEXT
            );''',
            '''
            CREATE TABLE IF NOT EXISTS equipamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                tipo TEXT,
                descricao TEXT
            );''',
            '''
            CREATE TABLE IF NOT EXISTS inventario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quantidade INTEGER,
                item_id INTEGER,
                FOREIGN KEY (item_id) REFERENCES item (id)
            );''',
            '''
            CREATE TABLE IF NOT EXISTS rituais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                circulo TEXT,
                descricao TEXT
            );''',
            '''
            CREATE TABLE IF NOT EXISTS domo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rituais_id INTEGER,
                FOREIGN KEY (rituais_id) REFERENCES rituais (id)
            );''',
            '''
            CREATE TABLE IF NOT EXISTS personagem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                agilidade INTEGER,
                forca INTEGER,
                intelecto INTEGER,
                presenca INTEGER,
                vigor INTEGER,
                classe_id INTEGER,
                trilha_id INTEGER,
                origem_id INTEGER,
                domo_id INTEGER,
                inventario_id INTEGER,
                FOREIGN KEY (classe_id) REFERENCES classes (id),
                FOREIGN KEY (trilha_id) REFERENCES trilhas (id),
                FOREIGN KEY (origem_id) REFERENCES origens (id),
                FOREIGN KEY (domo_id) REFERENCES domo (id),
                FOREIGN KEY (inventario_id) REFERENCES inventario (id)
            );
              ''']

        cursor = conn.cursor()

        for sql in tabela_create_sql:
            cursor.execute(sql)

        conn.commit()
        return f"Tabelas criadas com sucesso!"

    except sqlite3.Error as e:
        return f"Erro ao criar as tabelas: {e}"


def insert_personagem(conn, personagem):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO personagem (nome, agilidade, forca, intelecto, presenca, vigor, classe_id, trilha_id, origem_id, domo_id, inventario_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (personagem.nome, personagem.agilidade, personagem.forca, personagem.intelecto, personagem.presenca, personagem.vigor, personagem.classe_id, personagem.trilha_id, personagem.origem_id, personagem.domo_id, personagem.inventario_id))
        conn.commit()
        return f"Personagem {personagem.nome} inserido com sucesso!"

    except sqlite3.Error as e:
        return f"Erro ao inserir personagem: {e}"


def get_all_personagens(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(''' SELECT nome, agilidade, forca, intelecto, presenca, vigor FROM personagem ''')
        personagens = cursor.fetchall()
        return personagens

    except sqlite3.Error as e:
        return f"Erro ao buscar personagens: {e}"

def get_personagem_por_nome(conn, nome):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM personagem WHERE nome = ?
        ''', (nome,))
        personagem = cursor.fetchone()
        return personagem

    except sqlite3.Error as e:
        return f"Erro ao buscar personagem: {e}"

def close_connection(conn):
    conn.close()
    return f"Conexão fechada com sucesso!"
