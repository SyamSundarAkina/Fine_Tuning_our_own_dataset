!pip install nltk
import nltk
nltk.download('wordnet')  # Download WordNet for METEOR

from nltk.translate.meteor_score import meteor_score

meteor_score_value = meteor_score([expected_output.split()], generated_output.split())  # Replace with your actual outputs
print(meteor_score_value)