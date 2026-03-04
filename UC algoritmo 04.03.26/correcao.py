#2 
numero = int(input("digite um número: "))


if (numero % 2 == 0):
  resultado = numero **2
else:
  resultado = numero ** 3

print("Resultado", resultado)

#3construir programa que valida acesso do professor  á rede escolar. login1: usuário:procopio, senha:12345, login 2: usuário:paiva, senha:54321

usuario = input("Digite seu user: ")
senha = input("Digite sua senha: ")

if (usuario == "procopio"and senha == "12345") or (usuario == "paiva" and senha == "54321"):
  print("Seja bem-vindo")
else:
  print("Usuário e senha não conferem.")

  #4programa que recebe a senha de um correntista para validar o acesso ao sistema.senha:123456, mensagem:"olá, <SEUNOME> bem vindo". quando errar, mostrar: "senha incorreta, você tem duas tentativas", se errar"senha bloqueada, diriga-se ao caixa"

  nome = input("Digite seu nome: ")
  senhaCorreta = "123456"

  tentativa = 3


  while tentativa > 0:
    senha = input("Digite sua senha: ")


    if senha == senhaCorreta:
      print(f"Olá, {nome}! Seja bem vindo!")
      break
    else:
        tentativa -= 1

        if tentativa == 2:
          print("Senha errada, você tem 2 tentativas")
        elif tentativa == 1:
          print("Senha errada, você tem 1 tentativa")
        else:
          print("Senha bloqueada!")
      

