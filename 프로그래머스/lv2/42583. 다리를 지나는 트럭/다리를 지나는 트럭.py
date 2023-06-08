from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    bridge_weight= 0
    
    while bridge:
        answer += 1
        bridge_weight -= bridge.popleft()
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                bridge.append(t)
                bridge_weight += t
            else:
                bridge.append(0)
    return answer