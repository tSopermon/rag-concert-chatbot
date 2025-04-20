from langchain_core.prompts import ChatPromptTemplate

def generate_summary(text, instructions, llm):
    """
    Generate a custom summary of the text using the specified instructions.
    args:
        text (str): text to be summarized.
        instructions (str): instructions for the summary.
        llm: language model to be used.
    returns:
        summary (str): generated summary.
    """
    summary_prompt = ChatPromptTemplate.from_template(
        """
        Summarize the following concert document based ONLY on these instructions: {instructions}.
        Document: {text}
        """
    )
    try:
        chain = summary_prompt | llm
        response = chain.invoke({"instructions": instructions, "text": text})
    except Exception as e:
        print(f"Error generating summary: {e}")

    return response.content.strip()
