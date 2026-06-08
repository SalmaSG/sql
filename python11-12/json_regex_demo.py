#!/usr/bin/env python3
"""
Comprehensive demo of Python JSON, Regex, and Pip integration
Demonstrates practical patterns for JSON manipulation with regex validation/extraction
"""

import json
import re
from typing import List, Dict, Any
from pathlib import Path


class JSONRegexDemo:
    """Utility class for JSON and regex operations"""
    
    def __init__(self):
        self.demo_data = {
            "users": [
                {
                    "id": 1,
                    "name": "John Doe",
                    "email": "john.doe@example.com",
                    "phone": "+1-555-123-4567",
                    "tags": ["admin", "developer"]
                },
                {
                    "id": 2,
                    "name": "Jane Smith",
                    "email": "jane.smith@company.org",
                    "phone": "+1-555-987-6543",
                    "tags": ["user", "analyst"]
                },
                {
                    "id": 3,
                    "name": "Bob Wilson",
                    "email": "bob@invalid-email",
                    "phone": "555.888.9999",
                    "tags": ["guest"]
                }
            ],
            "metadata": {
                "version": "1.0.0",
                "timestamp": "2024-01-15T10:30:00Z"
            }
        }
    
    def validate_email(self, email: str) -> bool:
        """Validate email using regex pattern"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def extract_phone_digits(self, phone: str) -> str:
        """Extract only digits from phone number"""
        return re.sub(r'\D', '', phone)
    
    def format_phone(self, phone: str) -> str:
        """Format phone number to standard format (XXX) XXX-XXXX"""
        digits = self.extract_phone_digits(phone)
        if len(digits) == 10:
            return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        return phone
    
    def find_urls(self, text: str) -> List[str]:
        """Extract URLs from text using regex"""
        pattern = r'https?://[^\s]+'
        return re.findall(pattern, text)
    
    def sanitize_tags(self, tags: List[str]) -> List[str]:
        """Remove invalid characters from tags"""
        return [re.sub(r'[^a-zA-Z0-9_-]', '', tag) for tag in tags]
    
    def validate_json_structure(self, data: Dict) -> bool:
        """Validate required JSON structure"""
        required_keys = {'users', 'metadata'}
        return set(data.keys()) == required_keys
    
    # Demo 1: JSON Parsing and Pretty Printing
    def demo_json_parsing(self):
        """Demo 1: Parse and display JSON"""
        print("\n" + "="*60)
        print("DEMO 1: JSON Parsing and Pretty Printing")
        print("="*60)
        
        json_string = json.dumps(self.demo_data, indent=2)
        print("JSON Output:")
        print(json_string)
        
        parsed = json.loads(json_string)
        print(f"\nParsed back successfully: {type(parsed)}")
        print(f"Number of users: {len(parsed['users'])}")
    
    # Demo 2: Email Validation with Regex
    def demo_email_validation(self):
        """Demo 2: Validate emails using regex"""
        print("\n" + "="*60)
        print("DEMO 2: Email Validation with Regex")
        print("="*60)
        
        for user in self.demo_data['users']:
            email = user['email']
            is_valid = self.validate_email(email)
            status = "✓ VALID" if is_valid else "✗ INVALID"
            print(f"{email:<30} {status}")
    
    # Demo 3: Phone Number Formatting
    def demo_phone_formatting(self):
        """Demo 3: Extract and format phone numbers"""
        print("\n" + "="*60)
        print("DEMO 3: Phone Number Formatting with Regex")
        print("="*60)
        
        for user in self.demo_data['users']:
            original = user['phone']
            formatted = self.format_phone(original)
            digits = self.extract_phone_digits(original)
            print(f"Original:  {original}")
            print(f"Digits:    {digits}")
            print(f"Formatted: {formatted}")
            print()
    
    # Demo 4: URL Extraction
    def demo_url_extraction(self):
        """Demo 4: Extract URLs from text"""
        print("\n" + "="*60)
        print("DEMO 4: URL Extraction with Regex")
        print("="*60)
        
        sample_text = """
        Visit our website at https://example.com for more info.
        Check out the API docs at https://api.example.com/v1/docs
        Download from https://files.example.com/data.zip
        """
        
        urls = self.find_urls(sample_text)
        print("Found URLs:")
        for url in urls:
            print(f"  - {url}")
    
    # Demo 5: Data Filtering and JSON Output
    def demo_filtering(self):
        """Demo 5: Filter JSON data and output as JSON"""
        print("\n" + "="*60)
        print("DEMO 5: Filter and Output JSON")
        print("="*60)
        
        valid_users = []
        for user in self.demo_data['users']:
            if self.validate_email(user['email']):
                user['phone_formatted'] = self.format_phone(user['phone'])
                user['tags'] = self.sanitize_tags(user['tags'])
                valid_users.append(user)
        
        result = {
            "valid_users": valid_users,
            "count": len(valid_users)
        }
        
        print(json.dumps(result, indent=2))
    
    # Demo 6: JSON Schema Validation
    def demo_json_validation(self):
        """Demo 6: Validate JSON structure"""
        print("\n" + "="*60)
        print("DEMO 6: JSON Structure Validation")
        print("="*60)
        
        is_valid = self.validate_json_structure(self.demo_data)
        print(f"Valid structure: {is_valid}")
        print(f"Keys present: {list(self.demo_data.keys())}")
        
        if is_valid:
            print("✓ JSON structure matches expected schema")
        else:
            print("✗ JSON structure does not match expected schema")
    
    # Demo 7: Regex Pattern Matching
    def demo_regex_patterns(self):
        """Demo 7: Various regex pattern matching"""
        print("\n" + "="*60)
        print("DEMO 7: Common Regex Patterns")
        print("="*60)
        
        patterns = {
            "Email": (r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', 
                     "john@example.com"),
            "Phone (simple)": (r'^\+?1?-?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$',
                             "+1-555-123-4567"),
            "URL": (r'https?://[^\s]+', 
                   "https://example.com/path?query=value"),
            "Hex Color": (r'^#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$',
                         "#FF5733"),
            "IPv4": (r'^(\d{1,3}\.){3}\d{1,3}$',
                    "192.168.1.1")
        }
        
        for pattern_name, (pattern, test_string) in patterns.items():
            match = re.match(pattern, test_string)
            print(f"{pattern_name:<15} | Pattern: {pattern}")
            print(f"{'':15} | Test: {test_string}")
            print(f"{'':15} | Match: {'✓' if match else '✗'}\n")
    
    def run_all_demos(self):
        """Run all demonstrations"""
        print("\n" + "#"*60)
        print("# PYTHON JSON & REGEX COMPREHENSIVE DEMO")
        print("#"*60)
        
        self.demo_json_parsing()
        self.demo_email_validation()
        self.demo_phone_formatting()
        self.demo_url_extraction()
        self.demo_filtering()
        self.demo_json_validation()
        self.demo_regex_patterns()
        
        print("\n" + "#"*60)
        print("# ALL DEMOS COMPLETED SUCCESSFULLY")
        print("#"*60 + "\n")


def main():
    """Main entry point"""
    demo = JSONRegexDemo()
    demo.run_all_demos()
    
    # Example: Save results to JSON file
    output_data = {
        "demo_name": "JSON & Regex Patterns",
        "timestamp": "2024-01-15T10:30:00Z",
        "samples_processed": len(demo.demo_data['users']),
        "status": "completed"
    }
    
    output_path = Path(__file__).parent / "demo_results.json"
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)
    print(f"\nResults saved to: {output_path}")


if __name__ == "__main__":
    main()
