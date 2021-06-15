# todo 变量、参数  强制要求类型，才会更安全


def 求绝对值(*args, **kwargs)  :
    """
    返回传入参数的绝对值

    ===================================================

    =================  =========  =====================
    举例                返回值      说明
    求绝对值(1)          1          传入了正数1
    求绝对值(-1)         1          传入了负数1
    求绝对值(-3.14)      3.14       传入了负数3.14
    =================  =========  =====================
    """
    return abs(*args, **kwargs)


def 求最小(*args, key=None)  :  # todo
    """
    把可迭代对象的每一个元素，相加在一起（求可迭代对象的元素的总和，每个元素必须为数字类型，不然会出错）

    如果你传入一个空的可迭代对象，就返回0, 应该报错， 因为用户无法根据0判断代码是否正常，因为可能用户传入的数据里刚好 有0
    如果参数为空，返回None

    ===============================================

    ===============  =======  =====================
    举例              返回值    说明
    求最小(1,2,9)          0        传入了空的列表
    求最小([1,2,3])     6        传入了一个有3个元素的列表
    求最小((1,2,400))   403      传入了一个有3个元素的元组
    求最小({1,2,3})     6        传入了一个有3个元素的集合
    ===============  =======  =====================

    """
    return min(*args, key=None)
