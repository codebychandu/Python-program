# import math

# def is_perfect_square(num):
#     if num < 0:
#         return False

#     root = math.isqrt(num)
#     return root * root == num

# if __name__ == "__main__":
#     try:
#         num = int(input("Enter a number: "))
#         if is_perfect_square(num):
#             print(f"{num} is a perfect square.")
#         else:
#             print(f"{num} is not a perfect square.")
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")



# a = int(input("enter the no"))
# for i in range(1):
#     for j in range(i,i+a):
#         print(i+j, end=' ')
#     print(j)


# def print_pattern(rows):
#     for i in range(rows):
#         for j in range(1, rows + 1):
#             print(i + j, end=" ")
#         print()

# # Input the number of rows (in this case, 3)
# num_rows = int(input("enter the no"))
# print_pattern(num_rows)

