# parse
f = open("input.txt").read().strip().split("\n")[0]
bin_str = bin(int(f, 16))[2:].zfill(len(f) * 4)

# don't abuse parameters and walrus operator like this
def vwise_mult(a, v = 1): return [(v := v * n) for n in a][-1]

def handle_packet(s):
    packet_ver = int(s[:3], 2)
    packet_id = int(s[3:6], 2)
    
    if packet_id == 4: # literal
        num, pos = "", 6
        while True:
            num += s[pos + 1 : pos + 5]
            if s[pos] == "0": break
            pos += 5
        return [int(num, 2)], pos + 5, packet_ver

    else:
        pos, nums, s_ = None, [], packet_ver
        if s[6] == "1": # number of packets in the next 11 bits
            num_packets, pos = int(s[7:18], 2), 18
            for c in range(num_packets):
                n        = handle_packet(s[pos:])
                pos     += n[1]
                s_      += n[2]
                nums    += n[0]
        
        else: # number of bits
            num_bits, pos = int(s[7:22], 2), 22
            while True:
                n        = handle_packet(s[pos:])
                pos     += n[1]
                s_      += n[2]
                nums    += n[0]
                if pos == 22 + num_bits: break

        # cool use of walrus operator & lambdas
        if (f := {
            0: sum, 1: vwise_mult, 2: min, 3: max,
            5: lambda n: int(n[0] > n[1]),
            6: lambda n: int(n[0] < n[1]),
            7: lambda n: int(n[0] == n[1])
        }.get(packet_id)): nums = [f(nums)]

        return nums, pos, s_

# retrieve answer and pretty print
ans = handle_packet(bin_str)
print(f"Part 1: {ans[-1]}\nPart 2: {ans[0][0]}")
