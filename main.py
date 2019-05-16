from data_loader import Loader
from data_prepare import Prepare

def main():
  loader = Loader()
  prepare = Prepare()

  data = loader.load_csv('dataset')
  prepare.prepare(data)
  print(data)
if __name__ == "__main__":
  main()