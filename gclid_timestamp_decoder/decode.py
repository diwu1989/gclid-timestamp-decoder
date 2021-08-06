import base64
import datetime
from . import gclid_pb2

def decode_v1(gclid):
    decoded_gclid = base64.urlsafe_b64decode(gclid + '=' * (4 - len(gclid) % 4))
    g = gclid_pb2.GClIdv1()
    g.ParseFromString(decoded_gclid)
    return g

def convert_to_dt_v1(g):
    return datetime.datetime.fromtimestamp(g.n1.n1.n1.val1 / 1000000)

def decode_v2(gclid):
    decoded_gclid = base64.urlsafe_b64decode(gclid + '=' * (4 - len(gclid) % 4))
    g = gclid_pb2.GClIdv2()
    g.ParseFromString(decoded_gclid)
    return g

def convert_to_dt_v2(g):
    return datetime.datetime.fromtimestamp(g.n1.n2.val1)

def get_timestamp_from_gclid(gclid):
    try:
        if len(gclid) > 60:
            return convert_to_dt_v2(decode_v2(gclid))
        else:
            return convert_to_dt_v1(decode_v1(gclid))
    except:
        return None

def decode_gclid(gclid):
    try:
        if len(gclid) > 60:
            return decode_v2(gclid)
        return decode_v1(gclid)
    except:
        return None