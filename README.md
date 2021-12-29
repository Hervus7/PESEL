# PESEL
What is a PESEL? [https://en.wikipedia.org/wiki/PESEL]

# FEATURES
- Print some information about given PESEL
```
python pesel.py 23111649142
```
```
--- 23111649142 ---
Valid :  True
Gender :  female
Birth date : day: 16 month: 11 year: 1923
```
- Generate a valid PESEL with given parameters
```
python pesel.py -d 10 -m 12 -y 2022 -f 0
```
```
--- 22321044534 ---
Valid :  True
Gender :  male
Birth date : day: 10 month: 12 year: 2022
```

# RESOURCES (In Polish)
- https://romek.info/ut/pesel.html
- https://www.gov.pl/web/gov/czym-jest-numer-pesel
