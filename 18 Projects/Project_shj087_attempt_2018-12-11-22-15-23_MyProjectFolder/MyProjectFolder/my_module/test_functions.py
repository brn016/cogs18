from functions import getFrequency, findSummary

# test getFrequency
assert getFrequency([]) == {}
assert getFrequency([',','happy']) == {'happy': 1}
assert getFrequency(['happy','happy','like','coding','the']) == {'coding': 0.25, 'like': 0.25, 'happy': 0.5}

# test findSummary
text = "Coding can help to approach something interesting. I finish this task by coding. It is so interesting!"
findSummary(1, text) == ["Coding can help to approach something interesting."]