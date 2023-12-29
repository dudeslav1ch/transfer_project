from config import DATA_TEST, DATA_TEST_INFO, DATA_TEST_EXECUTED
from src.transfer import get_list_operations, get_true_list_operations, sort_list, get_date, get_card_info, \
    get_transfer_info


def test_get_list_operations():
    assert get_list_operations(DATA_TEST) == [1, 2, 3]


def test_get_true_list_operations():
    assert get_true_list_operations(DATA_TEST_EXECUTED) == [
        {
            "id": 114832369,
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890",
            "operationAmount": {
                "amount": "48150.39",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Classic 2842878893689012",
            "to": "Счет 35158586384610753655"
        }
    ]


def test_sort_list():
    assert sort_list([{"date": "2019-12-08T22:46:21.935582"}]) == [{"date": "2019-12-08T22:46:21.935582"}]


def test_get_date():
    assert get_date("2019-12-08T22:46:21.935582", "Открытие вклада") == '08.12.2019 Открытие вклада'


def test_get_card_info():
    assert get_card_info("Visa Classic 2842878893689012") == 'Visa Classic 2842 87** **** 9012'
    assert get_card_info("Счет 35158586384610753655") == 'Счет **3655'


def test_get_transfer_info():
    operations_data = get_list_operations(DATA_TEST_INFO)
    true_list_operations = sort_list(operations_data)
    assert get_transfer_info(true_list_operations) == (f"\n08.12.2019 Открытие вклада\n"
                                                       f" -> Счет **5907\n41096.24 USD\n")
