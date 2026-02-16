import datetime


def magic_calculator_reveal():
    # 1. 自动生成预言数字（基于当前日期和时间）
    # 格式：月日小时分钟，例如 2月16日 22:27 -> 2162227
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    # 组合成目标数字 (假设为 M-DD-HH-MM 格式)
    target_str = f"{month}{day:02d}{hour:02d}{minute:02d}"
    target_value = int(target_str)

    print(f"\n预设目标值: {target_value}")
    print(f"(代表 {month}月{day}日 {hour}:{minute:02d})\n")

    # 2. 模拟观众输入随机数
    try:
        num1 = int(input("请输入第一个随机数（模拟观众A）："))
        num2 = int(input("请输入第二个随机数（模拟观众B）："))
    except ValueError:
        print("错误：请输入有效的整数数字。")
        return

    # 3. 计算补差值 (Offset)
    current_sum = num1 + num2
    offset = target_value - current_sum

    print("\n魔术师：现在请几位观众在手机上随意点击产生一个长数字...")
    print(f"（系统自动录入补差值：{offset}）")

    # 4. 最终计算
    final_result = num1 + num2 + offset

    print("\n" + "=" * 30)
    print(f"最终计算结果：{final_result}")
    print("=" * 30)

    print(f"\n魔术师揭晓：")
    print(f"你看这个数字，它代表了此时此刻：")
    print(f"{month}月{day}号 {hour}点{minute:02d}分！")
    print("=" * 30)


if __name__ == "__main__":
    magic_calculator_reveal()
