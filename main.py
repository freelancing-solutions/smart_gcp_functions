import base64
from flask import Flask
from scrapper.loader_scrapper import load_scrapper_settings
from scrapper.scrapper import Scrapper
from api.api import ApiCaller


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



def parse_then_send_to_dataservice(event, context):
    """
        Triggered from a message on a Cloud Pub/Sub topic.
        Args:
             event (dict): Event payload.
             context (google.cloud.functions.Context): Metadata for the event.
    """

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)


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


