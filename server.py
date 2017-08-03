import astroby

from tornado import web
from tornado import httpserver
from tornado import websocket
from tornado import ioloop

from time import sleep


class BotHandler(websocket.WebSocketHandler):
    """
        bot class to control the robot
        also handles the websocket connection
    """

    def data_received(self, chunk):
        pass

    def check_origin(self, origin):
        return True

    def open(self):
        self.bot = astroby.Astroby()
        print('=' * 25)
        print('connection established')
        print('=' * 25)

    def on_close(self):
        print('closed connection')

    def on_message(self, message):
        print('incoming message: ' + message)

        self.execute_command(message)

    def execute_command(self, message):
        if message == 'forward':
            self.bot.forward()
            
        elif message == 'backward':
            self.bot.backward()
            
        elif message == 'stop':
            self.bot.stop()
            
        else:
            self.write_message('undefined command')


class Application(web.Application):
    def __init__(self):
        handlers = [(r'/bot', BotHandler)]

        web.Application.__init__(self, handlers, debug=True)


def instanciate_server():
    app = Application()
    server = httpserver.HTTPServer(app)
    server.listen(8000)
    ioloop.IOLoop.instance().start()


instanciate_server()
