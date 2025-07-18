import re 
import os

"""
Convert raw report as a txt file to a string, then further clean it
"""
def preprocess_report(text):
    """
    Preprocceses the report in the form of a string and returns a raw, cleaned string.
    """
    text = text.lower() # convert all to lower-case
    text = text.replace('-', ' ') # keeps hyphenated words as separate
    text = re.sub(r'[^a-z0-9\s]', '', text) # Remove non-alphanumeric characters (keep spaces)
    return text
    
def save_cleaned_text(input_filepath, output_filepath):
    """
    Reads a raw text file, preprocesses its content, and saves the
    cleaned content (as a space-separated string of words) to a new file.
    """
    try:
        with open(input_filepath, "r", encoding="utf-8") as f_in:
            raw = f_in.read()

        # Preprocess the text to get a set of unique words
        # For saving, we'll convert it back to a space-separated string
        cleaned_set = preprocess_report(raw)
        cleaned_str = " ".join(sorted(list(cleaned_set))) # Sort for consistent output

        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        with open(output_filepath, "w", encoding="utf-8") as f_out:
            f_out.write(cleaned_str)
        print(f"  Cleaned and saved: {output_filepath}")
    except Exception as e:
        print(f"Error processing {input_filepath}: {e}")


def txt_to_string(filepath):
    """
    Reads a cleaned text file and returns its content as a single string.
    Assumes the file contains space-separated words.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            return content # Return as a single string
    except FileNotFoundError:
        print(f"Error: Cleaned file not found at {filepath}")
        return ""
    except Exception as e:
        print(f"Error loading cleaned text from {filepath}: {e}")
        return ""

def file_to_string(dir):
    strlist = []
    labels = [] 
    if os.path.exists(dir):
        for dirpath, _, filenames in os.walk(dir):
            for filename in sorted(filenames):
                filepath = os.path.join(dirpath, filename)
                if filename.endswith('txt'):
                    cleaned_text = txt_to_string(filepath)
                    if cleaned_text:
                        strlist.append(cleaned_text)
                        labels.append(os.path.relpath(filepath, dir))
    return strlist, labels

"""
def preprocess_paper(p):
    # Step 1: Remove page numbers and headers
    p = re.sub(r'^\d+$\n', '', p, flags=re.MULTILINE)
   
    # Step 2: Fix hyphenations
    p = re.sub(r'(\w+)-\n(\w+)', r'\1\2', p)
    
    # Step 3: Normalize whitespace
    p = re.sub(r'\s+', ' ', p)
    p = re.sub(r'\n\s*\n', '\n\n', p)
    
    # Step 4: Remove empty lines and artifacts
    lines = p.split('\n')
    cleaned_lines = [line for line in lines if line.strip() and not re.match(r'^[\d\s]*$', line)]
    p = '\n'.join(cleaned_lines)
    
    # Step 5: Fix section headers (optional)
    p = re.sub(r'(\n\d+\.\d+\s+.+?\n)', r'\n\1\n', p)
    
    return p.strip() 
"""
