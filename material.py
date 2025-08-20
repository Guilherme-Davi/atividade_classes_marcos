class Material:
    def __init__(self, nome, largura, altura, comprimento, cor):
        self.nome = nome
        self.cor = cor
        self.largura = largura
        self.altura = altura
        self.comprimento = comprimento


    def calcular_area_volume(self):
        self.area = self.largura * self.altura
        self.volume = self.largura * self.altura * self.comprimento


    def exibir_informacoes(self):
        print("    ")
        print(f"O nome do material é: {self.nome}")
        print(f"A cor do material é: {self.cor}")
        print(f"A largura do material é: {self.largura}")
        print(f"A altura do material é: {self.altura}")
        print(f"O comprimento do material é: {self.comprimento}")
        print(f"A área do material é: {self.area}cm²")
        print(f"O volume do material é: {self.volume}cm³")
        print("    ")


    def mudar_cor(self):
        nova_cor = input("Digite a nova cor do material: ")
        self.cor = nova_cor
        print(f"A cor do material foi alterada para: {self.cor}")


    def criar_material():
        nome = input("Digite o nome do material: ")
        cor = input("Digite a cor do material: ")
        largura = float(input("Digite a largura do material (em cm): "))
        altura = float(input("Digite a altura do material (em cm): "))
        comprimento = float(input("Digite o comprimento do material (em cm): "))
        return Material(nome, largura, altura, comprimento, cor)


    def editar_obj(self, busca):
        if self.nome == busca:
            print("Material encontrado!")
            self.exibir_informacoes()
            self.mudar_cor()
            self.exibir_informacoes()