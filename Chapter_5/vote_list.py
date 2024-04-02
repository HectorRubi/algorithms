def check_voter(name, voted):
  if voted.get(name):
    print('Kick them out!')
  else:
    voted[name] = True
    print('Let them vote')

def main():
  voted = {}
  check_voter('Tom', voted)
  check_voter('mike', voted)
  check_voter('mike', voted)

if __name__ == "__main__":
  main()