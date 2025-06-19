# passphrase

**passphrase** is a minimal, secure, and entirely offline passphrase generator for Linux systems.

It uses the [EFF Large Wordlist](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases) to generate human-readable, high-entropy passphrases suitable for use as passwords, encryption keys, or anything else that needs strong but memorable security.

---

## 🔐 Features

* Installs to `/usr/local/bin/passphrase`
* Uses the [EFF diceware wordlist (large)](https://www.eff.org/dice) (downloaded once to `~/.eff/wordlist.txt`)
* Secure random word selection using Python’s `secrets` module
* Works fully offline after first install
* Simple CLI interface:

  ```bash
  passphrase 6
  ```

---

## 🧱 Prerequisites

You need:

* **Python 3.6+** (installed on most Linux distros by default)
* **curl**
* **sudo privileges** (for installing to `/usr/local/bin`)

---

## 🛠 Installation

To install globally, run:

```bash
curl -fsSL https://raw.githubusercontent.com/JackBinary/passphrase/refs/heads/main/install_passphrase.sh | bash
```

This will:

* Download the CLI tool from your GitHub repo
* Install it to `/usr/local/bin/passphrase`
* Download the EFF wordlist to `~/.eff/wordlist.txt` if it doesn't already exist

---

## 🧪 Usage

```bash
passphrase             # default: 6 words
passphrase 8           # generate 8 words
```

Example output:

```
acoustic-fossil-barrel-embrace-compute-saddle
```

You can use these as-is or adapt them for password managers, GPG keys, etc.

---

## 🔒 Why Passphrases?

Passphrases like `correct horse battery staple` are easier to remember than complex strings like `s$9Jv!dD2`, and with enough words, they're equally or more secure. This tool generates entropy equivalent to 77+ bits when using 6 words from the EFF list.

---

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).
