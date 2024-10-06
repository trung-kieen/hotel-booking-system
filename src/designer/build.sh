#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
EXTENSION="*.ui"
OUTPUT_EXTENSION=".py"  # Change this to your desired output extension
# uic -g python form.ui > ui_form.py



for file in "$SCRIPT_DIR"/$EXTENSION; do
    # Check if the file exists (to avoid errors if no files match)
    if [ -e "$file" ]; then
        output_file="${file%.*}$OUTPUT_EXTENSION"
        pyuic5 -x $file -o  $output_file

    else
        echo "No files found with the extension $EXTENSION in $DIRECTORY."
    fi
done
