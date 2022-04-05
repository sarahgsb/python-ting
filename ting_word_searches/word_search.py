from ting_word_searches.utils.word_search_util import file


def exists_word(word, instance):
    word_list = list()

    for line in instance._data:
        lines = file(word, line["linhas_do_arquivo"])
        if not len(lines):
            return lines

        data = [
            {
                "palavra": word,
                "arquivo": line["nome_do_arquivo"],
                "ocorrencias": word_list,
            }
        ]

        for _line in lines:
            word_list.append(
                {"linha": line["linhas_do_arquivo"].index(_line) + 1}
            )

        return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
