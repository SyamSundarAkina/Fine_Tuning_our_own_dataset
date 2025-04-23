!pip install nltk  # Install NLTK if you haven't already
import nltk
from nltk.translate.bleu_score import sentence_bleu

bleu_scores = []
for generated, expected in zip(generated_outputs, expected_outputs):
    # Convert 'expected' to a string before splitting
    bleu_score = sentence_bleu([str(expected).split()], generated.split())  # Calculate BLEU score
    bleu_scores.append(bleu_score)

average_bleu = sum(bleu_scores) / len(bleu_scores)
print(f"Average BLEU score: {average_bleu}")