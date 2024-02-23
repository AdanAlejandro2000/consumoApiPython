import requests

# Definición de la URL base de la API de Pokémon
url_api = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Solicitar al usuario el nombre del Pokémon que desea buscar
    pokemon_name = input('Dame el nombre del pokemon: ')
    
    # Construir la URL completa para la solicitud a la API
    pokemon_data_url = url_api + pokemon_name

    # Llamar a la función para obtener y mostrar la información del Pokémon
    data = get_pokemon_data(pokemon_data_url)

def get_pokemon_data(url_pokemon=''):
    """
    Función para obtener y mostrar información sobre un Pokémon utilizando la PokeAPI.

    Parámetros:
    - url_pokemon (str): La URL completa para la solicitud a la API de Pokémon.

    Retorna:
    - None: Si ocurre un error al obtener la información del Pokémon.
    - dict: Un diccionario con la información del Pokémon si la solicitud es exitosa.
    """
    # Diccionario para almacenar la información del Pokémon
    pokemon_data = {
        "name": '',            # Nombre del Pokémon
        "height": '',          # Altura del Pokémon
        "abilities": '',       # Habilidades del Pokémon
        "types": '',           # Tipos del Pokémon
        "weight": ''           # Peso del Pokémon
    }
    
    # Realizar la solicitud GET a la URL de la API de Pokémon
    response = requests.get(url_pokemon)
    
    # Verificar si la solicitud fue exitosa (código de estado HTTP 200)
    if response.status_code == 200:
        # Obtener la información del Pokémon en formato JSON
        pokemon_info = response.json()
        
        # Extraer la información relevante y almacenarla en el diccionario pokemon_data
        pokemon_data['name'] = pokemon_info['name']
        pokemon_data['height'] = pokemon_info['height']
        # Se obtienen las habilidades del Pokémon y se almacenan en una lista
        pokemon_data['abilities'] = [ability['ability']['name'] for ability in pokemon_info['abilities']]
        # Se obtienen los tipos del Pokémon y se almacenan en una lista
        pokemon_data['types'] = [type['type']['name'] for type in pokemon_info['types']]
        pokemon_data['weight'] = pokemon_info['weight']
        
        # Mostrar la información del Pokémon en la consola
        print(pokemon_data)
    else:
        # Si la solicitud no fue exitosa, mostrar un mensaje de error
        print(f'Error: No se pudo obtener información del pokemon {pokemon_name}')

# Verificar si el script se está ejecutando como el programa principal
if __name__ == '__main__':
    # Llamar a la función principal
    main()
