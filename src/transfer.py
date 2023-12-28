import json
from datetime import datetime as date


class Transfer:
    def __init__(self):
        self.list_transfer = []

    def get_list_operations(self, data_path):
        with open(data_path, 'r') as file:
            self.list_transfer = json.load(file)
        return self.list_transfer

    def get_true_list_operations(self, transfer_list):
        new_list = []
        for value in transfer_list:
            if value.get('state') == 'EXECUTED':
                new_list.append(value)
        self.list_transfer = new_list
        return self.list_transfer

    def sort_list(self, true_list_operations):
        self.list_transfer = sorted(true_list_operations, key=lambda dictionary: dictionary['date'], reverse=True)
        self.list_transfer = self.list_transfer[:5]
        return self.list_transfer

    def get_date(self, date_, description):
        """
        Get formatted date and description
        """
        transfer_date = date.fromisoformat(date_)
        transfer_date_formatted = transfer_date.strftime('%d.%m.%Y')
        return f"{transfer_date_formatted} {description}"

    def get_card_info(self, card_info):
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

    def get_transfer_info(self):
        list_transfer = self.list_transfer
        new_list = []
        for info in list_transfer:
            new_list.append(f"\n{self.get_date(info['date'], info['description'])}\n")
            if info.get('from') is None:
                info['from'] = ""
            info_from = self.get_card_info(info.get('from'))
            info_to = self.get_card_info(info.get('to'))
            new_list.append(f"{info_from} -> {info_to}\n")
            new_list.append(f"{info['operationAmount']['amount']} {info['operationAmount']['currency']['name']}\n")
        return ''.join(new_list)
