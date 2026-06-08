# JSON & Regex Demo - Setup and Usage Guide

## Files Generated

1. **json_regex_demo.py** - Main demo file with 7 comprehensive demonstrations
2. **requirements.txt** - Pip dependencies (optional enhanced packages)
3. **SETUP_GUIDE.md** - This setup guide

## Quick Start

### Option 1: Run Without Dependencies (Recommended)
The demo uses only Python standard library (json, re, typing). No installation needed:

```bash
python json_regex_demo.py
```

### Option 2: Install Optional Dependencies
Install enhanced packages for additional functionality:

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/Scripts/activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

## What the Demo Includes

### Demo 1: JSON Parsing and Pretty Printing
- Parse JSON strings
- Pretty print JSON output
- Count nested objects

### Demo 2: Email Validation with Regex
- Email regex pattern: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
- Validate multiple email addresses
- Display validity status

### Demo 3: Phone Number Formatting
- Extract digits using `\D` negation
- Format phone numbers to standard format: (XXX) XXX-XXXX
- Support multiple phone number formats

### Demo 4: URL Extraction
- Extract URLs from text: `https?://[^\s]+`
- Find all occurrences in multi-line text

### Demo 5: Filter and Output JSON
- Filter JSON data based on criteria
- Sanitize tags by removing special characters
- Output filtered results as formatted JSON

### Demo 6: JSON Structure Validation
- Validate required keys exist
- Check schema compliance
- Display validation status

### Demo 7: Common Regex Patterns
- Email patterns
- Phone number patterns
- URL patterns
- Hex color codes
- IPv4 addresses

## Regex Patterns Reference

| Pattern | Use Case | Regex |
|---------|----------|-------|
| Email | Validate email addresses | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` |
| Phone | Match phone numbers | `^\+?1?-?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$` |
| URL | Extract URLs | `https?://[^\s]+` |
| Hex Color | Validate color codes | `^#?([a-fA-F0-9]{6}\|[a-fA-F0-9]{3})$` |
| IPv4 | Validate IP addresses | `^(\d{1,3}\.){3}\d{1,3}$` |
| Digits Only | Extract numbers | `\d+` |
| Non-digits | Remove numbers | `\D` |

## Key Python Functions Used

### JSON Operations
- `json.dumps()` - Convert Python object to JSON string
- `json.loads()` - Parse JSON string to Python object
- `json.dump()` - Write to file
- `json.load()` - Read from file

### Regex Operations
- `re.match()` - Match at beginning of string
- `re.search()` - Search anywhere in string
- `re.findall()` - Find all occurrences
- `re.sub()` - Replace pattern with string

## Output Files

The script creates:
- **demo_results.json** - Summary of execution results

## Common Use Cases

1. **API Data Validation**
   ```python
   data = json.loads(api_response)
   if all(validate_email(user['email']) for user in data['users']):
       print("All emails valid")
   ```

2. **Log File Parsing**
   ```python
   with open('app.log') as f:
       errors = re.findall(r'ERROR: (.+)', f.read())
   ```

3. **Config File Processing**
   ```python
   with open('config.json') as f:
       config = json.load(f)
       # Process and validate
   ```

4. **Data Cleaning**
   ```python
   cleaned_data = {
       'phone': re.sub(r'\D', '', raw_phone),
       'email': raw_email.strip().lower()
   }
   ```

## Running Individual Demos

The `JSONRegexDemo` class has individual methods you can call:

```python
demo = JSONRegexDemo()
demo.demo_email_validation()  # Run just email validation
demo.demo_phone_formatting()  # Run just phone formatting
# etc.
```

## Dependencies Breakdown

| Package | Purpose | Optional |
|---------|---------|----------|
| json | JSON serialization (built-in) | No |
| re | Regular expressions (built-in) | No |
| typing | Type hints (built-in) | No |
| jsonschema | JSON schema validation | Yes |
| regex | Enhanced regex engine | Yes |
| mypy | Static type checking | Yes |
| black | Code formatting | Yes |

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'jsonschema'`
**Solution**: This demo works without it. Install with `pip install jsonschema` if needed.

**Issue**: Regex patterns not matching
**Solution**: Use raw strings (r'...') for patterns to avoid escape character issues.

**Issue**: JSON decode errors
**Solution**: Ensure JSON is valid. Use `json.JSONDecodeError` to catch errors.

## Next Steps

1. Run: `python json_regex_demo.py`
2. Modify demo data in `JSONRegexDemo.__init__()` for your use case
3. Add custom regex patterns for your needs
4. Save results to JSON with custom schema
5. Integrate into your projects

---

Generated: 2024-01-15
Python Version: 3.8+
