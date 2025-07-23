import time
from fastapi import FastAPI
from devices import Device, ClimateController, AnomalyDetector, NLPProcessor
from speech_recognition import listen_for_commands
from data_storage import store_data

app = FastAPI()

light = Device("Light")
climate_controller = ClimateController()
anomaly_detector = AnomalyDetector(threshold=25)
nlp_processor = NLPProcessor()

@app.post("/control/device/")
async def control_device(device_name: str, action: str):
    if device_name.lower() == "light":
        if action.lower() == "on":
            light.turn_on()
        elif action.lower() == "off":
            light.turn_off()
        else:
            return {"error": "Invalid action"}
        return {"status": f"{device_name} {action}ed"}

def main():
    try:
        historical_data = [...]  # Historical temperature data
        climate_controller.train(historical_data)

        while True:
            command = listen_for_commands()
            if command:
                nlp_processor.process_command(command)

            sensor_reading = 32  # Simulated sensor reading
            store_data(sensor_reading, predicted_temperature)

            if anomaly_detector.detect_anomaly(sensor_reading):
                print("Anomaly detected!")

            external_temperature = 25  # External temperature reading
            predicted_temperature = climate_controller.predict(external_temperature)
            print("Predicted temperature:", predicted_temperature)

            time.sleep(5)  # Simulated sensor polling interval

    except KeyboardInterrupt:
        print("Smart home automation stopped by user")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
