from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list) # key: firma del anagrama, value: lista de strings con esa firma

        for i in strs:
            # sorted() parte el string en caracteres y los ordena (devuelve lista);
            # lo paso a tupla porque las listas no se pueden usar como key
            newgroups = tuple(sorted(i))
            groups[newgroups].append(i)

        return list(groups.values())  # retornamos los valores en los grupos de anagramas ya formados