"""
This module defines the ConversationalAgent class for interacting with the openai-agents SDK.
"""
import os
from dotenv import load_dotenv
import logging
from typing import AsyncIterator

from agents import Agent, Runner, trace

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from .prompts.agent_instructions import AGENT_INSTRUCTIONS, PDTA_INSTRUCTIONS, pdta_text



class ConversationalAgent:
    """
    A conversational agent leveraging the openai-agents SDK.
    Handles conversation flow and interaction with the configured OpenAI model.
    """
    def __init__(self):
        """
        Initializes the ConversationalAgent.
        Loads environment variables, validates the OpenAI API key, and configures the agent.
        """
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logger.error("OPENAI_API_KEY not found in environment variables.")
            raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")

        agent_name = "ConversationalAgent"
        agent_instructions = AGENT_INSTRUCTIONS + PDTA_INSTRUCTIONS.format(pdta_text=pdta_text)
        agent_model = "gpt-4o-mini"

        self.agent = Agent(
            name=agent_name,
            instructions=agent_instructions,
            model=agent_model
        )
        logger.info(f"Agent '{self.agent.name}' initialized with model '{agent_model}'.")
        logger.debug(f"Agent instructions: {agent_instructions}") # Log instructions at debug level

        # Stores the conversation history for the current session
        self.conversation_history = []

    async def get_streamed_response(self, user_message: str) -> AsyncIterator[str]:
        """
        Processes a user message using the openai-agents SDK Runner and returns a stream of the agent's response.

        Args:
            user_message: The message input by the user.

        Returns:
            An async iterator that yields chunks of the agent's response as they are generated.
        """
        logger.info(f"Received user message for streaming: '{user_message}'")

        # Append user message to the history before sending to the runner
        self.conversation_history.append({"role": "user", "content": user_message})
        logger.debug(f"Current conversation history (before streaming): {self.conversation_history}")

        try:
            logger.info(f"Running agent '{self.agent.name}' in streaming mode...")
            # Use run_streamed for streaming responses
            with trace("ConversationalAgent Streaming Workflow") as my_trace:
                result = Runner.run_streamed(
                    starting_agent=self.agent,
                    input=self.conversation_history,
                )

            full_response = ""
            async for event in result.stream_events():
                if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
                    chunk = event.data.delta
                    if chunk:
                        full_response += chunk
                        yield chunk

            # After streaming is complete, append the full response to history
            if full_response:
                self.conversation_history.append({"role": "assistant", "content": full_response})
                logger.info("Streaming response completed and added to history")
            else:
                logger.warning("No response was generated during streaming")

        except Exception as e:
            logger.exception(f"An error occurred during streaming: {e}")
            error_msg = f"Sorry, an error occurred while streaming the response: {e}"
            yield error_msg

    async def get_response(self, user_message: str) -> str:
        """
        Processes a user message using the openai-agents SDK Runner and returns the agent's complete response.
        For non-streaming use cases.

        Args:
            user_message: The message input by the user.

        Returns:
            The agent's complete response as a string.
        """
        logger.info(f"Received user message: '{user_message}'")

        # Append user message to the history before sending to the runner
        self.conversation_history.append({"role": "user", "content": user_message})
        logger.debug(f"Current conversation history (before runner): {self.conversation_history}")

        try:
            logger.info(f"Running agent '{self.agent.name}'...")
            # Runner handles the interaction cycle with the agent
            with trace("ConversationalAgent Workflow") as my_trace:
                result = await Runner.run(
                    starting_agent=self.agent,
                    input=self.conversation_history, # Send the updated history
                )
            logger.debug(f"Runner result object: {result}") # Log the full result for debugging

            # Extract the final response string from the result
            agent_response = result.final_output

            if not agent_response:
                logger.warning("Agent returned an empty response.")
                agent_response = "I did not receive a valid response from the agent." # Provide a default error message
            else:
                logger.info(f"Agent '{self.agent.name}' generated response.")
                logger.debug(f"Raw agent response: {agent_response}")

            # Append agent response to history after receiving it
            self.conversation_history.append({"role": "assistant", "content": agent_response})

            return agent_response

        except Exception as e:
            logger.exception(f"An error occurred while running the agent: {e}") # Use logger.exception to include traceback
            # Return a user-friendly error message
            return f"Sorry, an error occurred while processing the message: {e}"

    def clear_history(self):
        """
        Clears the internal conversation history for the agent.
        """
        self.conversation_history = []
        logger.info("Conversation history cleared.")
        