""" Main.py """

def inc(x_value):
    """ Increment Function adds one to the x_value"""
    return x_value + 1

def test_answer():
    """This tests the function"""
    assert inc(4) == 5
