from python.utilities import build_nodes, to_list
from .main import Solution


def test_1():
    assert to_list(Solution().mergeNodes(build_nodes(
        [0,3,1,0,4,5,2,0]
    ))) == [4,11]

def test_2():
    assert to_list(Solution().mergeNodes(build_nodes(
        [0,1,0,3,0,2,2,0]
    ))) == [1,3,4] 