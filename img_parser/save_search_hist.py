import json

def add_searched_param_to_search_hist(searching_param):
    with open('../searched_params.json', 'r') as f:
        data: dict[str, list[str]] = json.load(f)
    data['searched_params'].append(searching_param)
    with open('../searched_params.json', 'w') as f:
        json.dump(data, f)