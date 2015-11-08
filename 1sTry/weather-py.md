# 让python自动获取天气

> 更新日志：
- 20151017 添加第一次-第二次尝试

## 第一次尝试
用beautiful soup和requests来完成，  
总是提示  
NotImplementedError: Only the following pseudo-classes are implemented: nth-of-type.
猜测是天气预报网站的css标签是beautiful soup不支持的，或者是我没找到合适的引用方式。

## 第二次尝试
搜索python get weather  
发现了[python-weather-api](https://www.google.com.hk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CBoQFjAAahUKEwiDpfakp8jIAhVDKaYKHTpJAvs&url=https%3A%2F%2Fcode.google.com%2Fp%2Fpython-weather-api%2F&usg=AFQjCNHpEKs5Z18QXVj3q4CIFjIc3yCNwA&sig2=jnH2MTpeXE7FUM6n93BepA)

安装完成后，获取城市株洲(id：CHXX5650)的天气：

```
import  pywapi
import string

weather_com_result = pywapi.get_weather_from_weather_com('CHXX5650')

print("Weather.com says: It is " + str.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in Zhuzhou.\n\n")
```

## 拓展思路
- 搜索今日的预报，而不是仅仅是当下的天气
- 可以自己搜索城市名称，不输入就自动反显株洲