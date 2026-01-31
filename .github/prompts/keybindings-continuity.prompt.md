---
agent: agent
---
Ensure references/keybindings.json is kept consistent with the keybinding conventions and context key usages defined in .github/agents/keybindings-expert.agent.md and .github/instructions/keybindings-conventions.instructions.md.
When making changes to keybindings or `when` clauses in keybindings.json, follow these guidelines:
- Use the correct context keys as specified in the keybindings-expert agent prompt.md.
- Maintain proper sorting of `when` clauses as per the constraints in the keybindings-expert agent prompt.md.
- Validate that all keybinding commands exist and are appropriate for the described contexts.
- Provide explanations for any changes made, referencing the relevant sections of the keybindings-expert agent prompt.md when necessary.

Validate equivalent keybinding pairs exist for alt+arrow and alt+h/j/k/l (and vice versa), for example alt+left and alt+h should both containt he same when clause and command.