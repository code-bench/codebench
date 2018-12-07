# codebench
Automated code benchmark solution. Empower developers with tools to trace and analyze project performances.

## Sample Usage

See [codebench-sample](https://github.com/li-boxuan/codebench-sample) for details.
```bash
codebench --before ./before_script.sh --start ./benchmark.py \
--report_type chart --commits cb91b8 3cd96d bb1541
```
![memory_usage](https://user-images.githubusercontent.com/25746010/49643853-c0dffd80-fa51-11e8-8ffb-95da64347a41.png)
![elapsed_time](https://user-images.githubusercontent.com/25746010/49643851-c0476700-fa51-11e8-8014-064c666336e7.png)
![cpu_usage](https://user-images.githubusercontent.com/25746010/49643850-c0476700-fa51-11e8-9d28-5dbe818a3bf3.png)


### TODO:
- prettier report (maybe a web page)
- more reported information (disk, memory, etc.)
- samples (put into readme)
- first release
- add CI
- specify commit range (instead of a list)
- use configuration file (with parser maybe)
- should monitor child processes
- exception handling (should reset commit when encountering exception)

### DONE:
- specify a list of commits, run benchmark
- report CPU usage information

