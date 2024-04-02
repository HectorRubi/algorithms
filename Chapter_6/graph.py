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

  print(graph)

if __name__ == "__main__":
  main()