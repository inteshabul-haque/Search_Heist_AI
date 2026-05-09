from memory.chat_memory import (
    get_recent_memory
)

# -----------------------------------
# BUILD CONVERSATION CONTEXT
# -----------------------------------

def build_conversation_context(chat_history):

    recent_messages = get_recent_memory(
        chat_history
    )

    memory_context = ""

    for message in recent_messages:

        role = message["role"]
        content = message["content"]

        memory_context += f"""

        {role.upper()}:
        {content}

        """

    return memory_context