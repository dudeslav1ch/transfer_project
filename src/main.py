from config import DATA
from src.transfer import get_true_list_operations, sort_list, get_transfer_info


def main():
    operations_data = get_true_list_operations(DATA)
    true_list_operations = sort_list(operations_data)
    print(get_transfer_info(true_list_operations))


main()
