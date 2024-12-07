if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # Solution:
    # Create a tuple from the input integers
    mytuple = tuple(integer_list)
    #
    # Compute and print the hash value of the tuple
    result = hash(mytuple)
    print(result)
