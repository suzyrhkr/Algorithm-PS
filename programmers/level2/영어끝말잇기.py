def solution(n, words):
    answer = []
    prior = ''
    prior_words = []
    
    for i, word in enumerate(words):
        if i==0:
            prior_words.append(word)
            prior = word[-1]
            continue

        if word[0] != prior or word in prior_words:
            answer = [(i%n)+1, (i//n)+1]
            break
            
        prior_words.append(word)
        prior = word[-1]

    if not answer:
        answer = [0,0]
    
    return answer