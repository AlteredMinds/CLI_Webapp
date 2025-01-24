# CLI Accessible Resume Web App

A web application designed for accessing a website through a command line interface. Built with Flask, this app formats content information for terminal-based access, providing a unique way to explore my professional profile.

## Overview

This project creates a web app that present my professional profile through CLI interactions. It is built using Flask and serves content based on user-agent detection to ensure that the app is accessed through CLI tools like `curl`, `wget`, or `powershell`.

## Features

The application offers the following features:

- **CLI Compatibility**: Responds to specific user agents associated with CLI tools and provides instructions tailored for those tools.
- **Content Routes**: Provides routes for viewing different sections of the resume and portfolio in a text-based format.
- **Restricted Access**: Restricts access to user agents other then `curl`, `wget`, or `powershell` with a custom denial page.

### Routes

1. **`/` (Home Route)**  
   Displays a welcome message and navigation instructions based on the user agent. If accessed by non-CLI user agents, a denial page is shown.

2. **`/portfolio`**  
   Shows a list of projects and their descriptions, accessible in a text-based format for CLI users.

3. **`/resume`**  
   Provides a detailed resume including education, skills, certifications, and work experience in a text-based format.

4. **`/about`**  
   Shares background information and the professional journey of the user in a text-based format.

5. **`/contact`**  
   Displays contact information in a text-based format.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/AlteredMinds/CLI_Webapp.git
   cd CLI_Webapp
2. **Install Dependencies**
   Ensure you have Python 3.8 installed, then install the required packages:
   ```bash
   pip install Flask
4. **Run the Application**  
   Start the application by navigating to the directory containing app.py and running:
   ```bash
   python3 app.py 

The application will be accessible at http://127.0.0.1:5000.

## Help

Page Not Loading?

If you're having trouble loading the page, ensure the application is running in debug mode. Verify that line 99 in app.py is set as follows:

    app.run(debug=True, host='0.0.0.0')

Deploying the Application?

For deployment, make sure the application is behind a WSGI server and reverse proxy. In this case, line 99 in app.py should be updated to:

    app.run()
