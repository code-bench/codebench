<p align="center">
  <a href="https://github.com/li-boxuan/codebench">
    <img src="https://user-images.githubusercontent.com/25746010/49685836-0ec63580-fb26-11e8-8c33-d8597319d15b.png" width=200>
  </a>
</p>

<p align="center"><b>Automated code benchmark solution.</b></p>
<p align="center">Empower developers with tools to trace and analyze project performances.</p>

## Introduction

### What is Codebench?

Codebench is a tool that runs user-defined benchmark programs, monitors system
information and generates reports. It is most powerful when using in a project
tracked by git. It runs benchmarks based on different commits and reports the
system usage difference, so that users can compare and track performance
changes of their project across commits. It can also be used in CI (Continuous
Integration) to detect recent commits that increases/decreases project
performance.

### What Codebench is not?

Codebench itself does not provide benchmark programs. It is not smart
enough to generate a benchmark program for your code. Instead, it can be
considered as a wrapper or a supervisor for your benchmark.

### Features

- Normal Mode
    - comparison among commits
    - auto-generated report
- CI Mode (in development)
    - comparison with baseline
    - auto-generated report
    - threshold alarms

## Installation

Codebench can be simply installed by running:

```bash
pip install codebench
```

## Usage

### Command Line Interface

Codebench provides a command line interface. Run `codebench -h` for details.

### Sample

See [codebench-sample](https://github.com/li-boxuan/codebench-sample)
for details.

A quick demo is demonstrated below:

```bash
codebench --before ./before_script.sh --start ./benchmark.py \
--report_type chart --commits cb91b8 3cd96d bb1541
```

![memory_usage](https://user-images.githubusercontent.com/25746010/49643853-c0dffd80-fa51-11e8-8ffb-95da64347a41.png)
![elapsed_time](https://user-images.githubusercontent.com/25746010/49643851-c0476700-fa51-11e8-8014-064c666336e7.png)
![cpu_usage](https://user-images.githubusercontent.com/25746010/49643850-c0476700-fa51-11e8-9d28-5dbe818a3bf3.png)
