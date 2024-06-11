# Identity Theft and Fraud Detection System

## Overview

This project implements an Identity Theft and Fraud Detection System for the finance sector using the Random Forest algorithm. The system aims to detect fraudulent activities and identity theft in financial transactions, providing a reliable and efficient solution to enhance security.


## Objectives

- Detect fraudulent transactions in real-time
- Use Random Forest for robust classification
- High accuracy and low false-positive rate
- Scalable and adaptable to various financial environments

## Dataset

The dataset used for training and testing the model contains the following features:

1. **distance_from_home**:
   - **Fraud Prediction**: Higher values. Transactions far from the cardholder's home could indicate unauthorized use.
   - **Non-Fraud Prediction**: Lower values. Transactions close to home are more likely to be legitimate.

2. **distance_from_last_transaction**:
   - **Fraud Prediction**: Higher values. Large distances between successive transactions might suggest unusual activity.
   - **Non-Fraud Prediction**: Lower values. Smaller distances are typical for regular usage patterns.

3. **ratio_to_median_purchase_price**:
   - **Fraud Prediction**: Significant deviation (either much higher or lower). Fraudulent transactions often involve unusually large or small amounts compared to typical spending.
   - **Non-Fraud Prediction**: Values close to 1. Transactions within the normal range of spending.

4. **repeat_retailer**:
   - **Fraud Prediction**: 0 (no). Transactions at new retailers could indicate fraudulent activity.
   - **Non-Fraud Prediction**: 1 (yes). Transactions at familiar retailers are more likely to be genuine.

5. **used_chip**:
   - **Fraud Prediction**: 0 (no). Transactions not using a chip might be less secure and thus more prone to fraud.
   - **Non-Fraud Prediction**: 1 (yes). Chip transactions are typically more secure and less likely to be fraudulent.

6. **used_pin_number**:
   - **Fraud Prediction**: 0 (no). Transactions without a PIN might be less secure.
   - **Non-Fraud Prediction**: 1 (yes). PIN usage adds a layer of security.

7. **online_order**:
   - **Fraud Prediction**: 1 (yes). Online transactions have a higher risk of fraud due to less stringent verification.
   - **Non-Fraud Prediction**: 0 (no). In-person transactions are generally more secure.

8. **fraud**:
   - This is the target variable that indicates the outcome. The analysis of the above features helps to predict this variable.

## Model

The model is built using the Random Forest algorithm, which is an ensemble learning method for classification. It operates by constructing multiple decision trees and outputs the mode of the classes as the prediction.


## Results

The Random Forest model achieves high accuracy and low false-positive rates in detecting fraudulent transactions.


## Contact

For any questions or inquiries, please contact:

- **ELIUD SIMON**
- **Email:** kikotaeliud@gmail.com
- **GitHub:** [Elly81](https://github.com/Elly81)

---

Thank you for using our Identity Theft and Fraud Detection System! We hope it helps in making financial transactions safer and more secure.
