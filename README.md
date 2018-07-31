# dagstatus

Small utility to turn HTCondor DAG status file into more useful summary output

## Install

```
git clone https://github.com/raggleton/dagstatus.git
cd dagstatus
pip install --user -e .
```

## Running

First ensure your DAG outputs a status file by adding a line:

```
NODE_STATUS_FILE <status filename>
```

Then once your DAG is running:

```
DAGstatus <status filename>
```

To avoid printing the status of all nodes, use the `-s` option.

## Customise

Play with `bin/DAGstatus_config.json`
