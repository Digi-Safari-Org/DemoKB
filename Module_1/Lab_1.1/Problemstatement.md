## Lab 1.1: Contextual Prompts for Large Internal Repos
#### Objective:

In this lab, learners will: 

- Learn to write effective contextual prompts to leverage Copilot's understanding of large codebases.

#### Instructions:

1. Start with a comment and a partial function signature.

2. Observe Copilot’s suggestion. Accept or refine it as needed.

3. Add more context with additional prompts:

4. Test the function with sample input:

    ```python
    print(validate_enterprise_email("test@yourcompany.com"))       # Expected: True
    print(validate_enterprise_email("invalid@gmail.com"))          # Expected: False
    print(validate_enterprise_email("no.dot@yourcompany.com"))     # Expected: False
    ```
