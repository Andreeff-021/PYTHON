# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1

    encoding += str(count) + prev_char
    return encoding

def rle_decode(data):
    decode = ''
    count = ''

    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

with open('file_en.txt', 'r') as f:
    data = f.read()

print(rle_encode(data))

with open('file_de.txt', 'w') as f:
    f.write(rle_encode(data))

with open('file_de.txt', 'r') as f:
    data = f.read()

with open('file_en.txt', 'a') as f:
    f.write('\n' + rle_decode(data))

print(rle_decode(data))




