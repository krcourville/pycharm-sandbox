import requests


def test_it_says_hello():
    res = requests.get('http://127.0.0.1:5000')
    assert res.content == b"Hello World!"

