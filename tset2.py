import numpy as np


def get_noisy_digit(value0, epsilon0):
    u = np.random.random() - 0.5
    print(np.log(1.0 - 2 * np.abs(u)))
    noisy_digit = 0 - value0 / epsilon0 * np.sign(u) * np.log(1.0 - 2 * np.abs(u))
    return np.rint(noisy_digit)


if __name__ == '__main__':
    company_salary = [6000, 6000, 6000]  # 真实的人力资源数据
    noisy_salary = [6000, 6000, 6000]  # 新建的人力资源数据
    value = 1000  # 薪水最大差1000
    epsilon = 1  # 隐私保护预算，值越小泄露风险越小，噪声越大
    for i in range(len(noisy_salary)):
        noisy_salary[i] = (noisy_salary[i] + get_noisy_digit(value, epsilon))  # 逐个加噪声
    print(company_salary)
    print(noisy_salary)
