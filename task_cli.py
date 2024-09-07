import argparse
import json
import os

# File to store tasks
TASK_FILE = 'tasks.json'


# Load tasks from the file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return {}


# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = max(map(int, tasks.keys())) + 1 if tasks else 1
    tasks[task_id] = {'description': description, 'status': 'todo'}
    save_tasks(tasks)
    print(f'Task added successfully (ID: {task_id})')


# Update an existing task
def update_task(task_id, description):
    tasks = load_tasks()
    task_id = str(task_id)
    if task_id in tasks:
        tasks[task_id]['description'] = description
        save_tasks(tasks)
        print(f'Task {task_id} updated successfully')
    else:
        print(f'Task {task_id} not found')


# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    task_id = str(task_id)
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        print(f'Task {task_id} deleted successfully')
    else:
        print(f'Task {task_id} not found')


# Mark a task as "in-progress"
def mark_in_progress(task_id):
    update_status(task_id, 'in-progress')


# Mark a task as "done"
def mark_done(task_id):
    update_status(task_id, 'done')


# Update task status
def update_status(task_id, status):
    tasks = load_tasks()
    task_id = str(task_id)
    if task_id in tasks:
        tasks[task_id]['status'] = status
        save_tasks(tasks)
        print(f'Task {task_id} marked as {status}')
    else:
        print(f'Task {task_id} not found')


# List tasks, optionally filtered by status
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = {k: v for k, v in tasks.items() if v['status'] == status}

    if tasks:
        for task_id, task in tasks.items():
            print(f'{task_id}: {task["description"]} [{task["status"]}]')
    else:
        print(f'No tasks{" with status " + status if status else ""} found')


# Main function to parse command line arguments
def main():
    parser = argparse.ArgumentParser(description='Task Tracker CLI')

    subparsers = parser.add_subparsers(dest='command')

    # Add task
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', type=str, help='Task description')

    # Update task
    parser_update = subparsers.add_parser('update', help='Update a task')
    parser_update.add_argument('id', type=int, help='Task ID')
    parser_update.add_argument('description', type=str, help='New task description')

    # Delete task
    parser_delete = subparsers.add_parser('delete', help='Delete a task')
    parser_delete.add_argument('id', type=int, help='Task ID')

    # Mark task in progress
    parser_in_progress = subparsers.add_parser('mark-in-progress', help='Mark task as in-progress')
    parser_in_progress.add_argument('id', type=int, help='Task ID')

    # Mark task as done
    parser_done = subparsers.add_parser('mark-done', help='Mark task as done')
    parser_done.add_argument('id', type=int, help='Task ID')

    # List tasks
    parser_list = subparsers.add_parser('list', help='List tasks')
    parser_list.add_argument('status', nargs='?', default=None, choices=['todo', 'in-progress', 'done'],
                             help='Task status to filter by')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'mark-in-progress':
        mark_in_progress(args.id)
    elif args.command == 'mark-done':
        mark_done(args.id)
    elif args.command == 'list':
        list_tasks(args.status)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
