python
import sqlite3
import hashlib

def fazer_login(usuario, senha):
    try:
        conexao = sqlite3.connect('banco_de_dados.db')
        cursor = conexao.cursor()

        # 1) Parametrização: os valores nunca entram na query como texto
        query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
        cursor.execute(query, (usuario, senha))
        resultado = cursor.fetchone()
        conexao.close()

        # 2) Mensagem genérica: não informa se o usuário ou a senha estão errados
        if resultado:
            return "Acesso Permitido"
        else:
            return "Acesso Negado."

    except sqlite3.Error as e:
        # 3) Não expõe detalhes internos do banco para o atacante
        return "Erro interno. Tente novamente mais tarde."