
class Atendente:
    _id_increment = 0
    def __init__(self, nome, email, login, senha):  
        Atendente._id_increment += 1
        self._id = Atendente._id_increment
        self._nome = nome
        self._email = email
        self._login = login
        self._senha = senha
        
    def __str__(self):
        return "ID {0} Nome {1} Email {2} login {3} senha {4}". \ 
        format(self._id, self._nome, self._email, self._login, self._senha)
        