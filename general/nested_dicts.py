#§§§ Nested Dictionaries Deep Dive in Python

# =============================================================================
# 1. CREATING NESTED DICTIONARIES
# =============================================================================

#%% Method 1: Direct creation
company = {
    "employees": {
        "john": {"age": 30, "department": "IT", "salary": 75000},
        "jane": {"age": 25, "department": "HR", "salary": 65000},
        "bob": {"age": 35, "department": "IT", "salary": 80000}
    },
    "departments": {
        "IT": {"budget": 100000, "head": "john", "employees": ["john", "bob"]},
        "HR": {"budget": 50000, "head": "jane", "employees": ["jane"]}
    },
    "projects": {
        "project_a": {
            "budget": 25000,
            "team": ["john", "bob"],
            "status": "active",
            "milestones": {
                "phase1": {"due": "2025-07-01", "completed": True},
                "phase2": {"due": "2025-08-01", "completed": False}
            }
        }
    }
}

#%% Method 2: Using defaultdict for automatic nesting
from collections import defaultdict

def make_nested_dict():
    return defaultdict(make_nested_dict)

auto_nested = make_nested_dict()
auto_nested["level1"]["level2"]["level3"] = "value"
print("Auto-nested:", dict(auto_nested))

# Method 3: Building incrementally
config = {}
config.setdefault("database", {})["host"] = "localhost"
config.setdefault("database", {})["port"] = 5432
config.setdefault("cache", {})["redis"] = {"host": "redis-server", "port": 6379}

print("Config:", config)

# =============================================================================
# 2. ACCESSING NESTED VALUES
# =============================================================================

#%% Basic access (can raise KeyError)
john_age = company["employees"]["john"]["age"]
print(f"John's age: {john_age}")

#%% Using get() method (returns None if missing)
john_salary = company.get("employees", {}).get("john", {}).get("salary")
print(f"John's salary: {john_salary}")

#%% Safe access function (from your example, enhanced)
def safe_get(dictionary, *keys, default=None):
    """Safely navigate nested dictionary using multiple keys"""
    for key in keys:
        try:
            dictionary = dictionary[key]
        except (KeyError, TypeError):
            return default
    return dictionary

#%% Enhanced version with path support
def get_nested_value(data, path, default=None, separator='.'):
    """Get nested value using dot notation: 'employees.john.age'"""
    keys = path.split(separator) if isinstance(path, str) else path
    return safe_get(data, *keys, default=default)

# Examples
print("Safe access examples:")
print(f"John's age: {safe_get(company, 'employees', 'john', 'age')}")
print(f"Missing person: {safe_get(company, 'employees', 'nonexistent', 'age', default='Not found')}")
print(f"Using path notation: {get_nested_value(company, 'employees.john.department')}")

# =============================================================================
# 3. MODIFYING NESTED DICTIONARIES
# =============================================================================

#%% Adding new nested values
def set_nested_value(data, path, value, separator='.'):
    """Set nested value using dot notation"""
    keys = path.split(separator) if isinstance(path, str) else path
    for key in keys[:-1]:
        data = data.setdefault(key, {})
    data[keys[-1]] = value

#%% Add new employee
set_nested_value(company, "employees.alice", {"age": 28, "department": "IT", "salary": 70000})

#%% Update existing values
company["employees"]["john"]["salary"] = 78000
set_nested_value(company, "employees.john.skills", ["Python", "JavaScript", "SQL"])

print("After modifications:")
print(f"Alice: {safe_get(company, 'employees', 'alice')}")
print(f"John's new salary: {safe_get(company, 'employees', 'john', 'salary')}")

# =============================================================================
# 4. ITERATING THROUGH NESTED STRUCTURES
# =============================================================================
#%%
def iterate_nested_dict(data, parent_key='', separator='.'):
    """Flatten nested dictionary to show all paths and values"""
    items = []
    for key, value in data.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(iterate_nested_dict(value, new_key, separator).items())
        else:
            items.append((new_key, value))
    return dict(items)

print("\nFlattened view of company data:")
flattened = iterate_nested_dict(company)
for path, value in list(flattened.items())[:10]:  # Show first 10 items
    print(f"{path}: {value}")

#%% Recursive traversal with custom logic
def find_all_employees_in_department(data, target_dept):
    """Find all employees in a specific department"""
    employees = []
    for emp_name, emp_data in data.get("employees", {}).items():
        if emp_data.get("department") == target_dept:
            employees.append({
                "name": emp_name,
                "age": emp_data.get("age"),
                "salary": emp_data.get("salary")
            })
    return employees

it_employees = find_all_employees_in_department(company, "IT")
print(f"\nIT Department employees: {it_employees}")

# =============================================================================
# 5. ADVANCED OPERATIONS
# =============================================================================

#%% Deep merge function
def deep_merge(dict1, dict2):
    """Recursively merge two nested dictionaries"""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

#%% Example: Add new department data
new_data = {
    "departments": {
        "IT": {"equipment_budget": 15000},  # Add to existing IT dept
        "Marketing": {"budget": 40000, "head": "alice"}  # New department
    },
    "employees": {
        "charlie": {"age": 32, "department": "Marketing", "salary": 68000}
    }
}

merged_company = deep_merge(company, new_data)
print(f"\nAfter merge - IT equipment budget: {safe_get(merged_company, 'departments', 'IT', 'equipment_budget')}")

#%% Search through nested structure
def search_nested_dict(data, search_term, case_sensitive=False):
    """Search for a term in all string values of nested dictionary"""
    results = []
    
    def _search_recursive(obj, path=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{path}.{key}" if path else key
                _search_recursive(value, new_path)
        elif isinstance(obj, (str, int, float)):
            str_obj = str(obj)
            search_str = search_term if case_sensitive else search_term.lower()
            compare_str = str_obj if case_sensitive else str_obj.lower()
            if search_str in compare_str:
                results.append({"path": path, "value": obj})
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                _search_recursive(item, f"{path}[{i}]")
    
    _search_recursive(data)
    return results

#%% Search for "john" in the company data
search_results = search_nested_dict(company, "john", case_sensitive=False)
print(f"\nSearch results for 'john': {search_results}")

# =============================================================================
# 6. VALIDATION AND ERROR HANDLING
# =============================================================================
#%%
def validate_nested_structure(data, schema):
    """Validate nested dictionary against a schema"""
    def _validate_recursive(obj, schema_part, path=""):
        if isinstance(schema_part, dict):
            if not isinstance(obj, dict):
                return [f"Expected dict at {path}, got {type(obj).__name__}"]
            
            errors = []
            for key, expected_type in schema_part.items():
                current_path = f"{path}.{key}" if path else key
                if key not in obj:
                    errors.append(f"Missing required key: {current_path}")
                else:
                    errors.extend(_validate_recursive(obj[key], expected_type, current_path))
            return errors
        else:  # It's a type or callable
            if not isinstance(obj, schema_part):
                return [f"Expected {schema_part.__name__} at {path}, got {type(obj).__name__}"]
            return []
    
    return _validate_recursive(data, schema)

#%% Define schema for employee data
employee_schema = {
    "age": int,
    "department": str,
    "salary": int
}

#%% Validate John's data
john_data = safe_get(company, "employees", "john")
validation_errors = validate_nested_structure(john_data, employee_schema)
print(f"\nValidation errors for John: {validation_errors}")

# =============================================================================
# 7. PERFORMANCE OPTIMIZATIONS
# =============================================================================

#%% Using __getitem__ for faster access when you know the structure
class FastNestedDict:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, path):
        """Access using tuple of keys: obj[('employees', 'john', 'age')]"""
        result = self.data
        for key in path:
            result = result[key]
        return result
    
    def get(self, path, default=None):
        """Safe version of __getitem__"""
        try:
            return self[path]
        except (KeyError, TypeError):
            return default

fast_company = FastNestedDict(company)
print(f"\nFast access - John's age: {fast_company.get(('employees', 'john', 'age'))}")

# =============================================================================
# 8. REAL-WORLD USE CASES
# =============================================================================

#%% Configuration management
app_config = {
    "database": {
        "primary": {
            "host": "db1.example.com",
            "port": 5432,
            "credentials": {"username": "app_user", "password": "secret"}
        },
        "replica": {
            "host": "db2.example.com", 
            "port": 5432,
            "credentials": {"username": "app_user", "password": "secret"}
        }
    },
    "api": {
        "rate_limits": {"requests_per_minute": 1000, "burst": 50},
        "endpoints": {
            "/users": {"auth_required": True, "cache_ttl": 300},
            "/public": {"auth_required": False, "cache_ttl": 3600}
        }
    }
}

#%% API response parsing
api_response = {
    "status": "success",
    "data": {
        "user": {
            "id": 123,
            "profile": {
                "name": "John Doe",
                "preferences": {
                    "theme": "dark",
                    "notifications": {"email": True, "push": False}
                }
            }
        }
    },
    "meta": {"timestamp": "2025-06-19T10:30:00Z", "version": "v2"}
}

print(f"\nUser theme preference: {get_nested_value(api_response, 'data.user.profile.preferences.theme')}")

#%% Game state management
game_state = {
    "player": {
        "stats": {"health": 100, "mana": 50, "level": 5},
        "inventory": {
            "weapons": [{"name": "sword", "damage": 25}],
            "consumables": {"health_potion": 3, "mana_potion": 1}
        },
        "location": {"x": 10, "y": 5, "zone": "forest"}
    },
    "world": {
        "time": {"hour": 14, "day": 1},
        "weather": "sunny"
    }
}

def use_health_potion(state):
    """Example of modifying nested game state"""
    potions = safe_get(state, "player", "inventory", "consumables", "health_potion", default=0)
    if potions > 0:
        # Use potion
        state["player"]["inventory"]["consumables"]["health_potion"] -= 1
        current_health = state["player"]["stats"]["health"]
        state["player"]["stats"]["health"] = min(100, current_health + 25)
        return True
    return False
#%%
print(f"\nBefore potion - Health: {game_state['player']['stats']['health']}, Potions: {game_state['player']['inventory']['consumables']['health_potion']}")
game_state["player"]["stats"]["health"] = 75  # Simulate damage
use_health_potion(game_state)
print(f"After potion - Health: {game_state['player']['stats']['health']}, Potions: {game_state['player']['inventory']['consumables']['health_potion']}")

# =============================================================================
# 9. SUMMARY OF BEST PRACTICES
# =============================================================================
#%%
print("\n" + "="*50)
print("NESTED DICTIONARIES BEST PRACTICES:")
print("="*50)
print("1. Use safe_get() or get() chains for optional nested values")
print("2. Validate structure when loading external data") 
print("3. Use defaultdict for automatic nesting when building incrementally")
print("4. Consider flattening for simple key-value storage")
print("5. Use tuple keys for fast access patterns: obj[('a', 'b', 'c')]")
print("6. Implement deep merge for combining configurations")
print("7. Use path notation ('a.b.c') for human-readable access")
print("8. Handle KeyError and TypeError in navigation functions")
print("9. Consider alternative data structures (namedtuple, dataclass) for fixed schemas")
print("10. Use recursion carefully - watch for circular references")
#%%