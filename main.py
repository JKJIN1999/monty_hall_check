import os
import random
import argparse
import sys
sys.path.append("../MontyHallProv/")
from monti_hall import *


def main(cars, doors, show, time):
    correct, wrong = monti_hall_result(cars, doors, show, time)
    print("The situation of Monti Hall Equation shows, ")
    print("Probability of first answer being correct : {}".format(correct))
    print("Probability of changing the first answer being correct : {}".format(wrong))
    total = correct + wrong
    correct_per = str(int(correct / total * 100))
    wrong_per = str(int(wrong / total * 100))
    print(correct_per + "%")
    print(wrong_per + "%")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Proving Monti Hall Probability Equation', add_help=False)

    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Go read README')
    parser.add_argument('-d', metavar='doors',
                        help='type door amount in number', default=3, type=int)
    parser.add_argument('-c', metavar='cars',
                        help='type car amount in number', default=1, type=int)
    parser.add_argument('-s', metavar='show',
                        help='type how many door will be revealed', default=0, type=int)
    parser.add_argument('-t', metavar='time',
                        help='type how many test will be done', default=1000, type=int)
    args = parser.parse_args()
    main(cars=args.c, doors=args.d, show=args.s, time=args.t)
