from src.textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        self.model_path = Path(self.config.model_path)
        self.tokenizer_path = Path(self.config.tokenizer_path)

    def is_ready(self) -> bool:
        return self.model_path.exists() and self.tokenizer_path.exists()

    def predict(self, text: str):
        # if not self.is_ready():
        #     raise FileNotFoundError(
        #         "Model artifacts are not available. Train the model pipeline first."
        #     )

        tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.model_path)

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