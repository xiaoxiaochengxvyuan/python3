
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df = pd.read_excel('work/C12-链家网400来电到成交转化漏斗_月累计.xls')
df_1 = df.loc[df['业务类型'] == "买卖"]
df_1_m=df_1[['大区','400唯一来电量_月','400来电转录入量_月','400录入转带看量_月']]
df_2 = df.loc[df['业务类型'] == "租赁"]
df_2_z = df_2[['大区','400唯一来电量_月','400来电转录入量_月','400录入转带看量_月']]
df_outer=pd.merge(df_1_m,df_2_z,on='大区')
df_outer=df_outer.rename(columns={'400唯一来电量_月_x': '唯一商机量(买)','400来电转录入量_月_x':'录入量(买)','400录入转带看量_月_x':'带看量(买)'
                        ,'400唯一来电量_月_y':'唯一商机量(租)','400来电转录入量_月_y':'录入量(租)','400录入转带看量_月_y':'带看量(租)'}) 


# In[3]:

df_n = pd.read_excel('work/C12-链家网400来电到成交转化漏斗_月累计.xls')
df_n_1 = df.loc[df['业务类型'] == "买卖"]
df_n_1_m=df_n_1[['大区','400唯一来电量_月','400来电转录入量_月','400录入转带看量_月']]
df_n_2 = df.loc[df['业务类型'] == "租赁"]
df_n_2_z = df_n_2[['大区','400唯一来电量_月','400来电转录入量_月','400录入转带看量_月']]
df_n_outer=pd.merge(df_n_1_m,df_n_2_z,on='大区')
df_n_outer=df_n_outer.rename(columns={'400唯一来电量_月_x': '唯一商机量(买)','400来电转录入量_月_x':'录入量(买)','400录入转带看量_月_x':'带看量(买)'
                        ,'400唯一来电量_月_y':'唯一商机量(租)','400来电转录入量_月_y':'录入量(租)','400录入转带看量_月_y':'带看量(租)'})


# In[4]:

df_outer_1 =df_outer[['唯一商机量(买)','录入量(买)','带看量(买)','唯一商机量(租)','录入量(租)','带看量(租)']]
df_n_outer_1=df_n_outer[['唯一商机量(买)','录入量(买)','带看量(买)','唯一商机量(租)','录入量(租)','带看量(租)']]
df_n_outer_2=df_n_outer_1.sub(df_outer_1,axis=0)
d=df_n_outer['大区']
df_n_outer_2.insert(0,'大区',d)


# In[6]:

df_n_outer_2


# In[22]:

df_im= pd.read_excel('work/C14-链家网IM咨询到成交转化漏斗_月累计_1.xls')
df_im=df_im[['大区','唯一会话数_月','当月会话后被会话经纪人录入的会话数','当月会话后被会话经纪人录入且带看的会话量']]


# In[23]:

df_im_n=df_im_n[['大区','唯一会话数_月','当月会话后被会话经纪人录入的会话数','当月会话后被会话经纪人录入且带看的会话量']]
df_im_n_s=df_im_n[['唯一会话数_月','当月会话后被会话经纪人录入的会话数','当月会话后被会话经纪人录入且带看的会话量']]
df_im_s=df_im[['唯一会话数_月','当月会话后被会话经纪人录入的会话数','当月会话后被会话经纪人录入且带看的会话量']]


# In[30]:

df1=df_im_n_s.sub(df_im_s,axis=0)
df1=df1.rename(columns={'唯一会话数_月': '唯一商机量(IM)','当月会话后被会话经纪人录入的会话数':'录入量(IM)',
                    '当月会话后被会话经纪人录入且带看的会话量':'带看量(IM)'})
frame=[df_n_outer_2,df1]
result = pd.concat(frame,axis=1)


# In[32]:

result


# In[ ]:



