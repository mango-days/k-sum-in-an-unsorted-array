{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 array = [ 10, 12, 9, 8, 10, 15, 1, 3, 2 ]\
n = len( array )\
k = 3\
\
# initial value of window\
temp_sum = sum( array [ :k ] )\
max_sum = temp_sum\
\
# window is now sliding\
for index in range ( k , n ) :\
    temp_sum\
    temp_sum = temp_sum - array [ index-k ] + array [ index ]\
    if temp_sum > max_sum : max_sum = temp_sum\
    \
print ( max_sum )}