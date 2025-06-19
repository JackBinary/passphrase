#!/bin/bash

set -e

INSTALL_PATH="/usr/local/bin/passphrase"
SCRIPT_URL="https://raw.githubusercontent.com/JackBinary/passphrase/refs/heads/main/passphrase.py"
WORDLIST_URL="https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
WORDLIST_DIR="$HOME/.eff"
WORDLIST_PATH="$WORDLIST_DIR/wordlist.txt"

echo "Installing passphrase tool from GitHub..."

# Download script
curl -sSLo "/tmp/passphrase" "$SCRIPT_URL"
chmod +x "/tmp/passphrase"
sudo mv "/tmp/passphrase" "$INSTALL_PATH"

echo "Installed passphrase to $INSTALL_PATH"

# Ensure wordlist is available
if [ ! -f "$WORDLIST_PATH" ]; then
    echo "Downloading EFF wordlist to $WORDLIST_PATH..."
    mkdir -p "$WORDLIST_DIR"
    curl -sSLo "$WORDLIST_PATH" "$WORDLIST_URL"
else
    echo "EFF wordlist already exists at $WORDLIST_PATH"
fi

echo "Installation complete. You can now run:"
echo "  passphrase [num_words]"
