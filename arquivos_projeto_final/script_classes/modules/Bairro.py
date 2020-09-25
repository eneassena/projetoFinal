class Bairro:
    _idBairro

    def __init__(self, rua, cep, complemento, valor_entrega):
        Bairro._idBairro += 1
        self._id_bairro = Bairro._idBairro
        self._rua = rua
        self._cep = cep
        self._complemento = complemento
        self._valor_entrega = valor_entrega
        self._campos_bairros


    def __str__(self):
        return "Rua {} | Cep {} | Complemento {} | Valor De Entrega {}".\
        format(self._rua, self._cep, self._complemento, self._valor_entrega)
    
    def add(self):
        self._campos_bairros.append(self)
    
    def view(self):
        texto = ""
        