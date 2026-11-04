class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""  # Το άδειο string όπου θα κολλάμε τα πάντα
        
        for word in strs:
            # 1. Βρίσκουμε το μήκος της λέξης: str(len(word))
            # 2. Κολλάμε το σύμβολο: "#"
            # 3. Κολλάμε την ίδια τη λέξη: word
            res += str(len(word)) + "#" + word
            
        return res

    def decode(self, s: str) -> List[str]:
        res= []
        i=0

        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            lenght = int (s[i:j])

            word=s[j+1:j+1+lenght]

            res.append(word)

            i = j + 1 + lenght
        return res