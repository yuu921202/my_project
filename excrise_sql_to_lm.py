import mysql.connector
import requests

# A. 連接到你剛剛建立的 MySQL 資料庫
db = mysql.connector.connect(
    host="localhost",
    user="root",         # 你的資料庫帳號
    password="aa12255679",  # 你的資料庫密碼
    database="test"      # 剛才建立的資料庫名稱
)

cursor = db.cursor()

# B. 執行剛才練過的 SQL 查詢
query = "SELECT Department, SUM(SalesAmount) FROM demo GROUP BY Department"
cursor.execute(query)
result = cursor.fetchall()

# C. 把結果整理成白話文，準備餵給 Gemma
data_summary = f"目前各部門業績如下：{result}"
prompt = f"你是資深顧問，請根據這份業績數據：{data_summary}，給我一個簡短的經營建議。"

# D. 呼叫你的本地 Gemma (LM Studio)
url = "http://127.0.0.1:1234/v1/chat/completions"
payload = {
    "model": "google/gemma-4-e4b",
    "messages": [{"role": "user", "content": prompt}]
}

response = requests.post(url, json=payload)
print("--- Gemma 的分析建議 ---")
print(response.json()['choices'][0]['message']['content'])