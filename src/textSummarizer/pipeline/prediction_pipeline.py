from src.textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text: str):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)

        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512).to(device)
        generated_ids = model.generate(
            **inputs,
            length_penalty=0.8,
            num_beams=8,
            max_length=128,
            early_stopping=True,
        )
        output = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

        print("Dialogue:")
        print(text)
        print("\nModel Summary:")
        print(output)

        return output