import requests
import json
from config import keys

class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')


        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Неудалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Неудалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неудалось обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        # r = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_ticker}&symbols={quote_ticker}')
        # разница между api в том, что с вашего примера приходит ответ в виде простейшего словаря, в другом же искомое значение находится в виде словаря,
        # находящимся в 1 значении другого словаря.
        # Хоть убейте, но я так и не понял, как вытащить его -_-
        total_base = json.loads(r.content)[keys[base]]*amount

        return total_base