from langchain_core.prompts import ChatPromptTemplate

def generate_summary(text, instructions, summarizer, llm):
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
        return response.content.strip()
    except Exception as e:
        print(f"Error in custom summary: {e}")
        # Fallback to bart-large-cnn if ChatOllama fails
        summary = summarizer(text, max_length=200, min_length=30, do_sample=False)

        return summary[0]['summary_text']