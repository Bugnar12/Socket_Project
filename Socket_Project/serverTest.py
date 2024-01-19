import socket
import os
import pickle
import random
import util_sort
import time
import json

def client_handler(client_socket):
    # Sort each array with one method and see which is the most efficient one

    # Recieve the arrays from the client
    try:
        data = client_socket.recv(1048500)
    except ConnectionResetError:
        print("Client disconnected")
        client_socket.close()
        os._exit(0)

    
    array_data = json.loads(data)

    array1, array2, array3 = array_data[0], array_data[1], array_data[2]  # sorted, random, reverse

    print("A new client has connected to the server !")

    #array1 - the sorted one
    nr_steps1_1 = util_sort.bubble_sort(array1)
    nr_steps1_2 = util_sort.merge_sort(array1)
    aux_arr1, nr_steps1_3 = util_sort.recursive_selection_sort(array1)

    # array2 - the random one
    nr_steps2_1 = util_sort.bubble_sort(array2)
    nr_steps2_2 = util_sort.merge_sort(array2)
    aux_arr2, nr_steps2_3 = util_sort.recursive_selection_sort(array2)

    # array3 - the reverse one
    nr_steps3_1 = util_sort.bubble_sort(array3)
    nr_steps3_2 = util_sort.merge_sort(array3)
    aux_arr3, nr_steps3_3 = util_sort.recursive_selection_sort(array3)

    # return all the nr. of steps to the client
    response = [[nr_steps1_1, nr_steps2_1, nr_steps3_1], [nr_steps1_2, nr_steps2_2, nr_steps3_2],
                [nr_steps1_3, nr_steps2_3, nr_steps3_3]]
    serialize1 = json.dumps(response)
    serialized_response = serialize1.encode('utf-8')

    try:
        name = socket.gethostname()
        ip_name = socket.gethostbyname(name)
        print(f"Data will be sent to the client with ip {ip_name} after a short delay.")

        time.sleep(5) #the concurrency is better observed
        client_socket.send(serialized_response)
    except BrokenPipeError:
        print("Client disconnected")
        client_socket.close()

    client_socket.close() #close the socket
    os._exit(0) #exit the child process


#---The actual server---


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if(server_socket == -1):
    print("Error creating socket")
    exit(1) #exit(0) -> success ; exit(1) -> failure in program execution
else:
    server_address = ('172.22.227.56', 2345)
    server_socket.bind(server_address)

    server_socket.listen(5)
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection accepted from ip {client_address[0]} with the port {client_address[1]}")

        pid = os.fork()

        #If child process -> we handle the sortings
        if pid == 0:
            client_handler(client_socket)
        #Else parent process -> we wait for more clients to connect so the child can handle them
