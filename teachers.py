# -*- coding: utf-8 -*-
"""teachers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G3DXFwk-xL54dVscq_phK1O_kvugOtuf
"""

import pandas as pd
teacher = pd.DataFrame({
    "FISH": ['Qadamova Zulayxo', 'Karimov Sardor', "Ibragimov Navro'zbek", "Muxtarov No'monjon", "To'rayeva Ma'rifat", "Azizov Iskandar", "Xusanova Moxiraxon", "Raxmonov Ozodbek", "Ibragimov Navro'zbek", "Azizov Iskandar"],
    "Fan": ["Sun'iy intellekt asoslari", "Sun'iy intellekt asoslari", 'Mikroiqtisodiyot',  'Mikroiqtisodiyot', 'Sotib olish tamoyillari', 'Sotib olish tamoyillari', "Kiberxavfsizlik", "Kiberxavfsizlik", "Bugalteriya hisobi va tamoyillar", "Bugalteriya hisobi va tamoyillar"],
    "Mashg'ulot turi": ['amaliy', "ma'ruza", "ma'ruza", 'amaliy', 'amaliy', "ma'ruza", "ma'ruza", 'amaliy', "ma'ruza", "amaliy"]
})
print(teacher)

teacher.to_excel('Karimov.xlsx')