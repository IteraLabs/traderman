# --- ------------------------------------------------------------------- --- #
# --- File: clients.py
# --- ------------------------------------------------------------------- --- #

import hmac
import hashlib
import requests
from urllib.parse import urlencode
import time
import pandas as pd

from traderman.tools.generic import get_system_timestamp

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


def get_server_timestamp(
    server_url: str,
):
    """
    a simple REST API type of call to retrieve a remote's server time

    Args:
        server_url: str
            url string to query the time

    Returns:
        The time as known by the server

    Raises:
        TypeError: if server_url is not str

    """

    # Get the current time from the Binance's Server
    servertime = requests.get(server_url)
    servertimeobject = json.loads(servertime.text)
    servertime = servertimeobject["serverTime"]

    return servertime


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


def hash_content(
    content_string,
    secret_key,
    encoding_type: str = "utf-8",
    hash_method: str = "sha256",
):
    """ """

    encoded_secret = secret_key.encode(encoding_type)
    encoded_string = content_string.encode(encoding_type)
    hash_method = getattr(hashlib, hash_method)
    r_hased = hmac.new(encoded_secret, encoded_string, hash_method)

    return r_hased.hexdigest()


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


def dispatch_request(
    http_method,
    api_key,
):
    """ """

    session = requests.Session()
    session.headers.update(
        {"Content-Type": "application/json;charset=utf-8", "X-MBX-APIKEY": api_key}
    )

    r_dispatched = {
        "GET": session.get,
        "DELETE": session.delete,
        "PUT": session.put,
        "POST": session.post,
    }.get(http_method, "GET")

    return r_dispatched


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


def send_signed_request(
    http_method,
    url_path,
    payload={},
    base_url: str = "",
    api_key: str = "",
    secret_key: str = "",
):
    """ """

    query_string = urlencode(payload, True)

    if query_string:
        query_string = "{}&timestamp={}".format(query_string, get_system_timestamp())

    else:
        query_string = "timestamp={}".format(get_system_timestamp())

    url = "".join(
        [
            base_url,
            url_path,
            "?",
            query_string,
            "&signature=",
            hash_content(query_string, secret_key=secret_key),
        ]
    )

    params = {"url": url, "params": {}}
    response = dispatch_request(http_method, api_key=api_key)(**params)

    return response.json()


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


def send_public_request(
    url_path,
    payload={},
    base_url: str = "",
    api_key: str = "",
):
    """ """

    query_string = urlencode(payload, True)
    url = base_url + url_path

    if query_string:
        url = url + "?" + query_string

    response = dispatch_request("GET", api_key=api_key)(url=url)

    return response.json()
