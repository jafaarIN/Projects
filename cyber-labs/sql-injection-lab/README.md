
# SQL-injection Lab

Streamlit link: https://sql-injection-lab.streamlit.app/

An interactive Streamlit app that demonstrates how SQLi (Structured Query Language injection) attacks work; from injection and execution to bypassing firewalls and defending against them.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sql-injection-lab.streamlit.app/)

## What's Inside

- Finding SQLi vectors – how attackers find SQLi vectors
- Exploitation Walkthrough – demonstrating how exactly attackers exploit SQLi vulnerabilities
- Bypass – how attackers bypass firewalls
- Defense – learn the best practices to prevent it as a developer

---

## Stack

- Python
- Streamlit
- HTML & SQL

---

## How to Run Locally

```bash
git clone https://github.com/jafaarIN/Projects/cyber-labs/sql-injection-lab
cd sql-injection-lab
pip install -r requirements.txt
streamlit run app.py
