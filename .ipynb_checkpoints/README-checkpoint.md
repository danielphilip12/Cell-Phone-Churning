# Cell-Phone-Churning

## Problem Statement
- This dataset contains customer information about their cell phone plan usage, such as the number of calls made, account length, customer service calls, etc. 

- The purpose of this analysis and model is to predict whether a customer will churn (stop their plan) or stay. 

## Data Dictionary

| Column Name | Description |
|-------------|-------------|
| account_length|  amount of time the customer has had an account | 
| vmail_message |     number of voicemail messages a customer has | 
| day_mins   |        how many minutes calls lasted during the daytime | 
| day_calls  |        number of calls in the daytime| 
| day_charge  |       charges accumulated during the daytime| 
| eve_mins    |       how many minutes calls lasted during the evening| 
| eve_calls    |       number of calls in the evening| 
| eve_charge  |       charges accumulated during the evening| 
| night_mins  |        how many minutes calls lasted during the night| 
| night_calls |        number of calls in the night| 
| night_charge  |     charges accumulated during the night| 
| intl_mins     |      how many minutes for international calls | 
| intl_calls   |       number of calls internationally | 
| intl_charge   |     charges for international calls| 
| custserv_calls |    number of customer service calls | 
| churn          |    did the customer churn or not | 

## Executive Summary

### Data Cleaning Steps
The dataset contains no missing values, and outliers are all valid data. However, for analysis purpose, I did make plots showing the distributions of a few columns with and without the outliers, to see if they distribution type remains the same. 

### Key Visualizations


#### Visualization 1: [Day Calls]
The first histogram is the original data, where we can see that the range goes from 0 calls to over 150 calls. It seems to follow a bell curve normal distribution, but does have a slight left skew. 

When the outliers are removed (second histogram), we can see better that the distribution follows a normal distribution, without any skew. 

![Day Calls Original](./images/day_calls_org.png)
![Day Calls Outliers Removed](./images/day_calls_out.png)

#### Visualization 2: [Account Length]
The first histogram shows the original distribution, which, like day calls, seems to be bell-curved, but with a slight right skew. 

Once the outliers are removed for the second histogram, we see the normal distrution more clearly. 

![Account Length Original](./images/account_length_org.png)
![Account Length Outliers Removed](./images/account_length_out.png)

#### Visualization 3: [Customer Service Calls]
The first histogram shows the original distribution of the customer service calls, showing that there are a few customers who call quite a bit, while most call only a couple times. 

Once the outliers are removed for the second histogram, we see that the range reduces to be 0 to 3 calls, meaning that customers who call 4 or more times are an abnormaility. 

![Customer Service Calls Original](./images/custserv_calls_org.png)
![Customer Service Calls Outliers Removed](./images/custserv_calls_out.png)

## Conclusions/Recommendations
When creating my machine learning model, I used Random Forest, Logistic Regression and K Nearest Neighbors (KNN). By testing different test sizes (and neighbors for KNN), I was able to find the optimal parameters for each. The results are below. 

| Model | Accuracy | Precision (True) | Precision (False) | Recall (True) | Recall (False) |
| ----- | -------- | --------- | ------ | -- | -- |
| Random Forest | 0.91 | 0.8 | 0.93 | 0.55 | 0.95 |
| Logisitic Regression | 0.85 | 0.48 | 0.86 | 0.07 | 0.99 |
| KNN | 0.90 | 0.75 | 0.91 | 0.45 | 0.98 |

As we can see, random forest did the best, as it has the best balance of accurately finding False values (customers do not churn), while also having a relatively low number of false negatives (predict they will stay when they actually churn).

Below is the confusion matrix for the Random Forest Regression. 

![Random Forest Conf Matrix](./images/rf_conf.png)

The above confusion matrix tells us the number of True Positives (bottom right, predicted true, is true), True Negatives (top left, predicted false, is false), False Positives (top right, predicted true, is false) and False Negatives (bottom left, predicted false, is true)

So in this case, the model accurately predicted 780 False results, and 74 True results. 

However, it missed 61 true results, and 19 false results. So, 61 customers that it predicted would not churn did, and 19 customers it predicted would churn didn't. 

## Additional Information
Include any additional information, references, or resources that might be relevant for understanding the analysis.

---

Feel free to replace the placeholders with your actual content. Additionally, if you have images for your visualizations, make sure to replace the placeholder paths with the correct file paths or URLs.

Once you've filled in the content, save the file with a `.md` extension (e.g., `README.md`). You can use this Markdown file on platforms like GitHub to provide a well-structured README for your analysis.
