from socketIO_client import SocketIO, BaseNamespace
import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class ClientNamespace(BaseNamespace):
    def on_connect(self):
        logger.info('[Connected]')

    def on_reconnect(self):
        logger.info('[Reconnected]')

    def on_disconnect(self):
        logger.info('[Disconnected]')

    def on_aaa(self, *args):
        logger.info('on_aaa ' + str(args))

socketIO = SocketIO('localhost', 5000)
chat_namespace = socketIO.define(ClientNamespace, '/client')

socketIO.wait(seconds=1)
