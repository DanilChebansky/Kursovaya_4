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

