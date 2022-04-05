import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }

    if path_file not in [index["nome_do_arquivo"] for index in instance._data]:
        instance.enqueue(data)
        sys.stdout.write(str(data))


def remove(instance):
    if not instance.__len__():
        return sys.stdout.write("Não há elementos\n")

    data = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {data} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        return sys.stdout.write(str(instance.search(position)))
    except IndexError:
        return sys.stderr.write("Posição inválida\n")
