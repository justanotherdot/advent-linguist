from hashlib import md5

#prefix = 'abcdef'
prefix = 'yzbqklnj'
n = -1
m = md5()
encryption = '%s%d' % (prefix, n)
m.update(encryption)
while str(m.hexdigest()[:5]) != '00000':
    m = md5()
    n += 1
    encryption = '%s%d' % (prefix, n)
    m.update(encryption)
    print m.hexdigest(), encryption, n
