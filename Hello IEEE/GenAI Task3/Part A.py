
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Tokenization isn't always predictable, unbelievably"
encoded = tokenizer(text)
tokens = tokenizer.convert_ids_to_tokens(encoded["input_ids"])

print("Text: ", text)
print("Tokens:", tokens)
print("IDs: ", encoded["input_ids"])
print("Mask: ", encoded["attention_mask"])

my_text = "Xochitl deployed the kubernetes cluster before lunch"
my_encoded = tokenizer(my_text)
my_tokens = tokenizer.convert_ids_to_tokens(my_encoded["input_ids"])

print("\nText: ", my_text)
print("Tokens:", my_tokens)
print("IDs: ", my_encoded["input_ids"])
print("Mask: ", my_encoded["attention_mask"])

