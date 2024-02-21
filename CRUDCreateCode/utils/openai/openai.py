import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

def generate_text(prompt):
    # Call the completion endpoint to generate text based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the GPT model, e.g., "text-davinci-003"
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Example usage
prompt = "Once upon a time"
generated_text = generate_text(prompt)
print(generated_text)
