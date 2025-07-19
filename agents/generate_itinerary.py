from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
import json 

def generate_itinerary(state):
    llm = ChatOllama(model="mistral", base_url="http://localhost:11434")
    prompt = f"""
    Using the following preferences, create a detailed itinerary:
    {json.dumps(state['preferences'], indent=2)}

    Include sections for each day, dining options, and downtime.
    """
    try:
        result = llm.invoke([HumanMessage(content=prompt)]).content
        return {"itinerary": result.strip()}
    except Exception as e:
        return {"itinerary": "", "warning": str(e)}