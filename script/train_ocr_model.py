from transformers import TrOCRProcessor, VisionEncoderDecoderModel

# Load and fine-tune TrOCR model
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

# Add your training dataset and fine-tune the model
# Save the fine-tuned model
model.save_pretrained("./ocr_model")
processor.save_pretrained("./ocr_model")
