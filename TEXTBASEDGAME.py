#Comandos necessários
vida = 100
mochila = []
luta = []
continuar = True
fino = True

def adicionar_item(item, mochila):
  mochila.append(item)

def remover_item(item, mochila):
    if item in mochila:
        mochila.remove(item)
#------------------------------------------------------------------------------------------------------
#Introdução

introducao = input("Deseja jogar este jogo? (Sim (S) / Não (N)): ")
nome = input("Como é que queres que o teu personagem se chame? ")

if introducao == "S":
   print("\n==================== 𝙱𝙴𝙼-𝚅𝙸𝙽𝙳𝙾 𝙰̀ 𝙵𝙻𝙾𝚁𝙴𝚂𝚃𝙰 𝙾𝙱𝚂𝙲𝚄𝚁𝙰! ====================")
   print(f"\n Olá {nome}! Estavas com os teus amigos a explorar uma floresta abandonada, estavam-se a divertir muito até eles afastarem-se de ti e ficas-te sozinho e perdido no meio da floresta, encontras um caminho e segues o mesmo. Para ires embora, tens de os encontrar pois eles têm o mapa para voltar para casa. Ao longe do percurso irás encontrar obstáculos onde irás ter que fazer boas decisões. 𝗘𝗡𝗖𝗢𝗡𝗧𝗥𝗔 𝗢𝗦 𝗧𝗘𝗨𝗦 𝗔𝗠𝗜𝗚𝗢𝗦!!!")

elif introducao == "N":
   print("\nOh nãoo. Volta outro dia :) ")
else:
   print("\nInsira uma opção válida!")
#-----------------------------------------------------------------------------------------------------
#Jogo | FASE 1
if introducao == "S":
    adicionar_item("Pão", mochila)
    adicionar_item("Maça", mochila)
    escolha = input("\nEncontras-te 2 caminhos! Escolhe um: (Esquerda (E) / Direita (D): ")
    if escolha == "E":
      print("\nBoa encontraste uma espada!")
      adicionar_item("Espada", mochila)
      print("\nAgora tens uma espada na tua mochila.")
    elif escolha == "D":
      luta = input("\nMá sorte! Encontraste uma cobra! Tem a opção de fugir ou atacar. (Atacar/Fugir): ")
    if luta == "Fugir":
      print("\nBoa! Conseguiste escapar da cobra sem perder vida!")
    elif luta == "Atacar":
      hp = vida - 3
      print(f"\nBoa! Conseguiste derrotar a cobra! Porém perdeste vida. Agora tens {hp} de saúde.")
#-----------------------------------------------------------------------------------------------------
#Jogo | FASE 2

seguinte = input("\nDigite SEGUINTE para continuar o jogo! ")
print("\nBoa! Já vi que conseguiste passar pelo primeiro desafio. Agora irás encontrar mais 2 caminhos.")
print("\nEncontras-te mais 2 caminhos!")
print("\nQual opção escolhes? ( Esquerda (E) | Direita (D) | Ver mochila (M)): ")
opcao = input("OPÇÃO AQUI: ")
if opcao == "E":
  porta1 = input("\nOh não! Deste de frente com um lobisomen! Para passar por ele vais ter de atacar ou fugir. Qual escolhes? ")
  if porta1 == "atacar" or porta1 == "Atacar":
    print("\nBoa! Conseguiste derrotar o lobisomen e passar por ele! Ganhaste um escudo! Porém perdeste a tua espada!")
    adicionar_item("Escudo", mochila)
    remover_item("Espada", mochila)
    seguinte1 = input("Boa! Conseguiste passar de fase.")
elif opcao == "D":
  falar = input("\nUm senhor desconhecido apareceu. Deseja falar com o mesmo? (Sim (S) | Não (N): ")
  if falar == "S":
    input("\nSenhor: Olá meu jovem! O que estás tu aqui a fazer?")
    input(f"\n{nome}: Estou perdido. Quero encontrar os meus amigos...")
    input("\nSenhor: Ora bolas! Eu conheço muito bem esta floresta, se quiseres posso te ajudar a chegar até eles!")
    decisao = input(f"\n{nome} para si mesmo: O que lhe respondo? Sim, por favor! Quero que me ajude a encontrá-los (1) | Não! Os meus pais sempre me disseram para não falar com estranhos (2): ")
    if decisao == "1":
      input("\nSenhor: Fixe! Vamos por aqui.")
      input("\nPassado uns minutos...")
      input("\nSenhor: Basta ir por aquela ponte e vai conseguir seguir para estar cada vez mais perto deles!")
      input("\nAo chegares lá vês que falta uma parte da ponte e procuras por toda a parte.")
      ponte = input("\nEncontras um pedaço de madeira. Desejas pegar ou encontrar outro caminho? ( Pegar (P) | Outro (O) ): ")
      if ponte == "P":
        print("A madeira foi adicionada à tua mochila")
        adicionar_item("Madeira", mochila)
        madeira = input("Agora tens que ir até à ponte e colocar.")
        if madeira == "Colocar madeira" or madeira == "Colocar":
          print("\nBoa! Conseguiste passar à próxima fase!")
      elif ponte == "O":
        fino = input("\nEncontras outro caminho, porém é no rio e vais ter que saltar de pedra em pedra com peixes assassinos. (Se fosses fino, usavas a comida que tens na tua mochila): ")
        while fino:
          resposta = input("\nQueres jogar de novo? (Sim (S) | Não (N)): ")
          if resposta == "S":
              fino = False
          elif resposta == "N":
            break
    elif decisao == "2":
      input("\nSenhor: Tens a certeza pequenote?")
      input(f"\n{nome}: Sim, tenho.")
      input("\nSenhor: Então vou ter que fazer uma coisa que não vais gostar.")
      input(f"\n{nome}: O quê?")
      hp = hp - 5
      input(f"\nO homem pega numa faca e faz-te um corte na perna, agora perdeste saúde. Estás com {hp} mas conseguiste escapar dele!")
elif opcao == "M":
    print(mochila)
  
#-----------------------------------------------------------------------------------------------------
#Jogo | FASE 3
seguinte = input("\nDigite SEGUINTE para continuar o jogo! ")
input("\nBoa! Estás quase a chegar lá. Faltam-te apenas alguns obstáculos.")
mescolha = input("\nEncontras-te mais 2 portas. Escolhe (Esquerda (E) | Direita (D)) | Ver mochila (M)")
if mescolha == "E":
    input("\nEncontraste uma bruxa muito estranha que começou a falar uma língua estranha.")
    input(f"\n{nome}: Olá? Pode me ajudar a encontrar os meus amigos?.")
    input("\nBruxa: ...")
    input(f"\n{nome}: Senhora? O que está a dizer?")
    input("\nBruxa: ...")
    input(f"\n{nome}: Está a brincar comigo? Você não serve para nada...")
    input("\nDito isso, a bruxa levanta a cabeça e começa-se a rir e faz um gesto estranho e tudo à vossa volta mudou.")
    input(f"\n{nome}: Senh-Senhora? O que está a fazer?")
    input(f"\nA bruxa estala o dedo e apercebeste que perdeste tudo que tinhas na tua mochila")
    remover_item("Maça",mochila)
    remover_item("Pão",mochila)
    esc = input("\nFicas apenas com o escudo e tens 2 opções. (Usar Escudo (U) | Guardar Escudo (G)): ")
    if esc == "U":
      vd = vida - 11
      input(f"\nUsas-te o escudo e conseguiste proteger dela. Mas agora tens {vd} de saúde.")
    elif esc == "G":
      input("\nOh não. Morreste.")
      while continuar:
        resposta = input("\nQueres jogar de novo? (Sim (S) | Não (N)): ")
        if resposta == "S":
            continuar = False
        elif resposta == "N":
          break
elif mescolha == "D":
  input("\nQuando abriste a porta, viste um lago gigante cheio de corcodilos e hipopótamos esfomeados.")
  croc = input("\nDesejas dar comida ou tentar fugir? (Comida (C) | Fugir (F))")
  if croc == "F":
    input("\nOh não. Foste um alimento fácil para os predadores.")
    continuar = True
    while continuar:
      resposta = input("\nQueres jogar de novo? (Sim (S) | Não (N)): ")
      if resposta == "S":
          continuar = False
      elif resposta == "N":
        break
  elif croc == "C":
    remover_item ("Maça", mochila)
    seguinte3 =input("\nFoste inteligente! Utilizaste a maça para atrair os predadores para longe de ti, agora consegues escapar sem problemas. Digite Seguinte para continuar. ")
  elif croc == "M":
    print(mochila)
#-----------------------------------------------------------------------------------------------------
#Jogo | FASE 4

seguinte3 = "Seguinte"
input("Boa! Conseguiste chegar aos teus amigos! Agora pegai no mapa para voltarem para casa.")
input(f"Fim do jogo! Obrigado por jogares o jogo {nome}!")
while continuar:
    resposta = input("\nQueres jogar de novo? (Sim (S) | Não (N)): ")
    if resposta == "S":
        continuar = False
    elif resposta == "N":
      break
