from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

postList = [
    {
        "title": 'Title 1',
        "content": "Content 1"
    },
    {
        "title": 'Title 2',
        "content": "Content 2"
    }
]


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        dataFromClient = request.username
        print(f'Data from client: {dataFromClient}')
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.username)

    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.username)

    def GetPostList(self, request, context):
        return helloworld_pb2.PostsList(postList=postList)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
