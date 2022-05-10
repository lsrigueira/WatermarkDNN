from typing import Sequence
import funcitions
import argparse        

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-m', metavar='mode', type=str, required=True, nargs=1, choices=["SS", "STDM"],
                    help='Types of watermark', dest="mode")
args = parser.parse_args()

secret_key = funcitions.toBinary("O")
neurons = funcitions.emulateDNN()
Ti = funcitions.get_Ti(len(neurons),len(secret_key))
pseudo_random_sequence = funcitions.get_pseudorandom_sequence(Ti)
print(pseudo_random_sequence)
if(args.mode[0]=="SS"):
    watermarked_neurons = funcitions.watermarkSS(original_neurons=neurons, key=secret_key ,Ti=Ti, sequence=pseudo_random_sequence)
    decoded_watermark = funcitions.decodeSS(watermarked_neurons, Ti=Ti, sequence= pseudo_random_sequence)
else:
    ri = funcitions.get_Ri(neurons, Ti=Ti, sequence= pseudo_random_sequence)
    watermarked_neurons = funcitions.watermarkSTDM(original_neurons=neurons, key=secret_key)
    

print("********")

for bit in decoded_watermark:
    print(chr(int(bit, 2)))

print("********")
