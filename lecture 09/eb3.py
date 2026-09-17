def divide (a, b):
    return a / b

a, b = map(int, input("Enter two number separed by space: ").split())
print(divide(a, b))
print("End of program")

def divide (a, b):
    try :
        result = a/b
    except Exception as e :
        print(f"Error: {e}")
        return None
    else :
        return result

a,b = map(int, input().split())
print(divide(a,b))
print("End of progeram")