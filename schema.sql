CREATE TABLE utilizador (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    perfil TEXT NOT NULL
);

CREATE TABLE categoria (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    descricao TEXT
);

CREATE TABLE produto (
    id INTEGER PRIMARY KEY,
    codigo_sku TEXT NOT NULL UNIQUE,
    nome TEXT NOT NULL,
    categoria_id INTEGER NOT NULL,
    stock_atual INTEGER NOT NULL DEFAULT 0,
    stock_minimo INTEGER NOT NULL DEFAULT 0,
    preco_unitario REAL NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categoria (id)
);

CREATE TABLE movimento (
    id INTEGER PRIMARY KEY,
    produto_id INTEGER NOT NULL,
    utilizador_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    data_hora TEXT NOT NULL,
    motivo_observacoes TEXT,
    FOREIGN KEY (produto_id) REFERENCES produto (id),
    FOREIGN KEY (utilizador_id) REFERENCES utilizador (id)
);