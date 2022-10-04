import grpc
import user_pb2
import user_pb2_grpc
import exceptions

channel = grpc.insecure_channel('localhost:65437')
stub = user_pb2_grpc.UserStub(channel)
user = user_pb2.UserData(name="", id=-1, count_trees=0)

while True:
    comand = input("Enter one of the available commands:\n1. Register\n2. Plant\n3. CutDown\n")
    if comand == "Register":
        user.name = input("\nEnter your name:")
        try:
            id = stub.Register(user).data
            user.id = id
            print("You are registered, your id = ", user.id, "\n")
        except Exception as err:
            print(err)

    elif comand == "Plant":
        try:
            print(stub.Plant(user).data, "\n")
        except Exception as err:
            print(err)
    elif comand == "CutDown":
        try:
            print(stub.CutDown(user).data, "\n")
        except Exception as err:
            print(err)