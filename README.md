# Average Grade Calculator in Python

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg?style=flat-square)](https://github.com/cymriccc/Average-Grade-Calculator-Python-/graphs/commit-activity)

A lightweight CLI tool designed to automate student grade aggregation, compute overall averages, and evaluate academic performance against customizable thresholds.

---

## Overview

`Average-Grade-Calculator-Python-` provides a clean, user-friendly console application for calculating grade averages. Engineered with strict input validation and type checking, it handles numerical conversion errors gracefully while producing instant feedback on performance status (e.g., Passing vs. Failing).

---

## Key Features

* **Dynamic Input Handling**: Allows users to input multiple assessment or subject scores cleanly.
* **Defensive Validation**: Guards against non-numeric inputs and out-of-range percentage scores (e.g., values outside 0–100).
* **Automated Pass/Fail Evaluation**: Evaluates calculated overall averages against standard academic pass marks.
* **Formatted Console Output**: Displays formatted arithmetic summaries directly in the terminal interface.

---

## Repository Structure

```text
Average-Grade-Calculator-Python-/
├── main.py          # Primary entry point & grade evaluation logic
├── README.md        # Technical documentation
└── .gitignore       # Python tracking exclusions (__pycache__, bytecode)
```

---

## Getting Started

### Prerequisites

* **Python 3.8+** installed on your system.

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cymriccc/Average-Grade-Calculator-Python-.git
   cd Average-Grade-Calculator-Python-
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

---

## Usage Example

```text
========================================
       AVERAGE GRADE CALCULATOR          
========================================
Enter grade for Subject 1: 88.5
Enter grade for Subject 2: 92.0
Enter grade for Subject 3: 79.5
----------------------------------------
Calculated Average : 86.67%
Academic Status    : PASSED
========================================
```

---

## License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

**Author**: [@cymriccc](https://github.com/cymriccc)
