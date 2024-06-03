import argparse
from core import calculate_volume
import argparse


def main():
    parser = argparse.ArgumentParser(description='Calculate the volume of a sphere where R is the radius')
    parser.add_argument('radius', type=float, help='Radius of the sphere')
    args = parser.parse_args()

    try:
        volume = calculate_volume(args.radius)
        print(f'The volume of the sphere is: {volume}')
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
