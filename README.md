# SSO-auto-login
SSO auto login at university of miyazaki




# Installation
1. Please intall python in advance
2. You need check your Google Chrome browser version in settings.
![image](https://user-images.githubusercontent.com/115391575/212496621-4c19a73d-f7f5-403b-a870-a5a63e0107f5.png)


3. Rewrite the version you just checked in the chromedriver-binary section of requirements.txt. If it is the version in the image, change requirements.txt as follows
```
chromedriver-binary == 109.0.5414.75
```

4. Install packages
```
pip install -r requirements.txt
```

If you get the following error, please select the 「chromedriver-binary」 version that is smaller and closest to your version.
![image](https://user-images.githubusercontent.com/115391575/212497730-e6022275-2998-4048-82a9-ec1e4749a8f3.png)


# Usage
execution
```
python sso_auto_login.py <username> <passward> <minutes>
```
sso_auto_login.py must take three command arguments.

Args
- username: your SSO username
- passward: your SSO passward
- minutes: You can choose how often you want to monitor the login screen. ex) 30

