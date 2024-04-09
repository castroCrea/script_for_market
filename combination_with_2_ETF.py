import argparse
import math

def calculate_possibilities(target, num1, num2):

  if (num1 >= num2):
    bigger_number = num1
    smallest_number = num2
  else:
    bigger_number = num2
    smallest_number = num1

  number_of_divisions_possible = math.floor(target / bigger_number)

  all_data = []

  for i in range(number_of_divisions_possible):
    rest_after_Trim_bigger_number = target - (bigger_number * i)
    number_of_divisions_possible = math.floor(rest_after_Trim_bigger_number / smallest_number)
    rest = target - (bigger_number * i) - (smallest_number * number_of_divisions_possible)

    all_data.append([bigger_number, i, smallest_number, number_of_divisions_possible, rest])

  sorted_list = sorted(all_data, key=lambda x: x[4])

  for item in sorted_list:
    print(item[0], " x ", item[1], " + ", item[2], " x ", item[3], " -> rest ", item[4])


# Parse command-line arguments
parser = argparse.ArgumentParser(description='Calculate possibilities')
parser.add_argument('-t', '--total', type=float, help='The total amount of money', required=True)
parser.add_argument('-1', '--num1', type=float, help='Price of your first action', required=True)
parser.add_argument('-2', '--num2', type=float, help='Price of your second action', required=True)
args = parser.parse_args()

calculate_possibilities(args.target, args.num1, args.num2)

