import re
import os

def RemoveTag(line):
    line = re.sub(r'\#{1}[^#\s]+', "", line)
    return line

def ConvertFile(file):
    # 1. convert the admonition format
    # 2. remove the tag in the line
    with open(file, 'r') as f, open('.temp.md', 'w') as buffer:
        
        match_admonition = False
        for line in f:

            # begin of the admonition
            if re.search('```ad-info', line):
                match_admonition = True
                buffer.write('!!! info' + '\n')
                continue
            # end of the admonition
            elif re.search('\s*```\s*$', line) and match_admonition:
                match_admonition = False
                buffer.write('\n')
                continue
            
            line = RemoveTag(line)

            # If in admonition, add tab before the line
            # Otherwise, output straightforwardly
            if match_admonition:
                buffer.write('\t' + line)
            else:
                buffer.write(line)

        # close files and flush the buffer
        buffer.close()
        f.close()
        os.rename('.temp.md', file)
    return

def ImportFile(file):

    # only markdown file
    if re.search('\.md$', file) is None:
        return
    
    # convert file from obsidian form into mkdocs form
    ConvertFile(file)
    return