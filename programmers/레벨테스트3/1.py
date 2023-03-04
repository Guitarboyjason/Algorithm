import heapq
def solution(operations):
    answer = []
    queue = list()
    for operation in operations:
        operation,number = operation.split()
        if operation == "I":
            heapq.heappush(queue,int(number))
        if operation == "D":
            if not len(queue):
                continue
            if number == "-1":
                heapq.heappop(queue)
            else:
                queue = [-i for i in queue]
                heapq.heapify(queue)
                heapq.heappop(queue)
                queue = [-i for i in queue]
                heapq.heapify(queue)
    if len(queue)>1:
        min_value = heapq.heappop(queue)
        queue = [-i for i in queue]
        heapq.heapify(queue)
        max_value = -heapq.heappop(queue)
        answer = [max_value,min_value]
    elif len(queue):
        value = heapq.heappop(queue)
        answer = [value,value]
    else:
        answer = [0,0]
    return answer
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))
