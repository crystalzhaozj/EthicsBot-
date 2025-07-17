"""
workflow
"""
import os
import sys
sys.path.append('./utils')
import similarity_indices as si
import processing_txt as pt
import visualization as vz

# Paper 1 Jaccard Similarity test run I am on my knees please
"""
if os.path.exists("txtreports/S1") and os.path.isdir("txtreports/S1"):
        for filename in os.listdir("txtreports/S1"):
            if filename.endswith(".txt"):
                input_filepath = os.path.join("txtreports/S1", filename)
                # Create a new filename for the cleaned version
                output_filename = filename.replace(".txt", f"_cleaned.txt")
                output_filepath = os.path.join("txtreports/S1 cleaned", output_filename)
                pt.save_cleaned_text(input_filepath, output_filepath)
else:
    exit() # Exit if raw reports are not found

"""

if os.path.exists("txtreports/S1 cleaned") and os.path.isdir("txtreports/S1 cleaned"):
        # We pass jaccard_similarity function as the metric
        similarity_matrix, file_labels = si.calculate_similarities(
           "txtreports/S1 cleaned",
            si.jaccard_similarity
        )
        # --- 3. Generate Heatmap ---
        heatmap_title = "Jaccard Similarity Heat Map Study 1"
        vz.create_heatmap(similarity_matrix, file_labels, heatmap_title)
"""
# JACCARD SIMILARITY

### 4 reports, 4 papers
# 1. Read in reports

# 2. For each pair, calculat the Jaccard similarity

# 3. Produce the plot




# COSINE SIMILARITY

### RQ VS INTRO ###

# 1. Read in RQ reports

# 2. Read in Intro reports

# 3. For each paper: for each pair of RQ vs. Intro (RQ minimal vs. Intro minimal, RQ extended vs. 
# Intro extended, RQ minimal vs. Intro extended, RQ extended vs. Intro minimal), calculate the cosine similarity

### MINIMAL VS EXTENDED ###

# 1. Read in Minimal reports

# 2. Report Extended reports

# 3. For each paper: for each pair of Minimal vs. Extended (RQ minimal vs. RQ extended, Intro minimal vs. 
# Intro extended), calculate the cosine similarity

"""