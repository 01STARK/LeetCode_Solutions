class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        possible_Times=[]
        for h in range(12):
            for m in range(60):
                if (bin(h).count('1')+bin(m).count('1'))==turnedOn:
                    timestr=f'{h}:{m:02d}'
                    possible_Times.append(timestr)
        return possible_Times