import json
from agents.client import client, TEXT_MODEL

def run(category: str, priority: str, description: str) -> dict:
    prompt = f"""Assign department.

Category: {category}
Priority: {priority}

Return JSON:
{{
  "department": "<department>",
  "resolution_days": <days>
}}"""

    res = client.chat.completions.create(
        model=TEXT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = res.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "")

    try:
        return json.loads(raw)
    except:
        return {"department": "Municipal", "resolution_days": 7}