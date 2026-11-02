import sqlite3
from config import DB_PATH

def inserir_produto_db(codigo_sku, nome, preco_unitario, categoria_id, stock_minimo=0, stock_atual=0):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO produto (codigo_sku, nome, preco_unitario, categoria_id, stock_minimo, stock_atual)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (codigo_sku, nome, preco_unitario, categoria_id, stock_minimo, stock_atual))
    conn.commit()
    conn.close()

def listar_produtos_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, codigo_sku, nome, preco_unitario, stock_atual FROM produto")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def categoria_existe(categoria_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM categoria WHERE id = ?", (categoria_id,))
    existe = cursor.fetchone() is not None
    conn.close()
    return existe