import requests


class HTTP:
    """
    http请求发送
    """

    # 静态方法，没有用到 类的self
    @staticmethod
    def get(url, return_json=True):
        response = requests.get(url)
        # 特判
        if response.status_code != 200:
            # restful 返回的是 json
            return {} if return_json else ''
        return response.json() if return_json else response.text
