class Device:
    def __init__(self, name, state=False):
        self.name = name
        self.state = state

    def turn_on(self):
        self.state = True
        print(f"{self.name} turned on")

    def turn_off(self):
        self.state = False
        print(f"{self.name} turned off")

class ClimateController:
    def __init__(self):
        self.model = LinearRegression()
        self.scaler = StandardScaler()

    def train(self, historical_data):
        X = [[data["external_temperature"]] for data in historical_data]
        y = [data["target_temperature"] for data in historical_data]

        # Feature scaling
        X = self.scaler.fit_transform(X)

        self.model.fit(X, y)

    def predict(self, external_temperature):
        scaled_temperature = self.scaler.transform([[external_temperature]])
        predicted_temperature = self.model.predict(scaled_temperature)
        return predicted_temperature

class AnomalyDetector:
    def __init__(self, threshold=30):
        self.threshold = threshold

    def detect_anomaly(self, sensor_reading):
        # More advanced anomaly detection methods (e.g., Isolation Forest, Autoencoders)
        if sensor_reading > self.threshold:
            return True
        return False

class NLPProcessor:
    def __init__(self):
        nltk.download("punkt")
        self.vectorizer = CountVectorizer()

    def process_command(self, command):
        tokens = word_tokenize(command)
        command_vector = self.vectorizer.transform([" ".join(tokens)])

        # More advanced NLP models (e.g., BERT, Transformers) for intent recognition
        if "turn" in tokens and "on" in tokens and "lights" in tokens:
            light.turn_on()
        elif "turn" in tokens and "off" in tokens and "lights" in tokens:
            light.turn_off()
