def majority3(in1: bool, in2: bool, in3: bool) -> bool:
    """
    Returns True if at least two of (in1, in2, in3) are True.
    """
    return (in1 and in2) or (in1 and in3) or (in2 and in3)
