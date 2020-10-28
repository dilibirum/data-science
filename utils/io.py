import os
from datetime import datetime


class Writer:

    def __init__(self, **params):
        self.params = params
        self.date = datetime.now().strftime("%Y-%m-%d")

    def write_txt(self,
                  text='',
                  title='',
                  filename=None,
                  path=None,
                  logs=True):
        """
        """

        if filename is None and 'filename' in self.params:
            filename = self.params['filename']

        if path is None and 'path' in self.params:
            path = self.params['path']

        full_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_path = f'{path}{self.date}_{filename}.txt'

        if not os.path.exists(full_path):
            with open(full_path, 'a') as f:
                f.write(f'Аналитический отчет создан {full_date} \n')

        with open(full_path, 'a') as f:
            f.write(f'\n{title} \n')
            f.write(f'{text} \n')

        if logs:
            print(f'Записано в файл: {full_path} в {full_date}')

    def _test(self, filename=None, path=None):
        if filename is None:
            filename = self.params['filename']

        if path is None:
            path = self.params['path']

        return f'{path}{filename}.txt'


def read_file(path):
    """Функция читает файл построчно и записывает его в список

    Аргументы:
    :params: path -- путь до файла
    :return: список со строками файла
    """
    res = []
    with open(path) as f:
        for line in f.readlines():
            res.append(line.strip())

    return res


def write_file(path, source_list):
    """Функция пишет файл построчно из списка

    Аргументы:
    :params: path -- путь до файла
    :params: source_list -- исходный список
    :return: список со строками файла
    """

    with open(path, 'w') as f:
        for item in source_list:
            f.write(str(item) + '\n')
