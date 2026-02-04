# Schema compatibility checker
def check_schema_compatibility(old_schema, new_schema):
    """Check if new schema is backward compatible with old schema"""

    errors = []
    old_fields = {f['name']: f for f in old_schema.get('fields', [])}
    new_fields = {f['name']: f for f in new_schema.get('fields', [])}

    # Check for deleted columns
    deleted = set(old_fields.keys()) - set(new_fields.keys())
    if deleted:
        errors.append(f"Columns deleted (not allowed): {deleted}")

    # Check for type changes
    for name in old_fields:
        if name in new_fields:
            if old_fields[name].get('type') != new_fields[name].get('type'):
                errors.append(f"Column '{name}' type changed from {old_fields[name]['type']} to {new_fields[name]['type']}")

    # Check for PK changes
    old_pk = [f['name'] for f in old_schema.get('fields', []) if f.get('primary_key')]
    new_pk = [f['name'] for f in new_schema.get('fields', []) if f.get('primary_key')]
    if old_pk != new_pk:
        errors.append(f"Primary key changed from {old_pk} to {new_pk}")

    return {
        'compatible': len(errors) == 0,
        'errors': errors,
        'added_columns': list(set(new_fields.keys()) - set(old_fields.keys()))
    }
