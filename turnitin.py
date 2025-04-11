#!/usr/bin/env python3

"""Module to compare two simplified strings."""

__author__ = 'Lydia Frame'
__date__ = '4/11/2025'


def main():
    """Prompt user for two strings, simplify them, and compare."""
    
    # Get user input and convert to lowercase
    string_one = input("String 1? ").lower()
    print()
    string_two = input("String 2? ").lower()
    print()

    # Remove commas and periods
    string_one = string_one.replace(",", "").replace(".", "")
    string_two = string_two.replace(",", "").replace(".", "")

    # Split by whitespace
    words_one = string_one.split()
    words_two = string_two.split()

    # Join words with dashes
    simplified_one = "-".join(words_one)
    simplified_two = "-".join(words_two)

    # Display simplified versions
    print(f"{string_one} simplifies to {simplified_one}")
    print(f"{string_two} simplifies to {simplified_two}")

    # Compare and report result
    if simplified_one == simplified_two:
        print("SAME")
    else:
        print("DIFFERENT")


if __name__ == '__main__':
    main()
