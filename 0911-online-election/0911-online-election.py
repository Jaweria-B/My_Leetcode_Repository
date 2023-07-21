class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        
        vote_count = {}
        winner = [0] * len(persons)
        mostVotePerson = -1
        
        for i in range(len(persons)):
            if persons[i] in vote_count:
                vote_count[persons[i]] += 1
            else:
                vote_count[persons[i]] = 1
            
            if mostVotePerson == -1 or vote_count[persons[i]] >= vote_count[mostVotePerson]:
                mostVotePerson = persons[i]
        
            winner[i] = mostVotePerson
        
        self.times = times
        self.winner = winner
        
        # print(times, winner, vote_count)
        
    def q(self, t: int) -> int:
        
        left = 0
        right = len(self.winner)-1
        
        while left <= right:
            mid = (right+left)//2
                        
            if self.times[mid] <= t:
                left = mid + 1
                
            else:
                right = mid - 1

        return self.winner[left-1]

    
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)