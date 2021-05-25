import re

seq = "GTAAATACTAACTTTACGTCATTACTAACGGGAC"
rgx = re.compile('GT...TACTAAC...AC')
answer = rgx.findall(seq)

print(answer)