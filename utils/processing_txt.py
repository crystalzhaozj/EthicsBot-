import re 

def preprocess_report(text):
    text = text.lower() # convert all to lower-case
    text = re.sub(r'[^a-z0-9\s]', '', text) # Remove non-alphanumeric characters (keep spaces)
    words = set(text.split()) # Split into words and return a list
    return words

def preprocess_paper(p):
    # Step 1: Remove page numbers and headers
    p = re.sub(r'^\d+$\n', '', text, flags=re.MULTILINE)
   
    # Step 2: Fix hyphenations
    p = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    
    # Step 3: Normalize whitespace
    p = re.sub(r'\s+', ' ', text)
    p = re.sub(r'\n\s*\n', '\n\n', text)
    
    # Step 4: Remove empty lines and artifacts
    lines = p.split('\n')
    cleaned_lines = [line for line in lines if line.strip() and not re.match(r'^[\d\s]*$', line)]
    p = '\n'.join(cleaned_lines)
    
    # Step 5: Fix section headers (optional)
    p = re.sub(r'(\n\d+\.\d+\s+.+?\n)', r'\n\1\n', text)
    
    return p.strip() 