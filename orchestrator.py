# Pipeline orchestrator - control plane entrypoint
import sys
import yaml
from validator import validate_config
from executor import execute_step

def run_pipeline(config_path):
    """Main orchestrator entry point"""

    print(f"=== Pipeline Orchestrator ===")
    print(f"Config: {config_path}\n")

    # Step 1: Validate config
    print("Step 1: Validating configuration...")
    validation = validate_config(config_path)

    if not validation['valid']:
        print(f"❌ Validation failed:")
        for error in validation['errors']:
            print(f"  - {error}")
        return False

    print("✅ Validation passed\n")
    config = validation['config']

    # Step 2: Execute transformations
    print("Step 2: Executing transformations...")
    retry_policy = config.get('retry_policy', {})
    max_retries = retry_policy.get('max_retries', 3)

    transformations = config.get('transformations', [])
    for i, step in enumerate(transformations, 1):
        success = execute_step(step, i, max_retries=max_retries)
        if not success:
            print(f"\n❌ Pipeline failed at step {i}")
            return False

    print("\n✅ Pipeline completed successfully")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python orchestrator.py <config_file>")
        sys.exit(1)

    run_pipeline(sys.argv[1])
