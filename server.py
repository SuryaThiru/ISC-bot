import astroby

from tornado import web
from tornado import httpserver
from tornado import websocket
from tornado import ioloop


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
        # control for the wheels together
        if message == 'forward':
            self.bot.forward()

        elif message == 'backward':
            self.bot.backward()

        elif message == 'stop':
            self.bot.stop()

        elif message == 'left':
            self.bot.left()

        elif message == 'right':
            self.bot.right()

        # control for wheel sets
        elif message == 'lforward':
            self.bot.LW_forward()

        elif message == 'lbackward':
            self.bot.LW_backward()

        elif message == 'lstop':
            self.bot.LW_stop()

        elif message == 'rforward':
            self.bot.RW_forward()

        elif message == 'rbackward':
            self.bot.RW_backward()

        elif message == 'rstop':
            self.bot.RW_stop()

        elif message == 'toggle_speed':
            self.bot.toggle_speed()

        else:
            self.write_message('server: undefined command')


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
