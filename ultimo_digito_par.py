# Caso No. 4: Dado un número entero determinar si su último dígito es un número par


print("-------------------------------")
print("--------Último dígito par------")
print("-------------------------------")

# input

n = int(input("Digite el número entero a evaluar: "))


# processing and output

num = n % 10
if num %2 == 0:
    print("El número",num,"es par, entonces si cumple la condición.")
else:
    print("El número",num,"es impar, vuelve a intentarlo.")