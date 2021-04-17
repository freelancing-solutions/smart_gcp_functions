

class DataParser:
    input_pub_sub_subscription = ""
    output_pub_sub_subscription = ""
    stocks: list = []
    brokers: list = []

    def __init__(self, html):
        self.html = html

    def parse_table_content(self, html):
        """

        :param html: a table of stock or broker
        :return:
        """
        pass

    def parse_stocks(self, content):
        """
            for each stock return buys sells and net
        :param content:
        :return:
        """
        pass

    def parse_brokers(self, content):
        """
            for each broker return buys sells and net
        :param content:
        :return:
        """
        pass

    def save_stocks(self, stocks):
        """
                save all stock data to data-service main database
            :param stocks:
            :return:
        """
        pass

    def save_brokers(self, brokers):
        """
            save all brokers data to data-service main database
        :param brokers:
        :return:
        """
        pass

    def get_single_stock(self, symbol):
        """
            parse data for just one stock symbol
        :param stocks:
        :return:
        """
        pass

    def send_to_pubsub_topic(self, stocks):
        """
            get single stock from the list of stocks then send that stock through pubsub
        :param stocks:
        :return:
        """
        pass
