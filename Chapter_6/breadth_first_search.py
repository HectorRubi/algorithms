from collections import deque

def person_is_seller(name):
  return name[-1] == 'm'

# breadth_first_search
def search_seller(graph, head):
  # Use a queue
  search_queue = deque()

  # Add all the first grade neighbors
  search_queue += graph[head]
  
  seller = None

  # Loop queue while is not empty
  while search_queue:
    # Get first element from the queue
    person = search_queue.popleft()

    # If it's what we are looking for
    if person_is_seller(person):
      # Done
      seller = person
      break
    else:
      # Add all neighbors at the end of the queue
      search_queue += graph[person]

  return seller


def main():
  graph = {}
  graph['you'] = ['alice', 'bob', 'claire']
  graph['bob'] = ['anuj', 'peggy']
  graph['alice'] = ['peggy']
  graph['claire'] = ['thom', 'jonny']
  graph['anuj'] = []
  graph['peggy'] = []
  graph['thom'] = []
  graph['jonny'] = []

  seller = search_seller(graph, 'you')
  print(seller)

if __name__ == "__main__":
  main()
