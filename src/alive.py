import falcon

from logger import Logger

class Alive(object):

    def __init__(self):
        self.ok = '{ "status": "ok", "response": ' + \
                 '[{ "status": "ok", "name": "zeta", "metadata":'
        self.failed = '{"status": "failed", "response": ' + \
                     '[{"status": "failed", "name": "zeta", "metadata":'
        self.tail = '}]}'

        log = Logger()
        self.log = log.log()

    def on_get(self,req,resp):
        resp.body = (self.ok+'"I\'m alive"'+self.tail)
        resp.status = falcon.HTTP_200
        self.log.info("Endpoint: '/alive' Method: GET Requester: '{}'"\
                        .format(req.remote_addr))
