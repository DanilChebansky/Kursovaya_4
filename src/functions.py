def filter_vacancies(list_, words):
    filtered_list = []
    if len(list_) == 0:
        return []
    elif len(words) == 0:
        return list_
    else:
        for vacancy in list_:
            for word in words:
                if word in vacancy["name"]:
                    filtered_list.append(vacancy)
        return filtered_list


def get_vacancies_by_salary(filtered_list, min_value=20000, max_value=200000):
    got_list = []
    if len(filtered_list) == 0:
        return []
    else:
        for vacancy in filtered_list:
            if int(max_value) > vacancy["mid_salary"] > int(min_value):
                got_list.append(vacancy)
        return got_list


def sort_vacancies(got_list):
    if len(got_list) == 0:
        return []
    else:
        sorted_list = sorted(got_list, key=lambda x: x['mid_salary'], reverse=True)
        return sorted_list


def get_top_vacancies(sorted_list, top_numb=5):
    if len(sorted_list) in [0, 1]:
        return sorted_list
    elif top_numb > len(sorted_list):
        return sorted_list[0:len(sorted_list)]
    else:
        return sorted_list[0:int(top_numb)]


def print_vacancies(top_list):
    if len(top_list) == 0:
        return []
    else:
        for vacancy in top_list:
            if vacancy["salary"]["from"] is None:
                vacancy["salary"]["from"] = "Не указано"
            if vacancy["salary"]["to"] is None:
                vacancy["salary"]["to"] = "Не указано"
            print(f"Название: {vacancy["name"]}\n"
                  f"Ссылка: {vacancy["url"]}\n"
                  f"Зарплата (от - до): {vacancy["salary"]["from"]} - {vacancy["salary"]["to"]}\n"
                  f"Требования: {vacancy["requirements"]}\n"
                  f"Требуемый опыт: {vacancy["experience"]}\n"
                  f"Область: {vacancy["area"]}\n")


def user_interaction(list_):
    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    except ValueError:
        top_n = 5
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split(",")
    try:
        min_salary = int(input("Введите минимальную зарплату: "))
    except ValueError:
        min_salary = 20000
    try:
        max_salary = int(input("Введите максимальную зарплату: "))
    except ValueError:
        max_salary = 200000

    filtered_vacancies = filter_vacancies(list_, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, min_salary, max_salary)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
