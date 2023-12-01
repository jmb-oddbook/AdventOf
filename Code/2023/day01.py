"""
Advent of Code
"""

# Frame for the first star
def star1(data):

    def first_last_digits(l):
        # pick out all the digits and store in a new list
        line = list(map(int, filter(lambda x: x in '123456789', l)))
   
        # first and last digits in each list element must form a two digit number
        # if there is only one digit, it is both
        return(line[0]*10 + line[-1])

    result = 0
    for line in input_data:
        result += first_last_digits(line)
    return result

# Frame for second star
def star2(data):
    # code solution here
    return data


if __name__ == "__main__":
    # data provided by AoC
    # replace the two hashes with the day 01 to 24
    input_data = open("input_data/input_d01.txt", "r")

    result = star1(input_data)
    print(f"Result for Star 1: {result}")

    result = star2(input_data)
    print(f"Result for Star 2: {result}")

