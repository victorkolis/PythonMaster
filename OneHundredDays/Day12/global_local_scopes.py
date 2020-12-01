# global_local_scopes.py

# Global variable declaration
eggs = 'eggs'

def change_variable():
    # Local variable declaration
    eggs = 12
    print(f"variable inside the def scope {eggs}")

change_variable()
print(f"variable outside the def scope {eggs}")
