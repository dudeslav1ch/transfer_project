import json
from datetime import datetime as date


def get_list_operations(data_path):
    with open(data_path, 'r') as file:
        list_transfer = json.load(file)
    return list_transfer


def get_true_list_operations(path):
    file = get_list_operations(path)
    transfer_list = []
    for value in file:
        if value.get('state') == 'EXECUTED':
            transfer_list.append(value)
    return transfer_list


def sort_list(clean_list_operations):
    sorted_operations = sorted(clean_list_operations, key=lambda dictionary: dictionary['date'], reverse=True)
    sorted_operations = sorted_operations[:5]
    return sorted_operations


def get_date(date_, description):
    """
    Get formatted date and description
    """
    transfer_date = date.fromisoformat(date_)
    transfer_date_formatted = transfer_date.strftime('%d.%m.%Y')
    return f"{transfer_date_formatted} {description}"


def get_card_info(card_info):
    list_card_info = card_info.split()
    new_list = []
    for info in list_card_info:
        if 'счет' in card_info.lower() and info.isdigit():
            new_list.append(f'**{info[-4:]}')
        elif 'счет' not in card_info.lower() and info.isdigit():
            new_list.append(f'{info[:4]} {info[4:6]}** **** {info[-4:]}')
        else:
            new_list.append(info)
    return ' '.join(new_list)


def get_transfer_info(list_transfer):
    new_list = []
    for info in list_transfer:
        new_list.append(f"\n{get_date(info['date'], info['description'])}\n")
        if info.get('from') is None:
            info['from'] = ""
        info_from = get_card_info(info.get('from'))
        info_to = get_card_info(info.get('to'))
        new_list.append(f"{info_from} -> {info_to}\n")
        new_list.append(f"{info['operationAmount']['amount']} {info['operationAmount']['currency']['name']}\n")
    return ''.join(new_list)
