def solution(brown, yellow):
    answer = []
    
    # x * y = yello
    # 4 + 2x + 2y = brown
    # 2 + x + y  = brown / 2
    # y = brown /2 - 2 - x
    
    # x * (brown / 2 - 2 - x) = yello
    # -x^2 -2x + (brown / 2) x = yello
    # x^2 + (2 - brown / 2) x + yello = 0
    # x = [brown / 2 - 2 +- ((2-brown/2)^2 -4yello)**0.5] / 2
    
    plusminus = ((2-brown/2)**2 - 4 * yellow) ** 0.5
    x1 = int((brown / 2 - 2 + plusminus) / 2)
    x2 = int((brown / 2 - 2 - plusminus) / 2)
    return [x1+2,x2+2] if x1 > x2 else [x2+2,x1+2]
    