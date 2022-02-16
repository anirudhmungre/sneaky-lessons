# Installing Tools and Packages After Upgrading to Catalina

Students with existing Anaconda installations are encouraged to reinstall both Anaconda (and MongoDB if applicable). The following instructions apply for both scenarios.

Follow these installation instructions in this order to avoid any additional complications.

## zsh vs bash terminal

The new macOS default terminal is `zsh`; moving forward, we are instructing students to use the bash terminal instead.

To use `bash` as the default terminal, open a zsh terminal and run the command `chsh -s /bin/bash`.

Each time a terminal window is opened, this message will appear:

```bash
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
```

Students and instructional staff should be advised to disregard that message and continue to use `bash`.

## Homebrew

If Homebrew isn't already installed, use the [official documentation](https://brew.sh/) to install it to your computer.

## Anaconda

Install Anaconda using official documentation instructions.

**Note**: Previously installed versions of Anaconda have been relocated to a different folder (which is why everything broke), so simply reinstalling it will not generate any excess errors or issues.

### Virtual Environments

New venvs will need to be created after installing/reinstalling Anaconda. Execute the following command to create a new environment: `conda create --name myenv python=3.7`.

Activate a new environment with `conda activate myenv`.

### Jupyter Notebook

With a fresh installation of Anaconda, Jupyter Notebook works as expected. After creating a new venv and activating it, attempting to run Jupyter Notebook via the terminal may result in an error regarding a "missing package". To fix, Jupyter Notebook will need to be installed using the command `python3 -m pip install jupyter` (while the venv is active).

Install other necessary packages with the `pip` command.

## ChromeDriver

Use Homebrew to install ChromeDriver by running `brew cask install chromedriver` in the bash terminal.

### Splinter/BeautifulSoup

The first time code is created to execute a scrape using ChromeDriver, you may encounter an error saying that Chromedriver isn't allowed. To fix this, you'll need to change a setting in System Preferences.

From System Preferences, navigate to Security & Privacy.

Click the "Allow Anyway" button next to the message about chromedriver being blocked. This may prompt you to click the lock to make changes (and input your password). After making those changes, return to your Jupyter Notebook and re-run the code.

![Example Screenshot](privacy-settings.png)

## MongoDB

Install MongoDB using the following commands in the bash terminal:

1. `brew tap mongodb/brew`
2. `brew install mongodb-community@4.2`
3. `brew services start mongodb-community@4.2`

To run mongo manually:

* `mongod --config /usr/local/etc/mongod.conf --fork` **This will replace the `mongod` command we used previously! This will be run each time a student wants to start a MongoDB instance**

To exit the Mongo shell:

* `quit()`
