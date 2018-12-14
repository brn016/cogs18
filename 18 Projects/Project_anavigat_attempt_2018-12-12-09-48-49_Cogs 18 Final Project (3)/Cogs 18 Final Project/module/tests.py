from module.funtions import my_func

assert callable(is_question)
assert isinstance(is_question('abc'), bool)
assert is_question('what?') == True

assert callable(is_question)
assert is_question('nope.') == False
assert is_question('how are you?') == True

assert callable(remove_punctuation)
assert isinstance(remove_punctuation('a'), str)
assert remove_punctuation("Hey! It's Tom!") == "Hey Its Tom"

assert callable(remove_punctuation)
assert remove_punctuation('a@b..i') == 'abi'
assert remove_punctuation('He^pp0!!!') == 'Hepp0'

assert callable(prepare_text)
assert isinstance(prepare_text('One two three.'), list)
assert prepare_text('Hi! Also, howdy.') == ['hi', 'also', 'howdy']

assert callable(prepare_text)
assert prepare_text("I'm a sentence.") == ['im', 'a', 'sentence']
assert prepare_text("j0kes, haha, oh boy.") == ['j0kes', 'haha', 'oh', 'boy']

assert callable(selector)
assert selector(['in', 'words'], ['words'], ['yes']) == 'yes'
assert selector(['in', 'words'], ['out'], ['yes']) == None

assert callable(selector)
test_out = selector(['this', 'is', 'a', 'test'], ['test'], ['out1', 'out2'])
assert test_out in ['out1', 'out2']
test_out = selector(['this', 'is', 'a', 'test'], ['vanish'], ['out1', 'out2'])
assert test_out is None

assert callable(string_concatenator)
assert isinstance(string_concatenator('hello', 'world', ' '), str)
assert string_concatenator('hello', 'world', ' ') == 'hello world'

assert callable(string_concatenator)
assert string_concatenator('yay', 'python', ' ') == 'yay python'
assert string_concatenator('other', 'test', '-') == 'other-test'

assert callable(list_to_string)
assert isinstance(list_to_string(['a', 'b'], '|'), str)
assert list_to_string(['a', 'b'], '|') == 'a|b'

assert callable(list_to_string)
assert list_to_string(['More', 'words'], ' ') == 'More words'
assert list_to_string(['and', 'again', 'aswell'], '!') == 'and!again!aswell'

assert callable(end_chat)
assert isinstance(end_chat(['a', 'b']), bool)
assert end_chat(['quit']) == True

assert callable(end_chat)
assert end_chat(['keep', 'going']) == False
assert end_chat(['yo', 'i', 'quit']) == True