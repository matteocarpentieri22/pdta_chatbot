import streamlit as st
import asyncio
import logging

from agent.agent import ConversationalAgent 

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set the title of the Streamlit app
st.title("🏥 Assistente Clinico per PDTA Polmonari")

# Function to initialize the agent, ensuring it's done only once
@st.cache_resource
def initialize_agent():
    logger.info("Initializing agent...")
    try:
        agent = ConversationalAgent()
        logger.info("Agent initialized successfully.")
        return agent
    except ValueError as e:
        logger.error(f"Agent initialization failed: {e}")
        st.error(f"Agent initialization failed: {e}. Make sure OPENAI_API_KEY is set in your .env file.")
        st.stop()
    except Exception as e:
        logger.error(f"An unexpected error occurred during agent initialization: {e}")
        st.error(f"An unexpected error occurred during agent initialization: {e}")
        st.stop()

# Initialize the agent
agent = initialize_agent()

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message from assistant
    welcome_message = """Ciao 👋 \n
Sono qui per aiutarti a interpretare il PDTA sulle lesioni polmonari\n 
Per iniziare, potresti fornirmi alcune informazioni sul contesto clinico del paziente? Ad esempio:

- Qual è la sintomatologia attuale del paziente? \n
- Ha una storia di fattori di rischio per il carcinoma polmonare (fumo, esposizione a sostanze nocive, ecc.)? \n
- Quali indagini diagnostiche sono state già effettuate? \n
- Quali sono i risultati delle indagini finora condotte? \n

Queste informazioni mi aiuteranno a comprendere meglio il caso e a fornire un'interpretazione adeguata dell'estratto del PDTA."""
    
    st.session_state.messages.append({"role": "assistant", "content": welcome_message})
    logger.info("Initialized message history in session with welcome message.")

# Sidebar configuration
st.sidebar.title("Configuration")

# Add streaming toggle to sidebar
use_streaming = st.sidebar.toggle("Use Streaming Response", value=True, 
                                help="Enable to see the response as it's generated, disable to see it only when complete")

# Add a button to clear history
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    if agent: # Check if agent was initialized successfully
        agent.clear_history() # Also clear history on the agent side
        logger.info("Chat history cleared.")
    st.rerun() # Rerun the app to reflect the cleared history

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Write a message..."):
    if not agent:
        logger.error("Agent is not available. Cannot process message.")
        st.error("Agent is not available. Cannot process message.")
        st.stop()

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    logger.info(f"User message added to history: '{prompt}'")
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        if use_streaming:
            # Stream the response
            async def stream_response():
                response_content = ""
                async for chunk in agent.get_streamed_response(prompt):
                    response_content += chunk
                    message_placeholder.markdown(response_content + "▌")
                message_placeholder.markdown(response_content)
                # Add assistant response to chat history after streaming is complete
                st.session_state.messages.append({"role": "assistant", "content": response_content})

            # Run the streaming response
            asyncio.run(stream_response())
        else:
            # Show thinking message
            message_placeholder.markdown("Thinking...")
            
            # Get non-streamed response
            async def get_full_response():
                response = await agent.get_response(prompt)
                message_placeholder.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Run the non-streaming response
            asyncio.run(get_full_response()) 