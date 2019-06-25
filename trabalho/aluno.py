import hashlib
class Aluno:
    def __init__(self,**kwargs):
        if(kwargs.get("codigo")): self._codigo = kwargs["codigo"]
        if(kwargs.get("idade")): self._idade = kwargs["idade"]
        if(kwargs.get("login")): self._login = kwargs["login"] 
    def __str__(self):
        return "Código: {}, Login: {}, Idade: {}".format(self._codigo,self._login,self._idade)
    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self,codigo):
        self._codigo = codigo
    @property
    def login(self):
        return self._login
    @login.setter
    def login(self,login):
        self._login = login
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self,idade):
        self._idade = idade
    def persistido(self):
        return hasattr(self,"_codigo") and self.codigo!=None 