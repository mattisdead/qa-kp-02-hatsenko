from flask import Flask
from flask_restful import Api

from API.BinaryApi import BinaryApi
from API.BufferApi import BufferApi
from API.DirectoryApi import DirectoryApi
from API.LogTextApi import LogTextApi

app = Flask(__name__)
api = Api(app)

api.add_resource(BinaryApi, '/binaryfile/<string:name>')
api.add_resource(BufferApi, '/bufferfile/<string:name>')
api.add_resource(DirectoryApi, '/directory/<string:name>')
api.add_resource(LogTextApi, '/logtextfile/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
