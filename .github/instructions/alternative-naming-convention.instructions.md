---
description: 'Guidelines for naming according to the AlterNative Naming Convention & Semantic Strategy'
applyTo: "**"
---
# Guidelines for naming according to the AlterNative Naming Convention & Semantic Strategy

## Overview
The naming convention for this project is designed as a **Universal Matcher**. It leverages a recursive, semantic expansion to ensure maximum searchability across GitHub, Google, and the VS Code Marketplace while maintaining a clever, pun-based brand identity.

## 1. Regex Specification
All project-related strings (repositories, packages, display names) must satisfy the following logic:
`[*-]alt[er[ |-native][<-*>]`

### Logic Breakdown:
- **`alt`**: The primary modifier and anchor for power-user searches.
- **`er`**: The phonetic bridge to "Alternative."
- **`native`**: The semantic promise (built-in feel) and phonetic suffix.
- **`<-*>`**: The functional component (e.g., `config`, `focus`, `keybindings`, `navigation`, etc).

## 2. Brand Hierarchy
| Level | Format | Example |
| :--- | :--- | :--- |
| **Brand (PascalCase)** | `AlterNative` | The primary extension name. |
| **Repository** | `vscode-alternative-<component>` | `vscode-alternative-keybindings` |
| **Internal Slug** | `altKey` | Used for configuration prefixes. |
| **Nickname** | `alt-key` | used for CLI or commands. |

## 3. Searchability Objectives
- **Exact Match:** `VS Code Alternative keybindings`
- **Modifier Match:** `alternative keybindings`
- **Short Match:** `alt-key`
- **Phonetic Match:** `AlterNative`

## 4. Constraint Enforcement
- Avoid unnecessary hyphens in the Brand Name, for example `AlterNative` not `Alt-er-native`.
- Use hyphens for the long-form repository name to satisfy SEO for "VS Code Alternative", e.g. `vscode-alternative-keybindings`.
- Ensure the prefix (i.e. `alt`) is always present in any sub-module or fork.
