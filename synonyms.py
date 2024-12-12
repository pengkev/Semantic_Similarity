import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):
    if norm(vec1) == 0 or norm(vec2) == 0:
        return 0
    
    numerator = 0
    for i in vec1.keys():
        if i in vec2:
            numerator += vec1[i] * vec2[i]
    return numerator / (norm(vec1) * norm(vec2))

def build_semantic_descriptors(sentences):
    semantic_descriptors = {}
    
    for sentence in sentences:
        unique_words = set(sentence)

        for word in unique_words:
            if word not in semantic_descriptors:
                semantic_descriptors[word] = {}
            for other_word in unique_words:
                if word != other_word:
                    if other_word in semantic_descriptors[word]:
                        semantic_descriptors[word][other_word] += 1
                    else:
                        semantic_descriptors[word][other_word] = 1

    return semantic_descriptors

def build_semantic_descriptors_from_files(filenames):
    import re
    
    sentences = []
    for filename in filenames:
        with open(filename, "r", encoding="latin1") as f:
            text = f.read().lower()
            split_sentences = re.split(r"[.!?]", text)
            for sentence in split_sentences:
                cleaned_sentence = re.sub(r"[,\-–:;]", " ", sentence).strip()
                words = cleaned_sentence.split()
                if words:
                    sentences.append(words)
    return build_semantic_descriptors(sentences)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    if word not in semantic_descriptors:
        return choices[0]

    similarity = 0
    pos = 0
    for i in range(len(choices)):
        if choices[i] not in semantic_descriptors:
            val = -1 
        else:
            val = similarity_fn(semantic_descriptors[word], semantic_descriptors[choices[i]])
        if val > similarity:
            similarity = val
            pos = i
    if similarity > 0:        
        return choices[pos]
    else:
        return choices[0]

        
def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    f = open(filename, "r", encoding="latin1")
    tguesses, cguesses = 0, 0
    for line in f:
        if not line.strip():
            continue
        tguesses += 1
        if most_similar_word(line.split()[0], line.split()[2:], semantic_descriptors, similarity_fn) == line.split()[1]:
            cguesses += 1

    return cguesses / tguesses * 100

sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt","ed.txt","gg.txt","oz.txt"])
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
print(res, "of the guesses were correct")