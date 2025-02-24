import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

# cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
# cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
# cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

# cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
# cursor.execute('DROP TABLE produtos')

# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(1, "Isadora", "Brasil", "isa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(2, "Maria", "Paraguai", "maria@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(3, "Luis", "EUA", "luis@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(4, "Lorena", "Bolivia", "lolo@gmail.com", 123456)')

# cursor.execute('DELETE FROM usuario where id=1')

# cursor.execute('UPDATE usuario SET endereco ="Argentina" WHERE nome="Luis"')

# dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')

# dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 2')

# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')

# cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
# cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(1, "Isadora", "Brasil", "isa@gmail.com")')
# cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(2, "Maria", "Paraguai", "maria@gmail.com")')
# cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(3, "Luis", "EUA", "luis@gmail.com")')
# cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(4, "Lorena", "Bolivia", "lolo@gmail.com")')

# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

# dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id')

dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')

for usuario in dados:
    print(usuario)

conexao.commit()
conexao.close