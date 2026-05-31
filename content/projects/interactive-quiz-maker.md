---
title: Interactive Quiz Maker
slug: interactive-quiz-maker
order: 9
description: A frontend utility that transforms structured JSON into highly-styled, interactive study quizzes.
repository_url: https://github.com/K41R0N/Interactive-Quiz-Maker
live_url: http://practicequizz.app/
language: CSS / JS
version: 1.0.0
license: MIT
---

## Overview

The **Interactive Quiz Maker** is a lightweight frontend utility designed to transform structured JSON data into engaging, highly-styled study quizzes. It enforces a strict separation of concerns, ensuring that the content layer (the questions, answers, and explanations) is entirely decoupled from the presentation and logic layers.

## Core Problem Solved

Creating interactive educational content often requires educators to hardcode questions directly into HTML or use bulky WordPress plugins. This makes updating quizzes tedious and error-prone. 

This project solves this by treating the quiz content as a simple JSON database. A teacher or student can generate a new quiz entirely by editing a structured text file (or having an LLM generate the JSON array). The JavaScript engine automatically ingests this data, handles state management (score tracking, user selection, answer validation), and renders the UI seamlessly.

## Key Features

- **JSON-Driven Content:** All questions, multiple-choice options, correct answers, and post-answer explanations are stored in a single JSON schema.
- **State Management:** Handles complex interactive states, including locking choices after selection, displaying immediate feedback, and calculating final scores.
- **Responsive Design:** Fully fluid CSS styling that works perfectly on mobile devices, ensuring accessibility for students studying on the go.
- **Zero-Dependency Architecture:** Built with pure vanilla JavaScript and CSS. No React, no Vue, no build step required—meaning it can be dropped into any existing webpage or CMS with zero configuration.

## Technologies Used

- **Vanilla JavaScript (ES6):** Core engine for state management and DOM manipulation.
- **CSS3:** For responsive layout, transitions, and interactive state styling (hover, active, disabled).
- **JSON:** The structural foundation for all quiz data.
