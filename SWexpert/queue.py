N = 10
Q = [-1] * N
front = rear = -1


def enqueue(item):
    global rear
    # if rear==N-1:
    #     rear=0
    # else:
    #     rear += 1
    rear = (rear + 1) % N
    Q[rear] = item


def dequeue():
    global front

    front = (front + 1) % d
    return Q[front]
