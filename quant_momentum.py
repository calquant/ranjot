import pandas as pd
import numpy as np

from quantopian.pipeline import CustomFactor,Pipeline
from quantopian.research import run_pipeline
from quantopian.pipeline.filters import Q1500US
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import SimpleMovingAverage

def make_pipeline():

    momentum = Momentum(inputs=[USEquityPricing.close], window_length=250)
    high=momentum.percentile_between(80, 100)
    low=momentum.percentile_between(0,20)
    
    return Pipeline(
        columns={
            'Momentum': momentum,
            'long':high,
            'short':low,
        },
        screen=Q1500US()
    )
class Momentum(CustomFactor):
    def compute(self, today, asset_ids, out, values):
        out[:] = ((values[-1]-values[0])/values[0])

my_pipe = make_pipeline()
result = run_pipeline(make_pipeline(), '2016-09-25', '2016-09-25')
result.head(1500)