def map_bucket(x):
    buckets = [0.2, 0.4, 0.6, 0.8, 1.0]
    for i in range(len(buckets)):
        if x < buckets[i]: # if x is less than the bucket number, than we want to return the index of that bucket number
            return(i)
    return(-1)  # Error

if __name__ ==  "__main__":
    print(map_bucket(0.36))
    print(map_bucket(0.81))
    print(map_bucket(0.1))
