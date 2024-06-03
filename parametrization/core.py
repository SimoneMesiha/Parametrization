import math


def calculate_volume(radius):
    if isinstance(radius, bool):  # very small edge case but worth considering either way to avoid application breaking
        raise TypeError("Radius must be a number, not a boolean")
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a positive number")
    if radius <= 0:
        raise ValueError("Radius must be a positive number")

    return (4 / 3) * math.pi * (radius ** 3)
