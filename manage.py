import base64
import hashlib
import hmac
import json
import time
from base64 import b64encode
from builtins import print
from hmac import HMAC
from urllib.parse import urlencode

import requests
from flask import Flask, current_app, request, jsonify
from flask_cors import cross_origin
from werkzeug.urls import url_encode, url_decode

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({
        "code": 0,
        "message": "success",
        "signature": '113'
    })


# app_key:1238c262556de363fcf2a347492010e1
# app_secret:acf8c6ce98750eac639532637928f5b3
app_id = 'c262556de363fcf2a347492010e1'
app_secret = 'acf8c6ce98750eac639532637928f5b3'


def sort_parms(query_str):
    """对请求参数排序"""
    parms_list = sorted([(i, v) for i, v in query_str.items()])
    return parms_list


@app.route('/auth/ximalaya', methods=['POST'])
@cross_origin()
def ximalaya():
    parm_list = sort_parms(json.loads(request.values.to_dict().get('params')))

    pre_sign = "&".join(f"{i[0]}={i[1]}" for i in parm_list)
    b64_sign = b64encode(pre_sign.encode('utf8'))

    aaa = hmac.new(app_secret.encode('utf8'), b64_sign, hashlib.sha1).digest()
    # hmac.HMAC
    xxx = hashlib.md5(aaa).hexdigest()

    return jsonify({
        "code": 0,
        "message": "success",
        "signature": xxx
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10086)
