#!/usr/bin/env python3
import secrets
import os
import sys
from pathlib import Path

WORDLIST_PATH = Path.home() / ".eff" / "wordlist.txt"
DEFAULT_WORDS = 4

def download_wordlist():
    import urllib.request
    url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
    WORDLIST_PATH.parent.mkdir(parents=True, exist_ok=True)
    print("Downloading EFF wordlist...")
    urllib.request.urlretrieve(url, WORDLIST_PATH)
    print(f"Saved to {WORDLIST_PATH}")

def load_wordlist():
    if not WORDLIST_PATH.exists():
        download_wordlist()

    with open(WORDLIST_PATH, "r") as f:
        return [line.strip().split()[1] for line in f if line.strip()]

def generate_passphrase(num_words=DEFAULT_WORDS):
    words = load_wordlist()
    return '-'.join(secrets.choice(words) for _ in range(num_words))

def main():
    if len(sys.argv) > 1:
        try:
            num_words = int(sys.argv[1])
        except ValueError:
            print("Usage: passphrase [num_words]")
            sys.exit(1)
    else:
        num_words = DEFAULT_WORDS

    print(generate_passphrase(num_words))

if __name__ == "__main__":
    main()
