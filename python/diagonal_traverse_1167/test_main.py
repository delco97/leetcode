from diagonal_traverse_1167.main import Solution


def test_1():
    assert Solution().findDiagonalOrder(
        [[1,2,3],[4,5,6],[7,8,9]]
    ) ==[1,2,4,7,5,3,6,8,9]

def test_2():
    assert Solution().findDiagonalOrder(
        [[1,2],[3,4]]
    ) == [1,2,3,4]
