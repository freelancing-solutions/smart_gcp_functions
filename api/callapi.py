import os

import requests
import typing

from flask import jsonify


class ApiCaller:
    accepted_apis: typing.List[str] = ['eod', 'pse']

    def __init__(self, api_name: str):
        self._api_name = api_name

    def _build_url(self, endpoint: str) -> typing.Optional[str]:
        if self._api_name == "pse":
            return os.environ.get('PSE_API_BASEURI') + endpoint
        elif self._api_name == "eod":
            return os.environ.get('EOD_API_BASEURI') + endpoint
        else:
            return None

    @staticmethod
    def _call_api(url: str, method: str, params: dict, data: dict) -> tuple:
        try:
            if method == "GET":
                response = requests.get(url=url, params=params)
                if response.ok:
                    data: dict = response.json()
                    jsonify({"status": True, 'payload': data, 'message': 'successfully fetched api data'}), 200
                else:
                    return jsonify({'status': False, 'message': 'error calling the api'}), 500
            elif method == "POST":
                response = requests.post(url=url, params=params, json=data)
                if response.ok:
                    data = response.json()
                    jsonify({"status": True, 'payload': data, 'message': 'successfully fetched api data'}), 200
                else:
                    return jsonify({'status': False, 'message': 'error calling the api'}), 500
            else:
                return jsonify({'status': False, 'message': 'unsupported method'}), 500
        except ConnectionError as e:
            return jsonify({'status': False, 'message': e}), 500

    def call_api(self, endpoint: str, method: str, params: dict, data: dict) -> tuple:
        if self._api_name in self.accepted_apis:
            url = self._build_url(endpoint=endpoint)
            if url is not None:
                return self._call_api(url=url, method=method, params=params, data=data)
            else:
                return jsonify({'status': False, 'message': 'cannot resolve api address'}), 500
        else:
            return jsonify({'status': False, 'message': 'API not initialized'}), 500