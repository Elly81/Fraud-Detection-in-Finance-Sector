from django.shortcuts import render
from .forms import TransactionForm, UploadFileForm  # Make sure you have this form for file upload
import joblib
import pandas as pd

# Load the trained model
model_path = r'C:\Users\HP PAVILION AERO\Documents\My Project\Group Project 4\credit_card_fraud_detection_model.pkl'
model = joblib.load(model_path)

def predict_fraud(request):
    if request.method == 'POST':
        if 'manual_submit' in request.POST:
            form = TransactionForm(request.POST)
            if form.is_valid():
                # Get input data from form
                distance_from_home = form.cleaned_data['distance_from_home']
                distance_from_last_transaction = form.cleaned_data['distance_from_last_transaction']
                ratio_to_median_purchase_price = form.cleaned_data['ratio_to_median_purchase_price']
                repeat_retailer = form.cleaned_data['repeat_retailer']
                used_chip = form.cleaned_data['used_chip']
                used_pin_number = form.cleaned_data['used_pin_number']
                online_order = form.cleaned_data['online_order']
                
                # Convert categorical inputs to binary values
                repeat_retailer = 1 if repeat_retailer == 'yes' else 0
                used_chip = 1 if used_chip == 'yes' else 0
                used_pin_number = 1 if used_pin_number == 'yes' else 0
                online_order = 1 if online_order == 'yes' else 0

                # Prepare data for prediction
                input_data = [[distance_from_home, distance_from_last_transaction, ratio_to_median_purchase_price, 
                               repeat_retailer, used_chip, used_pin_number, online_order]]
                input_df = pd.DataFrame(input_data, columns=['distance_from_home', 'distance_from_last_transaction', 
                                                             'ratio_to_median_purchase_price', 'repeat_retailer', 
                                                             'used_chip', 'used_pin_number', 'online_order'])
                
                # Make prediction
                prediction = model.predict(input_df)

                result = "fraudulent" if prediction[0] == 1 else "non-fraudulent"
                return render(request, 'result.html', {'result': result})
        elif 'file_submit' in request.POST:
            upload_form = UploadFileForm(request.POST, request.FILES)
            if upload_form.is_valid():
                # Handle file upload
                file = request.FILES['file']
                df = pd.read_excel(file)
                predictions = model.predict(df)
                results = ["fraudulent" if pred == 1 else "non-fraudulent" for pred in predictions]
                df['prediction'] = results
                result_html = df.to_html()
                return render(request, 'result.html', {'result_html': result_html})

    else:
        form = TransactionForm()
        upload_form = UploadFileForm()
    return render(request, 'predict.html', {'form': form, 'upload_form': upload_form})
