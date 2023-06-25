from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer

model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill", hub_token='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')
tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill", hub_token='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')

def generate_response(input_text):
    # tokenize the text
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')
    
    # generate a response
    response_ids = model.generate(input_ids, max_length=1000, num_beams=5, no_repeat_ngram_size=2)
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    
    return response_text

def main():
    while True:
        # prompt the user for input
        user_input = input('User: ')
        
        # generate a response
        response = generate_response(user_input)
        
        # print the response
        print('Bot: ' + response)

if __name__ == "__main__":
    main()