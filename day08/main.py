#!/bin/python

import fileinput

def load_data():
    inputs = []
    outputs = []
    for line in fileinput.input():
        ins, outs = line.strip("\n").split(" | ")
        inputs.append(list(map("".join, map(sorted,ins.split(" ")))))
        outputs.append(list(map("".join, map(sorted,outs.split(" ")))))
    return inputs, outputs

def part1():
    _, outputs = load_data()
    unique = 0
    for o in outputs:
        for s in o:
            if len(s) in [2, 3, 4, 7]:
                unique += 1
    return unique

def part2():
    lengths_to_number = {2:1, 3: 7, 4: 4, 7: 8}
    inputs, outputs = load_data()
    outputs_decoded = []
    for i in range(len(inputs)):
        ins = inputs[i]
        outs = outputs[i]
        lengths_to_signal = {x: [] for x in [2, 3, 4, 5, 6, 7]}
        for s in ins:
            lengths_to_signal[len(s)].append(s)
        signal_to_number = {}
        number_to_signal = {}
        # easy ones first
        for l in [2, 3, 4, 7]:
            s = lengths_to_signal[l][0]
            n = lengths_to_number[l]
            signal_to_number[s] = n
            number_to_signal[n] = s
        ##############
        # deductions #
        ##############
        # unknown: 0, 2, 3, 5, 6, 9
        # 6 is a length 6 signal that does not contain the c segment
        # in 1
        c = None
        f = None
        one_signal = number_to_signal[1]
        for signal in lengths_to_signal[6]:
            if signal.count(one_signal[0]) == 0 or signal.count(one_signal[1]) == 0:
                signal_to_number[signal] = 6
                number_to_signal[6] = signal
                if signal.count(one_signal[0]) == 0:
                    c = one_signal[0]
                    f = one_signal[1]
                else:
                    c = one_signal[1]
                    f = one_signal[0]
        # unknown: 0, 2, 3, 5, 9
        # Knowing c we can find 5
        for signal in lengths_to_signal[5]:
            if signal.count(c) == 0:
                signal_to_number[signal] = 5
                number_to_signal[5] = signal
        # unknown: 0, 2, 3, 9
        # add c to 5 gives us 9. The last unknown length-6 signal is 0
        nine_signal = "".join(sorted(number_to_signal[5]+c))
        lengths_to_signal[6].remove(number_to_signal[6])
        lengths_to_signal[6].remove(nine_signal)
        signal_to_number[nine_signal] = 9
        signal_to_number[lengths_to_signal[6][0]] = 0
        # unknown: 2, 3
        # knowing f we can identify 2
        lengths_to_signal[5].remove(number_to_signal[5])
        for signal in lengths_to_signal[5]:
            if signal.count(f) == 0:
                signal_to_number[signal] = 2
                number_to_signal[2] = signal
        # only unknown signal is now 3
        lengths_to_signal[5].remove(number_to_signal[2])
        signal_to_number[lengths_to_signal[5][0]] = 3
        #######################
        # deductions complete #
        #######################
        number = ""
        for o in outs:
            number += str(signal_to_number[o])
        outputs_decoded.append(int(number))
    return sum(outputs_decoded)

if __name__ == '__main__':
    print(part2())