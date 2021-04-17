from flask import jsonify
from api import ApiCaller
from MyParser import DataParser
from scrapper import Scrapper


def return_options() -> tuple:
    # Allows GET requests from origin https://mydomain.com with
    # Authorization header
    headers = {
        'Access-Control-Allow-Origin': 'https://data-service.pinoydesk.com',
        'Access-Control-Allow-Methods': 'POST,GET,PUT,DELETE,OPTIONS',
        'Access-Control-Allow-Headers': 'Authorization, Origin, Accept, Content-Type, X-Requested-With, '
                                        'X-CSRF-Token',
        'Access-Control-Max-Age': '3600',
        'Access-Control-Allow-Credentials': 'true'
    }
    return '', 204, headers


def scrapper_requester(request):
    """
        type: HTTP
        trigger: task scheduler - the task will run continually triggering functions with different
        symbols to scrape the data , then continually save scrapped data on temp storage
    """
    # For more information about CORS and CORS preflight requests, see
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request
    # for more information.
    # Set CORS headers for preflight requests
    if request.method == 'OPTIONS':
        return return_options()
    else:
        pass

    content_type = request.headers.get('content-type')
    if content_type == 'application/json':
        json_data = request.get_json(silent=True)
    else:
        return jsonify({"status": False, "payload": {}, "error": "JSON is Invalid"})

    from_date = json_data.get('from_date')
    to_date = json_data.get('to_date')
    use_scrapper = json_data.get('use_scrapper')
    scrapper_api: Scrapper = Scrapper()

    if use_scrapper == "stock":
        symbol = json_data.get('symbol')
        return scrapper_api.scrapper_stock(symbol=symbol, from_date=from_date, to_date=to_date)
    elif use_scrapper == "broker":
        broker_code = json_data.get('broker_code')
        return scrapper_api.scrapper_broker(broker_code=broker_code, from_date=from_date, to_date=to_date)
    else:
        return jsonify({"status": False, "message": "can only scrapper broker and stock at the moment"}), 500


def parse_and_save_data_service(request):
    """
        Triggered by HTTP from tasks on data-service
        will start triggering as soon as the MyParser is done
        Args:
             event (dict): Event payload.
             context (google.cloud.functions.Context): Metadata for the event.
             :param request:
    """

    if request.method == 'OPTIONS':
        return return_options()
    else:
        pass

    content_type = request.headers.get('content-type')
    if content_type == 'application/json':
        json_data = request.get_json(silent=True)
    else:
        return jsonify({"status": False, "payload": {}, "error": "JSON is Invalid"})

    data = json_data.get('data')
    use_parser = json_data.get('use_parser')
    parser_instance: DataParser = DataParser(html=data)
    if use_parser == "stocks":
        stocks_data = parser_instance.parse_stocks()
        return parser_instance.save_stocks(stocks=stocks_data)

    elif use_parser == "brokers":
        brokers_data = parser_instance.parse_brokers()
        return parser_instance.save_brokers(brokers=brokers_data)
    else:
        return jsonify({"status": False, "message": "can only parse stocks or brokers"}), 500


def api_requester(request):
    """
        triggered by a task scheduler with symbols
        to get data on pse or eod api to either compare with scrapped data or by admin
        to manually enter data
    """
    if request.method == 'OPTIONS':
        return return_options()
    else:
        pass

    content_type = request.headers.get('content-type')
    if content_type == 'application/json':
        json_data = request.get_json(silent=True)
    else:
        return jsonify({"status": False, "payload": {}, "error": "JSON is Invalid"})

    use_api = json_data.get("use_api")
    endpoint = json_data.get('endpoint')
    api_instance: ApiCaller = ApiCaller(api_name=use_api)
    # NOTE: the data from here can go directly to the data-service store
    return api_instance.call_api(endpoint=endpoint)