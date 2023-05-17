times = ('Botafogo', 'Palmeiras','Cruzeiro','Fortaleza','São Paulo',
         'Fluminense', 'Gremio', 'Internacional','Bahia','Atletico-PR')

print(f'Lista de times: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[1:6]}')
print('-='*15)
print(f'Os 4 ultimos colocados {times[-4:]}')
print('-='*15)
print(f'Ordem alfabética {sorted(times)}')
print('-='*15)
print(f'A posição da Chapecoense é {times.index("Internacional")+1}')
print()