from database.queries import inserir_produto_db, listar_produtos_db, categoria_existe

def registar_produto(codigo_sku, nome, preco_unitario, categoria_id, stock_minimo=0):
   
    if not nome or not nome.strip():
        raise ValueError("O nome do produto não pode estar vazio.")
    
    if not categoria_existe(categoria_id):
        raise ValueError(f"A categoria com ID {categoria_id} não existe.")
        
    if stock_minimo < 0:
        raise ValueError("O stock mínimo não pode ser negativo.")
    
    
    inserir_produto_db(codigo_sku, nome, preco_unitario, categoria_id, stock_minimo, stock_atual=0)

def obter_todos_produtos():
    return listar_produtos_db()

