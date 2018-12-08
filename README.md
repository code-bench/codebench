<p align="center">
  <a href="https://github.com/li-boxuan/codebench">
    <img src="https://user-images.githubusercontent.com/25746010/49685836-0ec63580-fb26-11e8-8c33-d8597319d15b.png" width=200>
  </a>
</p>

<p align="center"><b>Automated code benchmark solution.</b></p>
<p align="center">Empower developers with tools to trace and analyze project performances.</p>

## Sample Usage

See [codebench-sample](https://github.com/li-boxuan/codebench-sample) for details.
```bash
codebench --before ./before_script.sh --start ./benchmark.py \
--report_type chart --commits cb91b8 3cd96d bb1541
```
![memory_usage](https://user-images.githubusercontent.com/25746010/49643853-c0dffd80-fa51-11e8-8ffb-95da64347a41.png)
![elapsed_time](https://user-images.githubusercontent.com/25746010/49643851-c0476700-fa51-11e8-8014-064c666336e7.png)
![cpu_usage](https://user-images.githubusercontent.com/25746010/49643850-c0476700-fa51-11e8-9d28-5dbe818a3bf3.png)
