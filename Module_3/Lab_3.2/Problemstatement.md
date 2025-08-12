##  Lab 3.2: Proactive Security Vulnerability Identification & Remediation

###  Objective:
- Leverage GitHub Copilot to proactively detect and remediate **non-obvious, high-risk security flaws** in Python applications—specifically **insecure deserialization**, which may lead to **remote code execution (RCE)** or injection vulnerabilities.

---

###  Instructions:

####  Part 1: Review the Vulnerable Code

Open the provided `deserialization_lab.py` file. It contains the following function:

```python
def process_user_data_insecure(encoded_data: str):
    decoded_data = base64.b64decode(encoded_data)
    data = pickle.loads(decoded_data)
    print(f"Processed data: {data}")
    return data

```


#### Part 2: Trigger the Security Risk (Simulated)
1. Within the __main__ block:

   -  Review both the benign and malicious payload examples.
   -  Uncomment one payload at a time and run the code.
   -  Observe that the malicious payload executes a shell command, simulating a real-world RCE attack.

#### Part 3: Security Review and Copilot Prompt

1. Use Copilot Chat to review the vulnerability with a prompt.

2. Copilot should:

   -  Flag pickle.loads() as unsafe for untrusted input.

   -  Suggest secure alternatives such as:
   -  json.loads() (if structure is simple)

   -  Use of a custom schema validator

   -  Restricting allowed classes via pickle.Unpickler subclass (advanced)

#### Part 4: Apply a Secure Fix
1. Replace the unsafe pickle usage with json.loads and validate the input structure before use.

2. Make sure your function sanitizes input and rejects unexpected types/structures.

3. Try running the benign and malicious payloads again:

4. The benign payload should be processed safely.

5. The malicious payload should be rejected or fail harmlessly.