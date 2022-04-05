def file(word, lines):
    lines_list = list()

    for line in range(len(lines)):
        if word.capitalize() in lines[line]:
            lines_list.append(lines[line])

        if not len(lines_list):
            return list()

    return lines_list
