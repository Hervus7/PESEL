# PESEL
What is a PESEL? [https://en.wikipedia.org/wiki/PESEL]

# FEATURES
- Print informations about given PESEL
```
python pesel.py 23111649142
```
```
--- 23111649142 ---
Valid :  yes
Gender :  female
Birth date : day: 16 month: 11 year: 1923
```
- Generate a valid PESEL with specified parameters
```
python pesel.py -d 10 -m 12 -y 2022 -f 0
```
```
--- 22321044534 ---
Valid :  yes
Gender :  male
Birth date : day: 10 month: 12 year: 2022
```

- Get birth date from incomplete PESEL
```
python pesel.py 012125 # <- only first 6 digits passed
```
```
--- 012125 ---
Valid :  no
Gender :  -
Birth date : day: 25 month: 1 year: 2001
```
- Get gender from incomplete PESEL
```
python pesel.py 0121250007 # <- only 10 digits passed instead of 11
```
```
--- 0121250007 ---
Valid :  no
Gender :  male
Birth date : day: 25 month: 1 year: 2001
```

# RESOURCES (In Polish)
- https://romek.info/ut/pesel.html
- https://www.gov.pl/web/gov/czym-jest-numer-pesel
- https://youtu.be/4uj2t4cGqQU (got inspired by)
