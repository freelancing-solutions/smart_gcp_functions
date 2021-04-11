import base64
from flask import Flask
from loader_scrapper import load_scrapper_settings
from scrapper import Scrapper
from api import ApiCaller

from parser import Parser


def scrapper_requester(event, context):
    """
        Triggered from a message on a Cloud Pub/Sub topic.
        Args:
             event (dict): Event payload.
             context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
    load_scrapper_settings()

    # NOTE login_url and all the other settings could be configure here
    scrapper_api: Scrapper = Scrapper()

    return "OK", 200


def parse_then_send_to_dataservice(event, context):
    """
        Triggered from a message on a Cloud Pub/Sub topic.
        Args:
             event (dict): Event payload.
             context (google.cloud.functions.Context): Metadata for the event.
    """

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    parser_instance: Parser = Parser()

    return "OK", 200


def pse_api_requester(event, context):
    """
        Triggered from a message on a Cloud Pub/Sub topic.
        Args:
             event (dict): Event payload.
             context (google.cloud.functions.Context): Metadata for the event.
    """

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    api_instance: ApiCaller = ApiCaller()

    return "OK", 200


def eod_api_requester(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    api_instance: ApiCaller = ApiCaller()

    return "OK", 200