import argparse as ap
import sys

class Cli:
    def __init__(self):
        self.parser = ap.ArgumentParser(sys.argv[0])
    
    def parse_args(self) -> dict:
        args = self.parser.parse_args(sys.argv[1:])
        return None
