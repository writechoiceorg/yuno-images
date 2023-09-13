import os
import glob
import re

cwd = os.getcwd()

png_files = glob.glob(os.path.join(cwd, "*.png"))

for png_file in png_files:
    file_name, file_extension = os.path.splitext(png_file)

    # match = re.search(r"icons8-(.*?)-100", file_name)
    # match = re.search(r"(.*?)-circular", file_name)
    match = re.search(r"(.*?)-flag", file_name)
    if match:
        country_name = match.group(1) + file_extension

        new_file_name = f"icons8-{country_name}-flag-100{file_extension}"
        os.rename(png_file, country_name)
