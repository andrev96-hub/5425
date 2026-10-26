import sqlite3
from config import DB_PATH

def obter_conexao():
    conexao = sqlite3.connect(DB_PATH)
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao

def inicializar_base_dados():
    conexao = obter_conexao()
    with open("schema.sql", "r", encoding="utf-8") as f:
        conexao.executescript(f.read())
    conexao.commit()
    conexao.close()
    print("Base de dados criada.")

if __name__ == "__main__":
    inicializar_base_dados()