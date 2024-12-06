import requests
import re

def nl_to_sql(natural_language_query):
    table_sql = """
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    major VARCHAR(50),
    gpa NUMERIC(3, 2)
);
"""
    # Комбинированный промпт
    prompt = f"{table_sql}\n\nConvert this query into SQL: {natural_language_query}"

    # Формирование данных для запроса
    data = {
        "model": "llama3.1",  # Указываем модель
        "messages": [
            {"role": "system", "content": "You are an assistant that converts natural language queries to SQL."},
            {"role": "user", "content": prompt}
        ],
        "stream": False  # Ожидаем полный ответ, а не поток
    }

    # Отправка запроса
    response = requests.post(
        "http://localhost:11434/api/chat", 
        json=data
    )

    # Для отладки: выводим полный ответ
    # print("Response Text:", response.text)

    try:
        # Извлечение ответа из правильной части JSON
        response_json = response.json()
        generated_sql = response_json.get("message", {}).get("content", "")

        # Используем регулярное выражение для извлечения SQL-запроса
        sql_query_match = re.search(r'```sql\n(.*?)\n```', generated_sql, re.DOTALL)
        if sql_query_match:
            return sql_query_match.group(1)  # Возвращаем только сам SQL-запрос
        else:
            return "No SQL query found"

    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return "Error decoding JSON"

# Example
# nl_query = "Show all students who have a GPA greater than 3.5"
# sql_query = nl_to_sql(nl_query)
# print("SQL-запрос:", sql_query)
