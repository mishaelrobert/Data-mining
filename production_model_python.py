##################################################################################
###  Production example: from Orange3 workflow to a runnable Python script     ###
##################################################################################

import Orange
from Orange.data import Table, Domain
from Orange.preprocess import Normalize
import pickle


### 1. Data import
# filename: "emplpyee_attrition_test.csv"
data = Table('C:/Users/tomask/OneDrive for Business/מדעים/DataMining/emplpyee_attrition_test.csv')

### 2. Preprocess
# Normalize features: Normalize to interval [0,1]
normalizer = Normalize(zero_based=True,norm_type=Normalize.NormalizeBySpan)
normalized_data = normalizer(data)

### 3. Load Model
# filename: "production_model_example.pkcls"
with open("C:/Users/tomask/OneDrive for Business/מדעים/DataMining/production_model_example.pkcls", "rb") as f:
    model = pickle.load(f)

### 5. Predictions
pred_ind = model(normalized_data)  # array of predicted target values (indices)
#[model.domain.class_var.str_val(i) for i in pred_ind]  # convert to value names (strings)
prob = model(normalized_data, model.Probs)  # array of predicted probabilities

### 6. Select Columns
# remove all, leave only "Logistic Regression (Yes)" and "Logistic Regeression"


### 7. Save Data
#probability = Orange.data.variable.Continuous(prob)
#prediction = Orange.data.feature.Discrete(pred_ind)
#probability = Orange.data.Variable(prob)
#prediction = Orange.data.Variable(pred_ind.any())
#Domain = Orange.data.Domain([prob,pred_ind])

#df.probability = prob[:,1]
#df.prediction = pred_ind
#Table = Orange.data.Table([df.probability,df.prediction])
#Table.domain = df.domain

Table = Orange.data.Table([prob[:,1],pred_ind])

# filename: "hrm-employee-attrition_results.csv"
Table.save('C:/Users/tomask/OneDrive for Business/מדעים/DataMining/NewTable.tab')





