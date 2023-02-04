import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)

general, prenatal, sports = pd.read_csv(r"data\general.csv"), \
                            pd.read_csv(r"data\prenatal.csv"), \
                            pd.read_csv(r"data\sports.csv")
data = pd.concat([general,
                  prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}),
                  sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'})],
                 ignore_index=True).drop(columns=['Unnamed: 0'])

data.dropna(axis=0, how='all', inplace=True)
column_list = ['gender', 'bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']

for i in column_list:
    data[i] = data[i].fillna(0)

data['gender'] = data['gender'].replace([0],'f')
data['gender'] = data['gender'].replace(['male','man'],'m')
data['gender'] = data['gender'].replace(['female','woman'],'f')



# ANSWERS FOR THE PREVIOUS STAGE
q1 = data.hospital.mode()[0]
q2 = round((data.loc[data['hospital'] == 'general', 'diagnosis']).value_counts()['stomach'] / len(
    (data.loc[data['hospital'] == 'general', 'diagnosis'])), 3)
q3 = round((data.loc[data['hospital'] == 'sports', 'diagnosis']).value_counts()['dislocation'] / len(
    (data.loc[data['hospital'] == 'sports', 'diagnosis'])), 3)
q4 = int(data.loc[data['hospital'] == 'general', 'age'].median() - (
    data.loc[data['hospital'] == 'sports', 'age'].median()))
q5_1 = data.loc[data['blood_test'] == 't', 'hospital'].mode()[0]
q5_2 = data.loc[data['hospital'] == q5_1, 'blood_test'].count()

print(f'The answer to the 1st question is {q1}')
print(f'The answer to the 2nd question is {q2}')
print(f'The answer to the 3rd question is {q3}')
print(f'The answer to the 4th question is {q4}')
print(f'The answer to the 5th question is {q5_1}, {q5_2}  blood tests')

gr1 = 0  # 0-15
gr2 = 0  # 15-35
gr3 = 0  # 35-55
gr4 = 0  # 55-70
gr5 = 0  # 70-80

gr1k = '0-15'  # 0-15
gr2k = '15-35'  # 15-35
gr3k = '35-55'  # 35-55
gr4k = '55-70'  # 55-70
gr5k = '70-80'  # 70-80

for age in data.age:
    if age < 15:
        gr1 += 1
    elif 15 <= age < 35:
        gr2 += 1
    elif 35 <= age < 55:
        gr3 += 1
    elif 55 <= age < 70:
        gr4 += 1
    else:
        gr5 += 1

gr_dict = {gr1k: gr1, gr2k: gr2, gr3k: gr3, gr4k: gr4, gr5k: gr5}
data.plot(y='age', kind='hist', bins=10)
plt.show()
print(f'The answer to the 1st question: {max(gr_dict, key=gr_dict.get)}')
data.diagnosis.value_counts().plot(kind='pie')
plt.show()
print(f'The answer to the 2nd question: {data.diagnosis.mode()[0]}')
sns.violinplot(x='height', y='hospital', data=data)
plt.show()
print("The answer to the 3rd question: It's because...")

# print(f'Data shape: {data.shape}', data.sample(n=20, random_state=30), sep='\n')
