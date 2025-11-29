import zmq
import json


total = 0

def hydration(request):
    global total
    action = request.get("action")
    amount = request.get("amount", 0)

    if action == "add":
        total += amount
        return {"message": "Added to total", "total": total}
    elif action == "get":
        return {"message": "Total for day", "total": total}
    elif action == "reset":
        total = 0
        return {"message": "Total reset", "total": 0}
    else:
        return {"message": "Error: Unknown Request"}


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5560")

    print("Hydration microservice running on port 5560...")

    while True:
        raw = socket.recv()
        request = json.loads(raw.decode())
        response = hydration(request)
        socket.send(json.dumps(response).encode())


if __name__ == "__main__":
    main()
