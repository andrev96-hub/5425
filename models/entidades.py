class Utilizador:
    def __init__(self, id, nome, email, password_hash, perfil):
        self.id = id
        self.nome = nome
        self.email = email
        self.password_hash = password_hash
        self.perfil = perfil

class Categoria:
    def __init__(self, id, nome, descricao=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao

class Produto:
    def __init__(self, id, codigo_sku, nome, categoria_id, stock_atual=0, stock_minimo=0, preco_unitario=0.0):
        self.id = id
        self.codigo_sku = codigo_sku
        self.nome = nome
        self.categoria_id = categoria_id
        self.stock_atual = stock_atual
        self.stock_minimo = stock_minimo
        self.preco_unitario = preco_unitario

class Movimento:
    def __init__(self, id, produto_id, utilizador_id, tipo, quantidade, data_hora, motivo_observacoes=None):
        self.id = id
        self.produto_id = produto_id
        self.utilizador_id = utilizador_id
        self.tipo = tipo  # 'ENTRADA' ou 'SAIDA'
        self.quantidade = quantidade
        self.data_hora = data_hora
        self.motivo_observacoes = motivo_observacoes