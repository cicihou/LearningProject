class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        time = releaseTimes[0]
        key = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i-1] == time:
                key = max(keysPressed[i], key)
            elif releaseTimes[i] - releaseTimes[i-1] > time:
                key = keysPressed[i]
                time = releaseTimes[i] - releaseTimes[i-1]
        return key
