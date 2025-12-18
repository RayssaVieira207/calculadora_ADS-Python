import math
from typing import Tuple

def ler_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg).replace(",","."))
        except ValueError:
            print("Por favor, Informe apenas números reais!")

def ler_inteiros(msg):
    while True:
         try:
            return int(input(msg))
         except ValueError:
            print("Por favor, Informe apenas números reais!")

def ler_opition(msg: str, options_valida: set[str]) -> str:
    while True:
        opt = input(msg).strip() 
        if opt in options_valida:
            return opt
        print(f"Digite apenas uma da seguintes opções: {', '.join(options_valida)}")            

def mostrar_menu(nome: str, a: float, b: float) -> None:
    print("<","-"*50,">")
    print(f"Olá {nome}! Escolha a Operação a ser realizada:")
    print(f" a = {a} | b = {b}")
    print("-" * 60)
    print("[1] Soma (a + b)")
    print("[2] Subtração (a - b)")
    print("[3] Multiplicação (a * b)")
    print("[4] Divisão (a / b)")
    print("[5] Potência (a ** b)")
    print("[6] Raiz Quadrada de a ou b")
    print("[7] Fatorial")
    print("[8] Alterar os números")
    print("[9] Sair")
    print("-" * 60)
    
def Operar_soma(a: float, b: float) -> None:
    print(f"A Soma: {a} + {b} = {a + b:.1f}")

def Operar_subtracao(a: float, b: float) -> None:
    print(f"A Subtração: {a} - {b} = {a - b:.1f}")

def Operar_multiplicacao(a: float, b: float) -> None:
    print(f"A Multiplicação: {a} x {b} = {a * b:.1f}")

def Operar_divisao(a: float, b: float) -> None:
    if b == 0:
        print("A Divisão por zero não existe em Reais.")
    else:
        print(f"A Divisão: {a} / {b} = {a / b:.1f}")

def Operar_potencia(a: float, b: float) -> None:
    try:
        resultado = a ** b
        print(f"A Potência: {a} ^ {b} = {resultado:,.0f}")

    except OverflowError:
        print("A Potência está exagerada, dê uma amenizada... ")        
    
def Operar_raiz(a: float, b: float) -> None:
    valor = ler_opition(f"Escolha entre a = {a} ou b = {b}: ",{"a","b"})
    valorCalc = a if valor == "a" else b
    if valorCalc < 0:
        print("Não é possivel a Rais Quadrada de um número negativo.")
    else:
        print(f"Raiz Quadrada de {valorCalc}: {math.sqrt(valorCalc):,.3f}")

def Operar_fatorial()-> None:
    n = ler_inteiros("Digite um número inteiro não negativo: ")
    if n < 0:
        print("O valor recebido não pode gerar fatorial")
        return
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    print(f"O Fatorial: {n}! = {resultado:,.2f}")
    
def alterar_numeros() -> Tuple[float,float]:
    print("\nInfrome os novos Valores: ")
    a = ler_float("Novo valor de a: ")
    b = ler_float("Novo valor de b: ")
    return a,b
    

def main() -> None:
    print("<--- Calculadora Python --->")
    nome = input("Digite o seu Nome: ").strip() or "Usuário"
    a = ler_float("Digite o primeiro número real: ")
    b = ler_float("Digite o segundo número real: ")
    
    mostrar_menu(nome, a, b)

    while True:
        mostrar_menu(nome, a, b)
        opcao = ler_opition("Digite sua escolha: ", set("123456789"))
        if opcao == "1":
            Operar_soma(a, b)
        elif opcao == "2":
            Operar_subtracao(a, b)
        elif opcao == "3":
            Operar_multiplicacao(a, b)
        elif opcao == "4":
            Operar_divisao(a, b)
        elif opcao == "5":
            Operar_potencia(a, b)
        elif opcao == "6":
            Operar_raiz(a, b)
        elif opcao == "7":
            Operar_fatorial()
        elif opcao == "8":
            a,b = alterar_numeros()
        elif opcao == "9":
            print("Obrigado por pela utilização da")
            print("------ Calculadora Python ------")
            print(" Espero que tenha gostado! <3")
            break
    
if __name__ == "__main__":
    main()