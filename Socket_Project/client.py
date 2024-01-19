import socket
import pickle
import util_sort
import json

#the arrays that will be passed to the server

sorted_array, random_array, reversed_array = util_sort.generate_arrays()

#creating socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if(client_socket == -1):
    print("Error when creating the client socket!")
    exit(1)
client_address = ('172.22.227.56', 2345)
client_socket.connect(client_address)

#preapre data and send it to the client
data = [(sorted_array), (random_array), (reversed_array)]
serialized_data = json.dumps(data)
serialize1 = serialized_data.encode('utf-8')
try:
    client_socket.send(serialize1)
    print("Data sent successfully!")

except socket.error as e: 
    print ("Error sending data: %s" % e) 
    sys.exit(1) 

response = client_socket.recv(100500) # ~ the maximum size for sending and reciving through TCP 
final_response = json.loads(response)

result1, result2, result3 = final_response

util_sort.printings(result1, result2, result3)
client_socket.close() #closing the client socket
