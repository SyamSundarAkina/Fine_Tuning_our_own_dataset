!pip install rouge-score
from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

# Calculate and print ROUGE scores for all generated outputs
for generated_output, expected_output in zip(generated_outputs, expected_outputs):
  scores = scorer.score(generated_output, str(expected_output))  # Convert expected_output to string
  print(f"Generated Output: {generated_output}")
  print(f"Expected Output: {expected_output}")
  print(f"ROUGE Scores: {scores}")
  print("-" * 20)  # Print a separator between examples