import zmq
import json


def hydration_request(payload):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5560")
    socket.send(json.dumps(payload).encode())
    reply = json.loads(socket.recv().decode())
    print("Response:", reply)



hydration_request({"action": "add", "amount": 12})
hydration_request({"action": "add", "amount": 8})
hydration_request({"action": "get"})
hydration_request({"action": "reset"})
hydration_request({"action": "get"})
