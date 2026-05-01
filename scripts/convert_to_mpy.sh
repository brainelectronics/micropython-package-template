#!/bin/bash
#
# Cross compile all *.py files of a given directory into .mpy files
#
# The output directory should be the same if upy-package validation is used
# as it extracts the packages directory from the setup.py file
#
# Run the script like:
# sh scripts/convert_to_mpy.sh be_upy_blink/
#

source_dir=${1%/}
mpy_file_extension="mpy"
target_dir=${source_dir}

echo "Processing *.py files in ${source_dir}"

for file in ${source_dir}/*.py; do
    filename=$(basename -- "${file}")
    filename_without_extension="${filename%.*}"

    echo "Compiling ${file} to ${target_dir}/${filename_without_extension}.${mpy_file_extension}"

    # the "bytecode 6" is supporting v1.19.x and higher
    # https://docs.micropython.org/en/v1.28.0/reference/mpyfiles.html#versioning-and-compatibility-of-mpy-files
    mpy-cross \
        --bytecode 6 \
        -v ${file} \
        -o ${target_dir}/${filename_without_extension}.${mpy_file_extension} \
        -v
done
