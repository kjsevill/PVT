import math
def uo(colums, API, T):
    """

    Parameters
    ----------
    colums
        Correlación usada
    API
        Gravedas API
    T
        Temperatura en °R
    Returns
        uo en cp
    -------

    """
    a= 10**(0.43 + (8.33/API))
    a1=(10.313 * math.log10(T-460)) - 36.447
    print(a)
    if colums == "Beal":
        uo=(0.32 + ((1.8*(10**T))/(API**4.53))) * (360/(T-260))**a
    else:
        uo= 3.141 * (10**10) * (T-460)**(-3.414) * (math.log10(API))**a1
    return uo
