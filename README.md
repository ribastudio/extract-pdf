<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Ocr_doc" />

  &#xa0;

  <!-- <a href="https://ocr_doc.netlify.app">Demo</a> -->
</div>

<h1 align="center">Extract PDF</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/{{YOUR_GITHUB_USERNAME}}/ocr_doc?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/{{YOUR_GITHUB_USERNAME}}/ocr_doc?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/{{YOUR_GITHUB_USERNAME}}/ocr_doc?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/{{YOUR_GITHUB_USERNAME}}/ocr_doc?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/ocr_doc?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/ocr_doc?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/ocr_doc?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Ocr_doc 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Describe your project

## :sparkles: Features ##

:heavy_check_mark: Convert PDF file to txt, only text content;\
:heavy_check_mark: Convert PDF file to PDF with selectable text, to find texts where the content are only image based;\
:heavy_check_mark: After convert, the text files version will be zipped to be sent or uploaded/downloaded;

## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Python Packaging](https://packaging.python.org/)
- [PDF2Image](https://pypi.org/project/pdf2image/)
- [Pillow](https://pypi.org/project/pillow/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [PyTesseract](https://pypi.org/project/pytesseract/)
- [tqdm](https://tqdm.github.io/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/)installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/ribastudio/ocr_doc

# Access
$ cd ocr_doc

# Generate env - if you like
$ python3 -m venv .venv
$ source .venv/bin/activate

# Install dependencies
$ python pip install -r requirements.txt

# Run the script
$ python extract.py [file]

# The extract will be convert PDF to TXT or generate an one PDF file to find text, etc
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">{{YOUR_NAME}}</a>

&#xa0;

<a href="#top">Back to top</a>
