"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json

from queue import *
# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.
    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = json.load(urlopen(req, jsondataasbytes))
    return response

def bfs(start, end):
    rooms = []
    actions = []
    end_tile = ((None,  None))
    q = Queue()
    q.put((start , None))
    while(q.qsize() > 0):
        u = q.get()
        for room in get_state(u[0]['id'])['neighbors']:
            if room not in rooms:
                if room['id'] == end['id']:
                    print("reached")
                    end_tile = u
                rooms.append(room)
                q.put((room, u))
    while (end_tile[1] is not None):
        actions.append(transition_state(end_tile[1][0]['id'], (end_tile[0])['id']))
        end_tile = end_tile[1]
    actions.reverse()
    actions.append(transition_state(actions[len(actions)-1]['id'], end['id']))
    return actions
def dikjstra(start, end):
    parents = {}
    dist = {}
    dist[start['id']] = 0
    parents[start['id']] = None
    actions = []
    q = PriorityQueue()
    q.put((0, start['id']))
    v = None
    visited = []
    for v in get_state(start['id'])['neighbors']:
        if v['id'] is not start['id']:
            dist[v['id']] = 0
            parents[v['id']] = None
        q.put((dist[v['id']], v['id']))
    while(q.qsize() > 0):
        u = q.get()
        for room in get_state(u[1])['neighbors']:
            if room['id'] not in dist:
                dist[room['id']] = 10000000
            if(room['id'] in visited):
                continue
            alt = u[0] + transition_state(u[1],room['id'])['event']['effect']
            print(alt)
            if alt > dist[room['id']] and room['id'] not in visited:
                dist[room['id']] = alt
                parents[room['id']] = u[1]
                q.put((alt, room['id']))
                visited.append(room['id'])
                #print(visited)
    room = end
    while (parents[room['id']] is not None):
        actions.append(transition_state(parents[room['id']], room['id']))
        room = get_state(parents[room['id']])
    actions.reverse()
    return actions
if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    dark_room = get_state('f1f131f647621a4be7c71292e79613f9') 
    #print(empty_room)
    #print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
    
    bfs_result = bfs(empty_room, dark_room)
    bfs_hp = 0
    for action in bfs_result:
        bfs_hp += action['event']['effect']
        print(action)
    print("Total HP: "+ str(bfs_hp))
    
#    dij_result = dikjstra(empty_room, dark_room)


