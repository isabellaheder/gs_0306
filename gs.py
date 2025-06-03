qtd_desastres = int(input("quantidade de desastres?"))
n = 0

while n != qtd_desastres:
    tipo_desastre = input("qual o tipo do desastre?")
    pais_desastre = input("qual o pais do desastre?")
    cidade_desastre = input("qual a cidade do desastre?")
    bairro_desastre = input("qual o bairro do desastre?")
    rua_desastre = input("qual a rua do desastre?")
    qtd_pessoas_afetadas = int(input("Quantas pessoas foram afetadas?"))
    qtd_criancas = int(input("quantas eram crianças?"))
    qtd_adultos = int(input("quantos eram adultos?"))
    qtd_idosos = int(input("quantos eram idosos?"))
    qtd_mob_red = int(input("quantos tinham mobilidade reduzida?"))
    qtd_feridos = int(input("quantos ficaram feridos?"))

    soma = qtd_feridos + qtd_idosos + qtd_criancas + qtd_adultos + qtd_mob_red
    if qtd_pessoas_afetadas == soma:
        print("ok")
        n = n+1
    else:
        print("quantidade de pessoas afetadas está diferente da soma das categorias")
        continue


