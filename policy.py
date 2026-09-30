from retriever import Retriever
from npc import NPC
from personality import Personality
from memory import Memory

class Policy:
    def __init__(self, npc):
        self.npc = npc

    def decide(self, query, memories):
        retriever = Retriever(memories)
        relevant_memories = retriever.retrieve(query)
        # print(relevant_memories)
        # For simplicity, we will just return the content of the most relevant memory
        if not relevant_memories:
            return "DEFLECT"
        if self._question_touches_secret(query, relevant_memories) == True:
            print("The question touches a secret.")
            if self.npc.personality.honesty >= 0.8:
                return "OMIT"
            else:
                return "LIE"
        print("The question does not touch a secret.")
        return "TRUTH"
        
    def _question_touches_secret(self, query, relevant_memories):
        query_words = set(query.lower().split())

        for memory, score in relevant_memories:

            secret_words = set(memory.content.lower().split())

            overlap = query_words & secret_words

            if not overlap:
                continue

            ratio = len(overlap) / len(secret_words)

            # print("Memory:", memory.content)
            # print("Overlap:", overlap)
            print("Overlap ratio:", ratio)

            if ratio >= 0.3:
                return True

        return False

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
    memory = Memory(
        id="m1",
        npc_id="npc001",
        content="I saw Barbie in the rose garden",
        event_id=None,
        timestamp=100,
        importance=0.9
    )
    memories = [memory]
    policy = Policy(npc)
    result = policy.decide(
        "Where did you see Barbie?",
        memories
    )

    print(result)