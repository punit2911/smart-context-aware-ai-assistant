from transformers import pipeline

# Use 'text-generation' instead of 'conversational'
chat_pipeline = pipeline("text-generation", model="microsoft/DialoGPT-large")

# Function to interact with the model
def chat_with_bot(input_text):
    # Generate a response from the model
    response = chat_pipeline(input_text, max_length=150, num_return_sequences=1)
    return response[0]['generated_text']

# Test the function with a sample input
if __name__ == "__main__":
    input_text = "Hello, how are you?"
    print(chat_with_bot(input_text))



