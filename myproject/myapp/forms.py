from django import forms

class TransactionForm(forms.Form):
    distance_from_home = forms.FloatField(label='Distance from Home in (miles)')
    distance_from_last_transaction = forms.FloatField(label='Distance from Last Transaction in (miles)')
    purchase_price = forms.FloatField(label='Purchase Price in (Tsh)')
    median_purchase_price = forms.FloatField(label='Median Purchase Price in (Tsh)')
    repeat_retailer = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label='Repeat Retailer')
    used_chip = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label='Used Chip')
    used_pin_number = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label='Used Pin Number')
    online_order = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label='Online Order')
    ratio_to_median_purchase_price = forms.FloatField(label='Ratio of Purchase Price to Median Purchase Price', required=False)

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Upload Excel File')
