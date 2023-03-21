# this-is-my-portfolio
First iteration of my portfolio site. 

## Features
- Adding new projects
- Animated cards
- SQLite database

## Installation
- Install Python: If you haven't installed Python already, download the latest version of Python from the official website (https://www.python.org/downloads/), and install it on your system.
- Open Command Prompt: Press the Windows key + R to open the Run dialog box. Type "cmd" and press Enter to open the Command Prompt.
- Navigate to the directory containing your Python script: Use the "cd" command to navigate to the directory where your Python script is saved. For example, if your script is saved on the desktop in directory, type "cd C:\Users<username>\Desktop\myapp" and press Enter.
- Run the Python script: Once you are in the directory where your script is saved, type "python <filename>.py" and press Enter. Replace <filename> with the name of your Python script. Your script will run, and the output will be displayed in the Command Prompt.

### Dependencies installation
- To install the dependencies from a requirements.txt file in your Python web app, you can follow these steps:
- Open a Command Prompt or terminal: To install the dependencies, you will need to use the command prompt or terminal on your system.
- Navigate to the directory where the requirements.txt file is located: Use the "cd" command to navigate to the directory where the requirements.txt file is located. For example, if the file is located in a folder called "myapp" on your desktop, type "cd C:\Users<username>\Desktop\myapp" and press Enter.
- Activate the virtual environment (if you are using one): If your Python web app is using a virtual environment, make sure to activate it before proceeding. You can activate the virtual environment using the command: ``` .\venv\Scripts\activate ``` or any other you are usually using.
- Install the dependencies: To install the dependencies from the requirements.txt file, run the following command: ``` pip install -r requirements.txt ```

## Run
Website should run on ``` http://127.0.0.1:5000 ```. Head there on your browser and you should see something like this:
![image](https://user-images.githubusercontent.com/106775028/226760833-5410e84c-2f4f-4f68-8c4d-1c4b8b136b77.png)

## Modify database with your projects 
You can use ```DB Broweser (SQLite)``` app to modify current database file.
- Alterantively you can delete ```project.db``` from ```instance``` directory. And delete `#` from comments in `main.py` file from lines `23` and `24` this will create an empty database file.
### 
Adding projects to database is as simple as heading to `http://127.0.0.1:5000/add`
![image](https://user-images.githubusercontent.com/106775028/226761620-d35da6b5-5501-4371-bbe1-f07f2be9d9bf.png)

Now all you need to do is fill these fields. Images to a project should be uploaded to `C:\Users<username>\Desktop\myapp\static\images` and they need to be square sized for best experience, like: `240x240`px
