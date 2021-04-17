import os
from flask import jsonify
import requests


class Scrapper:
    base_data_service_api_url: str = os.environ.get('DATA_SERVICE_BASE_URI')
    temp_store_api_save: str = os.environ.get("TEMP_STORE_ADD_DATA")
    temp_store_api_delete: str = os.environ.get("TEMP_STORE_ADD_DELETE")

    username: str = ""
    password: str = ""
    stocks: list = []
    brokers: list = []

    scrape_stock_sellenium_uri: str = "https://sellenium.pinoydesk.com/browse/parse-stock"
    scrape_broker_sellenium_uri: str = "'https://sellenium.pinoydesk.com/browse/parse-broker'"

    def __init__(self, username: str = None, password: str = None):
        self.username = username or os.environ.get('username')
        self.password = password or os.environ.get('password')

    def get_all_stocks(self) -> tuple:
        """
            :return: a list of stock details from data-service api
        """
        try:
            url: str = self.base_data_service_api_url + '/api/v1/all/stocks'
            response = requests.post(url=url)
            if response.ok:
                json_data: dict = response.json()
                stocks_list: list = json_data.get('payload')
                if isinstance(stocks_list, list):
                    self.stocks = stocks_list
                    return jsonify({"status": True, "payload": stocks_list,
                                    "message": "successfully fetched stocks list"})
                else:
                    return jsonify({"status": False,
                                    "message": "Unable to download stocks"}), 500
            else:
                return jsonify({"status": False,
                                "message": "Unable to download stocks"}), 500

        except ConnectionError as e:
            return jsonify({"status": False, "message": e}), 500

    def get_all_brokers(self) -> tuple:
        """
            :return: a list of brokers from data service api
        """
        try:
            url: str = self.base_data_service_api_url + '/api/v1/all/brokers'
            response = requests.post(url=url)
            if response.ok:
                json_data: dict = response.json()
                brokers_list: list = json_data.get('payload')
                if isinstance(brokers_list, list):
                    self.brokers = brokers_list
                    return jsonify({"status": True, "payload": brokers_list,
                                    "message": "successfully fetched brokers list"})
                else:
                    return jsonify({"status": False,
                                    "message": "Unable to download brokers"}), 500
            else:
                return jsonify({"status": False,
                                "message": "Unable to download stocks"}), 500
        except ConnectionError as e:
            return jsonify({"status": False, "message": e}), 500

    def scrapper_stock(self, symbol: str, from_date: str = "", to_date: str = "") -> tuple:
        """
            parse a stock through sellenium headless service
            api call: /browse/parse-stock
            see documentation on sellenium

            :param to_date: optional
            :param from_date: optional
            :param symbol: required

            :return: stock trades by brokers
        """
        try:
            data: dict = {'symbol': symbol, 'from_date': from_date, 'to_date': to_date}
            url: str = self.scrape_stock_sellenium_uri
            response = requests.post(url=url, json=jsonify(data))
            json_data = response.json()
            if response.ok is True:
                # payload already includes required data
                return json_data, 200
            else:
                # error message already contained in message
                return json_data, 500
        except ConnectionError as e:
            return jsonify({'status': False, 'message': e}), 500

    def scrapper_broker(self, broker_code: str, from_date: str = "", to_date: str = "") -> tuple:
        """
            parse a broker through sellenium headless chrome service
            api call: /browse/parse-broker
            see docs
        :param to_date:
        :param from_date:
        :param broker_code:
        :return: broker trades by stock
        """
        try:
            data = {'broker_code': broker_code, 'from_date': from_date, 'to_date': to_date}
            url = self.scrape_broker_sellenium_uri
            response = requests.post(url=url, json=jsonify(data))
            json_data = response.json()
            if response.ok:
                return json_data, 200
            else:
                return json_data, 500
        except ConnectionError as e:
            return jsonify({'status': False, 'message': e}), 500

    def build_broker_list_with_parser(self) -> tuple:
        """
            use the parse and parse for brokers list to build our data services api
            :return: a list of brokers on each call
        """
        pass

    def build_stock_list_with_parser(self) -> tuple:
        """

            :return: a list of stocks
        """
        pass

    @staticmethod
    def login(self) -> bool:
        """
            call login
        :return:
        """
        try:

            data: dict = {'username': self.username, 'password': self.password}
            url = 'https://sellenium.pinoydesk.com/browse/login'
            response = requests.post(url=url, json=jsonify(data))
            json_data: dict = response.json()
            return json_data['status']
        except ConnectionError:
            print('cannot login')
            return False

    def save_to_data_service(self, content: str) -> bool:
        try:
            data = {
                "data": content,
                "status": True
            }
            url: str = self.base_data_service_api_url + self.temp_store_api_save

            response = requests.post(url=url, data=jsonify(data))
            if response.ok is True:
                data_response = response.json()
                return data_response['status']
            else:
                return False

        except ConnectionError:
            return False






