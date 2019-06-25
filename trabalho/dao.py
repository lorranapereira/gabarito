from aluno import Aluno
from psycopg2 import connect
from server import DAO
class AlunoDAO(DAO):
    def __init__(self):
        super().__init__()
    def excluir(self, aluno):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM aluno WHERE codigo = %s",str(aluno.codigo))
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no excluir -- exception seguindo para ser tratada")
            raise e
    def buscar(self, cod):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT * FROM aluno WHERE codigo = %s', [cod])
                row = cur.fetchone()
                aluno = Aluno(codigo=row[0],login=row[1],idade=row[2])
                cur.close()
                return aluno
        except BaseException as e:
            print ("Problema no buscar -- exception seguindo para ser tratada")
            raise e    
    def listar(self):
        vet = []
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT * FROM aluno')
                for row in cur.fetchall():
                    vet.append(Aluno(codigo=row[0],login=row[1],idade=row[2]))
                cur.close()
        except BaseException as e:
            print ("Problema no listar -- exception seguindo para ser tratada")
            raise e    
        return vet
    def inserir(self, aluno):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("insert into aluno(login,idade) values (%s, %s)",[aluno.login,aluno.idade])
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no inserir -- exception seguindo para ser tratada")
            raise e
    def alterar(self, aluno):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("UPDATE aluno SET login=%s, idade=%s WHERE codigo = %s", [aluno.login,aluno.idade,aluno.codigo])
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no alterar -- exception seguindo para ser tratada")
            raise e
    def salvar(self, pessoa):
        if pessoa.persistido():
            self.alterar(pessoa)
        else:
            self.inserir(pessoa)
