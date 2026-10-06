from golden_square.testing_bites.lib.gratitudes import *

def test_gratitudes_list():
    gratitudes = Gratitudes()
    gratitudes.add("Michael")
    assert gratitudes.gratitudes == ["Michael"]
    gratitudes.add("Michael 2")
    assert gratitudes.gratitudes == ["Michael", "Michael 2"]
    gratitudes.add("Michael 3")
    assert gratitudes.gratitudes == ["Michael", "Michael 2", "Michael 3"]

def test_gratitudes_format():
    gratitudes = Gratitudes()
    gratitudes.add("Michael")
    assert gratitudes.format() == "Be grateful for: Michael"
    gratitudes.add("Michael 2")
    assert gratitudes.format() == "Be grateful for: Michael, Michael 2"
    gratitudes.add("Michael 3")
    assert gratitudes.format() == "Be grateful for: Michael, Michael 2, Michael 3"