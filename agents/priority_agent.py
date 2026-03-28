import json
from agents.client import client, TEXT_MODEL

def run(category: str, description: str, visual_severity=None) -> dict:
    text = description.lower()

    # 🔥 RULE-BASED OVERRIDES (VERY IMPORTANT)
    if any(word in text for word in ["leak", "pipe", "water leakage", "sewage"]):
        return {"severity_score": 9, "priority": "HIGH"}

    if any(word in text for word in ["fire", "electric", "short circuit", "blast"]):
        return {"severity_score": 10, "priority": "CRITICAL"}

    if any(word in text for word in ["accident", "injury", "danger"]):
        return {"severity_score": 9, "priority": "CRITICAL"}

    # 🧠 AI PROMPT (improved)
    prompt = f"""
You are a civic issue priority classifier.

Rules:
- Water leakage, sewage → HIGH
- Fire, electrical hazard → CRITICAL
- Garbage → MEDIUM
- Minor issues → LOW

Category: {category}
Description: {description}

Return ONLY JSON:
{{
  "severity_score": <1-10>,
  "priority": "<LOW/MEDIUM/HIGH/CRITICAL>"
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

        # 🔒 Safety check
        if "priority" not in data:
            return {"severity_score": 5, "priority": "MEDIUM"}

        return data

    except Exception as e:
        print("Priority AI Error:", e)

        # fallback
        return {"severity_score": 5, "priority": "MEDIUM"}