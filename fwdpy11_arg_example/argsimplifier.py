import numpy as np
import msprime


class ArgSimplifier(object):
    __gc_interval = None
    __nodes = msprime.NodeTable()
    __edges = msprime.EdgesetTable()

    def __init__(self, gc_interval):
        self.gc_interval = gc_interval

    def __call__(self, generation, ancestry):
        if generation > 0 and generation % self.gc_interval == 0.0:
            ancestry.prep_for_gc(self.__nodes.time)
            na = np.array(ancestry.nodes, copy=False)
            ea = np.array(ancestry.edges, copy=False)
            samples = np.array(ancestry.samples, copy=False)
            flags=np.empty([len(na)], dtype=np.uint32)
            flags.fill(0)
            is_sample=np.empty([len(samples)], dtype = flags.dtype)
            is_sample.fill(1)
            flags[-len(samples):]=is_sample
            self.__nodes.set_columns(flags=flags,
                    population=na['population'],
                    time=na['generation'])
            self.__edges.append_columns(left=ea['left'],
                    right=ea['right'],
                    parent=ea['parent'],
                    children=ea['child'],
                    children_length=[1]*len(ea))
            print(ancestry.offspring_generation)
            msprime.sort_tables(nodes=self.__nodes, edgesets=self.__edges)
            print(len(self.__nodes.time))
            print("here")
            x=msprime.load_tables(nodes=self.__nodes, edgesets=self.__edges)
            x=x.simplify(samples=samples.tolist())
            x.dump_tables(nodes=self.__nodes, edgesets=self.__edges)
            sample_map = {i:j for i,j in zip(samples,x.samples())}
            print(sample_map)
            return (True,len(self.__nodes.time),sample_map)

        return (False,None)

    @property
    def gc_interval(self):
        return self.__gc_interval

    @gc_interval.setter
    def gc_interval(self, value):
        try:
            int(value)
        except:
            raise ValueError("GC interval must be an integer")
        if value <= 0:
            raise ValueError("GC interval must be and integer > 0")
        self.__gc_interval=int(value)
