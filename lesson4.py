def is_divisible_by_three(number):
    return number % 3 == 0

# 测试函数
number = int(input("请输入一个数字："))

if is_divisible_by_three(number):
    print(f"{number} 可以被3整除。")
else:
    print(f"{number} 不能被3整除。")


def divide_100_by_number(number):
    try:
        result = 100 / number
        return result
    except ValueError:
        return "输入必须是一个数字！"
    except ZeroDivisionError:
        return "不能除以零！"


# 获取用户输入的数字
try:
    user_number = float(input("请输入一个数字："))

    # 调用函数进行除法
    division_result = divide_100_by_number(user_number)

    print(f"结果是：{division_result}")
except ValueError:
    print("输入必须是一个数字！")


def is_magic_date(date):
    try:
        # 将日期字符串分割为年、月和日
        day, month, year = map(int, date.split('/'))

        # 检查是否为幻数日期
        if day * month == int(str(year)[-2:]):
            return "Thy"
        else:
            return False
    except ValueError:
        return False


# 获取用户输入的日期
user_date = input("请输入日期（格式：dd/mm/yyyy）：")

# 调用函数检查是否为幻数日期
result = is_magic_date(user_date)
if result:
    print(f"{user_date} 是一个幻数日期。")
else:
    print(f"{user_date} 不是一个幻数日期。")


def is_lucky_number(number):
    # 检查数字长度是否为偶数
    if len(number) % 2 != 0:
        return False

    # 将数字字符串转换为整数列表
    digits = list(map(int, number))

    # 计算前半部分和后半部分的和
    half_len = len(number) // 2
    first_half_sum = sum(digits[:half_len])
    second_half_sum = sum(digits[half_len:])

    # 检查和是否相等
    return first_half_sum == second_half_sum

# 测试函数
ticket_number = input("请输入票号：")

if is_lucky_number(ticket_number):
    print(f"{ticket_number} 是一个幸运号码。")
else:
    print(f"{ticket_number} 不是一个幸运号码。")