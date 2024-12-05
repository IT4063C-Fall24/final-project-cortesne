#!/usr/bin/env python
# coding: utf-8

# # Call Center Employee Burnout
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 
# With the growth of ecommerce, call centers are receiving more calls and chats that ever before. The interactions will range from product inquiry, order status, return details, and much more. This creates more and more interactions and volume that the customers need to take, which can lead to back to back interactions. The amount of work can and has led to burnout. Therefore, the problem I am hoping to bring up are: what steps can we take to address employee burnout? By addressing the causes of burnout, it will improve employee retention, improve customer satisfaction, and reduce costs going towards training new agents. 

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# What are main factors contributing to burnout among agents?
# 
# How does the workload correlate with employee retention/turnover rates?
# 
# What adjustments can be made to help reduce burnout?
# 

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 
# An answer would focus on addressing the barriers that cause employee burnout. For example, a line graph that tracks the number of agents who work from home and not quit. Or a heatmap that shows peak workload times in relation to burnout. 

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# The datasets that I am looking at are:
# - Employee Burnout
#     -This dataset is relevant to me because it provides a lot of information about factors that goes into burnout, such as work from home (WFM) status and mental fatigue. It has a wide set of information, that I believe I can get a lot of information from. With this dataset, I believe that I can make scatter and bar graphs to correlate factors in employee burnout. 
# 
# - Call-Center-Dataset
#     -With this dataset, it shows the type of call center, average handle time, and speed of answer. I believe with this dataset I can find a relationship with employee satisfaction and speed of answer/average handle time. I believe the higher speed of answer the lower the satisfaction rating, which will impact employee burnout.
# 
# - Employee Turnover
#     -With this dataset, I was able to fix it, so I can now pull the information. But, it also provides a lot of information. This set gives information about the type of customer relations employement, gender, and anxiety. I believe the anxiety and industry columns with be the main columns I use to help support other visuals. The data here can work with the Occupational Employment and Wage Statistics, which will help determine the wage influence on the anxiety. For example, if a certain industry has a high turnover, high anxiety, and low wage, then it can help paint a bigger picture.
# 
# - Occupational Employment and Wage Statisitics, May 2023
#     -This dataset provides information about different wages of different areas within customer relations. I believe this will work to support the data in the other datasets.  
# 
# *How are you going to relate these datasets?*
# - By looking at the data by state, I hope to get an understanding about the main factors of burnout are. 
# 

# In[ ]:


# Occupational Employment and Wage Statisitics, May 2023
import pandas as pd

df = pd.read_csv('OES_Report.csv')

df.head()


# In[10]:


#Employee Burnout
train = pd.read_csv("train.csv")

train.head()


# In[6]:


data = pd.read_excel("01 Call-Center-Dataset.xlsx")

data.head()


# In[8]:


#Turnover
df2 = pd.read_csv("turnover.csv")

df2.head()


# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->

# I will make graphs that will focus and highlight different factors. I imagine that there will be numerous factors that contribute to employee burnout. While I look into them, I want to determine and find out which one an employee could create a plan on ASAP to improve the work environment for their employee. For example, a burnout factor can be the interactions, such as the customers are rude. Unfortunately, there isn't anything an employer can do there. Therefore, I will analyze the data and see what can options exist to create short-term and long-term solutions. 

# ## Clean Dataset

# In[ ]:


#Cleaning the train dataset
train.info()

train.duplicated().sum()

train.drop_duplicates(inplace=True)

train.shape


# In[12]:


train.isnull().sum()


# In[13]:


train.dropna(subset=['Resource Allocation'], inplace=True)
train.dropna(subset=['Mental Fatigue Score'], inplace =True)
train.dropna(subset=['Burn Rate'], inplace=True)


# In[14]:


train.isna().sum()


# In[4]:


#Cleaning OES Report
df.info()
df.isna().sum()


# In[7]:


#Cleaning Call Center Dataset
data.info()
data.isna().sum()


# In[11]:


data.dropna(subset=['Speed of answer in seconds'], inplace=True)
data.dropna(subset=['AvgTalkDuration'], inplace =True)
data.dropna(subset=['Satisfaction rating'], inplace=True)

data.isna().sum()


# In[9]:


#Cleaning Turnover
df2.info()
df2.isna().sum()


# In[16]:


df2.dropna(subset=['novator'], inplace=True)

df2.isna().sum()


# ## Data Visualization

# In[32]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


##With this graph, it shows the satisfaction rating of different departments. This is beneficial because if a department is significantly lower or higher, it will be a good starting point to do additional research.
data.groupby('Topic')['Satisfaction rating'].mean().plot.bar()


# In[34]:


plt.figure(figsize=(8, 8))
resolved_counts = data["Resolved"].value_counts()
resolved_counts.plot(kind="pie", autopct="%1.1f%%", colors=["gold", "lightgreen"], startangle=140)
plt.title("Call Resolution Status")
plt.ylabel("")
plt.show() 


# In[35]:


plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=data, 
    x="Speed of answer in seconds", 
    y="Satisfaction rating", 
    hue="Agent", 
    palette="viridis"
)
plt.title("Satisfaction Rating vs Speed of Answer")
plt.xlabel("Speed of Answer (seconds)")
plt.ylabel("Satisfaction Rating")
plt.legend(title="Agent")
plt.show()


# In[27]:


train = pd.read_csv("train.csv")

plt.figure(figsize=(10, 6))
sns.lineplot(data= train, x="Date of Joining", y="Burn Rate", hue="Designation", marker="o")
plt.title("Burn Rate Over Time by Designation")
plt.xlabel("Date of Joining")
plt.ylabel("Burn Rate")
plt.legend(title="Designation")
plt.show()


# In[29]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Occupation (SOC code)", y="Hourly mean wage")
plt.title("Hourly Mean Wage Distribution")
plt.xlabel("Occupation")
plt.ylabel("Hourly Mean Wage")
plt.show()


# In[30]:


plt.figure(figsize=(10, 6))
data.set_index("Agent")[[
    "Speed of answer in seconds", "Satisfaction rating"
]].plot(kind="bar", figsize=(10, 6))
plt.title("Agent Performance Metrics")
plt.xlabel("Agent")
plt.ylabel("Metric Values")
plt.show()


# ## Machine Learning Plan
# 
# Below are some considerations I will be making when developing my machine learning plan.
# 
# ### Types of Machine Learning:
# 
# 1. **Regression Analysis:**
#    - **Use Case:** Predicting employee burnout rate based on factors such as resource allocation, mental fatigue score, and designation level.
#    - **Potential Insights:** Identifying key factors contributing to higher burnout rates and enabling targeted interventions to improve retention.
# 
# 2. **Clustering:**
#    - **Use Case:** Grouping employees based on mental fatigue scores, resource allocation, and designation to identify common patterns.
#    - **Potential Insights:** Highlighting clusters of employees at higher risk of burnout to prioritize support strategies.
# 
# 3. **Classification:**
#    - **Use Case:** Predicting whether an employee is likely to leave the organization based on demographic and workplace factors.
#    - **Potential Insights:** Enabling proactive measures to address potential turnover by identifying at-risk employees.
# 
# 
# ### Issues and Challenges:
# 
# 1. **Data Quality and Completeness:**
#    - **Issue:** Missing values in key columns such as "Mental Fatigue Score," "Burn Rate," and "Speed of Answer in Seconds."
#    - **Challenge:** Implementing robust data cleaning techniques, such as imputation or removing rows/columns with excessive missing values, to ensure data quality.
# 
# 2. **Feature Selection:**
#    - **Issue:** Identifying relevant features across datasets that contribute meaningfully to burnout and retention analysis.
#    - **Challenge:**Employing feature selection methods to focus on impactful variables.
# 
# 3. **Data Integration:**
#    - **Issue:** Combining diverse datasets (e.g., call center metrics, employee details, turnover events) with varying formats and levels of granularity.
#    - **Challenge:** Developing a unified schema and resolving inconsistencies (e.g., differing time frames or employee identifiers) for seamless integration.
# 
# 4. **Imbalanced Datasets:**
#    - **Issue:** Certain outcomes, such as employees with extremely high burnout rates or rare turnover events, may be underrepresented.
#    - **Challenge:** Addressing class imbalance through techniques like oversampling, undersampling, or using specialized algorithms.
# 
# 5. **Data Privacy and Confidentiality:**
#    - **Issue:** Handling sensitive employee information responsibly while analyzing datasets.
#    - **Challenge:** Ensuring compliance with data protection standards by anonymizing personal identifiers and securing data storage.

# ## Resources and References
# *What resources and references have you used for this project?*
# I used Kaggle and the U.S Bureau of Labor Statistics (BLS). Three of my datasets came from Kaggle, and with BLS, I got to customize of their reports on the site, which I pulled as a OES_Report.csv

# In[20]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

