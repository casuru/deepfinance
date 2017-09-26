#import tensorflow as tf
import argparse

parser = argparse.ArgumentParser(description = 'Give me a stock symbol to build a model on.')
parser.add_argument('symbol', metavar = 'S', type=str, help = 'a stock symbol you want a model built on')

args = parser.parse_args()

print(args.symbol)