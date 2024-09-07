
# Task Tracker CLI

A simple command-line interface (CLI) for managing tasks. This tool allows you to add, update, delete, and manage tasks in different statuses such as "todo", "in-progress", and "done". Tasks are saved to a local JSON file for persistence.

## Features

- Add new tasks
- Update task descriptions
- Delete tasks
- Mark tasks as "in-progress" or "done"
- List tasks by status
- Simple and easy-to-use command-line interface

## Prerequisites

- Python 3.x

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/MurtazaJ5253/task-tracker-cli.git
    ```

2. Navigate into the project directory:

    ```bash
    cd task-tracker-cli
    ```

3. Install any necessary dependencies (though the current version of the code does not have any external dependencies).

## Usage

Run the script with the appropriate command-line arguments. Below are some examples of how to use the task tracker.

### Adding a Task

```bash
python task_tracker.py add "Buy groceries"
```

This will add a new task with the description "Buy groceries".

### Updating a Task

```bash
python task_tracker.py update 1 "Buy groceries and cook dinner"
```

This will update the task with ID 1 to the new description "Buy groceries and cook dinner".

### Deleting a Task

```bash
python task_tracker.py delete 1
```

This will delete the task with ID 1.

### Marking a Task as In Progress

```bash
python task_tracker.py mark-in-progress 1
```

This will mark the task with ID 1 as "in-progress".

### Marking a Task as Done

```bash
python task_tracker.py mark-done 1
```

This will mark the task with ID 1 as "done".

### Listing All Tasks

```bash
python task_tracker.py list
```

This will list all tasks.

### Listing Tasks by Status

```bash
# List only "todo" tasks
python task_tracker.py list todo

# List only "in-progress" tasks
python task_tracker.py list in-progress

# List only "done" tasks
python task_tracker.py list done
```

## File Storage

Tasks are stored in a JSON file called `tasks.json` located in the project directory. The file is automatically created when you add the first task.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any issues or questions, feel free to reach out or open an issue on GitHub.


