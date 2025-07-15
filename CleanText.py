import re

def clean_text_file(text):
    # Step 1: Remove page numbers and headers
    text = re.sub(r'^\d+$\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'UIST ’25, 2025, Busan, Korea.*?\n', '', text, flags=re.DOTALL)
    
    # Step 2: Fix hyphenations
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    
    # Step 3: Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # Step 4: Remove empty lines and artifacts
    lines = text.split('\n')
    cleaned_lines = [line for line in lines if line.strip() and not re.match(r'^[\d\s]*$', line)]
    text = '\n'.join(cleaned_lines)
    
    # Step 5: Fix section headers (optional)
    text = re.sub(r'(\n\d+\.\d+\s+.+?\n)', r'\n\1\n', text)
    
    return text.strip()

# Read the file
with open('CredBot_Paper.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()

# Clean and save
cleaned_text = clean_text_file(raw_text)
with open('CredBot_Paper_CLEANED.txt', 'w', encoding='utf-8') as f:
    f.write(cleaned_text)