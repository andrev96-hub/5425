<<<<<<< HEAD
# Sistema de Gestão de Stock de Armazém (StockFlow)

Aplicação de consola em Python, com base de dados SQLite, para o controlo de inventário de um armazém.
**Estado:** Em desenvolvimento.

## Resumo
Projeto da formação de Programação e Algoritmia que aplica a programação orientada a objetos em Python. Permite gerir produtos, registar entradas e saídas de stock e receber avisos quando um produto está a ficar sem stock.

## Highlights
* Registo de entradas e saídas de stock, com o utilizador, a data e hora e o motivo.
* Validação dos dados: o stock nunca fica negativo.
* Aviso de stock mínimo para prevenir ruturas.
* Dois perfis de utilizador: Operador e Gestor.
* Configurações sensíveis fora do código (ficheiro `.env`) e palavras-passe guardadas com hash.

## Pré-visualização da Aplicação
*(Por acrescentar: captura de ecrã da consola)*

## Overview
Em armazéns pequenos, o controlo de stock sem validação de movimentos fica sujeito a erros de contagem, a quantidades negativas e a ruturas que só se descobrem quando o produto já falta. Esta aplicação centraliza esse controlo num único programa.

Cada entrada ou saída é registada no momento e atualiza o stock do produto na mesma transação da base de dados, por isso o movimento e o stock nunca ficam desencontrados. Uma saída que deixasse o stock negativo é recusada, e quando um produto fica igual ou abaixo do stock mínimo a aplicação avisa o utilizador.

### Utilizadores
* **Operador:** Trabalha com as entradas e saídas de stock.
* **Gestor:** Supervisiona o stock e gere o catálogo.

**Fora do âmbito:** Contabilidade (não processa faturas), vendas (não há vendas diretas ao cliente final) e recursos humanos (não controla horários nem salários).

## Arquitetura
O sistema está organizado em três camadas:

| Camada | Função |
| :--- | :--- |
| **Apresentação** | Menus de consola para o Operador e para o Gestor |
| **Lógica** | Validação de stock e regras de movimentos, em Python |
| **Dados** | Base de dados SQLite (`utilizadores`, `categorias`, `produtos` e `movimentos`) |

**Modelo de dados:** `Utilizador`, `Categoria`, `Produto` e `Movimento`. Uma `Categoria` tem vários `Produtos`, um `Produto` tem vários `Movimentos` e um `Utilizador` regista vários `Movimentos`. O esquema completo está em `db/schema.sql`.

## Tecnologias
| Área | Tecnologia |
| :--- | :--- |
| **Backend** | Python 3 |
| **Frontend** | Menus de consola |
| **Dados e infraestrutura** | SQLite (módulo `sqlite3`), `python-dotenv`, Git e GitHub |

## Estrutura do Projeto
(em desenvolvimento)
Projeto Final/
├── database/
│   └── database.py
├── docs/
├── models/
│   └── entidades.py
├── repositorio/
├── services/
│   └── stock.py
├── UI/
│   └── menus.py
├── config.py
├── README.md
└── schema.sql
=======
# 5425
Projeto final
>>>>>>> cf2507cbcd7f5c51667bf0a8aed9f5622bc18d4a
