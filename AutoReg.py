from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
import pandas as pd

# 读取账号信息表格，设置converters参数可以解决数字读取出来是科学计数形式的问题
data = pd.read_excel(' ', encoding='gb2312', converters={"学号": str})
for index, row in data.iterrows():
    # 注册页面url
    url = ' '
    chrome_option = Options()
    # 设置为开发者模式，防止被网站识别出来使用了Selenium
    chrome_option.add_experimental_option(
        'excludeSwitches', ['enable-automation']
    )
    driver = webdriver.Chrome(
        # chromedriver的路径
        executable_path=' ',
        options=chrome_option
    )
    driver.get(url)
    # 10秒内每隔500毫秒查找一次指定元素，找到了再继续向下运行
    # 时间到没找到则抛出异常
    wait = ui.WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.find_element_by_xpath(' '))
    reg_user = driver.find_element_by_xpath(' ')
    reg_name = driver.find_element_by_xpath(' ')
    reg_password = driver.find_element_by_xpath(' ')
    reg_button = driver.find_element_by_xpath(' ')
    reg_user.send_keys(row['学号'])
    reg_name.send_keys(row['姓名'])
    reg_password.send_keys(row['密码'])
    reg_button.click()
    driver.close()
