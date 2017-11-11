import json
import heapq


def main(order_ids, max_vehicle_volume):
    # h = [(12, 'a'), (11, 'b'), (10, 'c'), (6, 'd'), (5, 'e'), (5, 'f'), (4, 'g'), (1, 'h')]
    # for order_id in given_ids:
    #     heapq.heappush(order_ids, order_id)
    order_ids.sort()
    ids = []
    coupling_ids = []
    total_volume = 0
    while order_ids:
        # tuple_val = heapq.heappop(order_ids)
        tuple_val = order_ids.pop()
        volume = tuple_val[0]
        order_id = tuple_val[1]
        total_volume = total_volume + volume
        if volume > max_vehicle_volume or total_volume == max_vehicle_volume:
            coupling_ids.append(order_id)
            ids.append(list(coupling_ids))
            coupling_ids.clear()
            total_volume = 0
        elif total_volume < max_vehicle_volume:
            coupling_ids.append(order_id)
        elif total_volume > max_vehicle_volume:
            ids.append(list(coupling_ids))
            coupling_ids.clear()
            coupling_ids.append(order_id)
            total_volume = volume
    if coupling_ids:
        ids.append(coupling_ids)
    return ids
if __name__ == '__main__':
    given_ids = [(12, 'a'), (6, 'b'), (10, 'c'), (1, 'd'), (5, 'e'), (5, 'f'), (7, 'g'), (1, 'h')]
    max_vehicle_volume = 17
    '''
    Given list of tuples(value, key)
    segregate them as group whose sum of volume should not exceed max volume.
    This a kind of bin packing problem. 
    '''
    print('Given key, value tuples are ', given_ids)
    print('max volume', max_vehicle_volume)
    ids = main(given_ids, max_vehicle_volume)
    print('groups are', ids)
