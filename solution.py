def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    time_unit_len=0
    # getting the length of the series of consecutive ones and zeros '11100111' -> ones: [3,3] , zeros:[2]
    one_series_lengths = [len(chain.replace('0','')) for chain in bits.split('0') if chain.replace('0','')]
    zero_series_lengths = [len(chain.replace('1','')) for chain in bits.split('1') if chain.replace('1','')]

    # this represent the shortest consecutive 0s or 1s series
    min_ones_chain = min(one_series_lengths) if one_series_lengths else None
    min_zeros_chain = min(zero_series_lengths) if zero_series_lengths else None

    if not min_ones_chain:
        time_unit_len = min_zeros_chain
    if not min_zeros_chain:
        time_unit_len = min_ones_chain
    
    # check to see the shortest pattern to figure out the ratio to normalize the time unit to 1.
    if min_ones_chain and min_zeros_chain: 
        if min_ones_chain < min_zeros_chain:
            time_unit_len = min_ones_chain
        else:
            time_unit_len = min_zeros_chain

    """
    that should handle extra zeros situations,
    but it doesn't make sense to me, why would there be 0 as first or last character,
    I mean it's a signal coming, so it's always starting with 1 and ending with 1
    """
    if len(one_series_lengths)==1:
        time_unit_len = min_ones_chain
        bits = bits.replace('0','')
    # normalize the time unit to 1
    bits = word_zoom_out(bits,time_unit_len)
    # could have done it without '*' ,but i feel it's more accurate that way.
    return bits.replace('111', '-').replace('0000000','*').replace('000', ' ').replace('1', '.').replace('0', '')

def word_zoom_out(word,ratio):
    new_word=''
    for i in range(0,len(word),ratio):
        new_word+=word[i]
    return new_word

def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
            
    words = morseCode.split('*')
    char_lists = [w.split(' ') for w in words]
    sentence=''
    for char_list in char_lists:
        for char in char_list:
            sentence+=MORSE_CODE[char] if char else ''
        sentence+=' '
        
    return sentence.rstrip()
