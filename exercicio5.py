def inverted_string(string):

    characters = list(string)
    size = len(characters)
    start = 0
    end = size - 1

    while start < end:
        characters[start], characters[end] = characters[end], characters[start]
        start += 1
        end -= 1
    return ''.join(characters)


string = input("digite uma string: ")
inverted_string = inverted_string(string)

print("string invertida:", inverted_string)