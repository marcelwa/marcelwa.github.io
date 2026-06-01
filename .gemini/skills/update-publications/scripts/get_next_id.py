import os
import re

def get_next_id(year):
    publications_dir = '_publications'
    pattern = re.compile(rf'^{year}_(\d{{3}})\.md$')
    
    max_num = 0
    if os.path.exists(publications_dir):
        for filename in os.listdir(publications_dir):
            match = pattern.match(filename)
            if match:
                num = int(match.group(1))
                if num > max_num:
                    max_num = num
    
    return f"{year}_{max_num + 1:03d}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        year = sys.argv[1]
    else:
        from datetime import datetime
        year = datetime.now().strftime("%Y")
    print(get_next_id(year))
