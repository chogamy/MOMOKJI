from langchain.llms import HuggingFace
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


if __name__ == "__main__":
    llm = HuggingFace(model_name="gpt-neo-125m")

    # 프롬프트 템플릿 설정
    prompt = PromptTemplate(
        input_variables=["preferences"],
        template="I like {preferences}, what food would you recommend?",
    )

    # LLMChain 설정
    chain = LLMChain(llm=llm, prompt=prompt)

    respones = chain.run()
