

def are_strings_equal(word1, word2):
    # Concatenar los elementos de cada lista de strings
    string1 = "".join(word1)
    string2 = "".join(word2)

    # Comparar los resultados
    if string1 == string2:
        return True
    else:
        return False
print(are_strings_equal(["ab", "d"], ["a", "bc"]))
