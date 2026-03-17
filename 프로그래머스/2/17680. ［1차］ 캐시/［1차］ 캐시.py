from collections import deque

def solution(cacheSize, cities):
    answer = 0
    lru = deque()
    for i in cities:
        i = i.lower()
        if i in lru:
            answer += 1
            lru.remove(i)
            lru.append(i)
        else:
            answer += 5
            lru.append(i)
            if len(lru) > cacheSize:
                lru.popleft()
    return answer

# def solution(cacheSize, cities):
#     answer = 0
#     lower_cities = [city.lower for city in cities]
#     x = []
#     for i in range(len(lower_cities)) :
#         if cacheSize == 0 : 
#             answer += 5
#         elif lower_cities[i] in x:
#             answer += 1   
#             x.remove(lower_cities[i])
#             x.append(lower_cities[i])
#         else :
#             answer += 5
#             if len(x) == cacheSize :
#                 x.append(lower_cities[i])
#                 x.remove(x[0])
#             else : 
#                 x.append(lower_cities[i])  
#     return answer