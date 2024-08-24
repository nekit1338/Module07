def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, "w", encoding="utf-8") as file:
        index = 1
        for i in strings:
            position = file.tell()
            file.write(i + "\n")
            strings_positions[(index, position)] = i
            index += 1
    return strings_positions


if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

    print(result)
