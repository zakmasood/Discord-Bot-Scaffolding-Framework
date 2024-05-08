"""
Testing Harness for CRUD Operations

Author: Zakariya Masood

This script creates a testing harness to evaluate the performance of CRUD (Create, Read, Update, Delete) operations
on different tables using the functions provided in the `db_access_layer.py` module.

The harness generates synthetic data for each table and performs a specified number of CRUD operations on each table.
It measures the execution time, CPU usage, and memory usage for each set of operations.

The performance results are displayed in a formatted table using the `rich` library, showing the time taken,
CPU usage, and memory usage for each operation.

The script tests the performance with different numbers of operations: 1000, 10000, and 100000.

Dependencies:
- `db_access_layer.py`: Module containing the CRUD functions for the tables.
- `rich`: Library for rich text formatting and table display.
- `psutil`: Library for accessing system information and process utilities.
- `logging`: Library for logging messages and exceptions.

Usage:
1. Ensure that the `db_access_layer.py` module is in the same directory as this script.
2. Install the required dependencies (`rich`, `psutil`, and `logging`) if not already installed.
3. Run the script using a Python interpreter.
4. The performance results will be displayed in the console, and any exceptions will be logged to a file.

Note: This script assumes that the necessary tables are already created in the database.
"""

import platform
import time
import random
import string
import psutil
import logging
from rich import print
from rich.console import Console
from rich.table import Table
from db_access_layer import *
from create_tables import *

# Configure logging
logging.basicConfig(filename='test_harness.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def print_machine_specs():
    console = Console()
    table = Table(title="Test Machine Specifications")
    table.add_column("Specification", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    # System information
    system = platform.system()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()

    # CPU information
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq().current

    # Memory information
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 * 1024 * 1024)  # Convert to GB
    available_memory = memory.available / (1024 * 1024 * 1024)  # Convert to GB

    # Disk information
    disk = psutil.disk_usage('/')
    total_disk = disk.total / (1024 * 1024 * 1024)  # Convert to GB
    used_disk = disk.used / (1024 * 1024 * 1024)  # Convert to GB
    free_disk = disk.free / (1024 * 1024 * 1024)  # Convert to GB

    table.add_row("System", system)
    table.add_row("Release", release)
    table.add_row("Version", version)
    table.add_row("Machine", machine)
    table.add_row("Processor", processor)
    table.add_row("CPU Count", str(cpu_count))
    table.add_row("CPU Frequency", f"{cpu_freq:.2f} MHz")
    table.add_row("Total Memory", f"{total_memory:.2f} GB")
    table.add_row("Available Memory", f"{available_memory:.2f} GB")
    table.add_row("Total Disk Space", f"{total_disk:.2f} GB")
    table.add_row("Used Disk Space", f"{used_disk:.2f} GB")
    table.add_row("Free Disk Space", f"{free_disk:.2f} GB")

    console.print(table)

# Function to generate random user data with exception handling
def generate_user_data():
    try:
        user_id = random.randint(10000000000000000, 99999999999999999)
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        avatar = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        is_bot = random.choice([True, False])
        joined_at = int(time.time())
        return user_id, username, avatar, is_bot, joined_at
    except Exception as e:
        logging.error(f"Error generating user data: {str(e)}")
        return None

# Function to generate random server data with exception handling
def generate_server_data():
    try:
        server_id = random.randint(10000000000000000, 99999999999999999)
        name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        icon = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        prefix = random.choice(['!', '#', '$', '%'])
        language = random.choice(['en', 'es', 'fr', 'de'])
        mod_role = random.randint(10000000000000000, 99999999999999999)
        admin_role = random.randint(10000000000000000, 99999999999999999)
        mute_role = random.randint(10000000000000000, 99999999999999999)
        log_channel = random.randint(10000000000000000, 99999999999999999)
        return server_id, name, icon, prefix, language, mod_role, admin_role, mute_role, log_channel
    except Exception as e:
        logging.error(f"Error generating server data: {str(e)}")
        return None

# Function to generate random reminder data with exception handling
def generate_reminder_data(server_id, user_id):
    try:
        reminder_text = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        remind_at = int(time.time()) + random.randint(60, 3600)
        return server_id, user_id, reminder_text, remind_at
    except Exception as e:
        logging.error(f"Error generating reminder data: {str(e)}")
        return None

# Function to generate random moderation data with exception handling
def generate_moderation_data(server_id, user_id, moderator_id):
    try:
        action = random.choice(['WARN', 'KICK', 'MUTE'])
        reason = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
        created_at = int(time.time())
        return server_id, user_id, action, reason, moderator_id, created_at
    except Exception as e:
        logging.error(f"Error generating moderation data: {str(e)}")
        return None

# Function to generate random suggestion data with exception handling
def generate_suggestion_data(server_id, user_id):
    try:
        suggestion_text = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
        message_id = random.randint(10000000000000000, 99999999999999999)
        created_at = int(time.time())
        return server_id, user_id, suggestion_text, message_id, created_at
    except Exception as e:
        logging.error(f"Error generating suggestion data: {str(e)}")
        return None

# Function to generate random starboard data with exception handling
def generate_starboard_data(server_id):
    try:
        channel_id = random.randint(10000000000000000, 99999999999999999)
        min_stars = random.randint(1, 10)
        return server_id, channel_id, min_stars
    except Exception as e:
        logging.error(f"Error generating starboard data: {str(e)}")
        return None

# Function to perform CRUD operations and measure performance with exception handling
def perform_crud_operations(num_operations):
    try:
        console = Console()
        table = Table(title=f"Performance Results ({num_operations} Operations)")
        table.add_column("Operation", justify="right", style="cyan", no_wrap=True)
        table.add_column("Time (seconds)", style="magenta")
        table.add_column("CPU Usage (%)", justify="right", style="green")
        table.add_column("Memory Usage (MB)", justify="right", style="blue")

        # User CRUD operations
        start_time = time.time()
        cpu_percent_start = psutil.cpu_percent()
        memory_usage_start = psutil.Process().memory_info().rss / 1024 / 1024
        for _ in range(num_operations):
            user_data = generate_user_data()
            if user_data:
                create_user(*user_data)
                user_id = user_data[0]
                read_user(user_id)
                update_user(user_id, username='updated_user')
                delete_user(user_id)
        end_time = time.time()
        cpu_percent_end = psutil.cpu_percent()
        memory_usage_end = psutil.Process().memory_info().rss / 1024 / 1024
        execution_time = end_time - start_time
        cpu_usage = cpu_percent_end - cpu_percent_start
        memory_usage = memory_usage_end - memory_usage_start
        table.add_row("User CRUD", f"{execution_time:.2f}", f"{cpu_usage:.2f}", f"{memory_usage:.2f}")

        # Server CRUD operations
        start_time = time.time()
        cpu_percent_start = psutil.cpu_percent()
        memory_usage_start = psutil.Process().memory_info().rss / 1024 / 1024
        for _ in range(num_operations):
            server_data = generate_server_data()
            if server_data:
                create_server(*server_data)
                server_id = server_data[0]
                read_server(server_id)
                update_server(server_id, name='updated_server')
                delete_server(server_id)
        end_time = time.time()
        cpu_percent_end = psutil.cpu_percent()
        memory_usage_end = psutil.Process().memory_info().rss / 1024 / 1024
        execution_time = end_time - start_time
        cpu_usage = cpu_percent_end - cpu_percent_start
        memory_usage = memory_usage_end - memory_usage_start
        table.add_row("Server CRUD", f"{execution_time:.2f}", f"{cpu_usage:.2f}", f"{memory_usage:.2f}")

        # # Reminder CRUD operations
        # start_time = time.time()
        # cpu_percent_start = psutil.cpu_percent()
        # memory_usage_start = psutil.Process().memory_info().rss / 1024 / 1024
        # for _ in range(num_operations):
        #     user_data = generate_user_data()
        #     server_data = generate_server_data()
        #     if user_data and server_data:
        #         create_user(*user_data)
        #         create_server(*server_data)
        #         reminder_data = generate_reminder_data(server_data[0], user_data[0])
        #         if reminder_data:
        #             create_reminder(*reminder_data)
        #             reminder_id = read_reminder(1)[0]
        #             update_reminder(reminder_id, reminder_text='updated_reminder')
        #             delete_reminder(reminder_id)
        #         delete_user(user_data[0])
        #         delete_server(server_data[0])
        # end_time = time.time()
        # cpu_percent_end = psutil.cpu_percent()
        # memory_usage_end = psutil.Process().memory_info().rss / 1024 / 1024
        # execution_time = end_time - start_time
        # cpu_usage = cpu_percent_end - cpu_percent_start
        # memory_usage = memory_usage_end - memory_usage_start
        # table.add_row("Reminder CRUD", f"{execution_time:.2f}", f"{cpu_usage:.2f}", f"{memory_usage:.2f}")

        # # Moderation CRUD operations
        # start_time = time.time()
        # cpu_percent_start = psutil.cpu_percent()
        # memory_usage_start = psutil.Process().memory_info().rss / 1024 / 1024
        # for _ in range(num_operations):
        #     user_data = generate_user_data()
        #     server_data = generate_server_data()
        #     moderator_data = generate_user_data()
        #     if user_data and server_data and moderator_data:
        #         create_user(*user_data)
        #         create_user(*moderator_data)
        #         create_server(*server_data)
        #         moderation_data = generate_moderation_data(server_data[0], user_data[0], moderator_data[0])
        #         if moderation_data:
        #             create_moderation(*moderation_data)
        #             moderation_id = read_moderation(1)[0]
        #             update_moderation(moderation_id, reason='updated_reason')
        #             delete_moderation(moderation_id)
        #         delete_user(user_data[0])
        #         delete_user(moderator_data[0])
        #         delete_server(server_data[0])
        # end_time = time.time()
        # cpu_percent_end = psutil.cpu_percent()
        # memory_usage_end = psutil.Process().memory_info().rss / 1024 / 1024
        # execution_time = end_time - start_time
        # cpu_usage = cpu_percent_end - cpu_percent_start
        # memory_usage = memory_usage_end - memory_usage_start
        # table.add_row("Moderation CRUD", f"{execution_time:.2f}", f"{cpu_usage:.2f}", f"{memory_usage:.2f}")

        # # Suggestion CRUD operations
        # start_time = time.time()
        # cpu_percent_start = psutil.cpu_percent()
        # memory_usage_start = psutil.Process().memory_info().rss / 1024 / 1024
        # for _ in range(num_operations):
        #     user_data = generate_user_data()
        #     server_data = generate_server_data()
        #     if user_data and server_data:
        #         create_user(*user_data)
        #         create_server(*server_data)
        #         suggestion_data = generate_suggestion_data(server_data[0], user_data[0])
        #         if suggestion_data:
        #             create_suggestion(*suggestion_data)
        #             suggestion_id = read_suggestion(1)[0]
        #             update_suggestion(suggestion_id, status='approved')
        #             delete_suggestion(suggestion_id)
        #         delete_user(user_data[0])
        #         delete_server(server_data[0])
        # end_time = time.time()
        # cpu_percent_end = psutil.cpu_percent()
        # memory_usage_end = psutil.Process().memory_info().rss / 1024 / 1024
        # execution_time = end_time - start_time
        # cpu_usage = cpu_percent_end - cpu_percent_start
        # memory_usage = memory_usage_end - memory_usage_start
        # table.add_row("Suggestion CRUD", f"{execution_time:.2f}", f"{cpu_usage:.2f}", f"{memory_usage:.2f}")

        # # Starboard CRUD operations
        # start_time = time.time()
        # cpu_percent_start = psutil.cpu_percent()
        # memory_usage_start = psutil.Process().memory_info().rss / 1024 / 1024
        # for _ in range(num_operations):
        #     server_data = generate_server_data()
        #     if server_data:
        #         create_server(*server_data)
        #         starboard_data = generate_starboard_data(server_data[0])
        #         if starboard_data:
        #             create_starboard(*starboard_data)
        #             star_id = read_starboard(1)[0]
        #             update_starboard(star_id, min_stars=5)
        #             delete_starboard(star_id)
        #         delete_server(server_data[0])
        # end_time = time.time()
        # cpu_percent_end = psutil.cpu_percent()
        # memory_usage_end = psutil.Process().memory_info().rss / 1024 / 1024
        # execution_time = end_time - start_time
        # cpu_usage = cpu_percent_end - cpu_percent_start
        # memory_usage = memory_usage_end - memory_usage_start
        # table.add_row("Starboard CRUD", f"{execution_time:.2f}", f"{cpu_usage:.2f}", f"{memory_usage:.2f}")

        console.print(table)
    except Exception as e:
        logging.error(f"Error performing CRUD operations: {str(e)}")

# Invoke the function to create the tables
try:
    create_manobloom_tables()
except Exception as e:
    logging.error(f"Error creating tables: {str(e)}")

print_machine_specs()

# Test with different number of operations
perform_crud_operations(1000)
perform_crud_operations(10000)
perform_crud_operations(100000)