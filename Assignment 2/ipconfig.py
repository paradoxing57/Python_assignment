import platform
import subprocess

def get_default_gateway():
    system = platform.system()
    if system == 'Windows':
        cmd = 'ipconfig'
    elif system in ('Linux', 'Darwin'):
        cmd = 'ifconfig'
    else:
        return "Unsupported operating system"

    try:
        output = subprocess.check_output(cmd)
        output = output.decode('utf-8')  # Convert bytes to string
        if system == 'Windows':
            gateway_index = output.index('Default Gateway') + len('Default Gateway') + 2
            gateway = output[gateway_index:].split('\n', 1)[0]
        elif system == 'Linux':
            gateway_index = output.index('default') + len('default') + 2
            gateway = output[gateway_index:].split()[0]
        else:  # macOS
            gateway_index = output.index('default') + len('default') + 2
            gateway = output[gateway_index:].split()[0]
        return gateway
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Example usage
default_gateway = get_default_gateway()
print("Default Gateway:", default_gateway)
