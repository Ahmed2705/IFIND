from grades import calculate_grade

def test_excellent_grade():
    assert calculate_grade(95) == "A"

def test_good_grade():
    assert calculate_grade(85) == "B"

def test_average_grade():
    assert calculate_grade(75) == "C"

def test_passing_grade():
    assert calculate_grade(65) == "D"

def test_failing_grade():
    assert calculate_grade(45) == "F"

def test_maximum_grade():
    assert calculate_grade(100) == "A"

def test_minimum_grade():
    assert calculate_grade(0) == "F"

def test_passing_boundary():
    assert calculate_grade(60) == "D"

def test_failing_boundary():
    assert calculate_grade(59) == "F"