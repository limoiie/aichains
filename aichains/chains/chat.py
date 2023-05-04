from typing import Optional

from langchain import LLMChain, OpenAI, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

from aichains.annotators import render_output

template = """Assistant is a large language model trained by OpenAI.

Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics.
As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

Assistant is constantly learning and improving, and its capabilities are constantly evolving.
It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions.
Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics.
Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

{history}
Human: {question}
Assistant:"""

prompt = PromptTemplate(
    input_variables=['history', 'question'],
    template=template
)

chain: Optional[LLMChain] = None


@render_output
def chat(question: str, temperature=0.2, history_len=2, streaming=True, verbose=None):
    global chain
    if chain is None:
        chain = LLMChain(
            llm=OpenAI(temperature=temperature, streaming=streaming),
            prompt=prompt,
            verbose=verbose,
            memory=ConversationBufferWindowMemory(k=history_len),
        )

    if verbose is not None:
        chain.verbose = verbose

    return chain.predict(question=question, )
