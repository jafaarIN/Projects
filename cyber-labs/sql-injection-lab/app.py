import streamlit as st
import html

st.set_page_config(page_title="SQLi demonstration", layout="wide")
st.title("SQL-Injection Attacks Explained")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Finding SQL-Injection Vectors", 
    "Post Exploitation", 
    "Exploit Walkthrough", 
    "Bypass", 
    "Defend"
])

with tab1:
    st.subheader("How Hackers Find Possible SQL-Injection Vectors")
    st.markdown("""
Hackers typically find/exploit said vectors through:

1. Inspecting inputs like search forms, comment boxes, login fields.
2. Inspecting any internal service where communication to a DBMS (Database Management Service) occurs.
3. Using tools:
   - [SQLmap](https://github.com/sqlmapproject/sqlmap)
   - [Burp Suite](https://portswigger.net/burp/communitydownload)
   
**Here's an example on how SQLmap can be used to test parameters possibly succeptable to SQL injections:**
""")
    st.video("https://www.youtube.com/watch?v=SKKVcPjaIqI")
    st.markdown("""
    5. Inspecting requests:
    Open browser and use developer tools, check network tabs and submit the form.
    Then analyse the HTTP request to identify user controlled parameters (username, password, etc)
    Example captured request
    ```html
    POST /login
    username=admin&password=test
    ```
    Modify these parameters to test for SQL injections:
    The most basic SQL injections include:
    ```
    ' OR 1=1--
    ' AND 1=2--
    ```
    Then observe response differences or timing delays to confirm injection behaviour.
    """)

with tab2:
    st.subheader("How Hackers Exploit SQLi vulnerabilities")
    st.markdown("""
Once a succesfull SQLi payload is found, attackers might:

- Use the payload to communicate with a DBMS:
- Create arbitrary entries to databases connected to the DBMS
- Dump databases 
- Subsequently exfiltrate (likely sensitive) data from tables in databases that are connected to the DBMS (i.e, passwords, emails, etc).

Tools often used:
- SQLmap
- Burp Suite
""")


symbols = ["<", ">", "&"]

with tab3:
    st.subheader("**DO NOT RECREATE ON SERVICES YOU DO NOT OWN OR HAVE EXPLICIT PERMISSION TO USE ON, THIS IS FOR EDUCATIONAL PURPOSES ONLY AND ALL DEMONSTRATIONS SHOWN HAVE BEEN PERFORMED ON SERVICES I MYSELF HAVE CREATED FOR THE SOLE PURPOSE OF THIS DEMONSTRATION**: Refer to the video in the first tab:")
    st.markdown("**Step 1:** Identifying input field")
    st.image("cyber-labs/sql-injection-lab/step1", caption="The two input fields here are the username and password field.", use_container_width=True)
    st.markdown("---")
    st.markdown("**Step 2:** Intercept request *(Using either Burp Suite or a browser's inbuilt developer tools)*")
    st.image("cyber-labs/sql-injection-lab/step2.png", caption="These will be used as the target parameters when using SQLmap", use_container_width=True)
    st.markdown("---")
    st.markdown("**Step 3:** Experiment with the parameters using SQLmap, use different tests/techniques/tamper scripts/configurations")
    st.image("cyber-labs/sql-injection-lab/step3.png", caption="The specific script used in the demonstration was: sqlmap -u 'http://127.0.0.1:5000/login' --data='username=test&password=test' --level=5 --risk=3 --time-sec=2 --dbs --tables", use_container_width=True)
    st.markdown("---")
    st.markdown("**Step 4:** If success is faced in step 3, you can begin data exfiltration from the databases")
    st.image("cyber-labs/sql-injection-lab/step4.png", caption="From here you simple use --dump parameters alongside -T or -D parameters", use_container_width=True)
    st.markdown("---")
    st.markdown("**Step 5:** Post exploitation")
    st.image("cyber-labs/sql-injection-lab/step5.png", caption="At this stage attackers can do anything from using data from the database to do things like compromise user accounts, or delete entries/add entries.", use_container_width=True)


with tab4:
    st.subheader("Bypassing Filters")
    st.markdown("""
Attackers evade protections using:

- Obfuscation:
```html
<scr<script>ipt>alert(1)</script>
```
- Encoded tags:
```html
%3Cscript%3Ealert(1)%3C/script%3E
```
- Alternate vectors:
```html
<input onfocus=alert(1) autofocus>
<svg onload=alert(1)>
```

Advanced tools generate bypass payloads:
- XSStrike fuzzes and finds filtered contexts
- Burp Suite encodes payloads in real time
""")

with tab5:
    st.subheader("How Developers Prevent XSS")
    st.markdown("""
To defend against XSS

1. Escape Output:
   - Encode `<`, `>`, `"`, `'`, and `&`
   - Use `html.escape()` or frameworks with built-in escaping

2. Validate Input:
   - Use allowlists for expected content (e.g., `a-z`, `0-9`)
   - Strip HTML if not explicitly needed

3. Use Secure Functions:
   - Prefer `textContent` over `innerHTML`
   - Avoid direct DOM manipulation with user data

4. Security Headers:
   - `Content-Security-Policy`: disallow inline scripts
   - `X-XSS-Protection`: legacy browser protection

5. Libraries:
   - Use [DOMPurify](https://github.com/cure53/DOMPurify) for safe HTML sanitization
""")
