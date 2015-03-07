from abifpy import Trace
abi1 = Trace('abi/56-A5-5_H07_049.ab1', trimming=True)
abi2 = Trace('abi/55-A5-4_G07_051.ab1', trimming=True)
abi3 = Trace('abi/54-A4-4_F07_053.ab1', trimming=True)

expected = open('seq/expected.seq', 'r')
output = open('seq/result.txt', 'w')
expected = expected.read()
result = abi1.seq + abi2.seq + abi3.seq
print result
print expected

for i in range(0, len(expected)):
    if expected[i] == result[i]:
        output.write(expected[i])
    else:
        output.write('(E:' + expected[i] + ' R:' + result[i] + ')')
        
