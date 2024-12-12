# Semantic Similarity Tool

## Overview

This project implements a semantic similarity tool that computes the relationship between words based on their contextual co-occurrences in large text files. The system uses cosine similarity as the measure of closeness between word vectors built from text corpora.

The tool can be used to:

1. Build semantic word descriptors (word co-occurrence vectors) from text files.
2. Determine the most semantically similar word from a list of candidates.
3. Evaluate the system's accuracy using a test file with predefined word similarity questions.

---

## Features

1. **Semantic Descriptor Building**:

   - Processes large text files to construct word co-occurrence vectors.
   - Cleans and tokenizes sentences to ensure robust semantic relationships.

2. **Cosine Similarity**:

   - Measures the similarity between word vectors using cosine similarity.

3. **Similarity Testing**:
   - Tests the system's ability to select the correct word from a set of candidates using a test dataset.
   - Outputs the accuracy percentage.

---

## File Descriptions

- **`main.py`**: The main program containing all functions and logic.
- **Text Corpora Files**:
  - `wp.txt`, `sw.txt`, `ed.txt`, `gg.txt`, `oz.txt`: Input text files used to build the semantic descriptors. These files should contain large amounts of text.
- **`test.txt`**: A test file containing predefined word similarity questions in the following format:
  ```
  target_word correct_word choice1 choice2 choice3 ...
  ```
  Example:
  ```
  king queen prince emperor duke
  ```
- **README.md**: This documentation file.

---

## Prerequisites

To run the project, you need:

- Python 3.x
- A text editor or IDE (e.g., VSCode, PyCharm)

No additional libraries are required beyond Python's standard library.

---

## How to Run the Program

1. Place all the text corpora files (e.g., `wp.txt`, `sw.txt`) and the test file (`test.txt`) in the same directory as the program.
2. Run the script using the command line or an IDE.

### Example Usage

```bash
python synonyms.py
```

### Expected Output

The program will output the percentage of correct guesses based on the test file:

```
85.0 of the guesses were correct
```

---

## Code Description

The program is divided into the following main components:

### 1. **`norm(vec)`**

Computes the Euclidean norm of a word vector.

### 2. **`cosine_similarity(vec1, vec2)`**

Calculates the cosine similarity between two word vectors.

### 3. **`build_semantic_descriptors(sentences)`**

Builds semantic word descriptors (co-occurrence vectors) from a list of tokenized sentences.

### 4. **`build_semantic_descriptors_from_files(filenames)`**

Processes text files:

- Reads and lowercases the text.
- Splits it into sentences.
- Cleans punctuation and tokenizes words.
- Calls `build_semantic_descriptors` to generate word vectors.

### 5. **`most_similar_word(word, choices, semantic_descriptors, similarity_fn)`**

Determines the most similar word to a target word from a list of candidates using a similarity function (e.g., cosine similarity).

### 6. **`run_similarity_test(filename, semantic_descriptors, similarity_fn)`**

Runs the similarity test using a predefined test file and outputs the accuracy percentage.

---

## Test File Format (`test.txt`)

Each line in `test.txt` should follow this format:

```
target_word correct_word choice1 choice2 choice3 ...
```

- **`target_word`**: The word being compared.
- **`correct_word`**: The correct answer.
- **`choice1, choice2, ...`**: Other candidate words.

**Example**:

```
king emperor prince emperor duke
apple fruit banana fruit melon
```

---

## Example Run

Given text files `wp.txt`, `sw.txt`, etc., and a `test.txt` file:

```python
sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt", "ed.txt", "gg.txt", "oz.txt"])
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
print(res, "of the guesses were correct")
```

**Output**:

```
85.0 of the guesses were correct
```

---

## Notes

- Larger text corpora result in more accurate semantic descriptors.
- The cosine similarity function ensures that words with similar contexts have higher similarity scores.
- If a word in the test file or candidate list is missing from the descriptors, the program defaults to returning the first choice.

---

## Future Improvements

- Implement additional similarity functions (e.g., Euclidean distance).
- Include support for lemmatization and stop-word removal for better preprocessing.
- Use pre-trained word embeddings (e.g., GloVe, Word2Vec) to compare performance.

---

## Author

Kevin Peng

---

## Acknowledgments

This project is inspired by semantic similarity tools and NLP techniques commonly used in text analysis and machine learning.
