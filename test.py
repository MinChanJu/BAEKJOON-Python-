import sys
input = sys.stdin.read

def solve():
    n = int(input().strip())
    
    for i in range(1, n):
        print(f"? {i}")
        sys.stdout.flush()
        response1 = int(input().strip())
        
        print(f"? {i+1}")
        sys.stdout.flush()
        response2 = int(input().strip())
        
        if response1 == 0 and response2 == 1:
            print(f"! {i}")
            sys.stdout.flush()
            return
    
    # 조건을 만족하는 (i, i+1) 쌍이 없는 경우
    print("! -1")
    sys.stdout.flush()

if __name__ == "__main__":
    solve()