from vllm import LLM, SamplingParams

llm = LLM(model="meta-llama/Llama-2-7b-hf")

sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.95,
    max_tokens=200
)

prompt = "Explain Retrieval-Augmented Generation"

outputs = llm.generate(prompt, sampling_params)

for output in outputs:
    print(output.outputs[0].text)
