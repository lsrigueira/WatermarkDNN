from copy import copy
import math
import random

sign = lambda a: 1 if a>0 else 0 #Returning "0" instead of "-1" 

def toBinary(key: str) -> list:
    ascii_letters,binary_list=[],[]
    for letter in key:
        ascii_letters.append(ord(letter))
    for ascii_letter in ascii_letters:
        binary_list += str(bin(ascii_letter)[2:])
    for bit in range(0,len(binary_list)):
        if binary_list[bit]=="0":
            binary_list[bit]="-1"
    return binary_list

def get_Ti(number_of_neurons: list, numberBits: int) -> list:
    """
    TODO Improvement: Exclude randpositions already taken in randposition (not so hard)
    """
    Ti = []
    index_of_neurons = []
    neurons_per_bit = math.floor(number_of_neurons/numberBits)
    available_indexes = list(range(0,number_of_neurons))
    Ti = []
    for i in range(0,numberBits):
        chosen_neurons = sorted(random.sample(available_indexes,neurons_per_bit),reverse=True)
        Ti.append(chosen_neurons)
        [available_indexes.remove(x) for x in chosen_neurons]
    while len(available_indexes):
        randposition = random.randint(0,numberBits-1)
        randnumber = random.randint(0,len(available_indexes)-1)
        Ti[randposition].append(available_indexes[randnumber])
        available_indexes.pop(randnumber)
    return Ti

def emulateDNN():
    arraytest = [ 0.        , -0.01092257, -0.00831692, -0.00352718, -0.01508513,
        0.01507002, -0.00685849,  0.01130598, -0.01166142,  0.        ,
        0.0070408 , -0.00028764, -0.01546184, -0.01446157, -0.00315147,
        0.00401835, -0.00096207,  0.00087015, -0.01334227,  0.01066918,
        0.        , -0.00707702, -0.00967751, -0.0123127 , -0.00372471,
        0.00385199,  0.        ,  0.00288349,  0.00199223,  0.00073178,
        0.01053821, -0.00836252, -0.01492088,  0.00917929, -0.00448112,
        0.00094021,  0.00613541, -0.00697291, -0.0003342 , -0.01614688,
       -0.00051349, -0.0006589 ,  0.00416488,  0.        , -0.01204002,
        0.00884326,  0.01252847,  0.        ,  0.01518746,  0.00917775,
        0.01260246,  0.00487154,  0.00347087,  0.0080589 ,  0.        ,
       -0.01445353,  0.00150561,  0.00769909, -0.00377354,  0.0012338 ,
       -0.01539214,  0.        ,  0.00033866,  0.        ,  0.00642562,
       -0.01257618,  0.00293697, -0.01247544, -0.00238049,  0.        ,
        0.00616102, -0.00426442,  0.01158626, -0.00888341, -0.00484602,
       -0.01010166, -0.01184065, -0.01568035,  0.        , -0.00331217,
       -0.00055022, -0.01804244,  0.00506844, -0.01424075,  0.        ,
       -0.00876805,  0.00738887,  0.01071095,  0.00377327, -0.00588814,
       -0.00326708,  0.0048632 ,  0.00830318, -0.00611655, -0.0068477 ,
        0.01529362,  0.00026279, -0.01084496,  0.00113789, -0.00617988,
        0.        , -0.00167626,  0.00662374,  0.01415987,  0.01582992,
       -0.00850856, -0.01438626,  0.0033305 , -0.00208019,  0.01136615,
       -0.00085878, -0.00410804, -0.00621831,  0.01407547, -0.01117415,
        0.01043861, -0.01197298, -0.00219466,  0.00018706, -0.00023424 ]
    return arraytest

def get_pseudorandom_sequence(Ti: list) -> list:
    pseudorandom_sequence = []
    for bit in Ti:
        bit_sequence = []
        for weigth in bit:
            bit_sequence.append(random.gauss(0,1)) 
        pseudorandom_sequence.append(bit_sequence)
    return pseudorandom_sequence

def watermarkSS(original_neurons: list, key:list, Ti: list, sequence: list)-> list:
    strength = 0.5
    watermarked_neurons = copy(original_neurons)
    for bit_index in range(0,len(Ti)): #Bit a bit
        indexes_of_neurons_to_change = Ti[bit_index]
        for neuron_counter in range(0,len(indexes_of_neurons_to_change)-1):
            weigth = indexes_of_neurons_to_change[neuron_counter]
            watermarked_neurons[weigth] = original_neurons[weigth] + int(key[bit_index])*strength*sequence[bit_index][neuron_counter]
    return watermarked_neurons
    

def decodeSS(watermarked_neurons: list, Ti:list, sequence: list)->list:
    decoded_bits = []
    aux = ""
    for bit_index in range(0,len(Ti)): #bit a bit
        indexes_of_neurons_to_decode = Ti[bit_index]
        adition = 0
        for neuron_counter in range(0,len(indexes_of_neurons_to_decode)-1):
            weigth = indexes_of_neurons_to_decode[neuron_counter]
            adition += watermarked_neurons[weigth]*sequence[bit_index][neuron_counter]
        aux += str(sign(adition))
        if( (bit_index+1)%7 == 0):
            decoded_bits.append(aux)
            aux = ""
    return decoded_bits


def get_Ri(neurons: list, Ti:list, sequence: list)->list:
    ri = []
    aux = ""
    for bit_index in range(0,len(Ti)): #bit a bit
        indexes_of_neurons_to_decode = Ti[bit_index]
        adition = 0
        for neuron_counter in range(0,len(indexes_of_neurons_to_decode)-1):
            weigth = indexes_of_neurons_to_decode[neuron_counter]
            adition += neurons[weigth]*sequence[bit_index][neuron_counter]
    ri.append(adition)
    return ri

def watermarkSTDM(original_neurons: list, key:list)-> list:
    print("ol")


