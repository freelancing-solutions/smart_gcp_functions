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

    def __init__(self, login_url: str, target_url: str, username: str = None, password: str = None):
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

    def parse_stock(self, symbol: str) -> tuple:
        """
            parse a stock through sellenium headless service
            api call: /browse/parse-stock
            see documentation on sellenium
        :param symbol:
        :return:
        """
        pass

    def parse_broker(self, broker_code: str) -> tuple:
        """
            parse a broker through sellenium headless chrome service
            api call: /browse/parse-broker
            see docs
        :param broker_code:
        :return:
        """
        pass

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
            url = 'https://sellenium.pinoydesk.com/browse/login'
            response = requests.post(url=url)
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






