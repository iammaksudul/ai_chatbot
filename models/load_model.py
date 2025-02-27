from transformers import GPTNeoForCausalLM, GPT2Tokenizer

# Load the GPT-Neo model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-2.7B")

def generate_response(input_text):
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=512, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response