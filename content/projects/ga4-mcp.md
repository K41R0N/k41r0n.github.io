---
title: "GA4 Model Context Protocol"
slug: "ga4-mcp"
order: 2
description: "An MCP server that empowers AI agents to query, analyze, and visualize Google Analytics 4 data autonomously."
repository_url: "https://github.com/K41R0N/ga4-mcp"
language: "TypeScript"
version: "1.0.0"
license: "MIT"
---

## Overview

The **GA4 MCP (Model Context Protocol) Server** is a crucial bridge between modern AI coding agents (like Claude and local LLMs) and web analytics. By implementing the open-source Model Context Protocol, this server allows autonomous agents to safely authenticate, query, and interpret Google Analytics 4 (GA4) property data directly from their chat environments.

Instead of a human analyst manually clicking through the GA4 dashboard, an AI agent can use this tool to fetch real-time metrics, compare date ranges, and extract traffic insights, turning raw analytics into conversational, contextual intelligence.

## Core Problem Solved

AI agents excel at reasoning, but they are traditionally blind to private, real-time business data. If you ask an LLM, "Why did our conversion rate drop last week?", it cannot answer without external context. 

This project solves the data-silo problem by giving agents a standardized tool (`ga4_run_report`) to execute complex GA4 Data API queries. It translates natural language questions into precise API requests, fetches the dimensions and metrics, and returns structured data that the agent can then synthesize into actionable business intelligence.

## Key Features

- **Standardized MCP Interface:** Fully complies with the Model Context Protocol, making it universally compatible with any MCP-enabled client (e.g., Claude Desktop, Cursor, or custom orchestration scripts).
- **Dynamic Dimension/Metric Discovery:** Exposes a tool allowing agents to query the available GA4 schema, so the LLM can dynamically determine which dimensions (e.g., `city`, `sessionSource`) and metrics (e.g., `activeUsers`, `bounceRate`) are valid for a given property.
- **Advanced Query Support:** Supports complex filtering, date range comparisons, and ordering arrays, allowing the AI to perform deep-dive exploratory data analysis (EDA).
- **Secure Authentication:** Utilizes Google Cloud Service Accounts with strict, read-only OAuth scopes, ensuring the AI agent operates securely without requiring human credential management.

## Technologies Used

- **TypeScript:** Type-safe server implementation.
- **Model Context Protocol (MCP) SDK:** The foundational communication layer for agent-to-tool interaction.
- **Google Analytics Data API (v1):** The official Google library for fetching GA4 reports.
- **Zod:** Runtime schema validation to ensure the LLM provides correctly formatted query payloads before hitting the Google API.