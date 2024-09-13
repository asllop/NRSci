# NRSci

This project provides one Python 3 module, `nrsci`. It's used to tranform New Relic data (anything that can be queried with [NRQL](https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/introduction-nrql-new-relics-query-language/)) into Pandas data frames.

Sometimes we want to perfrom complex calculations with our data and NRQL isn't able cover our use cases. For these cases we have `nrsci`, that allows us to download data from New Relic in any arbitrary size, not limited to 2000 results, and convert it into data frames so we can apply any data science technique.

## Installation

First clone this repo, and then install the `nrsci` module with pip3:

```
$ pip3 install git+file:///path/to/cloned/repo/NRSci
```

## Requirements

NRSci makes use of the [NerdGraph API](https://docs.newrelic.com/docs/apis/nerdgraph/get-started/introduction-new-relic-nerdgraph/), so you will need to set up a [user key](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#user-api-key).

## Usage

You can use `nrsci` to load data from your New Relic account and perform complex calculations using Python:

```Python
from nrsci import NerdGraph, Mapper
import pandas as pd
import datetime as dt

# Set up NerdGraph access
ng = NerdGraph("YOUR ACCOUNT ID", "YOUR USER KEY", NerdGraph.Endpoint.US)

# Configure mapper, to obtain events of type 'MyEventType' from New Relic, since 60 minutes ago until now
mapper = Mapper(ng, "MyEventType").since(dt.datetime.now() - dt.timedelta(minutes = 60)).until(dt.datetime.now())

# Request data and return a Pandas DataFrame
df = mapper.request()
```

When creating the Mapper you can specify multiple event types separated by commas:

```Python
mapper = Mapper(ng, "MyEventType_1", "MyEventType_2", "MyEventType_N")
```

You can also avoid `since()` and `until()`, their default values are **60 minutes ago** and **now**, respectively.

You can also specify a **SELECT** statement, exactly like you would do in NRQL:

```Python
mapper = Mapper(ng, "MyEventType").select("actionName, round(timeSinceLoad / 60.0)")
```

If not specified, the default value is `"*"`.

## License
NRSci is licensed under the [Apache 2.0](http://apache.org/licenses/LICENSE-2.0.txt) License.
