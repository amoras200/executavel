import random
import time

print(f"{'='*20}JOKENPÔ {'='*20}")
def num(n):
    if n == 1:
        return 'Pedra'
    if n == 2:
        return ('Papel')
    if n == 3:
        return ('Tesoura')

while True:
    jogada = int(input(f"{'='*22} O {'='*23}\nFaça uma jogada!\n1.Pedra\n2.Papel\n3.Tesoura\n\n4.Fechar\n"))
    if jogada == 4:
        break
    if jogada != 1 and jogada != 2 and jogada != 3 and jogada != 4:
        print("Parece que escolheu o numero errado! use 1, 2 ou 3 para fazer uma jogada e 4 se quiser parar.")
    escolha_sistema = random.randint(1,3)
    resultado = F"nos vemos na proxima!"

    if jogada == escolha_sistema:
        resultado = "empate"
    if jogada == 1 and escolha_sistema==2:
        resultado = f"perdeu"
    if jogada == 1 and escolha_sistema==3:
        resultado = f"venceu"
    if jogada == 2 and escolha_sistema==1:
        resultado = f"venceu"
    if jogada == 2 and escolha_sistema==3:
        resultado = f"perdeu"
    if jogada == 3 and escolha_sistema==1:
        resultado = f"perdeu"
    if jogada == 3 and escolha_sistema==2:
        resultado = f"venceu"
    print(f"\nEMPATE! joguei: {num(escolha_sistema)}\nvocê jogou {num(jogada)} \n\n" if resultado=="empate" else(f"\ncê venceu! eu joguei {num(escolha_sistema)} você jogou {num(jogada)} \n\n" if resultado == "venceu" else (f"\nHAHAHAHA PERDEU! essa eu ganhei! escolhi {num(escolha_sistema)}\nvocê jogou {num(jogada)} \n\n" if resultado == "perdeu" else(f"Escolha um numero valido!\n\n\n") )))
    