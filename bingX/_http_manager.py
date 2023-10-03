from json.decoder import JSONDecodeError
from typing import Any

import requests

from bingX._helpers import generate_hash, generate_timestamp
from bingX.exceptions import ClientError, InvalidMethodException, ServerError


class _HTTPManager:
    __BASE_URL = "https://open-api.bingx.com"

    def __init__(self, api_key: str, secret_key: str) -> None:
        self.__secret_key = secret_key
        self.__session = requests.Session()
        self.__session.headers.update({'X-BX-APIKEY': api_key})

    def _generate_signature(self, query_string: str) -> str:
        """
        It takes a query string and returns a signature

        :param query_string: The query string that you want to sign
        :return: A string of the signature
        """

        hmac = generate_hash(self.__secret_key, query_string)
        signature = hmac.hexdigest()
        return signature

    def _generate_query_string(self, payload: dict[str, Any] = {}) -> str:
        """
        It takes a payload and returns a query string

        :param payload: The payload that you want to convert to a query string
        :return: A string of the query string
        """

        payload["timestamp"] = generate_timestamp()
        query_string = '&'.join(f'{k}={v}' for k, v in payload.items() if v)
        query_string += f"&signature={self._generate_signature(query_string)}"
        return query_string

    def _request(self, method: str, endpoint: str, payload: dict[str, Any] = {}, headers: dict[str, Any] = {}) -> requests.Response:
        """
        It takes a method, endpoint, payload, and headers, and returns a response

        :param method: The HTTP method to use (GET, POST, PUT, DELETE)
        :param endpoint: The endpoint you want to hit i.e. /openApi/swap/v2/trade/order
        :param payload: The data to be sent to the server
        :param headers: This is a dictionary of headers that will be sent with the request
        """
        if headers:
            self.__session.headers.update(headers)

        url = f"{self.__BASE_URL}{endpoint}?{self._generate_query_string(payload)}"
        match method:
            case "GET":
                req = self.__session.get(url)
            case "POST":
                req = self.__session.post(url)
            case "PUT":
                req = self.__session.put(url)
            case "DELETE":
                req = self.__session.delete(url)
            case _:
                raise InvalidMethodException(f"Invalid method used: {method}")

        if req.status_code != 200:
            raise ServerError(req.status_code, req.text)

        try:
            req_json: dict[str, Any] = req.json()
        except JSONDecodeError:
            return req
        else:
            #TODO: Check if this is the correct way to check for errors
            if req_json.get("code") is not None and req_json.get("code") != 0:
                raise ClientError(req_json.get("code"), req_json.get("msg"))
            return req

    def get(self, endpoint: str, payload: dict[str, Any] = {}, headers: dict[str, Any] = {}) -> requests.Response:
        """
        It makes a GET request to the given endpoint with the given payload and headers

        :param endpoint: The endpoint you want to hit i.e. /openApi/swap/v2/trade/order
        :param payload: The data to be sent to the server
        :param headers: This is a dictionary of headers that will be sent with the request
        :return: A response object
        """

        return self._request("GET", endpoint, payload, headers)

    def post(self, endpoint: str, payload: dict[str, Any] = {}, headers: dict[str, Any] = {}) -> requests.Response:
        """
        It makes a POST request to the given endpoint with the given payload and headers

        :param endpoint: The endpoint you want to hit i.e. /openApi/swap/v2/trade/order
        :param payload: The data to be sent to the server
        :param headers: This is a dictionary of headers that will be sent with the request
        :return: A response object
        """

        return self._request("POST", endpoint, payload, headers)

    def put(self, endpoint: str, payload: dict[str, Any] = {}, headers: dict[str, Any] = {}) -> requests.Response:
        """
        It makes a PUT request to the given endpoint with the given payload and headers

        :param endpoint: The endpoint you want to hit i.e. /openApi/swap/v2/trade/order
        :param payload: The data to be sent to the server
        :param headers: This is a dictionary of headers that will be sent with the request
        :return: A response object
        """

        return self._request("PUT", endpoint, payload, headers)

    def delete(self, endpoint: str, payload: dict[str, Any] = {}, headers: dict[str, Any] = {}) -> requests.Response:
        """
        It makes a DELETE request to the given endpoint with the given payload and headers

        :param endpoint: The endpoint you want to hit i.e. /openApi/swap/v2/trade/order
        :param payload: The data to be sent to the server
        :param headers: This is a dictionary of headers that will be sent with the request
        :return: A response object
        """

        return self._request("DELETE", endpoint, payload, headers)