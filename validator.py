# Config validator - guardrails before execution

import yaml

FORBIDDEN_PATHS = ["/system","/admin","/root"] # it can be hadoop or gcp paths in production

def validate_config_path(config_path):
    #this validates the pipeline config before execution
    with open(config_path,'r') as f:
        config = yaml.safe_load(f)

    errors = []

    #Check required fields
    if 'schema' not in config or 'version' not in config['schema']:
        errors.append("Schema version is required")

    #Check forbidden sink paths
    sink_path = config.get('sink',{}).get('path','')
    for forbidden in FORBIDDEN_PATHS:
        if sink_path.startswith(forbidden):
            errors.append(f"Sink path '{sink_path}' is forbidden as it starts with root path")

    #Check retry policy
    retry = config.get('retry_policy', {})
    if retry.get('max_retries', 0) > 3:
        errors.append("Max retries cannot exceed 3")

    return {
        'valid': len(errors) == 0,
        'errors': errors,
        'config' : config
    }

