#!/usr/bin/env python
# coding: utf-8

# In[4]:


#PROJECT 1
girls = ['Samantha','Jada','Jane','Claire','Elizabeth','Mary','Susan','Waje','Taibat','Lilian']
girls_ages = [17,16,17,18,16,18,17,20,19,17]
girls_heights = [5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5]
girls_scores = [80,85,70,60,76,66,87,95,50,49]

boys = ['Charles','Jude','James','Kelvin','Biodun','Wale','Kunle','Mattew','Tom','Kayode']
boys_ages = [19,16,18,17,20,19,16,18,17,19]
boys_heights = [5.7,5.9,5.8,6.1,5.9,5.5,6.1,5.4,5.8,5.7]
boys_scores = [74,87,75,68,66,78,87,98,54,60]

print('Name | Age | Height | Score')
for i in range(len(girls)) :
    print(girls[i],"|",girls_ages[i],"|",girls_heights[i],"|",girls_scores[i])

for i in range(len(girls)) :
    print(boys[i],"|",boys_ages[i],"|",boys_heights[i],"|",boys_scores[i])


# In[ ]:




