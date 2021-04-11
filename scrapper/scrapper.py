import os
from flask import jsonify
import requests


class Scrapper:
    base_data_service_api_url: str = os.environ.get('DATA_SERVICE_BASE_URI')
    login_url: str = ""
    username: str = ""
    password: str = ""
    target_url: str = ""
    input_pubsub_subscription: str = ""
    output_pubsub_subscription: str = ""
    temp_store_api_save: str = os.environ.get("TEMP_STORE_ADD_DATA")
    temp_store_api_delete: str = os.environ.get("TEMP_STORE_ADD_DELETE")

    def __init__(self, login_url: str = None, target_url: str = None, username: str = None, password: str = None):
        self.login_url = login_url
        self.username = username or os.environ.get('username')
        self.password = password or os.environ.get('password')
        self.target_url = target_url

    def get_all_stocks(self) -> tuple:
        """
            :return: a list of stock details from data-service api
        """
        pass

    def get_all_brokers(self) -> tuple:
        """
            :return: a list of brokers from data service api
        """
        pass

    @staticmethod
    def parse_stock(symbol: str, from_date: str = "", to_date: str = "") -> tuple:
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
            data = {'symbol': symbol, 'from_date': from_date, 'to_date': to_date}
            url = 'https://sellenium.pinoydesk.com/browse/parse-stock'
            response = requests.post(url=url, json=jsonify(data))
            json_data = response.json()
            if response.ok:
                # payload already includes required data
                return json_data, 200
            else:
                # error message already contained in message
                return json_data, 500
        except ConnectionError as e:
            return jsonify({'status': False, 'message': e}), 500

    @staticmethod
    def parse_broker(broker_code: str, from_date: str = "", to_date: str = "") -> tuple:
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
            url = 'https://sellenium.pinoydesk.com/browse/parse-broker'
            response = requests.post(url=url,json=jsonify(data))
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






