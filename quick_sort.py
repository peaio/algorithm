# 快速排序

"""
快速排序基于分治法
分治法三步曲
1. 划分子问题
2. 递归处理子问题
3. 子问题合并

快速排序实现步骤：
1. 确定分界点x：第一个数、中间的数、最后一个数、或者随机的数都可以。
2. 调整区间：让小于等于x在左边，让大于等于x的在右边（重点）。
3. 递归处理左右两边。
"""

"""
第一种实现方法——单路快排：
"""

# def partition(q,l,r):
#     # q是待排序列表, l是起始位置，r是结束位置
#     pivot = q[l] # 以第一个元素为基准
#     i = l # 默认最后小于基准元素的位置为起始位置
#     for j in range(l+1, r+1): # 遍历基准外的元素
#         if q[j]<pivot:  # 如果小于基准
#             q[j], q[i+1] = q[i+1], q[j] # 将其和大于基准的元素换位
#             i += 1  # 默认最后小于基准元素的位置后移
#     q[l], q[i],  = q[i], q[l]     # 基准元素与最后小于基准元素的元素位置交换
#     return i    # 返回基准位置
#
# def single_quick_sort(q,l,r):
#     if l>=r: return     # 递归终止条件
#     m = partition(q,l,r)
#     single_quick_sort(q,l,m-1)  # 基准已排好序左区间递归
#     single_quick_sort(q,m+1, r) # 右区间递归
#
# if __name__ == '__main__':
#     n = int(input())
#     q = list(map(int, input().split()))
#     single_quick_sort(q, 0, n-1)
#     print(*q)

"""
第二种优雅实现方法——双路快排：
1. 用两个指针i和j分别往中间靠齐。
2. i位置上的大于等于x，i停下来移动j，j位置上同样如果有小于x的数就停止，交换i和j位置上的数
3. 递归操作两边
"""

def double_quick_sort(q, l, r):
    if l>=r: return     # 递归终止条件
    pivot = q[l]    # 取基准点
    # 两个指针移动
    i = l+1
    j = r
    while True:
        while i<=r and q[i]<pivot:  # 如果i在r范围内且小于基准
            i+=1    # 指针后移
        while j>=l and q[j]>pivot:  # 如果j在l范围内且大于基准
            j-=1    # 指针前移
        if i<j:
            q[i], q[j] = q[j], q[i] # 两者停止则交换
            i+=1
            j-=1
        else:
            break
    q[l], q[j] = q[j], q[l]
    double_quick_sort(q, l, j-1)
    double_quick_sort(q, j+1, r)

if __name__ == '__main__':
    n = int(input())
    q = list(map(int, input().split()))
    double_quick_sort(q, 0, n-1)
    print(*q)
