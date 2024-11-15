import heapq
inp_number = int(input())

time_list = []
for i in range(inp_number):
    _, start, end = map(int, input().split())
    time_list.append((start,end))
time_list.sort(key=lambda x: x[0])
heap = []
heapq.heapify(heap)
answer = 0
for start, end in time_list:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    else:
        answer +=1
    heapq.heappush(heap, end)

print(answer)
