"""
En una lengua alienígena también utilizan las letras del español,
pero posiblemente en un orden diferente.
Es una permutación de nuestro alfabeto.

Tu desafío es, dada una secuencia de palabras escritas en el
idioma extranjero y el orden del alfabeto alienígena,
devolver verdadero si y solo si las palabras dadas están
ordenadas lexicográficamente según el orden de letras del
alfabeto alienígena dado.

Ejemplo 1:

// Input
const words1 = ["habito", "hacer", "lectura", "sonreir"];
const order1 = "hlabcdfgijkmnopqrstuvwxyz";
isAlienSorted(words1, order1);

// Output
true

Ejemplo 2:

// Input 1
const words2 = ["habito", "hacer", "sonreir", "lectura"];
const order2 = "hlabcdfgijkmnopqrstuvwxyz";
isAlienSorted(words2, order2);

// Output 2
false

Ejemplo 3:

// Input
const words3 = ["conocer", "cono"];
const order3 = "abcdefghijkmnopqrstuvwxyz";
isAlienSorted(words3, order3);

// Output:
false


"""


def compare_two_words_orden(actual_word, next_word, hash_map_alien_dictionary):
    min_length_of_two_words = min(len(actual_word), len(next_word))
    print(min_length_of_two_words)

    for i in range(0, min_length_of_two_words):
        print(f"{actual_word[i]} - {next_word[i]}")

        if (
            hash_map_alien_dictionary[actual_word[i]]
            < hash_map_alien_dictionary[next_word[i]]
        ):
            return True

        if (
            hash_map_alien_dictionary[actual_word[i]]
            > hash_map_alien_dictionary[next_word[i]]
        ):
            return False

    return len(actual_word) <= len(next_word)


def is_alien_dictionary_sorted(words_list, dictionary_order):
    hash_map_alien_dictionary = dict()

    for index, letter in enumerate(dictionary_order):
        hash_map_alien_dictionary[letter] = int(index)

    for index in range(1, len(words_list)):
        if (
            compare_two_words_orden(
                words_list[index - 1],
                words_list[index],
                hash_map_alien_dictionary,
            )
            is False
        ):
            return False

    return True


if __name__ == "__main__":
    order1 = "hlabcdfgijkmnopqrstuvwxyz"
    words1 = ["habito", "hacer", "lectura", "sonreir"]

    is_sorted_alien_dictionry = is_alien_dictionary_sorted(words1, order1)
    print(is_sorted_alien_dictionry)
