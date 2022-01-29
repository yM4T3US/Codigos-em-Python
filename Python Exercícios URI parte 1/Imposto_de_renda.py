renda = float(input())
if renda <= 2000.00:
    print('Isento')
elif renda <= 3000.00:
    imp = 0.08 * (renda - 2000.00)
    print('R$ {:.2f}'.format(imp))
elif renda <= 4500.00:
    imp = 0.08 * 1000.00 + 0.18 * (renda - 3000.00)
    print('R$ {:.2f}'.format(imp))
else:
    imp = 0.08 * 1000.00 + 0.18 * 1500.00 + 0.28 * (renda - 4500.00)
    print('R$ {:.2f}'.format(imp))
