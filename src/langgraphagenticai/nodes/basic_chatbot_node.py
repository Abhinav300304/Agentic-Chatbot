from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot login Implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Processes the input state and generates a chatbor response
        """

        return {"messages":self.llm.invoke(state['messages'])}
