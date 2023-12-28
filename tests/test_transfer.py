from config import DATA_TEST, DATA_TEST_INFO
from src.transfer import Transfer


def test_get_list_operations():
    assert Transfer().get_list_operations(DATA_TEST) == [1, 2, 3]


def test_get_true_list_operations():
    assert Transfer().get_true_list_operations([{'state': 'EXECUTED'}]) == [{'state': 'EXECUTED'}]


def test_sort_list():
    assert Transfer().sort_list([{"date": "2019-12-08T22:46:21.935582"}]) == [{"date": "2019-12-08T22:46:21.935582"}]


def test_get_date():
    assert Transfer().get_date("2019-12-08T22:46:21.935582", "Открытие вклада") == '08.12.2019 Открытие вклада'


def test_get_card_info():
    assert Transfer().get_card_info("Visa Classic 2842878893689012") == 'Visa Classic 2842 87** **** 9012'
    assert Transfer().get_card_info("Счет 35158586384610753655") == 'Счет **3655'


def test_get_transfer_info():
    transfers = Transfer()
    transfers.get_list_operations(DATA_TEST_INFO)
    assert transfers.get_transfer_info() == (f'\n08.12.2019 Открытие вклада\n'
                                             f' -> Счет **5907\n41096.24 USD\n')
