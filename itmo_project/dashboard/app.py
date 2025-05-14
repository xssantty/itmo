import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, '..', 'data', 'vacancies_raw.json')

with open(file_path, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

vacancies = []
for vac in raw_data:
    if vac is None or not isinstance(vac, dict):
        continue

    salary = vac.get("salary") or {}
    experience = vac.get("experience") or {}
    employer = vac.get("employer") or {}
    area = vac.get("area") or {}

    vacancy = {
        "name": vac.get("name"),
        "area": area.get("name"),
        "salary_from": salary.get("from"),
        "salary_to": salary.get("to"),
        "experience": experience.get("name"),
        "employer": employer.get("name"),
        "key_skills": [s.get("name") for s in vac.get("key_skills") or []]
    }
    vacancies.append(vacancy)

df = pd.DataFrame(vacancies)

df['salary_avg'] = df[['salary_from', 'salary_to']].mean(axis=1)


plt.figure(figsize=(8, 5))
sns.boxplot(x='experience', y='salary_avg', data=df)
plt.title('Зарплаты по опыту')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
df['area'].value_counts().head(10).plot(kind='bar')
plt.title('Топ-10 регионов по числу вакансий')
plt.xticks(rotation=45)
plt.ylabel('Количество')
plt.tight_layout()
plt.show()

all_skills = df['key_skills'].explode().dropna().tolist()

if all_skills:
    skill_text = ' '.join(all_skills)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(skill_text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Часто встречающиеся навыки')
    plt.show()
else:
    print("Список навыков пуст.")
