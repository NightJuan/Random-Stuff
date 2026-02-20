def is_special(character):
  # Returns True if the character is NOT alphanumeric
  return not character.isalnum()

# Example usage:
print(f"'A' is special: {is_special('A')}")
print(f"'1' is special: {is_special('1')}")
print(f"'$' is special: {is_special('$')}")
print(f"' ' is special: {is_special(' ')}") # Note: Space is considered a special character here
