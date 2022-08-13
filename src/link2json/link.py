import http.client
import json
import hashlib


query_path = "/api/jsonBlob"
APP_JSON = 'application/json'
headers = {
    'Content-Type': APP_JSON,
    'Accept': APP_JSON
}
cached_responses = {}


def data_2_payload(data):
    return json.dumps(data)


def get_md5(payload):
    m = hashlib.md5()
    m.update(payload.encode('utf-8'))
    return m.hexdigest()


def cache_resp(payload, resp):
    cached_responses[get_md5(payload)] = resp


def get_cached(payload):
    md5 = get_md5(payload)
    if md5 in cached_responses:
        return cached_responses[md5]
    return False


def make_request(payload):
    conn = http.client.HTTPSConnection("jsonblob.com")
    conn.request("POST", query_path, payload, headers)
    res = conn.getresponse()
    conn.close()
    return res


def get_links_to_json(data):
    payload = data_2_payload(data)
    cached_resp = get_cached(payload)
    if cached_resp:
        return cached_resp
    res = make_request(payload)
    location = res.headers['location']
    resp = {
        'json': location,
        'json_ui': location.replace(query_path, '')
    }
    cache_resp(payload, resp)
    return resp


def get_link(data):
    return get_links_to_json(data)['json']


def get_ui_link(data):
    return get_links_to_json(data)['json_ui']


if __name__ == '__main__':
    pass
