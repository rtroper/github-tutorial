import argparse
import modules.math as math

parser = argparse.ArgumentParser()

parser.add_argument('numbers', type=float, nargs='+', help='Numbers to use in computation')
parser.add_argument('--op', choices=['add', 'sub'], type=str, help='Mathematical operation (add, sub)', default='add')

args = parser.parse_args()

result = 0
if(args.op == 'add'):
    result = math.add(args.numbers)
elif(args.op == 'sub'):
    result = math.sub(args.numbers)
else:
    result = math.add(args.numbers)

print(result)
