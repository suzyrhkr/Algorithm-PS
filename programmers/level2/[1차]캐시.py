def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        city = city.lower()
        # cache hit
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            # cache 가 빈 경우
            if len(cache) < cacheSize:
                cache.append(city)
            # cache 꽉 찬 경우
            elif len(cache) == cacheSize:
                del cache[0]
                cache.append(city)
        
    return answer