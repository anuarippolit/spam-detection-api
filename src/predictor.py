import os, joblib

class SpamPredictor:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        models_dir = os.path.abspath(os.path.join(current_dir, "..", "models"))

        model_path = os.path.join(models_dir, "model.pkl")
        vectorizer_path = os.path.join(models_dir, "vectorizer.pkl")

        if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
            raise FileNotFoundError(
                f"ML artifacts not found in {models_dir}. Did you run your Jupyter notebook cell to export them?"
            )
        
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def predict(self, text: str) -> str:
        text_vec = self.vectorizer.transform([text])
        prediction_numeric = self.model.predict(text_vec)[0]
        return "spam" if prediction_numeric == 1 else "ham"
    
predictor = SpamPredictor()