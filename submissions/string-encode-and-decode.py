class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # Encode the length of each string as a comma separated list
        lengths = [str(len(s)) for s in strs]
        lengths = ','.join(lengths)

        # Encode the strings themselves by concatenating them
        encoded = ''.join(strs)

        # Join the two parts with a hyphen
        result = lengths + "-" + encoded

        return result


    def decode(self, s: str) -> List[str]:

        lengths, encoded = s.split("-", maxsplit=1)

        # Recover the lengths of each string
        lengths = lengths.split(',')
        if not any(len(s) for s in lengths):
            return []
        else:
            lengths = [int(n) for n in lengths]

        # Recover the strings themselves
        strs = []
        for length in lengths:
            strs.append(encoded[:length])
            encoded = encoded[length:]

        return strs
