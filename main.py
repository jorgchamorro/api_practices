import requests
import json

# Simple character request
i = 1 
while i < 11:
    url = 'https://rickandmortyapi.com/api/character/{}'.format(i)
    r = requests.get(url)
    j = r.json()
    status = j['status']
    name = j['name']
    i += 1
    print('Character name is {} and is {}'.format(name, status))

# Request personajes por episodio
episodio = input("Enter an episode number: ")
print("#############################################################")
url_episodio = 'https://rickandmortyapi.com/api/episode/{}'.format(episodio)
r_episodio = requests.get(url_episodio)
j_episodio = r_episodio.json()
print("Episode #{} - {}".format(episodio, j_episodio['name']))
personajes = j_episodio['characters']
print("Characters on Episode:\n------------------------------------------------")
for personaje in personajes:
    url_personaje = personaje
    r_personaje = requests.get(url_personaje)
    j_personaje = r_personaje.json()
    nombre_personaje = j_personaje['name']
    especie_personaje = j_personaje['species']
    print("- {} | Especie: {}".format(nombre_personaje, especie_personaje))
print("\n")
i += 1