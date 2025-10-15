
def majority(in1, in2, in3):
    return (in1 and in2) or (in1 and in3) or (in2 and in3)


if __name__ == "__main__":
    print(majority(True, True, False))   # True
    print(majority(True, False, False))  # False
    print(majority(True, True, True))    # True
    print(majority(False, False, True))  # False
