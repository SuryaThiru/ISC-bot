import websocket

import _thread as thread

import joypad


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print('client: closed connection')


def send_command(ws, command):
    cmd_list = ['forward', 'backward', 'right', 'left', 'stop',
                'lforward', 'lbackward', 'rforward', 'rbackward',
                'lstop', 'rstop', 'toggle_speed']

    if command in cmd_list:
        ws.send(command)
    else:
        print('undefined command')


def on_open(ws):
    def run():
        # ws.send('client: opened connection')

        joypad.run_joypad_event_loop(lambda cmd: send_command(ws, cmd))

        ws.close()
        print('thread terminating...')

    thread.start_new_thread(run, ())


def run_client(host_url):
    # websocket.enableTrace(True)

    ws = websocket.WebSocketApp(host_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    ws.run_forever()


# run_client('ws://192.168.43.114:8000/bot')
run_client('ws://192.168.1.156:8000/bot')
