# # y = [[1, 2, 3], [2, 4, 5], [5, 5, 3]]
# #
# # print(y)
#
# # listof = [x for x in range(10)]
# # print(listof)
#
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
#
# # list = []
# #
# # for x in :
# #     print(list)
# # n = int(input())
# # print([[x, y, z] for x in [0, 1] for y in [0, 1] for z in [0, 1] if x + y + z != n])
#
# # x, y, z, n = (int(input()) for _ in range(4))
# # print([[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a + b + c != n])
#
# # for i in range(0, x + 1):
# #     for j in range(0, y + 1):
# #         for k in range(0, z + 1):
# #             if i + j + k != n:
# #                 list.append([i, j, k])
# # print(list)
#
# list01 = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if x + y + z != n]
# print(list01)
#
