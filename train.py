import tensorflow as tf
import argparse
from preprocess import make_dataset

parser = argparse.ArgumentParser(description = 'Give me a stock symbol to build a model on.')
parser.add_argument('symbol', metavar = 'S', type=str, help = 'a stock symbol you want a model built on.')
parser.add_argument('trailing', metavar = 'T', type=int, default = 5, help = 'The number of previous days to model.')

args = parser.parse_args()

inputs, targets = make_dataset(args.symbol, args.trailing)

print(inputs)

num_inputs = len(inputs)

X = tf.placeholder(tf.float32, [num_inputs, args.trailing, 4])
y = tf.placeholder(tf.float32, [None])

