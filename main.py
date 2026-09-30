from retriever import Retriever
from policy import Policy
from llm.prompts import PromptBuilder
from llm.client import LLMClient
from npc import NPC
from personality import Personality
from memory import Memory

class Game:

    def __init__(self, npc, memories):
        self.npc = npc
        self.memories = memories

        self.retriever = Retriever(memories)
        self.policy = Policy(npc)
        self.prompt_builder = PromptBuilder(npc)
        self.llm_client = LLMClient()

    def ask_npc(self, query):
        # 1. Retrieve relevant memories
        # 2. Decide how the NPC should respond
        response_type = self.policy.decide(
            query,
            memories
        )
        print("response_type:", response_type)
        # 3. Build the prompt
        prompt = self.prompt_builder.build(
            query,
            memories,
            response_type
        )
        print("prompt:", prompt)
        print("qqqqqq")
        # 4. Generate the response
        response = self.llm_client.generate(prompt)

        return response


if __name__ == "__main__":
    personality = Personality(
        honesty=0.5,
        courage=0.5,
        intelligence=0.5,
        kindness=0.5,
        suspicion=0.5,
        confidence=0.5
    )
    npc = NPC(
        npc_id="npc001",
        name="Emma",
        role="Maid",
        personality=personality
    )
    npc.add_secret("I saw Barbie in the rose garden")
    # print("1")
    memory = Memory(
        id="m1",
        npc_id="npc001",
        content="I saw Barbie in the rose garden",
        event_id=None,
        timestamp=100,
        importance=0.9
    )
    # print("2")
    memories = [memory]
    game = Game(npc, memories)
    # print("3")
    ask = "Where did you see Barbie?"
    print("ask:", ask)
    result = game.ask_npc(ask)

    print("response:", result)
    print("Game loaded successfully.")