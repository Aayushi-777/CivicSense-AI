import json
from agents.client import client, TEXT_MODEL

def run(description: str) -> dict:
    text = description.lower()

    # 🔥 RULE-BASED CATEGORY (VERY IMPORTANT)
    if any(word in text for word in ["water", "leak", "pipe", "sewage"]):
        return {"category": "Water"}

    if any(word in text for word in ["garbage", "waste", "trash"]):
        return {"category": "Garbage"}

    if any(word in text for word in ["road", "pothole"]):
        return {"category": "Road"}

    if any(word in text for word in ["electric", "light", "power"]):
        return {"category": "Electricity"}

    # 🧠 AI fallback
    prompt = f"""
Classify the civic issue into ONE category:

Options:
- Water
- Garbage
- Road
- Electricity
- Other

Description: {description}

Return ONLY JSON:
{{
  "category": "<category>"
}}
"""

    try:
        res = client.chat.completions.create(
            model=TEXT_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        raw = res.choices[0].message.content.strip()
        raw = raw.replace("```json", "").replace("```", "")

        data = json.loads(raw)

        return data

    except Exception as e:
        print("NLP Error:", e)

        return {"category": "Other"}