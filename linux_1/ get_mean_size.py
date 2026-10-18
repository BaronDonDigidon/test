

""" Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe): $ ls -l | python3 get_mean_size.py 
Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l, а возвращает средний размер файла в каталоге. """ 
import sys
def get_mean_size(ls_output: str) -> float:     
    """Вычисляет средний размер файла из вывода ls -l"""     
    lines = ls_output.splitlines()[1:]  # Пропускаем заголовок     
    if not lines:         
        return 0    
     
    total_size = 0     
    for line in lines:         
        columns = line.split()         
        file_size = int(columns[4])  # размер файла         
        total_size += file_size     
    return total_size / len(lines) 

if __name__ == '__main__':     
    data = sys.stdin.read()     
    print(get_mean_size(data))

