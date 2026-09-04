#!/usr/bin/env python3
# -*- mode: python; indent-tabs-mode: nil; python-indent-level: 4 -*-
# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

import sys
import os
import re
import math
import json
from pathlib import Path

TOOLBOX_HOME = os.environ.get('TOOLBOX_HOME')
if TOOLBOX_HOME is None:
    print("This script requires libraries that are provided by the toolbox project.")
    print("Toolbox can be acquired from https://github.com/perftool-incubator/toolbox and")
    print("then use 'export TOOLBOX_HOME=/path/to/toolbox' so that it can be located.")
    exit(1)
else:
    p = Path(TOOLBOX_HOME) / 'python'
    if not p.exists() or not p.is_dir():
        print("ERROR: <TOOLBOX_HOME>/python ('%s') does not exist!" % (p))
        exit(2)
    sys.path.append(str(p))
from toolbox.cdm_metrics import CDMMetrics

params = {}

class t_global(object):
     args = None

def process_options():
    import argparse
    parser = argparse.ArgumentParser(description = 'Post process raw benchmark data into Common Data Model output')

    parser.add_argument('--model',
                        dest = 'model',
                        help = '',
                        default = "llama"
                        )

    t_global.args, unknown = parser.parse_known_args()

    return()

def main():
    process_options()
    metrics = CDMMetrics()

    # The period used to report the official result is the 'measurement' period.

    iter_sample = {
        'primary-period': "measurement",
        'benchmark': "pytorch",
        'periods': [],
        'rickshaw-bench-metric': { 'schema': { 'version': '2021.04.12' } }
        }

    metric_files = []

    with open("benchmark/begin.txt", "r") as f:
        begin = int(math.floor(1000 * float(f.readline())))
    with open("benchmark/end.txt", "r") as f:
        end = int(math.floor(1000 * float(f.readline())))

    with open("benchmark/run_benchmark_output.txt", "r") as f:
        initial_data = f.readline()
        d = json.loads(f.read())

        # example file:
        # Running TorchBenchModelConfig(name='llama', test='eval', device='cuda', batch_size=None, extra_args=[], extra_env=None, output_dir=None) ... [done]
        # {
        # "name": "test_bench",
        # "environ": {
        #     "pytorch_git_version": "2d9a7eec9ccc362e00d2fd2b4b845d3f90d955aa",
        #     "pytorch_version": "2.3.1",
        #     "device": "NVIDIA L40S"
        # },
        # "metrics": {
        #     "model=llama, test=eval, device=cuda, bs=None, extra_args=[], metric=latencies": 4.101454,
        #     "model=llama, test=eval, device=cuda, bs=None, extra_args=[], metric=cpu_peak_mem": 0.8515625,
        #     "model=llama, test=eval, device=cuda, bs=None, extra_args=[], metric=gpu_peak_mem": 3.8720703125
        #  }
        # }

        iter_sample['primary-metric'] = 'latency-milliseconds'
        period = { 'name': 'measurement', 'metric-files': [] }
        file_id = 'measurement'
        desc = {'source' : 'pytorch', 'class': 'count', 'type': 'elapsed-time-milliseconds', 'default-aggregation': 'avg'}
        names = {}
        sample = {'begin': begin, 'end': end, 'value': end - begin}
        metrics.log_sample(file_id, desc, names, sample)

        for key in d['metrics'].keys():
            if (re.search("metric=latencies$", key) and re.findall("[0-9]+(?:[.][0-9]+)?", str(d['metrics'][key])) ):
                desc = {'source' : 'pytorch', 'class': 'latency', 'type': 'latency-milliseconds', 'default-aggregation': 'max'}
                sample = {'begin': begin, 'end': end, 'value': d['metrics'][key]}
                metrics.log_sample(file_id, desc, names, sample)
            else:
                print("skipping: " + key)

        metric_file_name = metrics.finish_samples()
        period['metric-files'].append(metric_file_name)
        iter_sample['periods'].append(period)
        with open('postprocess/post-process-data.json', 'w') as f:
            f.write(json.dumps(iter_sample))


if __name__ == "__main__":
    exit(main())
