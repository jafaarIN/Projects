
# XSS Cross-Site Scripting Lab

Streamlit link: https://xss-lab.streamlit.app/
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://xss-lab.streamlit.app/)

An interactive Streamlit app that demonstrates how Cross-Site Scripting (XSS) attacks work; from injection and execution to bypassing filters and defending against them.

## What's Inside

- Explanation tabs – how attackers find and use XSS
- Simulator – test your own payloads in sanitized vs raw contexts
- Bypass – try common XSS filter evasions
- Defense – learn the best practices to prevent it as a developer

---

## Stack

- Python
- Streamlit
- HTML & JavaScript

---

## How to Run Locally

```bash
git clone https://github.com/jafaarIN/Projects/cyber-labs/xss-lab
cd xss-lab
pip install -r requirements.txt
streamlit run app.py
