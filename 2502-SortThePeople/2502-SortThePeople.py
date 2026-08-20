# Last updated: 8/20/2026, 1:56:32 AM
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        height_to_name_map = {}

        for i in range(len(heights)):
            height_to_name_map[heights[i]] = names[i]


        sorted_heights = sorted(heights, reverse=True)

        # Create a list of sorted names based on descending heights
        sorted_names = [height_to_name_map[height] for height in sorted_heights]

        return sorted_names