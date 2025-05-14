import requests
import json
import time
from pathlib import Path

def fetch_vacancies(query="Python", pages=5, per_page=20, area=1):
    """
    Скачивает вакансии с hh.ru по ключевому слову.
    area=1 Россия в целом.
    """
    all_vacancies = []
    base_url = "https://api.hh.ru/vacancies"

    for page in range(pages):
        params = {
            "text": query,
            "area": area,
            "page": page,
            "per_page": per_page
        }
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print(f"Ошибка на странице {page}: {response.status_code}")
            continue
        data = response.json()
        all_vacancies.extend(data.get("items", []))
        time.sleep(0.5)

    return all_vacancies

def save_to_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    vacancies = fetch_vacancies(query="IT", pages=10)
    save_to_json(vacancies, data_dir / "vacancies_raw.json")
    print(f"Скачано вакансий: {len(vacancies)}")
