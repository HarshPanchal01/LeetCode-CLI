# LeetCode-CLI

A command-line interface to interact with LeetCode.

## Setup Instructions

Follow these steps to set up the LeetCode CLI on your local machine.

### Prerequisites

*   Python 3.7+
*   `git`

### 1. Clone the Repository

First, clone this repository to your local machine using git:

```bash
git clone https://github.com/HarshPanchal01/LeetCode-CLI.git
```

### 2. Navigate to the Project Directory

Change your current directory to the newly cloned project folder:

```bash
cd LeetCode-CLI
```

### 3. Create a Python Virtual Environment

It is highly recommended to use a virtual environment to manage project-specific dependencies. This keeps your global Python installation clean.

Create a new virtual environment:

```bash
python3 -m venv .venv
```

### 4. Activate the Virtual Environment

Before installing the dependencies, you need to activate the virtual environment.

*   **On macOS and Linux:**
    ```bash
    source .venv/bin/activate
    ```
*   **On Windows:**
    ```bash
    .venv\Scripts\activate
    ```

Your shell prompt should now be prefixed with `(.venv)`, indicating that the virtual environment is active.

### 5. Install Dependencies

Install the CLI and all its required Python packages using `pip`. The `-e` flag installs the project in "editable" mode, which means any changes you make to the source code will be immediately effective without needing to reinstall.

```bash
pip install -e .
```

### 6. Verify the Installation

You can now run the CLI using the `lc` command. To verify that it's working, you can check the help message:

```bash
lc --help
```

When you are finished using the CLI, you can deactivate the virtual environment by simply running:

```bash
deactivate
```

## Usage

### Login

To get started, you need to log in to your LeetCode account. This is done by providing your `LEETCODE_SESSION` and `csrftoken` cookies. You can get these cookies from your browser's developer tools after logging in to the LeetCode website.

```bash
lc login
```

You will be prompted to enter your username and cookies securely.

### Logout

To log out and clear your stored credentials, simply run:

```bash
lc logout
```

### View Problems

You can fetch a list of problems from LeetCode.

```bash
lc problems
```

**Options:**

*   `--limit <number>`: Specify the number of problems to fetch (default is 20).
*   `--tags <tag1> <tag2>`: Filter problems by one or more tags.
*   `--difficulty <EASY|MEDIUM|HARD>`: Filter problems by difficulty.

**Example:**

Fetch 10 easy problems with the "Array" tag:

```bash
lc problems --limit 10 --difficulty EASY --tags Array
```

### View a Specific Problem

To view the details of a specific problem, use the `view` command with the problem's "title slug". You can find the title slug in the URL of the problem on the LeetCode website (e.g., `https://leetcode.com/problems/two-sum/` has a title slug of `two-sum`).

```bash
lc view two-sum
```

### Submit a Solution

To submit a solution, you'll need the problem's title slug, the programming language, and the path to your solution file.

```bash
lc submit <title-slug> <language> <file-path>
```

**Example:**

```bash
lc submit two-sum python solutions/two_sum.py
```

### View Submission Stats

You can view your overall LeetCode statistics or a list of your recent submissions.

**View Overall Stats:**

```bash
lc stats
```

**View Recent Submissions:**

```bash
lc stats --submissions
```
