#module made to find the best matches for a question
def find_bm(question :str, base : dict) -> str:
    u_question = question
    question = question.lower()
    keys = base.keys()
    words = []
    most_match = 0
    new_match = 0
    magic_word : str
    answer  : str|bool

    for word in question:
        words.append(word)
    
    for key in keys:
        u_key = key
        key = key.lower()
        for i in words:
            if i in key:
                new_match += 1
        if new_match >= most_match:
            most_match = new_match
            magic_word = u_key
        else:
            pass
        new_match = 0
    if most_match != 0:
        answer = base[magic_word]
    else:
        answer = False
    return answer