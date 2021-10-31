#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по
# этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и
# общее количество занятий по нему. Вывести словарь на экран.

def calculate_hours(file_path):

    result = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                subject, numbers = line.split(':')
                subject_sum = sum(int(n) for word in numbers.split() for n in word.split('(') if n.isdigit())
                result[subject] = subject_sum
    except Exception as err:
        print('Ошибка:', err)
    return result

if __name__ == '__main__':
    from pprint import pprint
    res_dict = calculate_hours('test_6.txt')
    pprint(res_dict, width=1)

