## `pandasai` test

A quick test for the [pandasai](https://github.com/gventuri/pandas-ai) package.

## Setup

To get things running

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To play with `ai.py` in a shell, execute `python` in your virtualenv to start up the repl, and then in the repl do this:

```python
exec(open("ai.py").read())

# Now you can run commands like `df.chat`
df.chat("What was the metric with the highest value?")
```

Notes:

- The data corresponds to a 1hr window of data for the error ratio of three different functions
- `metric` refers to the metric name, which is `{module}.{function}`
- `value` refers to the error ratio, which is between 0 and 1

## Impressions

This loads the error rate for several functions into a dataframe enhanced with chat capabilities. Here were some very cursory findings:

- the only function with a nonzero error rate was app.panda and the ai isolated it (easy, i know)
- the error rate is effectively a random walk, and if a human looked at it, we wouldn't see a discernible "spike"... however it told me there was a spike in the data (at first)
- this implementation does not seem keen to explain how it calculated things — i asked it to explain why there was a spike, and it just returned the same answer
- HOWEVER when i asked it to use the adaptive threshold approach for calculating spikes (from the google sre book), it told me there was no spike. interesting.

```
>>> df.chat('Which metrics have the highest values?')
'The metrics with the highest values are: app.panda.'

>>> df.chat('Is there a spike in the values for metric app.panda at any point?')
'There is a spike in the values for metric app.panda.'

>>> df.chat('Is there a spike in the values for metric app.panda at any point? Explain why')
'There is a spike in the values for metric app.panda.'

>>> df.chat('Is there a spike in the values for metric app.panda at any point? Use the adaptive threshold approach defined in the google sre book')
'There is no spike in the values for metric app.panda.'
```