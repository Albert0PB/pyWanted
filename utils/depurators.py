def depurate_list(list_to_depurate: list):
    candidate_list = list()
    if is_there_internal_lists(list_to_depurate):
        for i in list_to_depurate:
            candidate_list.extend(j for j in i) if isinstance(i, list) else candidate_list.append(i)
    return candidate_list if not is_there_internal_lists(candidate_list) else depurate_list(candidate_list)


def is_there_internal_lists(list_to_check: list):
    for i in list_to_check:
        return True if isinstance(i, list) else False


