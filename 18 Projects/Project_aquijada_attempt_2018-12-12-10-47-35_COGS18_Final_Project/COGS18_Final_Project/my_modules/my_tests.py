#tests
def test_is_question():
    assert isinstance(is_question(input_string), bool)

    assert is_question('what?') == True

    assert is_question('huh') == False

def test_msg_question():
    assert  isinstance(is_msg_question(input_string), bool)

    assert is_msg_question('ask a question') == True

    assert is_msg_question('draw a card') == False

def test_remv_punct():
    assert isinstance(remove_punctuation(input_string), string)

    assert remove_punctuation('h.e:ll~o~') == 'hello'

    assert remove_punctuation('i. tried. my. best.') == 'i tried my best'

def test_prepare_text():
    assert isinstance(prepare_text(input_string), list)

    assert prepare_text('HeL.lo') == 'hello'

    assert prepare_text('Smelborp.is Problems backwards!') == ['smelborp', 'is', 'problems', 'backwards']

def test_selector():
    assert isinstance(selector(return_list), string)

    assert selector(['in', 'words'], ['words'], ['yes']) == 'yes'

    assert selector(['in', 'words'], ['out'], ['yes']) == None

def test_end_chat():
    assert isinstance(end_chat(['test1', 'test2']), bool)
    
    assert end_chat(['quit']) == True
