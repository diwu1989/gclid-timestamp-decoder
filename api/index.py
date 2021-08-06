from http.server import BaseHTTPRequestHandler
from urllib import parse

from gclid_timestamp_decoder.decode import get_timestamp_from_gclid, decode_gclid

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        ts = None
        if "gclid" in dic:
            ts = get_timestamp_from_gclid(dic["gclid"])
            if ts is None:
                result = "invalid gclid"
            else:
                result = ts.isoformat()
        else:
            result = "Please pass in gclid query param: ?gclid=***"
        if ts is None:
            self.send_response(400)
        else:
            self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result.encode())
        return