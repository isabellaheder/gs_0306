# RM 561300 - ISABELLA FRANCISO HEDER (Representante)
# RM 561050 - JOÃO VICTOR DALESSIO


qtd_desastres = int(input("quantidade de desastres? "))
n = 0
registro_desastre = []

# dados em string
tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []

# dados numericos (int)
total_afetados = [0]
criancas = [0]
adultos = [0]
idosos = [0]
mobilidade_reduzida = [0]
feridos = [0]

# criando loop para as perguntas serem feitas a qtd de vezes = a qtd de desastres
while n != qtd_desastres:
    tipo_desastre = input("qual o tipo do desastre? ")
    pais_desastre = input("qual o pais do desastre? ")
    cidade_desastre = input("qual a cidade do desastre? ")
    bairro_desastre = input("qual o bairro do desastre? ")
    rua_desastre = input("qual a rua do desastre? ")
# perguntas dos dados numericos
    qtd_pessoas_afetadas = int(input("Quantas pessoas foram afetadas? "))
    qtd_criancas = int(input("quantas eram crianças? "))
    qtd_adultos = int(input("quantos eram adultos? "))
    qtd_idosos = int(input("quantos eram idosos? "))
    qtd_mob_red = int(input("quantos tinham mobilidade reduzida? "))
    qtd_feridos = int(input("quantos ficaram feridos? "))

# garantindo que a soma das categorias seja = o total de afetados
    soma = qtd_feridos + qtd_idosos + qtd_criancas + qtd_adultos + qtd_mob_red
    if qtd_pessoas_afetadas == soma:
        # registro pra achar o local com maior desastre
        registro = {
            "tipo": tipo_desastre,
            "pais": pais_desastre,
            "cidade": cidade_desastre,
            "bairro": bairro_desastre,
            "rua": rua_desastre,
            "afetados": qtd_pessoas_afetadas
        }
        registro_desastre.append(registro)
        n += 1 # adicionando um na variavel para conseguir quebrar o loop quando for a hora
    else:
        print("A soma dos grupos não confere com o total de afetados. Tente novamente.")
        continue

    # colocando os dados tipo string nas listas
    tipos_desastres.append(tipo_desastre)
    paises.append(pais_desastre)
    cidades.append(cidade_desastre)
    bairros.append(bairro_desastre)
    ruas.append(rua_desastre)

    # colocando os dados (int) somando ao PRIMEIRO (index 0) item das listas
    total_afetados[0] += qtd_pessoas_afetadas
    criancas[0] += qtd_criancas
    adultos[0] += qtd_adultos
    idosos[0] += qtd_idosos
    mobilidade_reduzida[0] += qtd_mob_red
    feridos[0] += qtd_feridos

print()  # espaço
print("Total de desastres registrados:", n)
print("Total de pessoas afetadas:", total_afetados[0])
print()  # espaço
print("Resumo de pessoas afetadas por categoria:")
print("Total de crianças:", criancas[0])
print("Total de adultos:", adultos[0])
print("Total de idosos:", idosos[0])
print("Total com mobilidade reduzida:", mobilidade_reduzida[0])
print("Total de feridos:", feridos[0])

# criando conjunto p categorias
categorias = {"Crianças": criancas[0], "Adultos": adultos[0], "Idosos": idosos[0], "Mobilidade Reduzida": mobilidade_reduzida[0], "Feridos": feridos[0]}

# achando categoria mais afetada
categoria_mais_afetada = max(categorias, key=categorias.get)
print("A categoria mais afetada foi:", categoria_mais_afetada, "com", categorias[categoria_mais_afetada], "pessoas")

# criando conjunto p local
total_por_local = {}
for desastre in registro_desastre:  # registros salvos a cada desastre colocado
    key = (desastre["tipo"], desastre["pais"], desastre["cidade"], desastre["bairro"], desastre["rua"])
    total_por_local[key] = total_por_local.get(key, 0) + desastre["afetados"]

# achando o local com maior qtd de afetados
if total_por_local:
    max_local = max(total_por_local, key=total_por_local.get)
    print("Local com mais pessoas afetadas:")
    print("Tipo desastre:", max_local[0])
    print("País:", max_local[1])
    print("Cidade:", max_local[2])
    print("Bairro:", max_local[3])
    print("Rua:", max_local[4])
    print("Total de afetados:", total_por_local[max_local])
else:
    print("erro")



