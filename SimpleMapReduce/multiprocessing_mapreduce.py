# -*- coding=utf-8 -*-
import collections
import multiprocessing

class SimpleMapReduce(object):
    def __init__(self, map_func, reduce_func, num_workers=None, Pool=multiprocessing.Pool):
        self.map_func    = map_func
        self.reduce_func = reduce_func
        self.pool        = Pool(num_workers)

    def partition(self, mapped_values):
        partitioned_data = collections.defaultdict(list)
        for sublist in mapped_values:
            for key, value in sublist:
                partitioned_data[key].append(value)
        return partitioned_data

    def __call__(self, inputs, chunksize=1):
        mapped_values    = self.pool.map(self.map_func, inputs, chunksize=chunksize)
        partitioned_data = self.partition(mapped_values)
        reduced_values   = self.pool.map(self.reduce_func, partitioned_data.items())
        return reduced_values
