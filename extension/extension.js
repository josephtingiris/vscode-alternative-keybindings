const vscode = require("vscode");

/**
 * Activate the extension.
 * Registers command `altKey.resetLayout` which resets sidebar/panel placement
 * according to `altKey.orientation` setting.
 */
function activate(context) {
  const disposable = vscode.commands.registerCommand(
    "altKey.resetLayout",
    async () => {
      const config = vscode.workspace.getConfiguration("altKey");
      let orientation = config.get("orientation", "left");
      if (!orientation) orientation = "left";

      const workbench = vscode.workspace.getConfiguration("workbench");

      // Always set the panel to bottom first
      try {
        await vscode.commands.executeCommand(
          "workbench.action.positionPanelBottom",
        );
      } catch (e) {
        // ignore if command doesn't exist
      }

      // Behavior: 'default' should reset to VS Code default (left).
      // 'left' forces left, 'right' forces right.
      let target = "left";
      if (orientation === "right") {
        target = "right";
      } else {
        // For 'default' and any other value, default to 'left'
        target = "left";
      }

      try {
        await workbench.update(
          "sideBar.location",
          target,
          vscode.ConfigurationTarget.Global,
        );
        vscode.window.showInformationMessage(
          `altKey.resetLayout: set sideBar.location -> ${target}; panel -> bottom`,
        );
      } catch (e) {
        vscode.window.showErrorMessage(
          `altKey.resetLayout failed: ${e && e.message ? e.message : String(e)}`,
        );
      }
    },
  );

  context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = { activate, deactivate };
