# test_model_loading.py

# Import your model class
# test_model_loading.py
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carprediction.settings")
import django
django.setup()

from carapp.ml_model import CarPricePredictionModel  # Import the model class


# Define the model file path
model_file_path = 'carprediction\carapp\Models\Car_Price_Model.pkl'  # Update with the correct file path

# Load the model
car_price_predictor = CarPricePredictionModel(model_file_path)

# Example input data for testing
input_data = [[2014,1345678,5000,'Petrol','Dealer','Manual']]

# Make predictions and print the result
predictions = car_price_predictor.predict(input_data)
print("Predicted Prices:", predictions)