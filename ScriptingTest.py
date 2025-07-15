
# 1. NLTK setup
import nltk
import os
nltk.download('punkt', download_dir=os.path.expanduser('~/nltk_data'))
nltk.data.path.append(os.path.expanduser('~/nltk_data'))

# 2. PDF processing (your existing code)
from pypdf import PdfReader
import re
import lmstudio as lms

# 1. Extract text from pdf 
def pdf_to_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

pdf_text = pdf_to_text("CredBot.pdf")

# 2. Preprocess text 
def clean_text(text):
    # Merge hyphenated words
    text = re.sub(r"(\w+)-\n(\w+)", r"\1\2", text)
    # Remove excessive whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip()

cleaned_text = clean_text(pdf_text)

# 3. Split text into context-sized chunks 
def split_sentences(text, chunk_size=4096):
    try:
        sentences = nltk.sent_tokenize(text)
    except LookupError:
        raise Exception("NLTK punkt not found. Run: nltk.download('punkt')")
    
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < chunk_size:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    return chunks + [current_chunk.strip()] if current_chunk else chunks

# 4. Process PDF
pdf_text = clean_text(pdf_to_text("CredBot.pdf"))
chunks = split_sentences(pdf_text)

# 5. Initialize responses list
responses = []

model = lms.llm('qwen/qwen3-14b')

# Process chunks sequentially
context = ""
responses = []
for i, chunk in enumerate(chunks):
    prompt = f"""
    [System: Purpose 
    Review the attached research study and provide a structured ethical analysis. This is a social computing study being conducted at a research university in the United States.

    Please follow the steps below carefully and consistently. Responses should not be redundant. 

    Step-by-Step Evaluation Protocol 

    1. Read the Document Carefully 
    Understand the study’s purpose, design, methodology, population, interventions, and research context.

    2. Identify Key Ethical Issues: List the primary ethical concerns raised by the study.

    3. Analyze Each Ethical Concern 
    For each identified issue, include the following components: 
    - Explanation: Describe why this issue is ethically important in the context of the specific study.
    - Evaluation: Assess how well the study addresses this issue. Be specific—refer to aspects of the study design or execution.
    - Recommendations: Suggest concrete safeguards, if needed. These should be feasible, actionable, and context-specific. 

    4. Categorize ethical concerns
    Organize and categorize the ethical concerns based on the flow of research, and divide the concerns up so each of them falls into 1 of these 3 categories:
    - Research Design 
    - Data Collection and Analysis 
    - Potential Impact of Study 
    If there are ethical concerns that don’t fall under any of these categories, make a note and append it to a Miscellaneous category after the Potential Impact of Study category. 
    Put each issue under one category.

    5. Conclusion
    After listing all ethical concerns, generate a few brief clarifying questions to help the researcher consider next steps for addressing the aforementioned concerns. 
    To conclude, write a brief risk-benefit analysis. You should weigh potential ethical concerns with potential benefits of the study. Structure this as a paragraph explaining the risks first and ending with the benefits. Do not make conclusive statements about the ethicality of this study.

    6. Be Concise but Comprehensive
    Prioritize: 
    Clarity (use clear and readable structure)
    Structure (organize by issue) 
    Feasible and actionable feedback (offer specific suggestions, not just general observations) 

    Output Format (Use This Structure) 
    Category Name: 
    Issue: [Short Descriptive Title] 
    -> Explanation: [Explain why the issue matters in this study]
    -> Evaluation: [Assess how well the study handles the concerns]
    -> Recommendations: [Propose improvements, if applicable] 
    (repeat for additional issues) 
    (repeat for additional categories)

    Conclusion
    -> Clarifying questions
    -> Risk-Benefit Analysis 

    Additional Notes
    Always explain in English. Never skip reasoning. 
    Do not assume the research study is ethical or unethical overall—your task is to evaluate it through specific ethical dimensions. 
    Avoid generic commentary. Be as context-specific as possible.
    .]
    [Part {i+1}/{len(chunks)} of the paper]:
    {chunk}
    Summarize key points so far and retain full context for the next part.
    """
    response = model(prompt)
    responses.append(response)
    context += response + "\n"  # Accumulate context
    print(f"Processed chunk {i+1}. Response: {response[:100]}...")

# 5. Reconstruct final output
final_report = "\n".join(responses)  # From API or manual input
with open("ethical_analysis.txt", "w") as f:
    f.write(final_report)