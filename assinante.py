import random
import hashlib

class assinante:
    def __init__(self, nome: str, plano: str, senha_plana: str):
        self.id_conta = random.randint(1000, 9999)
        self.nome = nome
        self.plano = plano
        self.senha_hash = self._gerar_hash(senha_plana)

    def exibir_dados(self) -> str:
        return (f"ID {self.id_conta}, nome {self.nome}, plano {self.plano}, senha {self.senha_hash}")
        
        
    def _gerar_hash(self, senha_plana) -> str:
        return hashlib.sha256(senha_plana.encode()).hexdigest()





