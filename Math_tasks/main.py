def test_positive():
    assert geom_Euclid_alg(150, 84) == 6, "geom_Euclid_alg(150, 84) Should be 6"
    assert geom_Euclid_alg(10, 10) == 10, "geom_Euclid_alg(10, 10) Should be 10"
    assert geom_Euclid_alg(6, 7) == 1, "geom_Euclid_alg(6, 7) Should be 1"
    assert geom_Euclid_alg(237562835, 26535) == 5, "geom_Euclid_alg(237562835, 26535) Should be 5"
    assert geom_Euclid_alg(1, 7458490) == 1, "geom_Euclid_alg(1, 7458490) Should be 1"


def test_negative():
    assert geom_Euclid_alg(0, 7) == 0, "Testing 0 faild..."
    assert geom_Euclid_alg(6, 0) == 0, "Testing 0 faild..."
    assert geom_Euclid_alg(1, 0) == 0, "Testing 0 faild..."
    assert geom_Euclid_alg(0, 0) == 0, "Testing 0 faild..."
    assert geom_Euclid_alg(0, 1) == 0, "Testing negative faild..."
    assert geom_Euclid_alg(12.12, 21) == 0, "Testing not natural faild..."
    assert geom_Euclid_alg(15.789, 0) == 0, "Testing not natural faild..."
    assert geom_Euclid_alg(15.789, 13.67) == 0, "Testing not natural faild..."  
    assert geom_Euclid_alg(-1, 167) == 0, "Testing negative faild..."
    assert geom_Euclid_alg(-1, -125) == 0, "Testing negative faild..."
    assert geom_Euclid_alg(-15, 16.7) == 0, "Testing negative and not natural faild..."


def geom_Euclid_alg(num_1:int, num_2:int) -> int:
        while num_1 > 0 and num_1 == int(num_1) and num_2 > 0  and num_2 == int(num_2):
            while num_1 > num_2:
                num_1 = num_1 - num_2 
            while num_1 < num_2:
                    num_2 = num_2 - num_1
            if num_1 == num_2:
                return num_2
        return 0


if __name__ == '__main__':
    num_1 = float(input())
    num_2 = float(input())
    answer = geom_Euclid_alg(num_1, num_2)
    print(answer)
    test_positive()
    test_negative()
    print('Everything passed')