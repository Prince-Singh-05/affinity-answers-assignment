## Problem Statement - Shell Script

This question is to test your aptitude for writing small shell scripts on Unix. You are given this URL https://www.amfiindia.com/spages/NAVAll.txt. Write a shell script that extracts the Scheme Name and Asset Value fields only and saves them in a tsv file. And ever wondered if this data should not be stored in JSON?

### 1. Shell Script

**! Important**

- Make the **_extract_nav.sh_** executable if not already -

  ```
  chmod +x extract_nav.sh
  ```

- Run the bash command
  ```
  ./extract_nav.sh
  ```

### 2. Should this data be stored in JSON?

**Yes** — storing this NAV data in JSON can be beneficial.

**Benefits of JSON format:**

- Structured & machine friendly — JSON preserves relationships between fields clearly.
- Easy to parse — Almost every modern language has JSON parsers.
- Supports nested data — Good for funds with multiple related attributes.
- API ready — JSON is ideal for web APIs.
- Less ambiguity — Unlike text data separated by semicolons, JSON avoids parsing errors.

**However:**

- JSON files can be larger than TSV.
- For bulk/tabular data, TSV is faster for low-level processing.

**Conclusion:**

- If the goal is data storage, APIs, or integration → JSON is ideal.
- If the goal is quick batch processing → TSV is fine.
