# Example Package

**一个便捷的访问多层级dict的方法**

像操作类属性一样访问dict的属性，支持多级访问

针对场景：

针对复杂的多级dict的属性访问，如 user_info = {"name": "xxx", "address": {"city": "xxx", "country": "xxx"}}

老的方式：

```python
user_info = {"name": "xxx", "address": {"city": "xxx", "country": "xxx"}}

# 方式一 （当user_info没有address或address不为dict时，后面get会报错）：
user_info.get("address").get("city")
# 方式二（当user_info没有address或address不为dict时，后面get会报错）：
user_info['address']['city']

# 方式三 (增加多级判断)
(user_info.get("address") or {}).get("city")
```
使用amaze_dict：
```python
from amaze_dict import wrap_value
user_dict = {"name": "xiaoming", "age": 30, "address": {"city": "beijing", "country": "china"}}
user_amaze_dict = wrap_value(user_dict)
print(user_amaze_dict.address.city)
>> output: beijing
print(user_amaze_dict.address.country)
>> output: china
print(user_amaze_dict.contact.phone_num)
>> output: <amaze_dict.amaze_dict.LB_None object at 0x7f8664882cd0>
```
多级访问直接用属性递进查找，不受中间属性没有影响。 可直接对需要的属性进行访问和判断。


### 使用方法

#### 安装：

```python
pip install amaze-dict
```

```python
from amaze_dict import wrap_value

user_dict = {"name": "xiaoming", "age": 30, "address": {"city": "beijing", "country": "china"}}
user_amaze_dict = wrap_value(user_dict)

```
访问一级属性：

```shell
>>> print(user_amaze_dict.name)
xiaoming
>>>>print(user_amaze_dict.age)
30
```

访问多级属性：

```shell
>>> print(user_amaze_dict.address.city)
beijing
>>>>print(user_amaze_dict.address.country)
china

```

条件判断：

```shell
判断属性是否存在:
>>> if user_amaze_dict.address.community:
...     print(user_amaze_dict.address.city)
beijing

```
