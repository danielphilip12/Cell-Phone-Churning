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
Summarize the main findings from your analysis. If applicable, provide recommendations based on the insights gained from the data.

## Additional Information
Include any additional information, references, or resources that might be relevant for understanding the analysis.

---

Feel free to replace the placeholders with your actual content. Additionally, if you have images for your visualizations, make sure to replace the placeholder paths with the correct file paths or URLs.

Once you've filled in the content, save the file with a `.md` extension (e.g., `README.md`). You can use this Markdown file on platforms like GitHub to provide a well-structured README for your analysis.
