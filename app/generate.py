import requests
from core.config import settings

def generate_response(task_text: str) -> str:
    """Отправляем описание задания в Polza.ai (модель DeepSeek) и получаем готовый отклик"""
    if not settings.polza_api_key:
        raise ValueError("POLZA_API_KEY не задан в настройках!")

    url = "https://polza.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.polza_api_key}",
        "Content-Type": "application/json"
    }

    system_content = getattr(settings, "system_message", "Ты профессиональный дизайнер.")
    model_name = getattr(settings, "polza_model", "deepseek/deepseek-chat")

    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_content},
            {"role": "user", "content": task_text}
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Ошибка Polza:", e)
        return "Здравствуйте. Готов выполнить ваш проект. Напишите, пожалуйста, подробности."