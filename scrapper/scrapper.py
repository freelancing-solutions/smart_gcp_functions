import os
from flask import jsonify
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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

    def __init__(self, login_url: str, target_url: str, chrome_driver_path: str = None, username: str = None, password: str =None):
        self.login_url = login_url
        self.username = username or os.environ.get('username')
        self.password = password or os.environ.get('password')
        self.target_url = target_url

    def get_page(self, url: str) -> str:
        pass

    def login(self) -> bool:
        """
            call login through the our cloud run service
        :return:
        """


    @staticmethod
    def download_content(url: str, params: dict) -> str:
        try:
            response = requests.get(url=url, params=params)
            if response.ok:
                return response.text
        except ConnectionRefusedError:
            return ""
        except ConnectionError:
            return ""

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






