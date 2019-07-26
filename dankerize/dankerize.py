from random import uniform

def dankerize(string: str, upper_case_ratio=0.2) -> str:
    """
    Transform a string to lower case, and randomly set some characters
    to upper case and return the result.
        string: the string to dankerize
        upper_case_ratio: the upper_case/letter ratio
    """
    
    ret = ""
    for i in range(len(string)):
        if uniform(0, 1.0) <= upper_case_ratio:
            ret += string[i].upper()
        else:
            ret += string[i].lower()

    return ret
