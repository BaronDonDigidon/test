"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""


def human_readable_size(size: int, decimal_places=2) -> str:
    """Преобразует число байт в человекочитаемый формат"""
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size < 1024:
            break
        size /= 1024
    return f'{size:.{decimal_places}f} {unit}'


def get_summary_rss(ps_output_file_path: str) -> str:
    """Суммирует колонку RSS из файла ps aux и возвращает результат в удобной единице"""
    with open(ps_output_file_path) as ps_file:
        rss_sum = 0
        lines = ps_file.readlines()[1:]  # Пропускаем заголовок
        for line in lines:
            columns = line.split()
            rss = float(columns[5])  # 6-й столбец RSS
            rss_sum += rss
        return human_readable_size(rss_sum)


if __name__ == '__main__':
    path = 'output_file.txt'
    print(get_summary_rss(path))
