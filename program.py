print ('budiž pozdraven otče')
print ('jsem skvělí, nebo skvělí sem?')
# Vypíšeme instrukce pro uživatele.
print('Pokud souhlasíte, stiskněte MEZERNÍK a pak ENTER.')
print('Pokud nesouhlasíte, napište cokoliv jiného a stiskněte ENTER.')
print('---------------------------------------------------------')

# Připravíme si proměnnou 'volba', zatím může být prázdná.
volba = ''

# Spustíme smyčku, která poběží DOKUD obsah proměnné 'volba' NENÍ mezera.
# Znaky '!=' znamenají "nerovná se".
while volba != ' ':
    # Zeptáme se uživatele a jeho odpověď uložíme do proměnné 'volba'.
    volba = input('Zadejte svou volbu: ')

    # Teď zkontrolujeme, jestli uživatel konečně zadal mezeru.
    if volba == ' ':
        # Pokud ano, pochválíme ho. Smyčka při další kontrole skončí,
        # protože podmínka 'volba != ' '' už nebude platit.
        print('Skvělé! Děkuji za souhlas.')
    else:
        # Pokud ne, použijeme tvoji hlášku a cyklus se bude opakovat.
        print('Snad sis nemyslel, že máš možnost volby?\n Zkus to znovu.')

# Tento kód se vykoná až po úspěšném zadání mezery a ukončení smyčky.
print('---------------------------------------------------------')
input('Program nyní skončí. Stiskněte Enter pro zavření okna.')