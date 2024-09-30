import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import read_data, get_list_k, get_first, get_last, get_max, get_min, get_sum

FILENAME = "listes.csv"

@pytest.fixture(scope="module")
def setup():
    """
    fonction de test
    """
    try:
        data = read_data(FILENAME)
    except:
        data = []
    return data

listes = [
[90, 83, 36, 39, 74, 45, 77, 62, 41, 35],
[82, 39, 34, 63, 64, 91, 50, 42, 53, 66],
[56, 42, 62, 35, 50, 44, 37, 47, 92, 39],
[33, 58, 94, 46, 67, 55, 66, 90, 71, 96],
[97, 95, 67, 60, 86, 48, 90, 99, 53, 47],
[45, 51, 64, 74, 82, 36, 39, 44, 53, 68],
[82, 58, 86, 40, 83, 88, 89, 87, 50, 37],
[41, 34, 79, 51, 38, 82, 64, 65, 68, 81],
[63, 90, 55, 56, 75, 96, 89, 72, 82, 41],
[84, 83, 55, 36, 52, 90, 46, 71, 78, 64],
[37, 77, 46, 40, 62, 51, 96, 76, 53, 69],
[69, 68, 90, 98, 45, 70, 73, 85, 40, 50],
[37, 44, 36, 33, 68, 45, 83, 56, 80, 71],
[98, 91, 50, 36, 95, 61, 54, 47, 82, 99],
[51, 93, 95, 82, 84, 34, 42, 47, 85, 38],
[37, 65, 84, 50, 82, 72, 57, 42, 60, 49],
[74, 80, 48, 60, 37, 44, 81, 63, 65, 47],
[52, 58, 74, 78, 40, 85, 41, 64, 47, 73],
[71, 34, 47, 58, 57, 66, 35, 93, 94, 77],
[58, 79, 35, 70, 65, 89, 39, 54, 98, 62],
[48, 67, 53, 83, 58, 59, 74, 66, 98, 94],
[60, 36, 73, 88, 39, 94, 53, 54, 51, 76],
[41, 86, 89, 37, 72, 58, 77, 93, 70, 44],
[46, 48, 54, 52, 41, 65, 35, 53, 62, 43],
[77, 71, 95, 47, 40, 55, 76, 66, 52, 36],
[78, 50, 66, 56, 44, 91, 75, 85, 47, 59],
[53, 38, 74, 36, 86, 52, 57, 54, 77, 49],
[58, 85, 65, 61, 39, 71, 99, 86, 83, 49],
[43, 49, 54, 36, 38, 35, 62, 96, 85, 63],
[64, 43, 72, 52, 63, 77, 56, 35, 98, 88],
[36, 86, 81, 58, 79, 35, 76, 99, 37, 40],
[45, 62, 70, 68, 75, 37, 87, 93, 78, 86],
[34, 96, 70, 51, 38, 65, 46, 33, 77, 80],
[36, 81, 90, 76, 35, 58, 38, 86, 88, 70],
[81, 60, 35, 71, 96, 64, 38, 70, 61, 89],
[87, 93, 34, 38, 51, 39, 92, 86, 50, 66],
[93, 60, 79, 55, 51, 37, 38, 41, 98, 68],
[71, 84, 98, 81, 46, 67, 45, 56, 70, 47],
[68, 99, 59, 34, 42, 53, 70, 40, 82, 86],
[53, 73, 52, 69, 79, 72, 62, 94, 88, 67],
[91, 77, 41, 83, 40, 99, 93, 48, 36, 79],
[53, 97, 96, 62, 92, 58, 93, 48, 50, 78],
[65, 52, 70, 56, 49, 58, 34, 69, 95, 43],
[46, 76, 72, 78, 80, 47, 75, 65, 81, 94],
[41, 55, 86, 87, 66, 95, 88, 36, 96, 52],
[91, 56, 54, 92, 59, 77, 95, 37, 78, 57],
[62, 95, 52, 43, 67, 63, 41, 61, 46, 87],
[69, 64, 38, 65, 87, 63, 98, 62, 73, 92],
[66, 95, 65, 46, 68, 35, 49, 82, 58, 64],
[41, 52, 61, 57, 74, 93, 56, 80, 37, 60],
[38, 70, 62, 58, 84, 76, 79, 57, 42, 94],
[79, 76, 63, 39, 51, 56, 95, 73, 53, 88],
[57, 66, 82, 94, 36, 92, 83, 99, 62, 37],
[61, 37, 55, 59, 96, 94, 86, 98, 81, 64],
[49, 60, 54, 39, 48, 61, 78, 85, 82, 57],
[85, 72, 89, 86, 55, 57, 50, 46, 35, 40],
[76, 50, 82, 79, 75, 78, 96, 98, 55, 73],
[68, 80, 57, 59, 78, 97, 54, 73, 40, 74],
[90, 38, 89, 33, 71, 48, 66, 93, 65, 57],
[33, 78, 66, 34, 77, 68, 50, 70, 81, 79],
[49, 52, 70, 50, 91, 34, 82, 36, 42, 90],
[35, 84, 79, 75, 70, 86, 58, 43, 62, 34],
[65, 57, 90, 94, 96, 63, 82, 45, 49, 77],
[75, 78, 33, 56, 97, 55, 69, 85, 89, 47],
[45, 47, 84, 43, 88, 97, 91, 92, 67, 34],
[95, 93, 56, 88, 34, 41, 46, 62, 89, 49],
[71, 62, 78, 68, 48, 63, 59, 73, 87, 35],
[71, 39, 80, 78, 67, 76, 94, 79, 34, 77],
[34, 33, 93, 43, 77, 67, 57, 44, 62, 41],
[94, 78, 54, 85, 71, 41, 77, 69, 63, 59],
[41, 71, 62, 50, 67, 84, 55, 73, 97, 65],
[45, 85, 55, 40, 81, 87, 75, 43, 44, 79],
[54, 86, 82, 45, 61, 87, 43, 67, 72, 85],
[37, 56, 44, 47, 71, 95, 58, 70, 81, 35],
[36, 75, 79, 76, 54, 58, 33, 50, 65, 37],
[78, 88, 68, 80, 99, 81, 93, 53, 76, 66],
[65, 79, 73, 55, 90, 98, 87, 84, 85, 64],
[41, 91, 61, 59, 39, 66, 54, 57, 84, 55],
[94, 89, 44, 49, 82, 83, 87, 79, 80, 63],
[36, 34, 87, 66, 69, 39, 52, 92, 38, 74],
[89, 99, 61, 71, 93, 72, 87, 40, 80, 64],
[72, 53, 74, 81, 93, 49, 83, 59, 86, 95],
[45, 95, 51, 62, 83, 50, 74, 70, 41, 92],
[92, 85, 84, 36, 72, 98, 59, 75, 97, 33],
[63, 96, 84, 99, 79, 76, 98, 77, 55, 80],
[35, 77, 86, 98, 79, 64, 63, 38, 69, 54],
[86, 85, 99, 38, 43, 64, 93, 61, 78, 89],
[88, 81, 47, 61, 71, 54, 43, 60, 92, 89],
[62, 60, 78, 94, 41, 33, 90, 44, 91, 63],
[74, 70, 84, 92, 81, 85, 38, 65, 62, 48],
[36, 41, 58, 65, 87, 51, 92, 55, 60, 83],
[50, 78, 54, 47, 77, 61, 44, 93, 85, 71],
[79, 87, 47, 54, 51, 65, 99, 85, 46, 36],
[53, 95, 61, 69, 74, 94, 49, 88, 47, 44],
[42, 81, 41, 40, 77, 47, 33, 44, 35, 67],
[78, 77, 48, 87, 84, 50, 68, 70, 39, 38],
[59, 87, 84, 62, 58, 49, 34, 94, 51, 92],
[68, 78, 92, 47, 56, 86, 94, 90, 35, 38],
[75, 72, 95, 89, 92, 94, 54, 43, 37, 78],
[90, 41, 34, 80, 84, 89, 65, 67, 63, 64],
]


indices = [0, 1, 2, 16, 17, 30, 31, 55, 63, 68, 74, 81, 85, 91, 95, 98, 99]

input_output = []
for k in indices:
    input_output.append((k, listes[k]))
@pytest.mark.parametrize("input,expected", input_output)
def test_read_data(input, expected):
    """
    fonction de test
    """
    assert read_data(FILENAME)[input] == expected, input


@pytest.mark.parametrize("input,expected", input_output)
def test_get_list_k(setup, input, expected):
    """
    fonction de test
    """
    data = setup
    assert get_list_k(data, input) == expected, input


input_output = [ (0, 90), (1, 82), (2, 56), (16, 74), (17, 52), (30, 36), (31, 45), (55, 85), (63, 75),
                 (68, 34), (74, 36), (81, 72), (85, 35), (91, 50), (95, 78), (98, 75), (99, 90)]

@pytest.mark.parametrize("input,expected", input_output)
def test_get_first(setup, input, expected):
    """
    fonction de test
    """
    data = setup
    assert get_first(data[input]) == expected, input


input_output = [ (0, 35), (1, 66), (2, 39), (16, 47), (17, 73), (30, 40), (31, 86), (55, 40), (63, 47),
                 (68, 41), (74, 37), (81, 95), (85, 54), (91, 71), (95, 38), (98, 78), (99, 64)]

@pytest.mark.parametrize("input,expected", input_output)
def test_get_last(setup, input, expected):
    """
    fonction de test
    """
    data = setup
    assert get_last(data[input]) == expected, expected


input_output = [ (0, 90), (1, 91), (2, 92), (16, 81), (17, 85), (30, 99), (31, 93), (55, 89), (63, 97),
                 (68, 93), (74, 79), (81, 95), (85, 98), (91, 93), (95, 87), (98, 95), (99, 90)]

@pytest.mark.parametrize("input,expected", input_output)
def test_get_max(setup, input, expected):
    """
    fonction de test
    """
    data = setup
    assert get_max(data[input]) == expected, expected


input_output = [ (0, 35), (1, 34), (2, 35), (16, 37), (17, 40), (30, 35), (31, 37), (55, 35), (63, 33),
                 (68, 33), (74, 33), (81, 49), (85, 35), (91, 44), (95, 38), (98, 37), (99, 34)]

@pytest.mark.parametrize("input,expected", input_output)
def test_get_min(setup, input, expected):
    """
    fonction de test
    """
    data = setup
    assert get_min(data[input]) == expected, expected


input_output = [ (0, 582), (1, 584), (2, 504), (16, 599), (17, 612), (30, 627), (31, 701), (55, 615), (63, 684),
                 (68, 551), (74, 563), (81, 745), (85, 663), (91, 660), (95, 639), (98, 729), (99, 677)]

@pytest.mark.parametrize("input,expected", input_output)
def test_get_sum(setup, input, expected):
    """
    fonction de test
    """
    data = setup
    assert get_sum(data[input]) == expected, expected

