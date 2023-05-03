# 📩 Send LinkedIn Connection Request from Excel file 🗂️

This script will help you automate sending connection requests on LinkedIn with an excel containing first and last name. 

## 📚 Requirements

1. Python 3.6 or higher
2. pip (Python package installer)
3. Chrome browser
4. ChromeDriver

## 📥 Installation & Setup

### 1. Install Python

🔗 [Download Python](https://www.python.org/downloads/) and follow the instructions for your operating system.

### 2. Install required Python packages

📦 Run the following command in your terminal/command prompt to install the necessary packages:
```
pip install pandas selenium openpyxl
```

### 3. Download ChromeDriver

🔗 [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your Chrome version and operating system. Extract the downloaded file and save it to a location on your computer.

### 4. Update the script

📝 Open the script in anycode editor and replace the following:

- Replace `yourusernamehere` and `yourpasswordhere` with your LinkedIn username and password. Or you can type it in manually in the chromedriver.

```python
linkedin_username = "yourusernamehere"
linkedin_password = "yourpasswordhere"
```
-Update the path to the Excel file containing the list of names.
```
data = pd.read_excel("C:/Users/your_username/location/namelist.xlsx", engine='openpyxl')
```
-Update the executable_path parameter with the path to your ChromeDriver.
```
driver = webdriver.Chrome(executable_path="C:/Users/your_username/location/chromedriver.exe", options=options)
```
-Modify the waiting time.
To change the time the script waits before moving on to the next person, locate the following line of code in the script:
```
time.sleep(5)
```
Replace the number 5 with your desired waiting time in seconds.

# 🏃‍♂️ How to run the script

1. Open a terminal/command prompt and navigate to the folder containing the script.
2. Run the script with the following command:
```
python linkedinscript.py
```

(Replace `linkedinscript.py` with the actual name of the script file if you changed it)

3. The script will open a Chrome window and navigate to the LinkedIn login page.
4. Manually complete any CAPTCHAs or other security checks if needed.
5. Press `Enter` in the terminal/command prompt to start the automation process.

🎉 The script will now go through the names in the Excel file and send connection requests on LinkedIn. Enjoy your automated connections! 🤖
(Updated- check the changed the script so you have to click the connect botton yourself)


