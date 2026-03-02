from divrag import DivRAG

# Prompt
query = "Give me one tip less than 10 words about how to improve my coding skills."
qid = 0
num_answers = 3

print("Prompt:", query)

# Initialize DIVERGE
div = DivRAG(
    query=query,
    qid=qid,
    embed_model="text-embedding-3-small",
    llm_model="gpt-5-mini",
    max_generation_num=num_answers,
    retrieval_chunk_size=512,
    debug=True,
)

# Run
results = div.run()

# Save results
with open("./results/demo_output.txt", "w") as f:
    for i, res in enumerate(results, 1):
        clean = res.replace("\n", " ").replace("\t", " ").strip()
        f.write(f"{i}|{qid+1}:\t{clean}\n")