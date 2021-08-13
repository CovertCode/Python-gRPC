pip install grpcio
pip install grpcio-tools
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./helloworld.proto
python server.grpc.py
python client.grpc.py