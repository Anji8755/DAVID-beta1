for idx,val in enumerate(tables):
     query =query+(f'''({val} left join''')
     print(query)

     end =(f'''on {val}.{col[idx]}={tables[idx+1]}.{col[idx+1]})''')+end
     print(end)

     if val==tables[-1]:
             query=query+(f'''{val}''')


############### working
query=(f'''select * from''')
>>> end
'on z3.c3=z4.c4)on z2.c2=z3.c3)on z1.c1=z2.c2)'
>>> end=(f'''''')
>>> for idx,val in enumerate(tables):
...      query =query+(f'''({val} {join[0]} join''')
...      print(query)
...
...      end =(f'''on {val}.{col[idx]}={tables[idx+1]}.{col[idx+1]})''')+end
...      print(end)
...
...      if val==tables[-1]:
...              query=query+(f'''{val}''')
...