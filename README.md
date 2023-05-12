# LinkedIn Job Saver

This is a Python script that uses the Selenium web driver to automate the process of searching and saving jobs on LinkedIn.

## Getting Started

To use this script, you will need to have Python installed on your computer, as well as the following Python packages:

- Selenium
- dotenv

You will also need to have Chrome web driver installed on your computer and the path to the driver set in the script.

To get started, clone this repository to your local machine and navigate to the project directory. Then, create a file named `.env` in the project directory with your LinkedIn email and password like so:

```
LINKEDIN_ID=your_email_here
PASSWORD=your_password_here
```

## Running the Script

To run the script, open a terminal in the project directory and run the command:

```
python linkedin_job_saver.py
```

The script will open a Chrome window, navigate to the LinkedIn homepage, login with your credentials, search for "frontend intern" jobs, filter for "Easy Apply" jobs, and save all jobs that are listed.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
