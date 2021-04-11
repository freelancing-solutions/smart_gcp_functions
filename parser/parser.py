

class Parser:
    input_pub_sub_subscription = ""
    output_pub_sub_subscription = ""

    def __init__(self, html):
        self.html = html

    def parse_page_content(self, html):
        pass

    def parse_stocks(self, content):
        pass

    def save_stocks(self, stocks):
        pass

    def get_single_stock(self, stocks):
        pass

    def send_to_pubsub_topic(self, stocks):
        """
            get single stock from the list of stocks then send that stock through pubsub
        :param stocks:
        :return:
        """
        pass
