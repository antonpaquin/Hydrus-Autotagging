## Installation

Requires: python, pip

```
# Clone the repository to get this code:
git clone https://github.com/antonpaquin/Hydrus-Autotagging

# Go to the illust2vec-flask project
cd Hydrus-Autotagging/illust2vec-flask

# Get the model
wget https://github.com/antonpaquin/Hydrus-Autotagging/releases/download/0.1/illust2vec.h5
# Or just download it yourself and put it here

# Create a virtualenv to keep your python clean
virtualenv env --python=/usr/bin/python2
source env/bin/activate

# download requirements
pip install -r requirements.txt

# Run the local server
python __main__.py

# Add the parsing script to hydrus
network > manage parsing scripts > import > from png 
(select Hydrus-Autotagging/illust2vec-flask/parsing_script.png)
apply

# Add parsing scripts to your hydrus tag management panel
file > options > tag suggestions > file lookup scripts > show file lookup scripts on single-file manage tags windows
apply
```

## Usage

The parsing script requires the server to be running. To start the server when it has stopped,
```
cd Hydrus-Autotagging/illust2vec-flask
source env/bin/activate
python __main__.py
```

To get tags for an image,
```
right click > manage > file's tags > fetch tags
```

You can set the tag certainty threshold of the model (lower threshold == more tags, less quality)
```
network > manage parsing scripts > illust2vec > edit
threshold > edit
keep the "threshold" key, set the value to a number between 0 and 1 (default is 0.5)
```
