## TravelPlanner using Multi-AI-Agents and LangGraph.

Welcome to the **AI Travel Planner**, a modular multi-agent system built with Streamlit, LangGraph, and Ollama. This application leverages multiple AI agents to generate personalized travel itineraries and provide additional travel-related insights based on user preferences. The system is designed for modularity, with agents split into individual scripts for maintainability and scalability.

## Overview

The AI Travel Planner uses a LangGraph workflow to manage a set of agents that collaboratively process user inputs (e.g., destination, month, duration) to produce a detailed itinerary, activity suggestions, weather forecasts, packing lists, food/culture recommendations, useful links, and a chat interface. The system integrates with Ollama (for the `mistral` model) and the Google Serper API for web searches.

## Features
- Generate a detailed travel itinerary with daily plans, dining options, and downtime.
- Suggest unique local activities based on the itinerary and preferences.
- Fetch the top 5 travel guide links for the destination and month.
- Provide weather forecasts, packing lists, and food/culture recommendations.
- Offer a conversational chat to answer itinerary-related questions.
- Export the itinerary as a PDF.

## Overview
<img width="1078" height="966" alt="travel1" src="https://github.com/user-attachments/assets/01cdfcee-b750-4982-8d5b-20851a9e33ad" />
<img width="1091" height="978" alt="travel2" src="https://github.com/user-attachments/assets/b09b3102-248d-4335-ad8a-64e15e16c62a" />
<img width="1082" height="960" alt="travel3" src="https://github.com/user-attachments/assets/19d13a73-aff9-4a1c-a9b8-55f1f51370e3" />


## Directory Structure

```
TravelPlanner/
│
├── agents/
│   ├── generate_itinerary.py
│   ├── recommend_activities.py
│   ├── fetch_useful_links.py
│   ├── weather_forecaster.py
│   ├── packing_list_generator.py
│   ├── food_culture_recommender.py
│   └── chat_agent.py
│
├── export_utils.py
├── travel_agent.py
├── requirements.txt
└── .env
```

- **agents/**: Contains individual Python scripts for each agent, modularizing the logic.
- **export_utils.py**: Houses shared utility functions (e.g., PDF export).
- **travel_agent.py**: The main Streamlit application file that orchestrates the workflow and UI.
- **requirements.txt**: Lists project dependencies.
- **.env**: Stores environment variables (e.g., `SERPER_API_KEY`).

## Setup Instructions

### Prerequisites
- Python 3.8 or higher.
- Ollama installed and running locally with the `mistral` model (`ollama pull mistral`).
- A Google Serper API key.

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/prktypes/travel_planner
   cd TravelAgent
   ```
2. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your `SERPER_API_KEY`:
     ```
     SERPER_API_KEY=your_api_key_here
     ```
3.. Start Ollama locally (if not already running):
   ```bash
   ollama serve
   ```

### Running the Application
1. Launch the Streamlit app:
   ```bash
   streamlit run travel_agent.py
   ```
2. Open your browser and navigate to the provided URL (e.g., `http://localhost:8501`).

## Usage
- Enter your travel preferences (destination, month, duration, etc.) in the form.
- Click "Generate Itinerary" to create a base plan.
- Use the buttons to fetch additional details (e.g., activity suggestions, weather forecast).
- Interact with the chat to ask questions about your itinerary.
- Export the itinerary as a PDF using the "Export as PDF" button.
