from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    
    def predict(self, text):
    tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
    gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

    pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)

    print("Dialogue:")
    print(text)

    try:
        # Attempt to encode text using CP1252, replace invalid characters with '?'
        encoded_text = text.encode('cp1252', errors='replace')
        print("Encoded Text:")
        print(encoded_text.decode('cp1252'))  # Decode and print encoded text
    except Exception as e:
        print(f"Error encoding text: {e}")

    output = pipe(text, **gen_kwargs)[0]["summary_text"]
    
    try:
        # Attempt to encode summary using CP1252, replace invalid characters with '?'
        encoded_summary = output.encode('cp1252', errors='replace')
        print("\nEncoded Model Summary:")
        print(encoded_summary.decode('cp1252'))  # Decode and print encoded summary
    except Exception as e:
        print(f"Error encoding summary: {e}")

    return output