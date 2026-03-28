import agents.nlp_agent as nlp_agent
import agents.vision_agent as vision_agent
import agents.priority_agent as priority_agent
import agents.routing_agent as routing_agent

def process_complaint(complaint_id, description, image_path, db):
    # Step 1: NLP Analysis
    nlp_result = nlp_agent.run(description)

    # Step 2: Vision Analysis (optional)
    vision_result = {}
    if image_path:
        vision_result = vision_agent.run(image_path)

    # Step 3: Priority Calculation
    priority_result = priority_agent.run(
        nlp_result.get("category"),
        description,
        vision_result.get("visual_severity") if vision_result else None
    )

    # Step 4: Department Routing
    routing_result = routing_agent.run(
        nlp_result.get("category"),
        priority_result.get("priority"),
        description
    )

    # Final Output
    return {
        "category": nlp_result.get("category"),
        "severity": priority_result.get("severity_score"),
        "priority": priority_result.get("priority"),
        "department": routing_result.get("department")
    }