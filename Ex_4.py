# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc


def packing(text):
    char_count = {}
    character = text[0]
    count = 0
    for i in range(len(text)):
        if text[i] == character:
            count += 1
        else:
            char_count[count] = text[i-1]
            character = text[i]
            count = 1
        if i == len(text) - 1:
            char_count[count] = text[i]

    pack_code = ""
    for i in char_count:
        pack_code += (str(i) + char_count[i])
    return pack_code


def symbol_repeater(symbol, count):
    output_string = ""
    for i in range(count):
        output_string += symbol
    return output_string


def unpacking(packed_text):
    count = ""
    unpacked_text = ""
    for symbol in packed_text:
        if symbol.isdigit():
            count += symbol
        else:
            unpacked_text += symbol_repeater(symbol, int(count))
            count = ""
    return unpacked_text


with open("read_for_packing.txt", "r") as f:
    text1 = f.read()
with open("packed_text.txt", "w") as f:
    f.write(packing(text1))

with open("read_for_unpacking.txt", "r") as f:
    text2 = f.read()
with open("unpacked_text.txt", "w") as f:
    f.write(unpacking(text2))
