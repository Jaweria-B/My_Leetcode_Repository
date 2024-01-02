class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        e1_s, e1_e = event1
        e2_s, e2_e = event2
        
        def compare(time1, time2):
            t1_hr, t1_mint = time1.split(":")
            t1_hr, t1_mint = int(t1_hr), int(t1_mint)
            
            t2_hr, t2_mint = time2.split(":")
            t2_hr, t2_mint = int(t2_hr), int(t2_mint)
            
            if (t1_hr == t2_hr and t1_mint < t2_mint) or t2_hr > t1_hr  :
                return False
            
            return True
        
        return compare(e1_e, e2_s) and compare(e2_e, e1_s)