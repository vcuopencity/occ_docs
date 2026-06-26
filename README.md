# OpenCyberCity Testbed Documentation

[![Build and deploy docs](https://github.com/vcuopencity/occ_docs/actions/workflows/docs.yml/badge.svg)](https://github.com/vcuopencity/occ_docs/actions/workflows/docs.yml)

This repository contains the documentation source for the OpenCyberCity Testbed project, including system architecture, design specifications, and user guides. You can access the documentation by going to: [www.vcuopencity.github.io/occ_docs](www.vcuopencity.github.io/occ_docs)

## Features

- **Built with Sphinx**: The documentation is built using the Sphinx documentation generator, which allows for easy creation of professional-looking documentation.
- **Markdown Support**: The documentation is written in Markdown, making it easy to read and write. No need to learn reStructuredText (reST), or write HTML. Any exisiting documentation can be easily ported to this repository.
- **Automatic Table of Contents**: The documentation includes an automatically generated table of contents, making it easy to navigate through the different sections.

- **Search Functionality**: The documentation will include a search feature, allowing users to quickly find the information they need. (This feature is only available when the documentation is served through a [web server](#web-server))

- **Build Automation**: The documentation will be automatically built upon changes and deployed to a web server, ensuring that the latest version is always available to users.

- **No-cost Hosting**: The documentation will be hosted using GitHub Pages, making it accessible to all users without any cost.

### Website Preview
<img src="images/sphinx_rtd_theme.png" alt="Sphinx RTD Theme" width="100%" />

## Contributing to the Documentation

Check out the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to contribute to the documentation.

## Collaboration

Since the website is only deployed on pushes to main, if you wish to collaborate on your documentation and only deploy it when it is completely ready, simply create a new branch, and make your commits there. 

Once you are ready to deploy, simply submit a pull request, and once your branch has been merged, your work will show up on the website.

## Building Documentation Locally
While working on your documentation, you can preview what it looks like and resolve build errors by deploying the website locally.

If you wish to preview the documentation, you can do so by following these steps:

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/vcuopencity/occ_docs.git
    ```
2. Navigate to the cloned repository.
    ```bash
    cd occ_docs
    ```
3. Create a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

4. Install the required dependencies.
    ```bash
    pip install -r requirements.txt
    ```

5. Build and launch the website!
    - Launch an HTTP server to serve the documentation locally. You can use Python's built-in HTTP server for this purpose:
    ```bash
    cd docs/
    make serve
    ```
    - This will start a local web server at `http://localhost:8000`. You can open this URL in your web browser to view the documentation.

    *If you have any questions, comments, or concerns, please feel free to ask: diwany@vcu.edu*