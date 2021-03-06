# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/07_metrics.ipynb (unless otherwise specified).

__all__ = ['MaskedAccuracy', 'BPC', 'bpc']

# Cell
import torch, math
from fastai.basics import *
from functools import partial

# Cell
def _masked_accuracy(inp, targ, ignore=-100, dim=-1):
    pred, targ = flatten_check(inp.argmax(dim=dim), targ)
    mask = targ != ignore
    return (pred[mask] == targ[mask]).float().mean()

class MaskedAccuracy(AvgMetric):
    "Computes accuracy skipping values where targ=='ignore'"
    def __init__(self, ignore:int=-100, dim:int=-1):
        self.func = partial(_masked_accuracy, ignore=ignore, dim=dim)
    @property
    def name(self): return 'masked_accuracy'

# Cell
class BPC(AvgLoss):
    "Bit per character for Language Models"
    @property
    def value(self): return self.total/self.count/math.log(2) if self.count != 0 else None
    @property
    def name(self):  return "bpc"

bpc = BPC()