from memory import Memory

class Retriever:
    def __init__(self, memories):
        self.memories = memories
        # self.STOP_WORDS = ['did', 'you', 'the', 'a', 'is', 'was', 'I', 'me']

    def _score(self, query, memory):
        words = query.lower().split()
        score = sum(word in memory.content.lower() for word in words)
        return score * memory.importance


    def retrieve(self, query, top_k=5):
        scored_memories = [(memory, self._score(query, memory)) for memory in self.memories]
        scored_memories.sort(key=lambda x: x[1], reverse=True)
        return scored_memories[:top_k]
    
if __name__ == "__main__":
    m1 = Memory(
    id="m1",
    npc_id="npc001",
    content="I saw Barbie in the rose garden",
    timestamp=100,
    importance=0.9
    )
    m2 = Memory(
        id="m2",
        npc_id="npc001",
        content="Edward looked very nervous today",
        timestamp=200,
        importance=0.5
    )
    m3 = Memory(
        id="m3",
        npc_id="npc001",
        content="Barbie has been spending a lot of time alone recently",
        timestamp=300,
        importance=0.7
    )
    memories = [m1, m2, m3]
    retriever = Retriever(memories)
    results = retriever.retrieve("Barbie")
    print(results)
    