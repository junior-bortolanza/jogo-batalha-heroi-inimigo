# Personagem: classe mae
# Heroi: controlado pelo usuario
# Inimigo: adversario do usuario

class Personagem:
    def __init__(self,nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_vida()}"   

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida <=0:
            self.__vida = 0
    
    def atacar(self, alvo):
        dano = self.__nivel * 2
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"


class Jogo:
    """Classe orquestradora do jogo"""

    def __init__(self) -> None:
        self.heroi = heroi1 = Heroi(nome="Heroí",vida=100, nivel=5, habilidade="Mega força")
        self.inimigo = inimigo = Inimigo(nome="Morcego", vida=50, nivel=5, tipo="Voador")

    def iniciar_batalha(self):
        """Fazer a gestão da batalha em turnos"""
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens: ")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque ESpecial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            else:
                print("Escolha inválida escolha novamente")


        if self.heroi.get_vida() > 0:
            print("\nParabéns você venceu a batalha")
        else:
            print("\nVocê foi derrotado!")


# Cruar instância do jogo e iniciar batalha

jogo = Jogo()
jogo.iniciar_batalha()

