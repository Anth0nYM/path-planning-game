"""_summary_
Search helper functions
"""

# IMCOMPLETE 
import matplotlib.pyplot as plt

def segments_intersect(segment1, segment2):
    """__summary__
    Check whether the movement is valid by calculating the determinant."""
    k = segment1[0]
    l = segment1[1]
    m = segment2[0]
    n = segment2[1]
    det = (n[0] - m[0]) * (l[1] - k[1]) - (n[1] - m[1]) * (l[0] - k[0])
    if det == 0:
        return False
    s = ((n[0] - m[0]) * (m[1] - k[1]) - (n[1] - m[1]) * (m[0] - k[0])) / det
    t = ((l[0] - k[0]) * (m[1] - k[1]) - (l[1] - k[1]) * (m[0] - k[0])) / det
    return 0 < s < 1 and 0 < t < 1

def is_intersecting(segment, segment_list):
    for segment_n in segment_list:
        for seg in segment_n:
            if segments_intersect(segment, seg):
                return True
    return False

segment1 = [(0,0),(10,10)]
segment2 = [(0,10),(10,0)]
plt.figure(figsize=(8, 8))
plt.gca().set_aspect('equal', adjustable='box')
plt.plot()
#print(segments_intersect(segment1,segment2))