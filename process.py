import sys
import os
import os.path
import pathlib
import re

if(len(sys.argv) < 1):
    print("Pass the location of the tex source code as the first argument to the program.")
    exit(0)

tex_path = sys.argv[1]
tex_path = os.path.join(os.getcwd(), tex_path)

try:
    os.mkdir("content")
except:
    print("The markdown directory has been already created; overwriting any exisiting files.")

tex_file = open(tex_path, "r")
markdown_file = None
problem_counter = 0
for line in tex_file:
    line = line.strip()
    if line.startswith("\\Problem"):
        problem_counter += 1
    line = line.replace("\\Problem", "**Problem " + str(problem_counter) + ":** ")
    line = line.replace("\\TheSolution", "**Solution:**")
    line = line.replace("\\R", "\\mathbb{R}")
    line = line.replace("\\C", "\\mathbb{C}")
    line = line.replace("\\[", "$$")
    line = line.replace("\\]", "$$")
    line = line.replace("\\par", "")
    line = line.replace(" iff ", " if and only if ")
    line = line.replace("\\setcounter{problem}{0}", "")
    line = line.replace("\\end{document}", "")
    print(line)
    if line.startswith("\\subsection*{"):
        problem_counter = 0
        pattern = "\\\\subsection\\*{Chapter ([0-9]+)\\s*:\\s*([a-zA-Z0-9_ ]+)}"
        print(line, pattern)
        pattern = re.compile(pattern)
        regex_match = re.search(pattern, line)
        regex_groups = regex_match.groups()
        file_title = str(regex_groups[0]).zfill(3) + "_" + str(regex_groups[1]).replace(" ", "_")
        print(file_title)
        markdown_path = pathlib.Path("./content/" + file_title + ".md")
        markdown_path.touch(exist_ok=True)
        if markdown_file:
            markdown_file.close()
        markdown_file = open(markdown_path, "w")
        markdown_file.write("Title: " + str(regex_groups[1]) + "\n")
        markdown_file.write("Category: Whittaker-Watson\n")
        markdown_file.write("Date: 2022-07-27 12:00\n")
    elif markdown_file is not None:
        markdown_file.write(line + "\n")
