---
title: "reMarkable Quickshare Bot"
slug: "rm-quickshare-bot"
order: 6
description: "A Telegram-based automation tool to instantly fetch, format, and push web articles to the reMarkable tablet."
repository_url: "https://github.com/K41R0N/RM-quickshare-bot"
language: "Python"
version: "1.1.0"
license: "MIT"
---

## Overview

The **reMarkable Quickshare Bot** is an open-source Python utility designed for voracious readers who prefer e-ink over backlit screens. Operating primarily through a Telegram bot interface, users can simply paste a URL into their chat, and the bot will autonomously scrape the article, strip out ads and trackers, format it for perfect e-ink readability (ePub or PDF), and upload it directly to their reMarkable cloud account.

## Core Problem Solved

While the reMarkable tablet is unparalleled for focused reading and annotation, getting web content onto the device is a notoriously clunky process. The official browser extensions often fail on paywalled or heavily JavaScript-rendered sites, and require the user to be at their desktop computer.

This bot solves the "read-it-later" friction. Because it runs via a messaging app (Telegram), a user can be browsing Twitter or Hacker News on their phone, copy a link, send it to the bot, and by the time they pick up their reMarkable tablet, the article is already synced and waiting in their "Inbox" folder.

## Key Features

- **Headless Article Extraction:** Uses robust parsing libraries (like `newspaper3k` or `Readability`) to extract the core title, author, and body text while stripping away navigation menus, cookie banners, and advertisements.
- **E-ink Typography Formatting:** Generates clean, distraction-free PDFs or ePubs with typography (font size, line height, margins) specifically optimized for the reMarkable's 10.3-inch display.
- **Telegram Bot Interface:** Provides an asynchronous, conversational UI. The bot acknowledges receipt, provides progress updates during the scraping/conversion phase, and confirms successful sync.
- **rmAPI Integration:** Integrates deeply with the unofficial reMarkable API to handle cloud authentication, folder navigation, and secure file uploads.

## Technologies Used

- **Python 3:** Core application logic.
- **python-telegram-bot:** Asynchronous framework for managing the chat interface.
- **rmapy / rMAPI:** Libraries for authenticating and communicating with the reMarkable cloud infrastructure.
- **pdfkit / wkhtmltopdf:** For rendering the extracted HTML into perfectly sized PDFs.