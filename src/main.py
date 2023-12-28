from transfer import Transfer
from config import DATA


def main():
    transfers = Transfer()
    transfers.get_list_operations(DATA)
    transfers.get_true_list_operations(transfers.list_transfer)
    transfers.sort_list(transfers.list_transfer)
    print(transfers.get_transfer_info())


main()
