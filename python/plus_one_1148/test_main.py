from plus_one_1148.main import Solution

def test_1():
    assert Solution().plusOne(
        [1,2,3]
    ) == [1,2,4]

def test_2():
    assert Solution().plusOne(
        [4,3,2,1]
    ) == [4,3,2,2]

def test_3():
    assert Solution().plusOne(
        [9]
    ) == [1,0]

def test_4():
    assert Solution().plusOne(
        [9, 9]
    ) == [1, 0 , 0]