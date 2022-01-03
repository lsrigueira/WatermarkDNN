from typing import Sequence
import funcitions
        


secret_key =  funcitions.toBinary("OLA")
neurons = funcitions.emulateDNN()
Ti = funcitions.get_Ti(len(neurons),len(secret_key))
pseudo_random_sequence = funcitions.get_pseudorandom_sequence(Ti)
watermarked_neurons = funcitions.watermark(original_neurons=neurons, key=secret_key ,Ti=Ti, sequence=pseudo_random_sequence)
decoded_watermark = funcitions.decode(watermarked_neurons, Ti=Ti, sequence= pseudo_random_sequence)
print("********")

for bit in decoded_watermark:
    print(chr(int(bit, 2)))

print("********")
