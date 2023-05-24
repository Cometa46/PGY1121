from queue import PriorityQueue


print("datos personales")
print(" ---------------- \n")
Vnom = input("Ingrese nombre ")
while True:
    try:
        Vedad = int(input("Ingrese su edad "))
        break
    except:
        print("Valor no corresponde")
print(" ---------------- \n")
print(f"Su nombre es: {Vnom} \n su edad es: {Vedad}")

print("Programa finaizado")
