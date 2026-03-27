
# Comic PDF Script Cleaner
The purpose of this script is to help letter freinds who get all kinds of crazy scripts back from writing software (like Highland, Final Draft, or Scrivener). This script takes a `.pdf` input and outputs a `.txt` file. It uses Python to clean line breaks and removes tabs formatting.

## Requirements
- python3
- pymupdf

## Setting up Python
1. **Install Python**: download from [python.org](https://www.python.org/) and run the installer. Check "Add Python to PATH" during install.
2. **Open Terminal** (mac) or **Command Prompt** (windows)
3. **Install pymupdf**: use `pip install pymupdf` to install the package.

## Setting up the script
1. Make sure you're in the right folder `cd ~/your-folder/comic-cleaner`
2. **Add the PDF to the same folder as `clean.py`** so the script knows where to extract the text from
3. **Run the script** in the terminal by running `python clean.py your-file.pdf` (replace `your-file.pdf` with the title of your pdf file)


## Input
The input for this script must be a `.pdf` file. 

![alt text](image.png)

## Output
Output aims to:
- preserve `PAGE` headers to help flag page breaks (adds `---` before the word `PAGE`)
- Uses Capitalized words to add a line break before - to help with character name breaks like `CAPTION` and panels like `PANEL 2`
- Removes returns that are auto-inserted by scripting software


```
PAGE 10

PANEL 1
The elevator doors open, casting light into the sub level "control". There are soft lights in a dark room. Computer screens,  scrawling endless lines of code. Wires. As we progress further  into the room, the colors from the forest place will start to  seep in, as they are being cast out by a giant display at the  middle point of the room. 

CAPTION, THE VOICE
You stopped helping people.

PANEL 2
Samson is drawn forward by the big display in the middle of the  room.

SAMSON
What else was I supposed to do?
```
