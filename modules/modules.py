import requests


class BinanceCurrency:
    def __init__(
        self, _fiat: str = "RUB", _pay_types: list = ["TinkoffNew", "RosbankNew"]
    ):
        self._url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
        self._headers = {
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        }
        self._params = {
            "fiat": None,
            "page": 1,
            "rows": 10,
            "transAmount": None,
            "tradeType": None,
            "asset": "USDT",
            "countries": [],
            "proMerchantAds": False,
            "publisherType": None,
            "payTypes": None,
        }
        self._DEFAULT = {
            "RUB": {
                "fiat": "RUB",
                "transAmount": "10000",
                "tradeType": "buy",
                "payTypes": ["TinkoffNew", "RosBankNew"],
            },
            "KZT": {
                "fiat": "KZT",
                "transAmount": "50000",
                "tradeType": "sell",
                "payTypes": ["KaspiBank"],
            },
            "THB": {
                "fiat": "THB",
                "transAmount": "5000",
                "tradeType": "sell",
                "payTypes": ["Bank"],
            },
        }

    # ---------------------------getter---------------------------

    def get_param_pay_types(self):
        return self._params["payTypes"]

    def get_param_fiat(self):
        return self._params["fiat"]

    def get_default_params(self):
        return self._DEFAULT

    # ---------------------------compute---------------------------

    def compute_rates(self):
        response = requests.post(
            url=self._url, headers=self._headers, json=self._params
        ).json()
        return float(response["data"][0]["adv"]["price"])

    def compute_rates_top_5(self):
        response = requests.post(
            url=self._url, headcers=self._headers, json=self._params
        ).json()
        return [response["data"][i]["adv"]["price"] for i in range(5)]

    # ---------------------------setter---------------------------

    # set default by fiat
    def set_params_default_by_fiat(self, _fiat: str):
        for key, value in self._DEFAULT[_fiat].items():
            self._params[key] = value

    # TODO: other params
    def set_params_fiat_pay_types(self, _fiat: str, _pay_types: list):
        self.set_params_default_by_fiat(_fiat)
        self._params["payTypes"] = _pay_types
        # print(self._params)

    def set_params_custom(self, other_params: dict):
        for key, value in other_params.items():
            self._params[key] = value
        # print(self._params)


# CURRENCIES = {

#     "Rub": BinanceRubTinkoff().get_rates(),
#     "Thb": BinanceThbBank().get_rates(),
# }


# def get_rate(cur_a, cur_b):
#     return CURRENCIES[cur_a] / CURRENCIES[cur_b]
