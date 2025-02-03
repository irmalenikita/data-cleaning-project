#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df =pd.read_csv(r"C:\Users\mymac\Downloads\Untitled spreadsheet - Call List.csv")


# In[3]:


df


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


df=df.drop_duplicates()
df


# In[7]:


df= df.drop('Not_Useful_Column',axis=1)
df


# In[8]:


df.loc[:,'Last_Name']=df['Last_Name'].str.replace(r'[/,.,_]','', regex=True)


# In[9]:


df.loc[:,'Phone_Number']=df['Phone_Number'].str.replace(r'[/,|,-]','', regex=True)


# In[10]:


df.loc[:,'Phone_Number'] = df['Phone_Number'].str.replace(r'[^\d]', '', regex=True)
df.loc[:, 'Phone_Number'] = df['Phone_Number'].str.replace(r'(\d{3})(\d{3})(\d{4})', r'\1-\2-\3', regex=True)


# In[11]:


df


# In[ ]:





# In[12]:


df.loc[:, 'Paying Customer'] = df['Paying Customer'].replace({'Yes': 'Y', 'No': 'N'})



# In[13]:


df


# In[14]:


df.loc[:,'Do_Not_Contact']=df['Do_Not_Contact'].replace({'Yes':'Y','No':'N'})


# In[15]:


df


# In[16]:


df = df.replace('N/a','')
df=df.fillna('')
df


# In[17]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)

df


# In[18]:


for x in df.index:
    if df.loc[x,"Phone_Number"]=='':
        df.drop(x,inplace=True)
df


# In[19]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == '':
        df.drop(x, inplace=True)

df


# In[ ]:





# In[20]:


df.reset_index(drop=True)
df


# In[21]:


df = df.reset_index(drop=True)
df


# In[ ]:





# In[ ]:





# In[ ]:




