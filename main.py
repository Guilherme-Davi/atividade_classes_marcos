from material import Material

lista = []

while True:
    print("    ")
    deseja = input("Deseja adicionar um material?(-1 para parar): ")
    if deseja == "-1":
        break
    material = Material.criar_material()

    material.calcular_area_volume()
    material.exibir_informacoes()
    lista.append(material)
    print("Material adicionado: ", material.nome)
    print("    ")
for i in lista:
    print(i.nome)


while True:
    print("Digite 's' se dejesa editar a cor de algum material ou 'n' para não editar: ")
    resposta = input().strip().lower()
    if resposta == "s":
        nome_busca = input("Digite o nome do material que deseja editar: ")
        for material in lista:
            if material.nome == nome_busca:
                material.editar_obj(nome_busca)
                for i in lista:
                    print(i.nome)
            else:
                print("Material não encontrado.")
                break
    elif resposta == "n":
        print("Nenhum material será editado.")
        break


while True:
    print("Digite 's' se dejesa remover algum material ou 'n' para não remover: ")
    resposta = input().strip().lower()
    if resposta == "s":
        nome_busca = input("Digite o nome do material que deseja remover: ")
        for material in lista:
            if material.nome == nome_busca:
                lista.remove(material)
                for i in lista:
                    print(i.nome)
            else:
                print("Material não encontrado.")
                break
    elif resposta == "n":
        print("Nenhum material será removido.")
        break


for i in lista:
    Material.exibir_informacoes(i)