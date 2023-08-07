import re
import subprocess
import pandas as pd

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    return result.stdout

def analyze_laravel_controller(controller_file):
    issues = []
    with open(controller_file, 'r') as file:
        content = file.read()

    # # Check for authentication middleware
    # if 'middleware(\'auth\')' not in content:
    #     issues.append("Controller does not use 'auth' middleware.")

    # # Check for authorization middleware (example: middleware('can:view,post'))
    # if re.search(r"middleware\(['\"]can:[^'\"]+['\"]\)", content) is None:
    #     issues.append("Controller does not have any 'can:' authorization middleware.")

    # Check for method names starting with lowercase
    method_names = re.findall(r'public\s+function\s+([a-zA-Z0-9_]+)\s*\(', content)
    for method_name in method_names:
        if not method_name[0].islower():
            issues.append(f"Controller method '{method_name}' should start with a lowercase letter.")

    # Check for usage of request validation (e.g., $request->validate([...]))
    if re.search(r"\$request->validate\s*\(", content) is None:
        issues.append("Controller does not use request validation.")

    # Check for unnecessary use of 'exit' or 'die' functions
    if re.search(r'\b(exit|die)\(', content):
        issues.append("Controller should avoid using 'exit' or 'die' functions.")

    # Check for usage of Eloquent model directly in the controller
    if re.search(r'\buse\s+App\\[a-zA-Z0-9_]+\s*;', content):
        issues.append("Avoid using Eloquent model directly in the controller. Use dependency injection instead.")

        # Check for usage of the 'request' global helper function
    if re.search(r'\brequest\s*\(.*\)\s*->', content):
        issues.append("Controller should avoid using the 'request' global helper function. Use dependency injection instead.")

    # Check for proper usage of response objects (e.g., return response()->json([...]))
    if re.search(r'\breturn\s+response\s*\(\s*->', content):
        issues.append("Controller should use response()->json() instead of direct return response object.")

    # Check for proper usage of route names (e.g., route('route.name'))
    if re.search(r'\broute\s*\(\s*([\'"])[^\'"]+\1', content):
        issues.append("Controller should use named routes (route('route.name')) instead of hard-coded URLs.")

    # Check for proper usage of the compact() function
    if re.search(r'\bcompact\s*\(\s*[\'"][^\'"]+[\'"]', content):
        issues.append("Controller should avoid using compact() function with hardcoded variable names.")

    # Check for unnecessary or repeated use of whitespace
    if re.search(r'\s{3,}', content):
        issues.append("Controller contains unnecessary or repeated whitespace (three or more consecutive spaces).")

    # Check for proper usage of route model binding (e.g., public function show(Post $post))
    if re.search(r'public\s+function\s+[a-zA-Z0-9_]+\(\s*[A-Z][a-zA-Z0-9_]+\s+\$\w+\s*\)', content):
        issues.append("Controller should use route model binding for dependencies instead of manually resolving them.")

    # Check for usage of the 'app' global helper function
    if re.search(r'\bapp\s*\(.*\)\s*->', content):
        issues.append("Controller should avoid using the 'app' global helper function. Use dependency injection instead.")

    # Check for proper usage of Blade templates (e.g., return view('view_name', ['data' => $data]))
    if re.search(r'\breturn\s+view\s*\(\s*[\'"][^\'"]+[\'"]\s*,\s*\[.*\]\s*\)', content):
        issues.append("Controller should use Blade templates with compact() or with() method for passing data.")

    # Check for usage of CSRF protection
    if re.search(r'\bcsrf_field\s*\(\s*\)', content):
        issues.append("Controller should use @csrf Blade directive instead of csrf_field() function.")

    # Check for proper usage of middleware groups (e.g., middleware('web'))
    if re.search(r'middleware\([\'"]web[\'"]\)', content):
        issues.append("Controller should use middleware groups for routes, not individual middleware.")

    # Check for proper usage of route middleware parameters (e.g., middleware('role:admin'))
    if re.search(r'middleware\([\'"]\w+:\w+[\'"]\)', content):
        issues.append("Controller should use route middleware parameters for passing middleware arguments.")

    # Check for unnecessary or repeated blank lines
    if re.search(r'\n\s*\n\s*\n', content):
        issues.append("Controller contains unnecessary or repeated blank lines.")

    return issues

# def analyze_laravel_model(model_file):
#     issues = []
#     with open(model_file, 'r') as file:
#         content = file.read()

#     # Check for relationships (example: public function user() {})
#     if re.search(r"public\s+function\s+[a-zA-Z0-9_]+\s*\(", content) is None:
#         issues.append("Model does not define any relationships.")

#     # Check for validation rules (example: protected $rules = [])
#     if "protected $rules" not in content:
#         issues.append("Model does not have any validation rules defined.")

#     # Check for correct usage of model timestamps (timestamps = false;)
#     if re.search(r"public\s+\$timestamps\s*=\s*false;", content) is None:
#         issues.append("Model does not explicitly disable timestamps.")

#     # Check for correct usage of model fillable/guarded attributes
#     if not re.search(r"(protected|protected\s+fillable|protected\s+guarded)\s*=\s*\[.*\];", content):
#         issues.append("Model should have fillable or guarded attributes defined.")

#     return issues

# def analyze_laravel_view(view_file):
#     issues = []
#     with open(view_file, 'r') as file:
#         content = file.read()

#     # Check for proper indentation
#     if re.search(r"^\s{4}", content, re.MULTILINE) is None:
#         issues.append("View does not use 4-space indentation.")

#     # Check for proper use of @if, @else, @foreach, etc.
#     if re.search(r"@if|@else|@foreach|@endforeach|@for|@endfor|@while|@endwhile", content) is None:
#         issues.append("View does not use Laravel's control structures (@if, @else, @foreach, etc.)")

#     # Check for empty lines after @endif, @endforeach, etc.
#     if re.search(r"@(endif|endforeach|endfor|endwhile)\s*\n\s*\n", content) is not None:
#         issues.append("View has unnecessary empty lines after control structures.")

#     return issues

# def lint_laravel_file(file_path):
#     pylint_command = f"pylint {file_path}"
#     pylint_result = run_command(pylint_command)
#     print(pylint_result)

#     # Run 'black' code formatter check on the file
#     black_command = f"black --check {file_path}"
#     black_result = run_command(black_command)
#     print(black_result)

#     # Run 'flake8' code style check on the file
#     flake8_command = f"flake8 {file_path}"
#     flake8_result = run_command(flake8_command)
#     print(flake8_result)
#     pass

def main():
    laravel_root_path = '/home/w3care/Desktop/docker/core'
    laravel_controllers_dir = f'{laravel_root_path}/app/Http/Controllers/'
    laravel_models_dir = f'{laravel_root_path}/app/'
    laravel_views_dir = f'{laravel_root_path}/resources/views/'
    allowed_extensions = ['.php', '.blade.php']

    # Create lists to store issues and file paths
    controller_issues_list = []
    # model_issues_list = []
    # view_issues_list = []
    file_paths_list = []

    # Get a list of controller files
    controller_files = run_command(f"find {laravel_controllers_dir} -type f -name '*.php'").splitlines()

    # Get a list of model files
    #model_files = run_command(f"find {laravel_models_dir} -type f -name '*.php'").splitlines()

    # Get a list of view files
    #view_files = run_command(f"find {laravel_views_dir} -type f -name '*.blade.php'").splitlines()

    for file in controller_files:
        file_paths_list.append(file)
        issues = analyze_laravel_controller(file)
        controller_issues_list.append(", ".join(issues) if issues else "")

    # for file in model_files:
    #     file_paths_list.append(file)
    #     issues = analyze_laravel_model(file)
    #     model_issues_list.append(", ".join(issues) if issues else "")

    # for file in view_files:
    #     file_paths_list.append(file)
    #     issues = analyze_laravel_view(file)
    #     view_issues_list.append(", ".join(issues) if issues else "")

    # Make sure all lists have the same length
    #max_length = max(len(file_paths_list), len(controller_issues_list), len(model_issues_list), len(view_issues_list))
    max_length = max(len(file_paths_list), len(controller_issues_list))
    controller_issues_list += [""] * (max_length - len(controller_issues_list))
    # model_issues_list += [""] * (max_length - len(model_issues_list))
    # view_issues_list += [""] * (max_length - len(view_issues_list))

    # Create a DataFrame to store the data
    data = {
        'File Path': file_paths_list,
        'Controller Issues': controller_issues_list
        # 'Model Issues': model_issues_list,
        # 'View Issues': view_issues_list
    }
    df = pd.DataFrame(data)

    # Export DataFrame to an Excel file
    excel_file = '/home/w3care/Desktop/laravel_issues.xlsx'
    df.to_excel(excel_file, index=False)

if __name__ == "__main__":
    main()
