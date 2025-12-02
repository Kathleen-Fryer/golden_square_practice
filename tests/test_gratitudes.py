from lib.gratitudes import *

def test_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("family")
    result = gratitudes.format()
    assert result == "Be grateful for: family"

def test_gratitudes_join():
    gratitudes = Gratitudes()
    gratitudes.add("family")
    gratitudes.add("health")
    result = gratitudes.format()
    assert result == "Be grateful for: family, health"