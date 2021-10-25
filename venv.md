## Setup a Development Environment
-  Update Python to 3.8:
   - `sudo apt-get install python3.8`
   - `sudo update-alternatives –install /usr/bin/python3 python3 /usr/bin/python3.8 2`
   - `sudo update-alternatives –config python3`
   - Select the option for Python 3.8
- Install Python’s Virtual Environment Tool: ‘pip3 install virtualenv‘
-  Change to your ”home directory” for the next step. For all the operating systems we are
aware of, you accomplish this simply by typing ‘cd‘ and then pressing enter at the command
line.
- Create a Python 3 virtual environment for Augur: `virtualenv –python=python3 testing-assignment`. Alternately, you can use `python3 -m venv testing-assignment` without installing virtualenv. Use whatever works best for your current laptop.
- Activate your virtual environment `source testing-assignment/bin/activate` (In the case of Ubuntu,
you get the ‘source‘ command automatically put into your path using the ‘bash‘ shell. So, if
you get an error, type ‘bash‘ and then hit the enter key and try again.)
