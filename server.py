import grpc
from concurrent import futures
import time
import user_pb2
import user_pb2_grpc
import data_base
import exceptions

class UserServicer(user_pb2_grpc.UserServicer):
    def __init__(self) -> None:
        self.data_base = data_base.DataBase()

    def Register(self, request, context):
        if request.id != -1:
            raise exceptions.UserAlreadyRegisteredError()
        return user_pb2.ID(data=self.data_base.register(request.name))

    def Plant(self, request, context):
        return user_pb2.Message(data=self.data_base.plant(request.data))

    def CutDown(self, request, context):
        return user_pb2.Message(data=self.data_base.cutDown(request.data))


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
print('Starting server. Listening on port 65437.')
server.add_insecure_port('[::]:65437')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)