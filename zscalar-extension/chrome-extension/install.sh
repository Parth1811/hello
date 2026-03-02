#!/bin/bash
# Installs the native messaging host for the ZSA Token Launcher Chrome extension.
#
# Usage:
#   1. Load the unpacked extension in chrome://extensions (Developer mode)
#   2. Copy the extension ID from the extensions page
#   3. Run: ./install.sh <extension-id>

set -e

if [ -z "$1" ]; then
  echo "Usage: ./install.sh <chrome-extension-id>"
  echo ""
  echo "Steps:"
  echo "  1. Go to chrome://extensions and enable Developer mode"
  echo "  2. Click 'Load unpacked' and select the chrome-extension folder"
  echo "  3. Copy the extension ID shown on the card"
  echo "  4. Run this script with that ID"
  exit 1
fi

EXT_ID="$1"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOST_SCRIPT="$SCRIPT_DIR/native-host/zsa_launcher.sh"
MANIFEST_SRC="$SCRIPT_DIR/native-host/com.zsa.launcher.json"

# Where Chrome looks for native messaging host manifests on macOS
NM_DIR="$HOME/Library/Application Support/Google/Chrome/NativeMessagingHosts"
mkdir -p "$NM_DIR"

# Make the launcher executable
chmod +x "$HOST_SCRIPT"

# Write the manifest with the correct path and extension ID
cat > "$NM_DIR/com.zsa.launcher.json" <<EOF
{
  "name": "com.zsa.launcher",
  "description": "Native messaging host for ZSA Token Launcher",
  "path": "$HOST_SCRIPT",
  "type": "stdio",
  "allowed_origins": [
    "chrome-extension://$EXT_ID/"
  ]
}
EOF

echo "Installed native messaging host."
echo "  Manifest: $NM_DIR/com.zsa.launcher.json"
echo "  Script:   $HOST_SCRIPT"
echo ""
echo "You're all set. Reload the extension and visit the Zscaler SAML page."
