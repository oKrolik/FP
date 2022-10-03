"""
Find out the complete path to your Linux Home directory (default to "/usr/users2/2022/up202200000").

Write a Python script that:

    1. Assign each directory’s name to a new variable.
For example: dir1 = "usr"
    2. Print the original string by concatenating each variable, separated by a slash, using the + operator.
    3. Print the original string using the % sign.
For example: 'Hello, %s.' % 'world'
    4. Print the original string using the format() method.
For example: 'Hello, {}.'.format('world')
    5. Print the original string using f-strings.
For example: f'Hello, {"world"}.'
"""
dir1 = "usr"
dir2 = "users2"
dir3 = "2022"
dir4 = "up202200000"
print("/" + dir1 + "/" + dir2 + "/" + dir3 + "/" + dir4)
print("/%s/%s/%s/%s"%(dir1,dir2,dir3, dir4))
print("/{}/{}/{}/{}".format(dir1,dir2,dir3, dir4))
print(f"/{dir1}/{dir2}/{dir3}/{dir4}")
