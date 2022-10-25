import heapq
def solution(food_times, k):
    answer = -1
    food_heap = []
    
    for i in range(len(food_times)):
        # (음식을 먹는데 걸리는 시간, 음식 번호)
        heapq.heappush(food_heap, (food_times[i], i+1))

    food_count = len(food_times)
    previous = 0    # 이전에 제거된 음식의 food_time
    
    while food_heap:
        time_to_eat = (food_heap[0][0]-previous) * food_count

        if k >= time_to_eat:
            k -= time_to_eat
            previous, _ = heapq.heappop(food_heap)
            food_count -= 1
        else:
            idx = k % food_count
            food_heap.sort(key= lambda x: x[1])
            answer = food_heap[idx][1]
            break
    return answer