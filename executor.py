# Pipeline step executor with retry logic
import time
import json
from datetime import datetime

def execute_step(step_config, step_number, attempt=1, max_retries=3):
    """Execute a single pipeline step with retry logic"""

    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'step': step_number,
        'type': step_config.get('type'),
        'attempt': attempt,
        'status': None,
        'message': None
    }

    try:
        # Simulate step execution
        print(f"Executing step {step_number} (attempt {attempt}): {step_config.get('type')}")

        # Simulate random failures for demo (remove in production)
        import random
        if random.random() < 0.3 and attempt < max_retries:  # 30% failure rate
            raise Exception("Simulated transient failure")

        log_entry['status'] = 'success'
        log_entry['message'] = f"Step {step_number} completed successfully"

    except Exception as e:
        if attempt < max_retries:
            # Exponential backoff
            delay = 2 ** (attempt - 1)
            log_entry['status'] = 'retry'
            log_entry['message'] = f"Step failed: {str(e)}. Retrying in {delay}s"
            log_entry['next_attempt_in'] = delay

            print(json.dumps(log_entry))
            time.sleep(delay)

            # Recursive retry
            return execute_step(step_config, step_number, attempt + 1, max_retries)
        else:
            log_entry['status'] = 'failed'
            log_entry['message'] = f"Step failed after {max_retries} attempts: {str(e)}"

    print(json.dumps(log_entry))
    return log_entry['status'] == 'success'
