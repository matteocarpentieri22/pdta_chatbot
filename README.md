# OpenAI Agents SDK Chatbot Template with Streamlit

This template provides a starting point for building a conversational chatbot using the OpenAI Agents SDK and Streamlit, featuring conversation history and streaming responses

## Features

- 🤖 Conversational chatbot powered by OpenAI's Agents SDK
- 💬 Interactive chat interface using Streamlit
- 📝 Conversation history management
- 🔄 Persistent chat sessions
- 🎨 Clean and modern UI
- ⚡ Real-time streaming responses
- ⚙️ Configurable response mode (streaming/non-streaming)

## Prerequisites

- OpenAI API key

## Installation

1. Clone this repository:
```bash
git clone <your-repository-url>
cd pdta-agent
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Copy the `.env.example` file to `.env` and add your OpenAI API key:
```bash
cp .env.example .env
```

Then edit the `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Configure your preferences:
   - Use the "Use Streaming Response" toggle to enable/disable streaming responses
   - Use the "Clear Chat History" button to reset the conversation


4. Start chatting with the AI agent!

## Response Modes

The chatbot supports two response modes:

### Streaming Mode (Default)
- Responses appear in real-time as they're generated
- See the agent's thinking process as it happens
- More interactive and engaging experience
- Indicated by a blinking cursor (▌) while generating

### Non-Streaming Mode
- Responses appear all at once when complete
- Shows "Thinking..." while generating
- More traditional chat experience
- Useful for scenarios where you prefer complete responses

You can switch between modes at any time using the "Use Streaming Response" toggle in the sidebar.


## Project Structure

```
pdta-agent/
├── agent/
│   ├── __init__.py
│   └── agent.py          # OpenAI agent configuration and logic
├── main.py               # Main Streamlit application
├── requirements.txt      # Project dependencies
├── .env.example         # Example environment variables
├── .env                 # Environment variables (not tracked in git)
└── README.md            # This file
```


## Customization

### Modifying the Agent

You can customize the agent's behavior by modifying the `agent/agent.py` file. This includes:
- Changing the agent's instructions
- Adding custom tools and capabilities
- Modifying the conversation flow

### Styling the UI

The Streamlit UI can be customized by modifying the `main.py` file. You can:
- Change the theme
- Add custom components
- Modify the layout