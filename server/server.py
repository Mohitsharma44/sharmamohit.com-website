###
# Server to accept webhook notifications
# from github and (in-future) push to website
###

from tornado import web, ioloop

class GHHandler(web.RequestHandler):
    """
    Main class for handling post requests from github
    """
    def post(self, *args):
        print("Message received: ", self.request.body)
        print("arguments: ", [x for x in args])

settings = {}

app = web.Application(
    [(r'/ghpayload', GHHandler)],
    **settings
)

if __name__ == "__main__":
    app.listen(8888)
    ioloop.IOLoop.instance().start()
