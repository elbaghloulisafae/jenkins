
import sys 

print("=" * 4)
print("bienvenue dans mon premier job jenkins !")
print("=" * 40)

if len(sys.argv) > 1:
	nom = sys.argv[1]
else:
	nom = "etudiant jenkins "

print(f"Bonjour {nom}, ton job jenkins q reussi !")


a = 10
b = 5 

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")

assert a + b == 15, "le test a echoue !"
print(" Tous les tes passent avec succes ")
