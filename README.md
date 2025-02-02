# Custom-Firewall-Simulator

import random
import logging

logging.basicConfig(level=logging.CRITICAL)  # Log seviyesini ayarla

def generate_custom_ip():
    """Generate a custom IP address."""
    return f"10.0.0.{random.randint(1, 254)}"

def check_custom_rules(ip, custom_rules):
    """Check if the IP address matches any custom rule and return the action."""
    for rule_ip, action in custom_rules.items():
        if ip == rule_ip:
            return action
    return "allow"  # Default action if no rule matches

def simulate_network_traffic():
    # Define the custom rules (key: IP address, value: action)
    custom_rules = {
        "10.0.0.5": "block",
        "10.0.0.10": "block",
        "10.0.0.15": "block",
        "10.0.0.20": "block",
        "10.0.0.25": "block",
        "10.0.0.30": "block"
    }

    # Simulate network traffic
    for _ in range(12):
        ip_address = generate_custom_ip()
        action = check_custom_rules(ip_address, custom_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

# Global düzeyde custom_rules değişkeni tanımla
custom_rules = {}

def add_custom_rule():
    global custom_rules
    ip_address = input("Enter IP address: ")
    action = input("Enter action (block/allow): ")
    custom_rules[ip_address] = action
    logging.info(f"Custom rule added: IP {ip_address} will be {action}ed")

if __name__ == "__main__":
    simulate_network_traffic()
    add_custom_rule()
