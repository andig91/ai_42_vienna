import os

def start_chat():
    """
    Start the chat

    Args:
        None

    Returns:
        None
    """
    os.system('streamlit run ai_42_vienna/llm/chat_with_data.py')

def start_extract():
    """
    Start the chat

    Args:
        None

    Returns:
        None
    """
    os.system('streamlit run ai_42_vienna/llm/chat_with_data_extract.py')


def start_agent():
    """
    Start the agent

    Args:
        None

    Returns:
        None
    """
    os.system('streamlit run ai_42_vienna/llm/agent.py')