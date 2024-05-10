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
    