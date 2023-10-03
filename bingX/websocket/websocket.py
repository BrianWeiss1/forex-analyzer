import threading

class WebSocket(threading.Thread):
    def __init__(self, stream_url):
        threading.Thread.__init__(self)

        self._connected_event = threading.Event()
        self.stream_url = stream_url
   
    def _on_open(self, ws):
        self._connected_event.set()
        print('Connected to %s' % self.stream_url)
    
    def _on_message(self, ws, message):
        print(message)
    
    def _on_error(self, ws, error):
        print(error)
    
    def _on_close(self, ws):
        print('Connection closed')
    
    def run(self):
        pass