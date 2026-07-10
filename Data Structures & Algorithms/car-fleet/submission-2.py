class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p, s] for p, s in zip(position, speed)]
        fleets = []
        for p,s in sorted(pair)[::-1]:
            time = (target - p) / s
            fleets.append(time)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)
