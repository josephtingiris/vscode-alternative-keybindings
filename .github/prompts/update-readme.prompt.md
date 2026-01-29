---
agent: agent
description: Review and update the workspace root's README.md to ensure accuracy and completeness
model: GPT-5 mini (copilot)
name: update-readme
---
- First, review the entire repository.
- If a README.md file does not exist then create one.
- Include the following sections in the README.md:
  - Project Title & Description: Start with a clear title and a concise one-liner or short paragraph that explains what the project does and the problem it solves.
  - Installation Instructions: Provide simple, step-by-step, copy-paste-ready commands for users to get the project running locally. Avoid jargon and assume the reader may not know your specific environment.
  - Usage: Show practical, minimal examples of how to use the project with simple commands or code snippets. Focus on the core functionality without documenting the entire project.
  - Contributing Guidelines: If applicable, include a brief section on how others can contribute to the project, linking to a CONTRIBUTING.md file if it exists.
  - License Information: Clearly state the project's license and any important legal information.
- Use Markdown
- Be Concise and Readable
- When appropriate, incorporate badges (e.g., build status, coverage, license) at the top of the README.md.
- Use Relative Links for internal references.
- Consider your audience and adjust the tone and complexity of the language accordingly.
- If the README.md is long then add a Table of Contents after the introduction for easier navigation.
- Update only the workspace root's README.md to describe this repository's purpose, usage, and any other relevant information.
- Do not modify any other files in the repository.
- Ensure that the README.md is accurate, complete, and follows best practices for README.md formatting.
- If no changes have occurred since the last update, do not change or add anything new.

