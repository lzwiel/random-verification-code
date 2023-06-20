import random

def generate_verification_code():
    code = ""
    for _ in range(6):
        # 生成0到9之间的随机整数并转换为字符串
        digit = str(random.randint(0, 9))
        code += digit
    return code

# 调用函数生成验证码
verification_code = generate_verification_code()
print("生成的六位随机数验证码是:", verification_code)
