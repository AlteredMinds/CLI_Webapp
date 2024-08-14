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
   Shows a list of projects and their descriptions.

3. **`/resume`**  
   Provides a detailed resume including education, skills, certifications, and work experience.

4. **`/about`**  
   Shares background information and my professional journey.

5. **`/contact`**  
   Displays contact information.
