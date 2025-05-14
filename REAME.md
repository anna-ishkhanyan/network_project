# Comic Downloader

## Description

This is a network programming project written  in Python to automate the download of comic images from the [GoComics](https://www.gocomics.com) website. The program allows users to select from a list of cat-themed comics and input a specific date to download the comic image for that specific day.

The downloader uses:
- **Selenium** to handle JavaScript-rendered content.
- **BeautifulSoup** to parse HTML.
- **Requests** to fetch image content.
- **Pillow (PIL)** to save the image as a JPEG.

## Features

- Menu to choose from multiple cat-themed comics.
- Supports date-based retrieval in `YYYY-MM-DD` format.
- Downloads and saves the comic locally.
- Headless browser mode for reduced overhead.

## Installation

You can use the provided `Makefile`:

```bash
make
