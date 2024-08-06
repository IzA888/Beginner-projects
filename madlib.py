#string concatenation
#exemplo: "subscribe to ____"
youtuber = "fulaninho" #variável string

#Algumas formas de fazer isso.

print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"suscribe to {youtuber}")


adj = input("Adjetivo: ")
verb1 = input("Verbo 1: ")
verb2 = input("Verbo 2: ")
famous_person = input("Pessoa famosa: ")


madlib = f"Programar no computador é tão {adj}! Me deixa animada toda vez porque \
Eu adoro {verb1}. Mantenha-se hidratado e {verb2} como se fosse {famous_person}"

print(madlib)