from socketIO_client import SocketIO, BaseNamespace
import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
logger = logging.Logger(__name__)

class ClientNamespace(BaseNamespace):

    def on_aaa_response(self, *args):
        logger.info('on_aaa_response', args)
        print('on_aaa_response', args)

socketIO = SocketIO('localhost', 5000)
chat_namespace = socketIO.define(ClientNamespace, '/client')

socketIO.wait(seconds=1)
