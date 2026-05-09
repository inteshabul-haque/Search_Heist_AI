# -----------------------------------
# CHAT MEMORY FUNCTIONS
# -----------------------------------

def add_to_memory(chat_history, role, content):

    chat_history.append(
        {
            "role": role,
            "content": content
        }
    )

    return chat_history


# -----------------------------------
# RECENT CONVERSATION MEMORY
# -----------------------------------

def get_recent_memory(chat_history, limit=6):

    return chat_history[-limit:]