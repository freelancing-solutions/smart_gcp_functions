

class Scrapper:
    login_url: str = ""
    username: str = ""
    password: str = ""
    target_url: str = ""
    input_pubsub_subscription: str = ""
    output_pubsub_subscription: str = ""

    def __init__(self, login_url: str, username: str, password: str, target_url: str):
        self.login_url = login_url
        self.username = username
        self.password = password
        self.target_url = target_url

    def get_page(self, url: str) -> str:
        pass

    def login(self) -> bool:
        """
            try and learn how the token gets saved
        :return:
        """
        pass

    def select_input_by_css(self, css_selector: str) -> str:
        pass

    def select_input_by_id(self, element_id: str) -> str:
        pass

    def download_content(self, url: str) -> str:
        pass

    def save_content(self, content: str) -> bool:
        pass




