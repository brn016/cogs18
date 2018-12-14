def test_direction():
    assert direction_prompt() == None #function doesn't return any value, it just executes a conditional with the given input
    assert direction_prompt("saloon") == None
    assert direction_prompt("wilderness") == None
    assert direction_prompt("town") == None
#really, none of my defined functions returned any values.