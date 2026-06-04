from packages.services import Orchestrator
import sys

def main(args):
    orchestrator = Orchestrator()
    orchestrator.run()

if __name__ == '__main__':
    main(sys.argv[1:])