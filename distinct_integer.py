from mrjob.job import MRJob
class MRDistinctIntegers(MRJob):
    def mapper(self, _, line):
        for num in line.split():
            yield(int(num), 1)
    def reducer(self, num, counts):
        yield(num, sum(counts))

if __name__ == '__main__':
    MRDistinctIntegers.run()