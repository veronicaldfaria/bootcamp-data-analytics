import sqlite3

ex = sqlite3.connect('exercicios.db')
cursor = ex.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id
# (inteiro), nome (texto), idade (inteiro) e curso (texto).

# cursor.execute('CREATE TABLE alunos (id, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no
# exercício anterior.

# cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "João Silva", 22, "Engenharia")')
# cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Maria Oliveira", 19, "Medicina")')
# cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Carlos Santos", 25, "Engenharia")')
# cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Ana Costa", 30, "Arquitetura")')
# cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Lucas Pereira", 18, "Engenharia")')

# 3. Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".

# cursor.execute('SELECT * FROM alunos')

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

# cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

# cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome;')

# d) Contar o número total de alunos na tabela

# cursor.execute('SELECT COUNT(*) FROM alunos')

# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.

# cursor.execute('UPDATE alunos SET idade = 23 WHERE id = 1')

# b) Remova um aluno pelo seu ID.

# cursor.execute('DELETE FROM alunos WHERE id = 2')

# 5. Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada "clientes" com os campos: id (chave
# primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
# registros de clientes na tabela.

# cursor.execute('CREATE TABLE clientes (id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "João Silva", 35, 1200.50)')
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Maria Oliveira", 28, 800.00)')
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Carlos Santos", 40, 1500.75)')
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Ana Costa", 33, 2000.00)')
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Lucas Pereira", 45, 950.30)')

# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

# cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

# b) Calcule o saldo médio dos clientes.

# cursor.execute('SELECT AVG(saldo) FROM clientes')

# c) Encontre o cliente com o saldo máximo.

# cursor.execute('SELECT nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')

# d) Conte quantos clientes têm saldo acima de 1000.

# cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')

# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.

# cursor.execute('UPDATE clientes SET saldo = 1800.00 WHERE id = 2')

# b) Remova um cliente pelo seu ID.

# cursor.execute('DELETE FROM clientes WHERE id = 3')

# 8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id
# (chave primária), cliente_id (chave estrangeira referenciando o id
# da tabela "clientes"), produto (texto) e valor (real). Insira algumas
# compras associadas a clientes existentes na tabela "clientes".
# Escreva uma consulta para exibir o nome do cliente, o produto e o
# valor de cada compra.

# cursor.execute('CREATE TABLE compras (id INT, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 1, "Smartphone", 1200.00)')
# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 4, "Notebook", 2000.00)')
# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 1, "Fone de ouvido", 150.00)')
# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (4, 2, "Tablet", 800.00)')

# cursor.execute('SELECT c.nome, cp.produto, cp.valor FROM compras cp JOIN clientes c ON cp.cliente_id = c.id')

ex.commit()
ex.close