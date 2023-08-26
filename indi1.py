#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sentence = "Привет, сегодня неплохая погода."
output = ""
for i in range(len(sentence)):
    if i == 0 or i == 1 or (i-1) % 3 == 0:
        output += sentence[i] + "\n"
print(output)